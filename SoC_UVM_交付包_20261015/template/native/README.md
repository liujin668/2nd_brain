# 软件接口与镜像装载说明

本目录提供可供内网工程实现的 C 平台接口契约、一个不含启动代码的存储读写算法，以及可独立运行的 ELF 分段检查工具。当前没有 N2 BSP、真实 CPU startup、Synopsys loader 或 host DPI backend。

## 文件和适用范围

| 文件 | 内容 | 使用条件 |
| --- | --- | --- |
| shared/soc_platform.h | 64位地址的访问API、明确错误返回、软件结果字段 | 实现目标CPU或host DPI后端后链接 |
| sw_lib/platform_unconfigured.c | 未适配时明确拒绝构建 | 后端验收完成后从实际编译列表移除 |
| ../test/c/memory_smoke.c | 专用scratch区的定向读写测试算法 | 访问属性、地址范围、屏障语义已定义 |
| sw_lib/prepare_image.py | 静态AArch64 ELF64分段检查及导出 | Python 3.8及以上，标准库 |
| sw_lib/test_prepare_image.py | 镜像处理的单元测试 | 不需要EDA工具 |

`memory_smoke.c` 中的 `soc_memory_smoke()`不是`main()`或startup。由平台入口初始化后调用，再将返回值转成软件状态。scratch区必须避开代码、stack、页表、参数和结果区。

## 镜像处理工具

工具仅支持 little-endian ELF64、AArch64、ET_EXEC，不执行重定位，不接受动态链接/解释器段。每个 PT_LOAD 输出一个二进制文件，并记录内存大小与尾部零填充量。它不会把整个 ELF 文件的头部或段间空隙当成指令写入 DDR。

示例中的地址只是演示，必须替换成项目实际的许可装载窗口：

```sh
python3 native/sw_lib/prepare_image.py program.elf \
  --out image_export_001 \
  --address-kind paddr \
  --region 0x100000000:0x100000
```

输出：

```text
image_export_001/
  image_manifest.json
  segment_00.bin
  ...
```

`--out` 必须是不存在的新目录，防止旧段和新manifest混用。允许多个`--region`。工具拒绝越界、重叠装载区、文件截断、非法段大小、非法入口和不支持的ELF格式。

`entry_virtual` 是 ELF 入口，`entry_load_address` 是按选定段映射得到的装载地址。这两个字段不能自动替代 N2 的实际硬件 reset vector。若平台要求地址转换或启动跳板，内网 agent 必须单独实现并验证。

## 内网 memory loader 必须实现的操作

1. 读取并校验 manifest，记录源ELF SHA256。
2. 检查每个段文件的长度与 SHA256，确认文件路径属于本次镜像包。
3. 按字节把文件写入实际响应请求的 backing store。
4. 将`zero_fill`对应尾部区域清零，不按未初始化数组值猜测BSS。
5. 验证所有装载区与软件保留区的关系。
6. 后门读回至少核验全部装载内容及关键零填充区；首批测试再进行前门访问检查。
7. 发布`image_loaded`状态，确认后续reset不会清除此状态对应的存储内容。
8. 在fabric配置和CPU启动条件满足后才释放CPU。

工具限制是有意收窄的可验收格式。如果项目的ELF有合法重叠段、PIE或其他布局，应新增明确策略和测试，不能静默忽略。

## C 与 DPI 的接口契约

地址用`uint64_t`传递，数据位宽与地址位宽分开。DPI声明使用仿真器生成的header核验ABI；不要依赖host `unsigned long`恰好为64位。

每次访问返回`SOC_OK/BUS_ERROR/TIMEOUT/UNSUPPORTED/INVALID_ARGUMENT`。只有成功时输出数据有效。host DPI必须采用能等待事务完成的task/context调度方式，并能推动仿真时间；轮询不得变成不推进时间的C忙循环。

`cache clean/invalidate`、屏障和异常处理属于具体平台语义。host端不能通过空函数返回成功来冒充真实CPU的缓存/内存序验证。

## 软件结果协议

逻辑结果区是40字节little-endian字段：

| 偏移 | 位宽 | 字段 |
| --- | --- | --- |
| 0 | 32 | magic = 0x534F4352 |
| 4 | 32 | version = 1 |
| 8 | 64 | run_token |
| 16 | 32 | test_id |
| 20 | 32 | state，1 RUNNING，2 PASS，3 FAIL |
| 24 | 32 | error_code |
| 28 | 32 | reserved，写零 |
| 32 | 64 | heartbeat |

结构体只是API入参；wire格式需要显式序列化，不依赖编译器padding。runner/TB/软件需要约定本次run token，模板目前不自动把Python run_id写入裸机镜像。

开始前初始化结果区，TB拒绝旧token、错误test_id和非法状态跳转。结果更新的可见性必须保证：可选经过确认的非缓存映射，或正确的cache clean与屏障；只写`volatile`不足以保证TB能从DDR看到最新数据。

软件PASS是完成请求。TB还要排空测试相关事务并汇总检查，runner还要核对进程退出状态。

## 在内网补齐 N2 平台的顺序

确认硬件复位入口与异常级别，建立合法startup和栈，初始化BSS/数据，明确MMU/cache初态，配置必要fabric/安全属性，调用测试，发布结果，进入明确的等待或终止状态。不要从CA55工程直接改宏名称后声称N2已接入。

单元测试入口：

```sh
python3 -m unittest discover -s native/sw_lib -p 'test_*.py' -v
```

## 装载地址与启动地址的限制

manifest的`boot_entry_validated`固定为false。`requires_address_translation`说明所选装载地址是否与链接虚拟地址不同。物理装载映射不等于已经证明能够直接启动：ET_EXEC中的绝对引用仍依赖链接地址，MMU关闭直接执行通常需要已核实的identity布局或正确的启动跳板。内网实现必须根据实际启动模式核对所有段，而不只是入口所在段。

## 软件完成的提交顺序

发布最终结果时先写payload，确保payload可见，再最后提交state。平台必须确认对齐32位state写在TB观察边界不会被撕裂，并使提交写也可见。若该保证不成立，应采用有明确校验规则的序号或双缓冲协议。TB核对本次token/version，并读取稳定的提交状态后才能接受结果。不要按结构体字段顺序先写PASS再写error_code或heartbeat。

如果此测试要证明访问到了外部memory模型，scratch区应采用经过确认的非缓存映射或在平台代码中完成必要的cache维护。CPU对缓存内数据的写后读成功不能单独证明DDR路径已经发生实际访问。

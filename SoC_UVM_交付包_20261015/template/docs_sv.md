# SystemVerilog/UVM 模板说明与接入契约

本目录提供 UVM 1.2 环境的**事务层自检样例**。交付时没有在 VCS 或 Xcelium
上编译、运行；需要在工作服务器完成双工具编译与下面的正负测试验收。
已有内容不能作为 N2、CMN、AXI、DDR 或服务器 SoC 的验证结果。

## 1. 现有实现与限制

已实现：

- 静态 HDL/HVL 分层；唯一 HVL 入口先发布 virtual interface/config，再 run_test。
- Clock/reset 唯一 HDL 驱动者、串行请求和 ACK、显式时间单位。
- 独立 SVA checker 与 bind，静态错误汇总到同一结果文件。
- UVM sequencer/driver、事务观察 tap、独立 byte-addressed reference model、
  scoreboard、实际观察事件覆盖率、总仿真时间 watchdog。
- Reset → memory model 清空 → 数据 preload → release → 运行 → drain → 检查
  → 唯一 result writer 的生命周期。
- 正常测试和一次 read response 数据翻转的负向测试。
- 未接入 profile、缺组件、零检查、未完成事务、软件未完成、UVM/SVA 错误均不能 PASS。

尚未实现：

- 信号级 AXI/CHI driver/monitor、SNPS VIP adapter、CMN/N2/真实 SoC wrapper。
- 真实 CPU 执行、DDR boot、ELF 加载进真实 VIP、C-DPI bridge。
- RAL、跨域 reset 恢复、低功耗、GIC/SMMU/RAS、一致性与内存序 checker。
- 多 outstanding、乱序/拆分/合并、coherence、DDR timing/training。

这些是后续独立组件或 adapter 的明确接入点，不是已完成却被隐藏的功能。
框架里的 memory backend 为自定义阻塞事务模型，**不是 AXI**。
soc_tl_monitor 观察 backend 发出的事务对象，**没有解码 DUT 引脚**。
当前通过只能说明环境的这条自检链路工作，不能证明真实协议 monitor 的能力。

## 2. 目录职责和编译

| 位置 | 职责 |
|---|---|
| tb/common/soc_tb_defs_pkg.sv | 类型、枚举和自检常量；真实地址图应使用项目生成配置 |
| tb/common/soc_tb_defines.svh | 仅预处理宏，不能成为全部配置的堆积处 |
| tb/hdl_top/interfaces | 控制请求/ACK、观测接口和静态错误汇总接口 |
| tb/hdl_top/generators | Clock/reset pin 的唯一驱动者 |
| tb/hdl_top/assertions、binds | 独立 checker 与集中层次绑定 |
| tb/hdl_top/soc_demo_wrapper.sv | Clock/reset 行为示范模块，无 memory/AXI 逻辑 |
| tb/hvl_top/soc_hvl_top.sv | 唯一配置和 run_test 入口 |
| env | 环境组件、配置、事务、检查与结果 |
| env/seq | 可复用启动/内存场景 |
| test/sv | 具体 testcase 及负测配置 |
| flist/uvm_selftest.f | 唯一入口文件清单；头文件仅 include，不重复编译 |

编译时工作目录应为 template，选择两个 top：soc_hdl_top、soc_hvl_top。
UVM 1.2 由仿真器适配层引入一次，本 filelist 不再次编译 uvm_pkg。
VCS/Xcelium 的实际命令由统一 runner 生成。当前 filelist 不依赖商业 VIP 许可、
ACVM 或尚未得到的 Arm RTL。

所有模板 SV 作用域采用 timeunit 1ps/timeprecision 1ps，控制接口中 time
参数按同一单位传递。测试使用 10ns 周期；时钟最小周期为 2ps。实际项目仍应按
精度和性能要求确定约定，不能只改部分文件后继续传递无单位数值。
启动 sequence 还会测量相邻 posedge 的实际时间差，必须等于 10ns；
不匹配报告 CLOCK_PERIOD_MISMATCH，不能用加长 timeout 掩盖时间单位错误。

## 3. 控制与启动契约

只有 soc_clk_gen 写 clk，只有 soc_reset_gen 写外部 rst_n。
UVM 调用 set_clock()/set_reset()，不再赋值 pin 或 force DUT 内部 reset。
时钟在低电平边界接受命令，完整输出当前高脉冲后停止或切换周期。
控制接口内部 semaphore 使多个控制请求串行化；测试整体 watchdog 覆盖 ACK 丢失。

reset_gen 只表示外部 reset stimulus。真实 DUT 内部各域同步释放的正确性，
必须由实际 reset controller/synchronizer 及其 checker 验证，TB 不能代为实现。

模型 ready 在当前自检中由 build 完成保证。preload 发生在 reset asserted、
backend/reference 清空之后。若真实 VIP 在 reset release 后重新清空 memory，
应调整其初始化回调或使用设计已有的 CPU hold/boot-release 机制；不能用固定
延迟抢在 CPU 取指前加载。

SVA 的 reset effect 检查需先观察到稳定的 reset 采样，避免在首个 clock edge
用 NBA 更新前的 marker 值误判。真 DUT 的检查延迟应按设计规范定义。

自检只支持无 outstanding 时的初始 reset。运行中 reset 会报错；scoreboard
禁止默默删除 pending transaction。未来需按每种 reset 明确取消、重试、
保留和跨 epoch 事务处理，再开放相关测试。

## 4. 数据检查与负向验证

数据路径：

```text
sequence → driver.intent_ap → scoreboard.pending
                 ↓
      synthetic memory backend
                 ↓ completed_ap
      transaction observation tap
                 ├→ scoreboard + independent reference
                 └→ coverage collector
```

backend 和 reference 使用两份独立存储。preload 初始数据由场景分别写入，
reference 不读取 backend 来获取预期值。写请求的预期内容在成功 response
时提交；这是本阻塞、串行演示模型的规则，不能直接套到乱序总线或缓存一致性。

专属自检地址从 0x0000000100001000 开始，故意超过 4 GiB；它不属于用户 SoC
的已确认 DDR 地址映射。事务为 8-byte 对齐读写，写入带 8-bit byte enable。
未初始化 byte 定义为零，仅是本模型的约定。地址、操作和 byte-enable
保留四态并在访问存储前检查 X；写入仅检查有效 byte 的数据 X，preload
检查完整地址与数据。actual/reference 存储均使用 logic[7:0]，避免同时把 X
静默转成 0 后出现假通过。

| UVM_TESTNAME | 预期行为 |
|---|---|
| soc_selftest | 8 次 preload 读回；16 组 full write/read/masked write/read；72 个事务、72 次检查、40 次数据读比较；PASS |
| soc_selftest_mismatch | 同一场景第一次 read response 的 bit 0 被翻转；reference 不变；必须出现 DATA_MISMATCH，并输出 FAIL |

负测的设计结果始终是 FAIL。环境验收程序可以确认“预期失败已被检测”，但不能把
这次 design result 改写为 PASS。两项行为尚待真实 EDA 工具运行确认。

## 5. 运行及结果协议

runner 至少传入：

```text
+SOC_PROFILE=uvm_selftest
+SOC_RUN_ID=<本次唯一运行ID>
+SOC_RESULT_FILE=<完整输出JSON路径，父目录由runner提前建立>
+SOC_SEED=<unsigned 32-bit seed>
+UVM_TESTNAME=soc_selftest
```

也应把相同 seed 传给仿真器的随机种子开关。自检另有局部确定性 PRNG，避免
无关 UVM 对象创建改变数据模式。这里不把临时 SOC_RUN_ID 作为随机种子。

唯一 writer 是 soc_result_manager.final_phase；所有 check/report phase 完成后
再读取 UVM severity count、scoreboard 和静态 assertion 汇总。
其他组件不得在 final_phase 新增检查或自行输出结果 JSON。

JSON schema_version=1，包含 run_id、profile、test、seed、status、completed、
stimulus_count、checks_count、pending_count、uvm_errors、uvm_fatals、
assertion_errors、software_required、software_status、failures。
字符串引号、反斜杠及控制字符会转义。

状态为 PASS 的前提：

- 场景到达 DONE，且 completed=true。
- 非零实际 stimulus/check/read-check/observation/coverage sample。
- 每个 demo 请求恰有一次检查，pending=0。
- 无 UVM error/fatal、无静态 assertion error、无独立失败原因。
- 必需 SVA checker 已注册且采样数大于零；漏编 bind 报 ASSERTION_NOT_ACTIVE。
- 若 profile 需要软件，software_status 必须 PASS。

不可根据日志中出现“PASS”单独判定。配置阶段 fatal、进程崩溃、外部超时等情况
可能来不及执行 final_phase；结果缺失/损坏必须由 runner 判失败，不能补造 PASS。
runner 还应验证 run_id/test/seed/profile 与本次任务一致并检查仿真器退出码。

## 6. 真实 VIP/CMN/N2 接入要求

新增 profile 前应先提交以下实现及验收，不允许只改 profile 名称绕过保护：

1. 真实静态 wrapper/filelist，协议版本和位宽与选定 IP 配置一致；每个 port
   明确唯一驱动者。CPU RTL 活跃时相关内部 VIP 应 passive。
2. 实际 SNPS VIP adapter，使用本机已安装版本的真实 API。确认握手、ID、
   response、错误状态、backpressure 与 monitor 事件，不在模板中猜厂商类名。
3. monitor 用接受/完成事件构造独立观测；不能继续使用 driver 的请求对象
   代替实际响应。处理不同 hop ID 映射、拆分、合并和合法重排。
4. memory service 写入真正响应请求的 VIP backing store；独立预期数据
   模型不得从该 store 取“黄金值”。真实 mirror/alias/interleave 地址统一配置。
5. CMN 入口/出口协议确认。若出口是 CHI，AXI memory VIP 不能直接连接；
   需真实桥或匹配的 subordinate VIP。
6. N2 reset vector、启动模式、互连初始化、image preload、执行地址和结果区；
   先获得真实 RTL 后才可能验证从 DDR 窗口取指执行。
7. CPU profile 的 software_required=true；结果 mailbox 具有本次运行标识，
   cache/属性/barrier 方案保证 TB 可观察。软件 PASS 后仍需排空总线并完成检查。
8. 协议 checker、reference/scoreboard、coverage 与错误结果均做正负测试；
   无组件、零流量、断开的 monitor 不能通过验收。

真实接入时应保留 result/lifecycle 与 testcase contract，更换 backend、
driver/monitor adapter 和 profile-specific boot service；不把 ACVM、
LSF、仿真器命令或固定设计层次写进测试算法。

# dv_sva_lib 0.1.0

一套用于团队统一 SystemVerilog/SVA 写法的独立断言库。默认是纯 SV，不依赖 UVM；可选把失败路由到 UVM report。库只检查信号，不驱动 DUT。

包含 11 个常用宏、ready/valid 检查器、有界响应检查器、FIFO 占用量检查器、非侵入式 `bind` 示例，以及正例和故意违规的负例。它是接入项目的起点，协议参数和接受条件仍需按实际 DUT 确认。

**本机没有可用的商业仿真器，不将静态编译检查等同于仿真通过。实际检查结果、范围和未验证项见 [VALIDATION.md](VALIDATION.md)。** 本库没有修改已有 `SoC_UVM_交付包_20261015` 目录，也没有自动接入实际 DUT。

## 目录与快速接入

```text
include/dv_sva_macros.svh       公共宏、复位及报告约定
checkers/                      三个可实例化检查模块
examples/dv_sva_custom_rules.sv        宏调用示例
examples/demo_pipe_bind.sv      bind 示例
examples/bind_example.f         bind 示例文件列表
tests/cases.json                各用例及预期失败 ID
tests/dv_sva_tb.sv              独立测试平台
scripts/run_tests.py            商业仿真器回归入口
tools/check_compile.py          pyslang 静态编译入口
files.f                        检查模块文件列表
```

先进入库根目录。将 `include/` 加入编译器搜索路径，并把 `files.f` 纳入项目文件列表：

```text
+incdir+include
-f files.f
```

文件列表中的相对路径按库根目录解析；若在其他目录编译，应调整为项目使用的绝对路径或正确的相对路径。只有使用宏的源文件需要写：

```systemverilog
`include "dv_sva_macros.svh"

module req_ack_sva (
  input logic clk, rst_n,
  input logic req, ack
);
  `DV_SVA_KNOWN(a_control_known, ({req, ack}))
  `DV_SVA_NEXT(a_ack_next, req, ack)
endmodule
```

这表示：每个采样为 1 的 `req`，都要求下一采样沿 `ack` 为 1；它没有检查事务配对或禁止同拍响应。并发断言放在 HDL 的 module/interface/checker 等合适作用域中，UVM class 可继续通过虚拟接口产生激励。

## 统一语义

- 所有并发宏默认使用 `@(posedge clk)`，复位参数默认名为 `rst_n`，且必须是**低有效**。
- 统一禁用条件为 `disable iff ((RST_N) !== 1'b1)`：复位为 `0/X/Z` 时禁用，并异步取消正在进行的检查。复位未知时禁用，并不等于检查了复位本身已知。
- 本库宏自己指定时钟和禁用条件，**不依赖 `default clocking` 或 `default disable iff`**。
- 宏调用展开为完整语句/声明，调用后**不加分号**。同一作用域中的 `NAME` 必须唯一；不同实例可以复用相同 ID，通过层次区分。
- 含逗号的参数表达式增加一层括号，例如 `({req, ack})`；避免预处理器把拼接逗号识别为宏参数分隔符。
- X/Z 检测需要四态仿真器验证。仅有二态仿真结果不能证明 unknown 检查有效。

多时钟项目按域显式传入参数；宏固定使用所传时钟的上升沿。真正跨时钟的协议关系应另写专用 property/checker：

```systemverilog
`DV_SVA_ASSERT(a_link_ack, req |=> ack, link_clk, link_rst_n)

// 常量 1'b1 表示这条检查始终启用，从而检查复位本身的 X/Z。
`DV_SVA_KNOWN(a_reset_known, rst_n, clk, 1'b1)
```

`disable iff` 不能等同于在前件增加 `rst_n && ...`：后者不会异步取消已经开始的检查。它也不会自动清除 `$past` 等 sampled-value 函数的历史。

## 11 个用户宏 API

下表省略共有的可选末尾参数 `CLK=clk, RST_N=rst_n`；仅 `ASSERT_IMMEDIATE` 没有这两个参数。`PROP` 是原生 SVA property 表达式，`SEQ` 是覆盖的序列/property 表达式。

| 宏及主要参数                                               | 检查含义                                    |
| ---------------------------------------------------- | --------------------------------------- |
| `DV_SVA_ASSERT(NAME, PROP)`                          | 按统一时钟、复位和报告方式断言 `PROP`                  |
| `DV_SVA_ASSERT_MSG(NAME, PROP, MESSAGE)`             | 同上，附自定义失败消息                             |
| `DV_SVA_COVER(NAME, SEQ)`                            | 覆盖序列；不是断言，也不替代覆盖率分析                     |
| `DV_SVA_KNOWN(NAME, SIGNAL)`                         | 信号所有位均不含 X/Z                            |
| `DV_SVA_KNOWN_WHEN(NAME, SIGNAL, ENABLE)`            | ENABLE 为真时检查信号已知；ENABLE 的已知性须另查         |
| `DV_SVA_ONEHOT(NAME, SIGNAL)`                        | 所有位已知，且恰好一位为 1                          |
| `DV_SVA_ONEHOT0(NAME, SIGNAL)`                       | 所有位已知，且最多一位为 1，允许全零                     |
| `DV_SVA_PULSE(NAME, SIGNAL)`                         | 信号已知，且每个高样本的下一样本必须为低                    |
| `DV_SVA_NEXT(NAME, ANTECEDENT, CONSEQUENT)`          | 前件每个高样本都要求下一样本满足后件                      |
| `DV_SVA_HOLD_WHEN_STALLED(NAME, VALID, READY, DATA)` | 本拍 VALID 且非 READY，下一拍仍有 VALID 且 DATA 不变 |
| `DV_SVA_ASSERT_IMMEDIATE(NAME, EXPR)`                | 立即断言，放在过程语句位置；没有隐含时钟或复位                 |

脉冲宏检查的是**采样宽度**，不检测两个采样点之间的毛刺，也不保证物理脉宽。`HOLD_WHEN_STALLED` 不代替控制和有效数据的 X/Z 检查；需要完整组合时优先用 ready/valid 检查模块。

```systemverilog
`DV_SVA_ONEHOT0(a_grant_onehot0, grant)
`DV_SVA_PULSE(a_done_one_cycle, done)
`DV_SVA_KNOWN_WHEN(a_payload_known, data, valid)
`DV_SVA_ASSERT_MSG(a_mode_legal, mode != 2'b11, "reserved mode")

always_comb begin
  `DV_SVA_ASSERT_IMMEDIATE(a_cfg_limit, cfg_limit <= 16)
end
```

库不统一给 `|=>` 属性增加 `past_valid`：这些规则的后件本身已有上一拍，额外门控可能漏掉复位后的第一笔。自行添加直接使用 `$past(x,N)` 的属性时，需单独定义历史有效条件。

## ready/valid 检查器

```systemverilog
dv_sva_ready_valid #(
  .DATA_WIDTH(32),
  .CHECK_PAYLOAD_KNOWN(1'b1)
) u_tx_sva (
  .clk(clk), .rst_n(rst_n),
  .valid_i(tx_valid), .ready_i(tx_ready), .data_i(tx_data)
);
```

| 参数/端口 | 约定 |
|---|---|
| `DATA_WIDTH=32` | payload 宽度，至少为 1 |
| `CHECK_PAYLOAD_KNOWN=1` | 是否检查 valid 为真时的 payload X/Z |
| `valid_i, ready_i, data_i` | 同一时钟域，均只读 |
| `clk, rst_n` | 上升沿检查，低有效复位 |

独立检查 valid/ready 已知、有效数据已知，以及 `valid && !ready |=> valid && $stable(data)`。即使下一拍 ready 变为 1，发送方仍须在该接受沿保持原来的 valid/data。它不检查收发数据顺序、最大等待时长或交易数量。

主要失败 ID：`a_control_known`、`a_data_known`、`a_hold_on_stall`。`a_data_known` 位于 `g_payload_known` 生成块，只有参数开启时存在。

## 响应电平窗口检查器

`dv_sva_response_window` 的端口为 `clk, rst_n, req_i, rsp_i`。

| 参数 | 默认值 | 含义 |
|---|---:|---|
| `MIN_CYCLES` | 1 | 包含端点的最早响应周期；0 允许同拍 |
| `MAX_CYCLES` | 8 | 包含端点的最晚响应周期，须不小于 MIN |
| `TRIGGER_ON_RISE` | 1 | 1：每个采样上升沿触发；0：req 每个高样本触发 |

核心语义为触发后 `strong(##[MIN_CYCLES:MAX_CYCLES] rsp_i)`，并单独检查 req/rsp 已知。失败 ID 为 `a_control_known` 和 `a_response_window`。

这只要求窗口内出现**响应高电平**：不要求 rsp 上升沿，不作请求/响应一一配对，允许一个 rsp 满足多个重叠请求。过早响应本身不被禁止，但若窗口内没有响应，仍会失败。要验证 ID 匹配、outstanding 数量或严格响应次数，应另建 checker/scoreboard。

上升沿模式使用 sampled `$rose(req_i)`；复位退出时已经持续为高的 req 不保证被当成新请求。若需求是每个高样本都产生义务，使用 `TRIGGER_ON_RISE=0`。

`strong` 要求未完成义务不能在仿真结束时静默通过。正常用例应停止发起新请求、完成响应，再留足 `MAX_CYCLES+1` 个采样沿的 drain 后结束。`response_pending_end` 专门验证目标仿真器是否正确处理尾部未完成义务，不支持时不能把该项算作通过。

## FIFO 占用量检查器

`dv_sva_fifo` 的端口为 `clk, rst_n, push_i, pop_i, full_i, empty_i, count_i`。

| 参数 | 默认值 | 含义 |
|---|---:|---|
| `DEPTH` | 4 | FIFO 深度，至少为 1，支持非 2 次幂 |
| `COUNT_WIDTH` | 足以表示 0..DEPTH | 默认按 `$clog2(DEPTH+1)` 计算，内部先扩宽避免加法溢出 |
| `ALLOW_FULL_REPLACE` | 1 | 满时允许同时执行 push/pop，替换一个元素 |
| `ALLOW_EMPTY_BYPASS` | 0 | 空时是否允许同时执行 push/pop 的直通行为 |

**push/pop 是这个采样沿实际执行的操作，不是可能被拒绝的原始请求。count_i/full_i/empty_i 表示本沿执行操作前的状态。** 若 DUT 对满写、空读请求做了屏蔽，应连接屏蔽后的 fire；若还要检查原始请求本身的合法性，另加对应规则。

检查内容包括：控制/占用量已知、占用量不大于 DEPTH、full/empty 与占用量一致、满写/空读策略，以及下一拍计数变化：

| 本拍执行事件 | 下一采样沿的占用量 |
|---|---|
| 仅 push，且本拍未满 | 本拍 count + 1 |
| 仅 pop，且本拍非空 | 本拍 count - 1 |
| push/pop 同时发生，或均不发生 | 与本拍相同 |

计数运算扩宽一位，避免实际计数和期望表达式同时回绕而漏检。检查器不验证 payload、FIFO 数据顺序或复位期间 count 必须归零，也不支持延迟多拍才更新的占用量/标志；这些行为需要专门适配。

主要失败 ID：`a_control_known`、`a_count_known`、`a_count_range`、`a_full_flag`、`a_empty_flag`、`a_no_overflow`、`a_no_underflow`、`a_count_increment`、`a_count_decrement`、`a_count_stable`。

## bind 与 UVM 接入

[examples/demo_pipe_bind.sv](examples/demo_pipe_bind.sv) 展示把被动检查模块绑定到示例 DUT，不修改 RTL 本体；对应文件列表是 [examples/bind_example.f](examples/bind_example.f)。在库根目录使用 `-f examples/bind_example.f` 编译，并按文件列表选择示例 top。实际接入时，复制并调整 bind 目标类型、参数和信号映射，再加入项目的专用文件列表。

默认失败通过 `$error` 输出。需要进入 UVM 回归统计时，先让 `uvm_pkg` 在编译时可见，再增加：

```text
+define+DV_SVA_USE_UVM
```

失败会调用 `uvm_pkg::uvm_report_error`。库不负责定位或编译 UVM 安装包。报告含固定前缀，例如：

```text
DV_SVA_FAIL a_hold_on_stall | <instance hierarchy> | <message>
```

可在 include 前自定义 `DV_SVA_REPORT_ERROR(NAME, MESSAGE)` 适配项目报告系统；若使用随库回归脚本，保留 `DV_SVA_FAIL <NAME>` 前缀。自定义消息打印失败样本时，优先使用 `$sampled(signal)`，避免打印当前值而与断言采样值不一致。

`+define+DV_SVA_DISABLE_ASSERTIONS` 会有意移除断言，`+define+DV_SVA_DISABLE_COVERS` 会移除覆盖声明。禁用断言的构建不能拿来执行本库自测或证明检查生效。

## 静态检查与仿真回归

静态编译需要 Python 与 `pyslang>=12.1,<13`，安装依赖后在库根目录运行：

```sh
python -m pip install "pyslang>=12.1,<13"
python tools/check_compile.py
python tools/test_runner.py
```

如依赖安装到独立目录，可用 `--pyslang-path <目录>` 指定。静态检查验证语法、宏展开和 elaboration 等编译问题，不执行时序检查，不验证故意违规是否被检出。

仿真脚本通过自身路径定位库根；下面的相对脚本路径假定当前在库根目录：

```sh
python scripts/run_tests.py --list
python scripts/run_tests.py --sim questa --case positive
python scripts/run_tests.py --sim questa
```

也支持 `--sim vcs` 和 `--sim xrun`。可重复使用 `--case` 选择多个用例；不指定时执行全部。其他选项包括 `--tool-dir DIR`、`--build-dir DIR`、`--timeout N`（每次编译/运行默认 120 秒）。`--dry-run` 只打印命令，要求指定 simulator，**不算测试通过**。

默认结果位于 `build/<sim>/`：包含 `compile_N.log`、各 `<case>.log` 及 `results.json`。各用例的预期由 [tests/cases.json](tests/cases.json) 定义。负例只有命中全部预期断言 ID、没有其他库断言 ID，并到达测试完成标记，才被判为自测通过；不是“仿真器任意报错就算抓到问题”。

X/Z 用例要求四态能力，结束前未完成响应用例要求 strong 结束语义。脚本不会为不支持的工具自动降级这些要求。未运行、编译失败、工具不支持与真实通过必须在验证记录中分开说明。

## 团队采用建议与参考

先在目标仿真器上跑完整自测，再选择一个实际接口试接入。统一 assertion ID、复位策略、报告严重级别和覆盖率采集方法；新增公共规则时一并增加正例、故意违规的负例与复位边界测试。协议一旦改变，同时更新检查器和测试，避免仅把代码缩短却改变检查含义。

- [OpenTitan prim_assert.sv](https://github.com/lowRISC/opentitan/blob/master/hw/ip/prim/rtl/prim_assert.sv)：统一报告、默认时钟复位及常用断言封装的工程参考；本库不依赖该文件。
- [IEEE 1800-2017 SystemVerilog 标准（MIT 镜像）](https://fpga.mit.edu/6205/_static/F25/documentation/1800-2017.pdf)：第 16 章给出 SVA、采样、disable iff 与 strong 语义；§23.11 定义 bind。
- [slang / pyslang 官方仓库](https://github.com/MikePopoloski/slang)：静态检查前端及 Python bindings。

## DV_SVA_ASSERT 详解与时序模板

[逐项解释、波形与时序模板库](docs/DV_SVA_ASSERT_详解与时序库.md)。可编译示例源码为 [dv_sva_timing_catalog.sv](examples/dv_sva_timing_catalog.sv)，包含 9 个独立教学模块；按协议选择使用，不要求同时实例化。

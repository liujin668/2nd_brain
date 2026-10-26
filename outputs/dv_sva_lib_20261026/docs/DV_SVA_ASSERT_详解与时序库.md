# DV_SVA_ASSERT 详解与时序模板库

本页对应本地 `include/dv_sva_macros.svh` 的实际实现。模板源码：[dv_sva_timing_catalog.sv](../examples/dv_sva_timing_catalog.sv)。所有 C0/C1 都表示属性时钟的采样沿；波形表中的 `—` 表示该样例不约束，不是四态逻辑 X。

## 作用与参数

`DV_SVA_ASSERT` 是本库提供的预处理宏，不是 UVM 内置方法、task 或运行时函数。它把 SVA property 包装成一条使用统一时钟、复位和失败报告的并发断言。它不产生事务、不驱动 DUT，也不阻塞 sequence/driver。

```systemverilog
`DV_SVA_ASSERT(NAME, PROP, CLK=clk, RST_N=rst_n)
```

| 参数 | 含义 |
|---|---|
| NAME | 断言标签和失败 ID；同一作用域必须唯一 |
| PROP | 原生 SVA property；由它决定检查规则和拍数 |
| CLK | 可选时钟表达式；本宏使用其上升沿，默认信号名 clk |
| RST_N | 可选低有效复位；默认信号名 rst_n |

调用后按库风格不额外加分号。含逗号的宏参数用额外圆括号包住，例如 `({req, ack})`。这些是预处理宏，所以需要先 include，不通过 package import 引入。

```systemverilog
`include "dv_sva_macros.svh"
`DV_SVA_ASSERT(a_req_ack, req |=> ack)
```

在没有定义 `DV_SVA_USE_UVM` 或 `DV_SVA_DISABLE_ASSERTIONS` 时，等价于：

```systemverilog
a_req_ack: assert property (
  @(posedge (clk))
  disable iff ((rst_n) !== 1'b1)
  (req |=> ack)
) else begin
  $error("DV_SVA_FAIL %s | %m | %s",
         "a_req_ack", "property violated");
end
```

`DV_SVA_ASSERT` 先转到 `DV_SVA_ASSERT_MSG`；后者产生真正的 `assert property`。宏显式指定时钟和 disable 条件，不会自动继承其他 default clocking/default disable iff。不要再给 PROP 嵌套另一个 disable iff。

## 一拍请求示例

`req |=> ack` 的意思是：每个采样 req=1 的拍，都要求下一采样拍 ack=1。它不要求 ack 从 0 变 1，不禁止更早 ack，也不验证事务一一配对。

```text
采样沿          C0  C1  C2  C3  C4
req              0   1   1   0   0
ack              0   0   1   0   0

C1 的 req=1 -> C2 检查 ack=1 -> 通过
C2 的 req=1 -> C3 检查 ack=0 -> 失败，报告 a_req_ack
```

检查器不会因为等待 C2 就停止接收新检查。连续 req 会创建重叠的检查义务；它不是顺序执行的 `wait`。如果只想在采样上升沿触发，可写 `$rose(req) |=> ack`；req 在复位退出时已保持高，并不保证出现新的 sampled rising edge。

如果 req=0，则该拍不会产生 ack 检查义务，蕴含在这次尝试中空真通过。关键路径可加 `DV_SVA_COVER(c_req_ack, req ##1 ack)`，区分真正执行成功和从未触发。

## 采样、复位与报错

普通设计信号在 Preponed 区取快照，property 在 Observed 区评估；失败 action block 在 Reactive 区执行。不要把宏理解成在 Observed 重新读取所有 DUT 最新值。

例如 DUT 写 `always_ff @(posedge clk) ack <= req;`，本沿 NBA 才更新的 ack 不属于本沿 property 的沿前快照。req 在 C1 为 1、由此更新 ack 后，SVA 在 C2 才采到该 ack；这时 req |=> ack 符合单拍寄存响应关系。

复位 `disable iff ((rst_n) !== 1'b1)` 使用未采样的当前值，复位为 0/X/Z 时异步取消进行中的尝试；取消不算通过，也不算失败。它不是在前件加 `rst_n && req`。

```text
C1: req=1，产生下一拍检查
C1 与 C2 之间: rst_n=0 -> 取消这次检查
C2: ack=0 -> 被取消的尝试不报失败
```

本库选择未知复位时禁用检查。如需验证 reset 本身已知，另加：

```systemverilog
`DV_SVA_KNOWN(a_reset_known, rst_n, clk, 1'b1)
`DV_SVA_KNOWN(a_controls_known, ({req, ack}))
```

控制信号为 X 可能导致前件不匹配，因此时序检查不能代替 known 检查。复位取消也不会清空 `$past` 等 sampled-value 历史。

失败默认调用 `$error`，并不保证立即终止仿真。启用 `+define+DV_SVA_USE_UVM` 后改用 `uvm_pkg::uvm_report_error`；严重级别和停仿策略由项目配置决定。`+define+DV_SVA_DISABLE_ASSERTIONS` 会将断言展开为空；`DV_SVA_DISABLE_COVERS` 只控制 cover。

失败消息需要打印当次参与检查的值时，使用 `$sampled`：

```systemverilog
`DV_SVA_ASSERT_MSG(a_ack_debug, req |=> ack,
  $sformatf("sampled req=%b ack=%b", $sampled(req), $sampled(ack)))
```

这打印失败拍的采样值；若还要打印发起拍的数据，应另外记录该拍值，不把当前 req 误认为原始请求值。

## 可复制时序模板

各行独立使用，不表示同一个接口同时要求所有规则。延迟/重复参数须在 elaboration 时确定。

| 规则 | PROP 或调用 | A 在 C0 触发时检查哪些拍 |
|---|---|---|
| 同拍满足 | `A \|-> B` | B(C0)=1 |
| 下一拍满足 | `A \|=> B` | B(C1)=1 |
| 第 N 拍满足 | `A \|-> strong(##N B)` | B(CN)=1；不禁止更早的 B |
| MIN..MAX 内响应 | `A \|-> strong(##[MIN:MAX] B)` | 闭区间内至少一个 B=1；不负责请求/响应配对 |
| 只在采样上升沿触发 | `$rose(A) \|=> B` | A 从低采样到高时，下一拍检查 B |
| 单个高样本 | `DV_SVA_PULSE(a_pulse, sig)` | 每个高样本下一拍低，同时检查 sig 已知 |
| 反压保持 | `valid && !ready \|=> valid && $stable(data)` | 下一拍 valid 仍高且 data 与上拍相同，包含接受拍 |
| 连续 N 拍后低 | `start \|=> strong(busy[*N] ##1 !busy)` | busy(C1..CN)=1，busy(CN+1)=0，N>=1 |
| 寄存器捕获 | `load \|=> q == $past(d)` | q(C1) 等于 d(C0) |

调用示例：

```systemverilog
`DV_SVA_ASSERT(a_same, req |-> ack)
`DV_SVA_ASSERT(a_next, req |=> ack)
`DV_SVA_ASSERT(a_three, req |-> strong(##3 ack))
`DV_SVA_ASSERT(a_window, $rose(req) |-> strong(##[1:4] ack))
`DV_SVA_ASSERT(a_hold, valid && !ready |=> valid && $stable(data))
`DV_SVA_ASSERT(a_capture, load |=> q == $past(d))
```

默认宏只提供外壳，不会替任意 PROP 加 strong、known、超时或历史保护。窗口使用 strong，是为了避免结束时尚未完成的序列义务静默弱通过；仍需在目标仿真器核对结束语义，并留出 drain 周期。普通 NEXT/HOLD/PULSE 在结束前至少留一拍。

### 同拍、下一拍、第三拍的区别

```text
A 在 C0 触发     C0  C1  C2  C3  C4
A |-> B          B
A |=> B              B
A |-> ##3 B                  B
A |=> ##3 B                      B
```

最后一行是 4 拍，不是 3 拍。`|=>` 自身已向后移动一拍。如果前件是多拍序列，偏移参考的是前件匹配的结束拍，不是开始拍。

### 反压保持

```text
采样沿           C0  C1  C2  C3
valid             1   1   1   0
ready             0   0   1   —
data              A   A   A   —

C0 stall -> C1 保持
C1 stall -> C2 即使 ready=1，仍保持 data=A 完成接受
```

这些是采样关系，不检测采样间毛刺。针对任意直接引用 `$past(d,N)` 的新规则，要保证已有 N 个有效历史样本；不能用统一 past_valid 去门控所有规则，否则会漏掉复位退出后第一笔反压或脉冲违规。

## 验证状态

新增模板将纳入 `tools/check_compile.py` 的全部配置编译。源库已有 24 个动态用例；本机无 SVA 仿真器，尚未运行动态仿真。静态编译不能证明时序行为通过，结果见 [VALIDATION.md](../VALIDATION.md)。

参考：[本地宏源码](../include/dv_sva_macros.svh)、[IEEE 1800-2017 第16章](https://fpga.mit.edu/6205/_static/F25/documentation/1800-2017.pdf)。

# 验证记录

生成日期：2026-10-26。库版本：0.1.0。

## 已实际完成

| 检查 | 结果 | 说明 |
|---|---|---|
| 默认源码编译、类型检查、展开 | 0 错误，0 诊断 | pyslang 12.1.0；包含 3 个检查器、所有 SV 示例、测试平台与附加参数矩阵 |
| DV_SVA_DISABLE_ASSERTIONS 配置 | 0 错误，0 诊断 | 验证显式关闭断言时的宏展开，不代表检查功能通过 |
| DV_SVA_DISABLE_COVERS 配置 | 0 错误，0 诊断 | 验证关闭 cover 的分支 |
| DV_SVA_USE_UVM 配置 | 0 错误，0 诊断 | 使用只含 uvm_report_error 签名的编译桩；未运行真实 UVM |
| Python 回归结果判定器 | 10/10 通过 | 预期失败 ID、额外 ID、缺完成标记、fatal、许可证错误、超时/崩溃、正例退出码及命令生成 |
| 测试用例清单 | 24 个独立 CASE | 预期结果记录在 tests/cases.json |

机器可读的实际编译记录保存在 [validation/compile_report.json](validation/compile_report.json)。编译参数矩阵额外展开了：零拍响应窗口、逐拍电平触发、一位 payload、关闭 payload-known 检查、FIFO 深度 1 以及禁止满替换/空直通的配置。

编译前端检查了语法、类型、SVA 表达式、参数和 bind 连接；它不会推进时钟，也不会证明某条 assertion 能在动态违规时触发。

## 尚未执行

当前环境未发现 Questa、VCS、Xrun 或其他可用 SVA 仿真器。因此 **24 个 SystemVerilog 测试均未实际仿真**，X/Z 负例、复位中途取消、strong 在仿真结束时的失败行为，也尚未获得目标仿真器验证。

真实 UVM 包的编译、report catcher/回归统计接入，以及实际 DUT 的端口映射尚未验证。源码提供了入口和 bind 示例，没有修改现有 SoC_UVM 工程。

## 在目标环境复现

安装 Python 3.10+；静态编译工具 pyslang 需要 Python 3.11+。在库根目录执行：

```sh
python -m pip install -r tools/requirements-static.txt
python tools/check_compile.py
python tools/test_runner.py
python scripts/run_tests.py --list
python scripts/run_tests.py --sim questa
# 或：python scripts/run_tests.py --sim vcs
# 或：python scripts/run_tests.py --sim xrun
```

仿真器需已安装并可使用许可证。负例只有在预期 assertion ID 全部出现、没有额外 ID、且到达完成标记时才算通过；编译失败、缺工具或崩溃均不能算通过。未实现完整 SVA/四态/strong 结束语义的工具可能拒绝编译或使测试失败，本库不会自动削弱规则来换取通过。

测试结束前保留 drain 周期。NEXT/PULSE/HOLD 使用普通非重叠蕴含，不保证在仿真尾部报告所有未完成义务；response_window 另外使用 strong，专用 response_pending_end 用例用于核对目标工具的尾部行为。

## 时序模板补充

新增 examples/dv_sva_timing_catalog.sv 的 9 个独立模块与宏详解文档后，已重新纳入全部四种静态编译配置。最新结果见 validation/compile_report.json；原有 24 个动态用例没有改动，仍未在本机仿真。

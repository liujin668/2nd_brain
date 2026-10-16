# 服务器 SoC UVM 方案与环境模板

面向单 die、Arm Neoverse N2 加 CMN 的服务器 SoC，首目标为内存模型上的裸机最小冒烟。本交付包包含架构方案、组件接口、测试计划、内网 agent 实施任务书以及可继续开发的环境模板。

现有条件是N2 RTL和SoC集成尚未就绪，CMN型号与内存出口待定；使用VCS、Xcelium、UVM 1.2、Synopsys VIP和LSF。模板独立于ACVM，现有IP流程可通过适配器复用。

## 推荐阅读顺序

| 文件                                      | 解决的问题                                               |
| --------------------------------------- | --------------------------------------------------- |
| [总体架构与实施方案](docs/01_总体架构与实施方案.md)       | 目标、验证分层、目录、阶段路线和职责                                  |
| [组件与接口设计](docs/02_组件与接口设计.md)           | define、package、cfg、clk/reset、SVA、RAL、memory、软件及结果契约 |
| [运行回归与软件镜像说明](docs/03_运行回归与软件镜像说明.md)   | 构建、运行、LSF、回归、覆盖率、复现和镜像链路                            |
| [内网Agent实施任务书](docs/04_内网Agent实施任务书.md) | 把模板接到真实工程的顺序、需要调查的输入和交付证据                           |
| [公开参考与取舍](docs/05_公开参考与取舍.md)           | 公开一手资料、采用的方法以及适用边界                                  |
| [测试计划与验收矩阵](docs/06_测试计划与验收矩阵.md)       | 需求到场景、checker、覆盖与阶段验收的关联                            |
| [模板实现状态与验证记录](docs/07_模板实现状态与验证记录.md)   | 本次实际提供和检查了什么，哪些仍需内网验收                               |
| [模板运行说明](template/docs_flow.md)         | 实际CLI、配置和Python工具链自检                                |
| [模板SV说明](template/docs_sv.md)           | 实际UVM组件、编译关系和正负测试                                   |
| [软件接口与镜像工具](template/native/README.md)  | C平台契约、ELF分段及CPU启动适配                                 |

## 如何交给内网 Agent

把整个目录或同名ZIP送入内网工程工作区。让agent先阅读本README和实施任务书，再盘点真实工程，不要只把单个目录树或某个代码片段作为需求。

可以直接给内网agent这段任务：

> 请阅读本交付包README及docs中的方案，按照04_内网Agent实施任务书.md盘点现有工程并分阶段实现。优先复用已跑通的Synopsys AXI VIP示例和工具环境。先验收工具链和UVM自检，再接真实VIP、CMN和N2。每一步给出真实命令、日志和结果，不把mock或synthetic测试称为SoC验证通过。缺少真实IP接口时列出明确问题，继续完成不依赖该输入的工作。

## 模板的验证层级

- `mock`：Python工具链自检，报告级别为`FLOW_MOCK`。
- `uvm_selftest`：synthetic事务层内存与独立检查链路，并提供静态clock/reset/SVA示例。需要真实EDA工具才能验收SV。
- `vip_selftest`、`cmn_bfm`、`n2_boot`：目标接入阶段，当前未完成的适配明确阻塞。

纯事务层自检没有验证真实AXI总线握手或N2取指。使用memory VIP的N2测试也没有验证被替代的DDRC/PHY/DRAM路径。

完整架构章节描述最终环境目标，实际模板实现范围由07和模板源码说明界定。地址、clock period、队列和工具命令中的演示值不能直接作为芯片规格。

## 开始使用

进入`template`，先阅读`docs_flow.md`并查看命令帮助：

```sh
python3 script/socflow.py --help
python3 script/socflow.py doctor --profile mock
python3 script/socflow.py regress --suite regress/mock_smoke.json --jobs 2
python3 script/socflow.py regress --suite regress/mock_negative.json
```

如需设置工程根目录，在 `template` 目录中按当前 shell 选一条执行：

```sh
# bash/sh
. ./env_setup.sh
# csh/tcsh
source ./env_setup.csh
```

这两个入口只设置 `SOC_UVM_ROOT`；公司的工具、VIP 和许可证环境继续使用现有初始化方式。

Python工具链使用标准库。真实VCS/Xcelium运行需要在内网配置已有工具和UVM，不要求升级系统库。软件平台接口尚待实现，未配置的固件入口明确拒绝编译。

## 交付原则

每个实际信号有明确owner，checker与被检查对象独立；每个测试有能力要求、预期结果和结束条件；每次运行有独立身份及复现记录。无法证明完成、没有有效检查、存在非预期错误的运行不会被当作业务PASS。

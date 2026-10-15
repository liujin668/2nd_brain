# 独立运行与回归模板

此模板不依赖 ACVM。Python 3.8+、标准库；使用公司已有解释器，不要求 sudo 或系统库升级。Makefile 仅是可选薄入口。运行命令均从 template 根目录执行。

## 交付范围

| profile | 本模板状态 | 能说明什么 |
|---|---|---|
| mock | 可实际运行 | Python 流程、超时、结果契约和报告；绝不是 SV/SoC 验证 |
| uvm_selftest | 需要 site 真实命令 | SV/UVM 自测；不含真实 N2/CMN/SNPS VIP |
| vip_selftest | BLOCKED | 需接入授权 VIP 与真实协议fixture |
| cmn_bfm | BLOCKED | 需接入 CMN、请求端 BFM、内存模型及一致性检查 |
| n2_boot | BLOCKED | 需接入 N2/CMN、启动地址、镜像加载和软件结束握手 |

后 3 项默认拒绝运行，dry-run 也不能绕过。内网 agent 完成真实接入并验证后才可修改 profiles.json 的 readiness 状态；只改状态不构成验收。LSF、coverage merge 同样明确 BLOCKED，见后文。

## 立即可用命令

~~~sh
python3 script/socflow.py contracts
python3 script/socflow.py doctor --profile mock
python3 script/socflow.py validate --suite regress/mock_smoke.json
python3 script/socflow.py build --profile mock
python3 script/socflow.py run --profile mock --seed 666 --timeout 10
python3 script/socflow.py regress --suite regress/mock_smoke.json --jobs 2
python3 script/socflow.py regress --suite regress/mock_negative.json
python3 script/socflow.py run --profile mock --scenario late_error
python3 script/socflow.py regress --suite regress/mock_smoke.json --dry-run
python3 -m unittest discover -s tests_flow -v
~~~

late_error 命令应失败；这是结果契约检查，并非失败的芯片测试。默认输出在 regress/out。可用 --out 指定其他运行区。regress 的 profile 来自 suite 文件，避免同一个 suite 被 CLI 偷换验证层级。

~~~sh
python3 script/socflow.py report <run目录或regression目录>
python3 script/socflow.py repro <原run目录>
python3 script/socflow.py run --profile mock --build <build目录> --seed 777
python3 script/socflow.py config --design config/design.example.json --out config/generated/demo_01
~~~

config 仅生成 SV package、C header 和规范化 JSON；例子中的地址是演示值，不是真实 SoC 地址，生成结果也不会自动接入 DUT。重复生成到已有目录会被拒绝。

退出码：0 表示该命令完成或回归契约满足；1 表示失败；2 表示 BLOCKED。dry-run 输出 PLANNED，未执行任何仿真，不能算 PASS。validate 只校验清单结构；doctor 对真实后端只确认配置格式，不执行工具或声明许可证可用。

## 文件职责

- script/flow_common.py：配置、路径、hash、argv、进程组及超时。
- script/flow_engine.py：构建、独立run、manifest、worker、复现。
- script/flow_result.py：严格判定及 JSON/CSV/JUnit。
- script/flow_suite.py：冻结用例/seed、限制本地并发、完整性检查。
- script/flow_config.py：统一地址常量生成。
- script/job_worker.py：节点侧执行一个已准备的manifest；不负责提交LSF。
- script/mock_sim.py：可控假进程，专门验证流程故障路径。
- script/lsf_adapter_template.py：待完成接口，所有动作抛 NotImplementedError。
- config/site.example.json：禁用状态的站点配置，不提供虚假的仿真器命令。

## 接入 VCS / Xcelium

复制 site.example.json 为公司自己的 site.json。每个适配器明确设置 enabled、tool_identity、build_argv、可选 elaborate_argv、run_argv、build_inputs、build_artifacts、环境和日志规则。

argv 必须是字符串数组，每个参数单独一项；不使用 shell=True，不拼接一整条命令。支持占位符：

- {project_root}、{build_dir}、{run_dir}、{result_file}
- {profile}、{test}、{seed}、{run_id}、{python}

例如“调用本公司的真实wrapper”是允许的模式，但本交付包没有替你假造wrapper路径或工具flag。build_cwd 默认 project_root，便于 flist/uvm_selftest.f 的相对路径；run_cwd 默认独立 run_dir。SV selftest 两个top是 soc_hdl_top、soc_hvl_top；如何选择 top、UVM1.2、语言版本、seed、库和工作目录由已安装工具适配器决定。run_argv 必须把 {seed} 映射到该仿真器的实际随机种子机制；SOC_SEED只用于契约/软件侧记录，不能被假定为仿真器原生随机种子选项。

runner 自动追加并保留以下参数，site run_argv 和 --extra-arg 不得重复覆盖：

~~~text
+SOC_RUN_ID=<unique>
+SOC_RESULT_FILE=<absolute-json-path>
+SOC_SEED=<seed>
+UVM_TESTNAME=<class>
+SOC_PROFILE=uvm_selftest
~~~

tool_identity 由站点填写实际版本；模板不把它当成已执行版本探测。version_argv 是给后续 doctor 增强预留的字段，当前不执行。若依赖环境初始化，用已审查的wrapper执行source再exec工具；wrapper必须等待子进程结束并传播退出码，不能后台启动后立即返回0。不要把凭据写入site：manifest会保存适配器快照。

build_inputs 要列出 wrapper、filelist、RTL/TB、include、生成配置、镜像等实际输入；build_artifacts 列出独立 build_dir 下要校验的实际文件，包括运行所需库/快照文件。当前只支持文件清单，不自动展开依赖或递归校验库目录。未完整列出间接依赖前不能承诺完全复现。

VCS与Xcelium分开构建。没有自动构建缓存：每次build均为唯一目录。显式 --build 和 repro 会检查已列出的源文件与产物hash；这不会凭空补全未声明依赖。命令、profile、工具身份及输入摘要均写入manifest。

native_error_patterns 必须使用站点实际编译/仿真日志验证后填写，并将 log_contract_acknowledged 设为 true。内置规则仅捕获真正的UVM_ERROR/UVM_FATAL消息和 SOC_FLOW_ERROR/SOC_ASSERT_ERROR/SOC_ASSERTION_ERROR，排除 UVM_ERROR : 0 等summary行；不会泛搜 error 单词。原生SVA/仿真器错误仍要通过明确规则和TB计数接通，尤其要测试“写PASS后再报错”。日志规则只是辅助，不能替代完整结束判据。

~~~sh
python3 script/socflow.py doctor --profile uvm_selftest --simulator vcs --site config/site.json
python3 script/socflow.py regress --suite regress/uvm_selftest.json --simulator vcs --site config/site.json
python3 script/socflow.py regress --suite regress/uvm_negative.json --simulator vcs --site config/site.json
~~~

将 simulator 改为 xcelium 运行另一后端。本文命令仅在site真实接入后可执行；本地mock测试不证明这些EDA命令有效。

## 严格结果契约

tb_result.json 的所有字段见 contracts 命令。runner核对 schema_version、run_id、profile、test、seed，以及：

- completed 必须是真正的JSON boolean true；
- stimulus_count/checks_count 达到profile最低值，pending_count为0；
- 计数字段必须是int，不能用boolean冒充；
- 普通通过必须 status=PASS、failures为空、UVM/assertion错误计数均为0；
- software_required由runner profile决定，不能由TB自行选择NOT_REQUIRED；
- 需要软件时软件状态必须PASS，不需要时必须NOT_REQUIRED；
- 进程必须正常结束且退出码0，日志无非预期错误；
- 缺结果、截断结果、旧run_id、未完成、写PASS后崩溃均失败。

每个run有原子 worker.claim，拒绝再次执行和覆盖结果。独立进程组超时后先结束再回收；Windows路径仅服务模板本地自测，目标部署为Linux。wrapper不得把子进程脱离进程组；集群作业另需LSF取消协议。

normal suite不能配置expected_failures。专门的 negative_selftest suite需要精确ID数组（含重复次数），只有正常完整结束、无额外基础设施/日志问题且ID完全一致才记 acceptance=EXPECTED_FAILURE。原始run.status仍为FAIL，JUnit记录negative属性；没有把普通失败转换为PASS。

uvm_negative.json选择soc_selftest_mismatch，预期失败ID为DATA_MISMATCH、UVM_ERROR各一次。该精确集合应在真实EDA首次执行后核对；如果代码或实际结果改变，调查原因，不要扩大正则吞掉未知错误。

## 报告与复现

每次run保存manifest、command、process、sim.log、tb_result及result；回归冻结plan和全部case/seed，记录已建立的run目录。report输出summary.json、summary.csv、junit.xml。缺结果/未启动case保持INCOMPLETE，不能从分母消失。mock报告始终带FLOW_MOCK。

repro保留原test、seed、命令适配器、构建及输入摘要，创建新目录并关联parent_run。源码/产物变更会拒绝复现；移动整个工程后需显式调整站点路径并重建。固定seed仍不能消除RTL/TB竞争或外部模型非确定性。本版不支持自动重试、断点恢复、远端产物传输、自动源码checkout；不要将其描述成已实现。

## LSF接入契约（尚未实现，选择 --scheduler lsf 会BLOCKED）

job_worker.py可在计算节点执行已冻结的run manifest；当前控制器只完成本地调用。内网agent需实现独立“prepare manifest而不本地执行”的提交路径，然后完成：

1. 提交前持久化唯一submission_token、回归归属、资源请求；submit返回并立即保存job ID/cluster。
2. argv调用bsub；队列、内存单位、许可证资源、核数以本站配置为准。
3. 如果采用bsub -K，仍需及时得到job ID；等待超时/中断时必须能按ID取消。只kill本地bsub进程不算取消远端作业。
4. query批量查询live/history；PEND/RUN/挂起/UNKWN/DONE/EXIT各自保留，查询缺失要处理记账延迟。
5. 分离排队超时、运行墙钟超时、仿真时间超时；超时/取消按持久化ID处理并确认终态。
6. DONE只是作业脚本退出0；worker result缺失仍INCOMPLETE。job script必须传播worker原始退出码。
7. exact negative测试可以对应LSF EXIT，但需确认是worker功能失败且完整结果匹配；基础设施异常不能按预期负测接受。
8. 控制器恢复后查询原job，不能盲目重新提交；cancel只操作本回归确认拥有的job。
9. 增加提交响应丢失、重复提交防护、取消、节点失联、内存超限、许可证等待、历史查询延迟的验收。

没有上述验收之前保留TEMPLATE_ONLY；不应设置enabled=true来绕过实现。

## 覆盖率合并契约（尚未实现，coverage命令会BLOCKED）

保留各run的独立coverage产物。后续适配器按工具/版本、DUT配置和层次、elaboration/插桩选项、covergroup schema、testplan/exclusion版本分组；VCS与Xcelium数据库不直接混合。签核默认合并有效PASS数据，负测与失败数据另存诊断；检查缺库、空库、重复来源、合并退出码及报告输入清单。跨配置需求覆盖可在报告层汇总，但不能任意混数据库制造总体百分比。

## 流程自身验收

tests_flow含正常、功能失败、无完成、缺/坏结果、崩溃、超时、晚到错误、旧run_id、空检查/空刺激、未排空事务、软件契约、JSON类型、并发、不覆盖、重跑、旧产物拒绝、BLOCKED、dry-run、配置重叠、回归缺结果测试。仅用于验证框架。真实后端仍需分别做成功、checker注错、未完成、超时和晚到错误验收。

### 负测的额外计数约束

negative_selftest 的每个case还必须设置 expected_counts，精确包含 uvm_errors、uvm_fatals、assertion_errors；同时设置 expected_log_counts，规定每个允许UVM_ERROR日志ID出现的准确次数。日志计数总和必须等于预期uvm_errors，fatal负测不属于当前完整结束契约。

当前UVM负测配置为 expected_counts={"uvm_errors":1,"uvm_fatals":0,"assertion_errors":0}，expected_log_counts={"DATA_MISMATCH":1}。即使TB按ID去重，仅保留一个DATA_MISMATCH，额外同ID错误也会因计数不符而失败；即使结果文件已写完，随后出现同ID错误也会因日志次数超限而失败。不能通过只扩大allowed ID集合接收未知错误。

---
type: reference
status: draft
topics:
  - "[[CHI-MOC]]"
aliases: []
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: []
evidence: derived
verification: md-checked
created: 2026-09-09
updated: 2026-09-09
---

# CHI-知识库维护约定

本页是知识库编辑约定，不是 CHI 协议要求。

## 目录与类型

00_spec 保存来源；01_maps 保存 MOC；02_concepts 保存概念与理论模型；03_mechanisms 保存方法和机制；04_transactions 保存事务；05_cases 保存案例；06_reference 保存查询资料；07_questions 保存疑点；90_assets 预留已核实图示。

## 公共 YAML

- type：source / moc / concept / mechanism / transaction / case / reference / question。
- status：draft / reviewed / needs-review。首批保持 draft，不将生成等同于技术审核通过。
- topics：主题 MOC 链接列表；aliases：别名列表；tags：少量标签。
- sources：来源链接；spec_issue：解释依据版本，不等于功能引入版本。
- source_sections：章节号列表；多来源时在正文逐条对应。
- evidence：paraphrase / derived / mixed。清洗 Source 的英文正文为原文保留；其清洗说明为编辑说明。
- verification：md-checked / pdf-checked / needs-check。md-checked 仅表示所引文字已核对，不意味着整个章节的所有图表都核对过。
- created、updated：创建和实质更新日期。

## 证据和不确定性

重要结论标章节，末尾链接清洗 Source 的原始行号分段。涉及损坏图表、来源矛盾或材料不足时写“待确认”，进入 [[CHI-转换文本疑点]]，不推断缺失细节。

Source 的分段以原文件每 120 行为边界；便于确定性追溯，不将这些分段当作知识对象。原文短语粘连没有猜测修复。清洗 Source 不代替原文件。

## 避免重复与无效链接

新增前检查已有标题、别名和 [[CHI-事务索引]]。优先扩充已有 Note；仅在主题可以独立回答一个问题时拆分。链接必须有归属、依赖、应用、对照或证据意义。

例如 ReadShared 与 ReadUnique 当前合并比较，DMT/DCT/DWT 当前合并解释，P-Credit/L-Credit/Retry 当前共同解释。以后内容增长可拆分，但保留原入口导航，不复制两份解释。

## 范围

首批是核心知识层，不是完整逐条实现手册。C1 字段表、C2 合法通信矩阵、详细状态转移和全部波形尚未逐项清洗核验；应从 Source 回查，不能认为未整理的内容不重要。

后续更新采用“原文证据 → 中文规则与条件 → 必要链接 → 核对标记”的顺序。新版本保留旧 Source，不覆盖旧版本依据。

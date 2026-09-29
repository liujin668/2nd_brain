---
type: question
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: [CHI各种ID如何理解和记忆]
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: ["B2.4", "B2.5", "B3.3"]
evidence: mixed
verification: md-checked
created: 2026-09-10
updated: 2026-09-10
---

# CHI-如何理解和记忆各种ID

## 问题

B2.5 的事务流程中出现 ReturnNID、ReturnTxnID、HomeNID 等字段，如何理解它们的用途并记忆？

## 如何附加特殊ID
如果HN接到RN的req后向下游发req，则把RN的SrcID和TxnID放到ReturnNID和ReturnTxnID中给SN；
SN回给HN的flit，TxnID为HN的TxnID，其余的不需要，因为反正不去RN；
SN回给RN的flit，TxnID为RN的TxnID，HomeNID和DBID为HN的，方便RN继续完成给HN的应答；
RN回给HN的flit，TxnID为HN的TxnID，其余的不需要，因为反正不去SN；

FwdNID,FwdTxnID同理，是HN接到RN的req后向snoopee发req，则把RN的SrcID和TxnID放到FwdNID和FwdTxnID中给SN；

一旦需中转，加2个ID，如果是回复DBID，加一个ID.


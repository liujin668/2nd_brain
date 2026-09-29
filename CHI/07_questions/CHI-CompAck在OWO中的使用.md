---
type: question
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: ["CompAck在OWO中的使用"]
tags: [chi]
sources: []
source_sections: []
evidence: personal-notes
verification: unverified
updated: 2026-09-30
---

# CHI-CompAck在OWO中的使用

## 问题

Comp 和 CompAck 在 OWO、Streaming Ordered Write 及其优化流程中分别起什么作用？

> 以下保留原始推理，仅作结构整理，尚未根据协议核实。消息名称、适用条件及可见性结论均待核对。

## 普通 OWO：生产者与消费者的例子

中午思考了一下compack在owo中的使用，想通了comp和compack的具体作用及重要反例：假设要RN0要往地址A写数据DATA0，往地址B写数据DATA1，要求一定要先写进A，再写进B，因为RN1读到B的DATA1后会取DATA0,这个一个常见的生产者消费者flag模型。我们再复杂一点，让2个交易去往不同的HN,A->HN0,B->HN1。在OWO模式中，A的REQ发送完后，等到HN回复COMP，代表HN保证后续的REQ一定排在A之后，此时可以发B这个transaction。即使A的writedata还没有发，而B整个交易已经完成，但是此时别的RN如果来查询A的话，HN_0给SN_0的req会考虑ReadAfterWrite(这个由HN和SN之间的读写机制保证)，所以别的RN在A实际写入之前，不会读到数据，尽管读req在时间线上甚至比实际写入SN_0还早；

## Streaming Ordered Write：提前发请求与 CompAck

   但是这么做的缺点是还不够效率，所以streaming ordered write transaction进行了改进，改进的方法是，增加了ExpCompAck。这样第二笔写B的req不需要依赖于第一笔A的comp(而是接受到前一笔的DBID或者comp就行，因为代表HN建序处理)，既然req提前发了，那如何保序呢？由hn承担责任，通过compack来保证前序A comp了再让后续的B flag可见。compack除了代表接受到本笔的dbid or comp之外，还需要代表之前的所有ordered write的Comp都收到了。HN必须在本笔的CompAck收到后，才让本笔的写被全体RN所见。这里考虑2个场景，在普通OWO中，如果不等comp，而是在dbid收到后就继续进行B会怎么样：B完成了，全局可见，而A还不全局可见，读到的是旧值。在streaming OWO中，如果HN不等待下一笔CompAck，就让全局可见，会怎么样：没有compAck，则新的读可能直接读到了B，由于streaming没有等comp就发了，所以A的comp无法保证，此时读A可能是旧值。

## 进一步优化：不同 Target

进一步提升，如果是A和B是写不同的target，其实都不需要等前一个的dbid或者comp再发下一个，因为compack本身保证了前序的comp，而之前的等待dbid or comp实际是等hn建序，防止hn的建序前后颠倒从而死锁，但是现在destination不同的话天然不会死锁。

## 总结与类比

   精妙呀，今天的重点再理一下：dbid和comp都能保证hn建序干活，但是只有comp代表hn搞定后续的读，hn保证其他rn能读到新值，即使此时新值还没从rn0发给sn，hn会hang住rn1的读请求；也就是事实的读被hang住，直到写值写进去了，这样就可以让2笔写的实际写入数据的时间不需要顺序。类似于出自可以先做后面的菜，但是服务员永远按顺序端菜，则呈现的宴席顺序不会错。如果不等comp，req提前发来提高效率，那么通过compack来反应comp的完成。

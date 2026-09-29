---
type: question
status: draft
topics:
  - "[[CHI-事务与数据路径-MOC]]"
aliases: [CHI DAT单拍传输]
tags: [chi]
sources: ["[[CHI-Source-IHI0050H]]"]
spec_issue: "H"
source_sections: ["B2.9.4", "B2.9.5", "B4.2.1", "B4.2.3"]
evidence: mixed
verification: md-checked
created: 2026-09-10
updated: 2026-09-10
---

# CHI-256bit数据接口何时只传一拍

## 问题

DAT 数据宽度为 256 bit，一条 64 B cache line 通常需要两拍。是否可以只传一拍，例如读写 Size 为 32 B？

## 回答

**可以，但要区分事务 Size、有效字节数和整行大小。** 此处 256 bit 指 DAT 的 Data 载荷宽度，不包括其他字段；一拍可承载 32 B。

不使用 Limited Data Elision 时，数据分包数量由 Transaction Size 和 Data_Width 决定，不能只数 BE 中的有效字节。

| 场景 | 数据拍数 | 原因 |
| --- | --- | --- |
| ReadNoSnp，Size=32 B | 1 | 支持小尺寸读 |
| WriteNoSnpPtl，Size=32 B | 1 | 支持小尺寸写，BE 指定有效字节 |
| ReadShared / ReadUnique，Size=64 B | 2 | 这类读取完整缓存行的事务要求 64 B |
| WriteBackPtl，仅 32 B 有效 | 2 | 请求 Size 仍为 64 B，另一拍 BE 全零也不能自行省略 |

Issue H 的 ReadOnce 也允许小于整行的 Size；不要直接把此规则套用于所有旧版本。

**CPU 访问大小不等于 CHI REQ.Size。** CPU 读取 32 B 若触发 ReadShared 缓存填充，仍会返回完整 64 B、共两拍。只有实际发出的 opcode 允许小尺寸，并设置相应 Size，才能按小尺寸分包。32 B 在 REQ.Size 中编码为 0b101，64 B 编码为 0b110。

## DataID 不是从零开始的拍序号

256-bit 接口上的 DataID 标识数据在 64 B 行中的位置：

- 低 32 B：DataID=0b00。
- 高 32 B：DataID=0b10。

例如对齐的 ReadNoSnp，Addr=0x1020、Size=32 B，只返回一拍，DataID=0b10。字节放在自然 byte lane 位置，不能任意移位。

## 特例：64 B 事务也可能只发送一拍

支持并允许使用 **Limited Data Elision** 时，零值或重复数据拍可以由 NumDat、Replicate 表示，无需实际发送。

对于 256-bit 数据接口和 64 B 请求，可以用 NumDat=0b01 表示省略一拍；Replicate 指示被省略数据为零或复制所发送的数据。具体字段及适用约束需遵守 B2.9.5。

此时逻辑上仍传输了 64 B，接收端重建被省略的部分。**不能因半行无效就擅自省拍，也不能把数据省略误判成 Size=32 B。**

## 波形检查顺序

1. 看 opcode 是否允许小尺寸事务。
2. 看 REQ.Size 和地址。
3. 看数据宽度及 DataID。
4. 看 BE，再检查是否启用数据省略及 NumDat、Replicate。

## 相关笔记与原文依据

- [[CHI-通信粒度]]、[[CHI-通道与方向]]、[[CHI-ReadShared与ReadUnique]]。
- [[CHI-Source-IHI0050H#原文 L6841|B2.9.4 数据分包]]：原始 CHI.md 第 6907 行起。
- [[CHI-Source-IHI0050H#原文 L6961|B2.9.5 Limited Data Elision]]：原始 CHI.md 第 6987 行起。
- [[CHI-Source-IHI0050H]]：B4.2.1 读属性表、B4.2.3 写属性表，核对每种 opcode 的合法 Size。

依据 Issue H；已核对转换文本，未对全部原始 PDF 图表做视觉核验。

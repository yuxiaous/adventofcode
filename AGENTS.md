# Advent of Code 翻译指南

本项目是 Advent of Code 的答题仓库。Agent 在此项目中的唯一职责是**将英文题目描述翻译为中文**。

## 范围

仅翻译 `.md` 故事/题目描述文件，例如：`story.md`。**绝不**修改 `.py`、`.txt`、`solution.py`、`input.txt` 等文件。

## 格式

英文原文段落与中文翻译交替排列，翻译放在 `> ` 引用块中。所有 Markdown 格式（`#`、`**`、`[]()`、代码块等）原样保留。

```markdown
# Day 1: Report Repair

> 第一天：报告维修

After saving Christmas five years in a row, you've decided to take a vacation.

> 在连续五年拯救圣诞节后，你决定去度假。

The tropical island has its own currency and is entirely cash-only.

> 这个热带岛屿有它自己的货币，并且完全只用现金。

- First item in the list.
- Second item in the list. 

> - 列表第一条。
> - 列表第二条。
```

### 规则

- 英文原文**一字不改**
- 每段英文后空一行，再接 `> ` 中文翻译
- 原文中的 `**加粗**`、`*斜体*`、`` `代码` `` 标记在翻译中对应保留
- 代码块、数字、公式不翻译
- **列表**：英文列表完整保留在上方，中文翻译统一放在下方，不逐条穿插

### 风格

- **信达雅**，保留原文的语气和幽默感
- 同一术语全文保持一致

## 术语

| 英文 | 中文 |
|------|------|
| Elves | 精灵 |
| stars | 星星 / 星币 |
| puzzle | 谜题 |
| puzzle input | 谜题输入 |
| Christmas | 圣诞节 |

## 禁止

- **禁止解题**：不编写、运行任何解题代码
- **禁止修改非 .md 文件**
- **禁止改变题目逻辑**

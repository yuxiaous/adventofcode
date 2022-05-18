# [Day 10: Syntax Scoring](https://adventofcode.com/2021/day/10)

> 第10天：语法评分

You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

> 你要求潜水艇确定离开深海洞穴的最佳路线，但它只回答：

```'
Syntax error in navigation subsystem on line: all of them
```

> 导航子系统语法错误。出错的行：全部。

**All of them?!** The damage is worse than you thought. You bring up a copy of the navigation subsystem ([your puzzle input](day10.txt)).

**全部？！** 损伤比你想象的还严重。你打开了一份导航子系统的副本（[你的谜题输入](day10.txt)）。

The navigation subsystem syntax is made of several lines containing **chunks**. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must **open** and **close** with one of four legal pairs of matching characters:

> 导航子系统的语法由包含**块**的一些行组成。每行可以包含一个或多个块，并且块包也可以包含其他的块。相邻的块直接没有分隔符分隔。如果一个块停止，下一个块（如果有）可以立即开始。每个块必须由四个合法的且互相匹配的字符对之一进行**打开**和**关闭**：

- If a chunk opens with `(`, it must close with `)`.
- If a chunk opens with `[`, it must close with `]`.
- If a chunk opens with `{`, it must close with `}`.
- If a chunk opens with `<`, it must close with `>`.

> - 如果一个块用 `(` 打开，它必须用 `)` 关闭。
> - 如果一个块用 `[` 打开，它必须用 `]` 关闭。
> - 如果一个块用 `{` 打开，它必须用 `}` 关闭。
> - 如果一个块用 `<` 打开，它必须用 `>` 关闭。

So, `()` is a legal chunk that contains no other chunks, as is `[]`. More complex but valid chunks include `([])`, `{()()()}`, `<([{}])>`, `[<>({}){}[([])<>]]`, and even `(((((((((())))))))))`.

> 因此，`()` 是一个合法块，它不包含其他块的。`[]` 也是合法的。更复杂但有效的块包括 `([])`、`{()()()}`、`<([{}])>`、`[<>({}){}[([]) <>]]`，甚至是 `((((((((())))))))))`。

Some lines are **incomplete**, but others are **corrupted**. Find and discard the corrupted lines first.

> 有些行是**不完整的**，还有一些其他的行是**损坏的**。首先找到并丢弃损坏的行。

A corrupted line is one where a chunk **closes with the wrong character** - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

> 在一个损坏的行中，它的块是**以错误的字符关闭的** -- 也就是说，它打开和关闭的字符不是上面列出的四个合法字符对之一。

Examples of corrupted chunks include `(]`, `{()()()>`, `(((()))}`, and `<([]){()}[{}])`. Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

> 几个损坏的块的例子，包括 `(]`、`{()()()>`、`(((()))}` 和 `<([]){()}[{}])`。这样的块可以出现在一行中的任何位置，并且它的存在会导致整行被认为是损坏的。

For example, consider the following navigation subsystem:

> 例如，考虑下面的导航子系统：

```'
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
```

Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

> 有些行没有损坏，只是不完整。你现在可以先忽略这些不完整的行。剩下的五行是损坏的：

- `{([(<{}[<>[]}>{[]{[(<()>` - Expected `]`, but found `}` instead.
- `[[<[([]))<([[{}[[()]]]` - Expected `]`, but found `)` instead.
- `[{[{({}]{}}([{[{{{}}([]` - Expected `)`, but found `]` instead.
- `[<(<(<(<{}))><([]([]()` - Expected `>`, but found `)` instead.
- `<{([([[(<>()){}]>(<<{{` - Expected `]`, but found `>` instead.

> - `{([(<{}[<>[]}>{[]{[(<()>`) - 应为 `]`，但发现的是 `}`。
> - `[[<[([]))<([[{}[[()]]]` - 应为 `]`，但发现的是 `)`。
> - `[{[{({}]{}}([{[{{{}}([]` - 应为 `)`，但发现的是 `]`。
> - `[<(<(<(<{}))><([]([]()` - 应为 `>`，但发现的是 `)`。
> - `<{([([[(<>()){}]>(<<{{` - 应为 `]`，但发现的是 `>`。

Stop at the first incorrect closing character on each corrupted line.

> 在每个损坏的行中，在第一个不正确的结束字符处停止。

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the **first illegal character** on the line and look it up in the following table:

> 你是否知道语法检查器实际上有竞赛，看谁能从文件中获得语法错误的高分？这是真的！要计算一行语法错误的分数，取该行的**第一个非法字符**，并在下表中查询：

- `)`: `3` points.
- `]`: `57` points.
- `}`: `1197` points.
- `>`: `25137` points.

> - `)`：`3` 分。
> - `]`：`57` 分。
> - `}`：`1197` 分。
> - `>`：`25137` 分。

In the above example, an illegal `)` was found twice (`2*3 =` **`6`** points), an illegal `]` was found once (**`57`** points), an illegal `}` was found once (**`1197`** points), and an illegal `>` was found once (**`25137`** points). So, the total syntax error score for this file is `6+57+1197+25137 =` **`26397`** points!

> 在上面的例子中，非法的 `)` 被发现了两次（`2*3 =` **`6`** 分），非法的 `]` 被发现了一次（**`57`** 分），非法的 `}` 被发现了一次（**`1197`** 分），非法的 `>` 被发现了一次（**`25137`** 分）。所以，这个文件的语法错误总分是 `6+57+1197+25137 =` **`26397`** 分！

Find the first illegal character in each corrupted line of the navigation subsystem. **What is the total syntax error score for those errors?**

> 在导航子系统的每个损坏行中查找第一个非法字符。**这些错误的语法错误总分是多少？**

Your puzzle answer was `339537`.

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

## --- Part Two ---

Now, discard the corrupted lines. The remaining lines are **incomplete**.

> 现在，丢弃损坏的行，剩下的行是**不完整的**。

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out **the sequence of closing characters** that complete all open chunks in the line.

> 不完整的行没有任何不正确的字符 -- 相反的，它们是在行尾缺少一些结束字符。要修复导航子系统，你只需找出**结束字符的顺序**，让它们与行中所有打开字符向匹配。

You can only use closing characters (`)`, `]`, `}`, or `>`), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

> 您只能使用结束字符 (`)`、`]`、`}` 或 `>`），并且必须以正确的顺序添加它们，以便组成合法的配对，并且让所有块最终都闭合。

In the example above, there are five incomplete lines:

> 在上面的例子中，有五个不完整的行：

- `[({(<(())[]>[[{[]{<()<>>` - Complete by adding `}}]])})]`.
- `[(()[<>])]({[<{<<[]>>(` - Complete by adding `)}>]})`.
- `(((({<>}<{<{<>}{[]{[]{}` - Complete by adding `}}>}>))))`.
- `{<[[]]>}<{[{[{[]{()[[[]` - Complete by adding `]]}}]}]}>`.
- `<{([{{}}[<[[[<>{}]]]>[]]` - Complete by adding `])}>`.

> - `[({(<(())[]>[[{[]{<()<>>` - 通过添加 `}}]])})]` 完成。
> - `[(()[<>])]({[<{<<[]>>(` - 通过添加 `)}>]})` 完成。
> - `(((({<>}<{<{<>}{[]{[]{}` - 通过添加 `}}>}>))))` 完成。
> - `{<[[]]>}<{[{[{[]{()[[[]` - 通过添加 `]]}}]}]}>` 完成。
> - `<{([{{}}[<[[[<>{}]]]>[]]` - 通过添加 `])}>` 完成。

Did you know that autocomplete tools **also** have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of `0`. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

> 你是否知道自动完成工具**也**有比赛？这是真的！分数是通过考虑补完的字符串中的逐个字符来确定的。从总分 `0` 开始。然后，对于每个字符，将总分乘以 5，然后将总分乘以下表中为该字符提供的分值：

- `)`: `1` point.
- `]`: `2` points.
- `}`: `3` points.
- `>`: `4` points.

> - `)`: `1` 分.
> - `]`: `2` 分.
> - `}`: `3` 分.
> - `>`: `4` 分.

So, the last completion string above - `])}>` - would be scored as follows:

> 因此，上面的最后一个补完字符串 -- `])}>` -- 将得到如下的评分：

- Start with a total score of `0`.
- Multiply the total score by 5 to get `0`, then add the value of `]` (2) to get a new total score of `2`.
- Multiply the total score by 5 to get `10`, then add the value of `)` (1) to get a new total score of `11`.
- Multiply the total score by 5 to get `55`, then add the value of `}` (3) to get a new total score of `58`.
- Multiply the total score by 5 to get `290`, then add the value of `>` (4) to get a new total score of `294`.

> - 从总分 `0` 开始。
> - 将总分乘以 5 得到 `0`，然后加上 `]` 的分值(2)，得到新的总分 `2`。
> - 将总分乘以 5 得到 `10`，然后加上 `)` 的分值(1)，得到新的总分 `11`。
> - 将总分乘以 5 得到 `55`，然后加上 `}` 的分值(3)，得到新的总分 `58`。
> - 将总分乘以 5 得到 `290`，然后加上 `>` 的分值(4)，得到新的总分 `294`。

The five lines' completion strings have total scores as follows:

> 五行的补全字符串总分如下：

- `}}]])})]` - `288957` total points.
- `)}>]})` - `5566` total points.
- `}}>}>))))` - `1480781` total points.
- `]]}}]}]}>` - `995444` total points.
- `])}>` - `294` total points.

> - `}}]])})]` - 总共 `288957` 分。
> - `)}>]})` - 总共 `5566` 分。
> - `}}>}>))))` - 总共 `1480781` 分。
> - `]]}}]}]}>` - 总共 `995444` 分。
> - `])}>` - 总共 `294` 分。

Autocomplete tools are an odd bunch: the winner is found by **sorting** all of the scores and then taking the **middle** score. (There will always be an odd number of scores to consider.) In this example, the middle score is **`288957`** because there are the same number of scores smaller and larger than it.

> 自动完成工具是一个奇怪的工具：需要先**排序**所有分数，然后取**中间**分数来确定获胜者。（总会有奇数个分数需要考虑。）在这个例子中，中间分数是 **`288957`**，因为比它大和比它小的分数的数量相同。

Find the completion string for each incomplete line, score the completion strings, and sort the scores. **What is the middle score?**

> 找出每条不完整行的补全字符串，对补全字符串进行评分，并对分数进行排序。**中间分数是什么？**

Your puzzle answer was `2412013412`.

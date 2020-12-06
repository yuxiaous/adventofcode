# Day 6: Custom Customs

> 第六天：定制海关

As your flight approaches the regional airport where you'll switch to a much larger plane, [customs declaration forms](https://en.wikipedia.org/wiki/Customs_declaration) are distributed to the passengers.

> 你的航班接近了一个中转机场，在那里你将转乘更大飞机，乘客们分到了海关申报表。

The form asks a series of 26 yes-or-no questions marked `a` through `z`. All you need to do is identify the questions for which **anyone in your group** answers "yes". Since your group is just you, this doesn't take very long.

> 该表格会询问一系列 26 个是或否的问题，标记为 `a` 到 `z`。你需要做的就是确认团队中任意一个人回答为“是”的问题。由于你的团队就只有你一个人，因此不需要花费很长时间。

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

> 但是，坐在你旁边的人似乎遇到了语言障碍，并询问你是否可以提供帮助。对于他们团队中的每个人，你都要写下回答为“是”的问题，每人一行。 例如：

```'
abcx
abcy
abcz
```

In this group, there are **`6`** questions to which anyone answered "yes": `a`, `b`, `c`, `x`, `y`, and `z`. (Duplicate answers to the same question don't count extra; each question counts at most once.)

> 在这个团队中，回答为“是”的有 6 个问题，分别是 `a`、`b`、`c`、`x`、`y` 和 `z`。（对同一问题的重复答案不重复计算，每个问题最多计一次。）

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane ([your puzzle input](day06.txt)). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

> 另一个团队寻求你的帮助，然后再一个，最终你从飞机上的每个小组中收集了答案（[你的谜题输入](day06.txt)）。每个团队的答案用空行分隔，并且在每个团队中，每个人的答案都是单独的一行。例如：

```'
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

- The first group contains one person who answered "yes" to **`3`** questions: `a`, `b`, and `c`.
- The second group contains three people; combined, they answered "yes" to **`3`** questions: `a`, `b`, and `c`.
- The third group contains two people; combined, they answered "yes" to **`3`** questions: `a`, `b`, and `c`.
- The fourth group contains four people; combined, they answered "yes" to only **`1`** question, `a`.
- The last group contains one person who answered "yes" to only **`1`** question, `b`.

> 这个列表代表了五个团队的答案：
>
> - 第一个团队有一个人，回答为“是”的问题有 3 个：`a`、`b` 和 `c`。
> - 第二个团队有三个人，回答为“是”的问题合计有 3 个：`a`、`b` 和 `c`。
> - 第三个团队有两个人，回答为“是”的问题合计有 3 个：`a`、`b` 和 `c`。
> - 第四个团队有四个人，回答为“是”的问题合计只有 1 个：`a`。
> - 最后一个团队有一个人，回答为“是”的问题只有 1 个：`b`。

In this example, the sum of these counts is `3 + 3 + 3 + 1 + 1` = **`11`**.

> 在这个例子中，这些计数的和为 `3 + 3 + 3 + 1 + 1` = `11`。

For each group, count the number of questions to which anyone answered "yes". **What is the sum of those counts?**

> 对于每个团队，统计任意一人回答为“是”的问题的数量。这些计数的总和是多少？

Your puzzle answer was `6437`.

## --- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

> 当你完成最后一个团队的海关申报时，你发现你误读了说明中的一个词：

You don't need to identify the questions to which **anyone** answered "yes"; you need to identify the questions to which **everyone** answered "yes"!

> 你需要确认的不是任意一人回答为“是”的问题，你需要确认的是所有人都回答为“是”的问题！

Using the same example as above:

> 使用与上面相同的例子：

```'
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

- In the first group, everyone (all 1 person) answered "yes" to **`3`** questions: `a`, `b`, and `c`.
- In the second group, there is **no** question to which everyone answered "yes".
- In the third group, everyone answered yes to only **`1`** question, `a`. Since some people did not answer "yes" to `b` or `c`, they don't count.
- In the fourth group, everyone answered yes to only **`1`** question, `a`.
- In the fifth group, everyone (all 1 person) answered "yes" to **`1`** question, `b`.

> 这个列表代表了五个团队的答案：
>
> - 在第一个团队中，所有人（只有1人）回答为“是”的问题有 3 个：`a`、`b` 和 `c`。
> - 在第二个团队中，没有所有人都回答为“是”的问题。
> - 在第三个团队中，所有人回答为“是”的问题只有 1 个：`a`。由于一些人未对 `b` 或 `c` 回答为“是”，因此不计入。
> - 在第四个团队中，所有人回答为“是”的问题只有 1 个：`a`。
> - 在第五个团队中，所有人（只有1人）回答为“是”的问题 1 个：`b`。

In this example, the sum of these counts is `3 + 0 + 1 + 1 + 1` = **`6`**.

> 在这个例子中，这些计数的和为 `3 + 0 + 1 + 1 + 1` = `6`。

For each group, count the number of questions to which **everyone** answered "yes". **What is the sum of those counts?**

> 对于每个团队，统计所有人都回答为“是”的问题的数量。这些计数的总和是多少？

Your puzzle answer was `3229`.

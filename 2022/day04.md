# Day 4: Camp Cleanup

> 第4天：营地清理

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique **ID number**, and each Elf is assigned a range of section IDs.

> 在最后一批物资从船上卸下之前需要清理出空间，因此一些精灵被分配了清理营地各个区域的工作。营地每个区域都有一个唯一的 **ID 号**，每个精灵都被分配了一些区域 ID。

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments **overlap**. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a **big list of the section assignments for each pair** ([your puzzle input](day04.txt)).

> 然而，当一些精灵相互比较他们的区域分配时，他们注意到许多分配**重叠**了。为了快速找到重叠内容并减少重复工作，精灵们开始两两配对，并将每组配对的内容合并制作了一张**大的区域分配列表**（[你的谜题输入](day04.txt)）。

For example, consider the following list of section assignment pairs:

> 举个例子，考虑下面每组配对的区域分配列表：

```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```

For the first few pairs, this list means:

- Within the first pair of Elves, the first Elf was assigned sections `2-4` (sections `2`, `3`, and `4`), while the second Elf was assigned sections `6-8` (sections `6`, `7`, `8`).
- The Elves in the second pair were each assigned two sections.
- The Elves in the third pair were each assigned three sections: one got sections `5`, `6`, and `7`, while the other also got `7`, plus `8` and `9`.

> 对于前几组配对，这个列表表示：
>
> - 在第一组配对的精灵中，第一个精灵被分配了区域 `2-4`（即区域 `2`、`3` 和 `4`），第二个精灵被分配了区域 `6-8`（即区域 `6`，`7`，`8`）。
> - 第二组配对的精灵每人被分配了两个区域。
> - 第三组配对的精灵每人被分配了三个区域：一个得到了区域 `5`、`6` 和 `7`，另一个得到了 `7`，加上 `8` 以及 `9`。

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

> 这个例子中的列表使用了一位数的区域 ID 以便使其更易于展示，你的实际列表可能包含更大的数字。在视觉上，这些区域分配看起来像这样：

```
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
```

Some of the pairs have noticed that one of their assignments **fully contains** the other. For example, `2-8` fully contains `3-7`, and `6-6` is fully contained by `4-6`. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are **`2`** such pairs.

> 其中一些配对信息显示，他们中的一个任务**完全包含**另一个任务。例如，`2-8` 完全包含了 `3-7`，`6-6` 完全被包含在 `4-6` 中。在一项任务完全包含另一项任务的情况下，配对中的一个精灵将重复清理他们的伙伴已经清理过的部分，因此这些似乎是最需要重新考虑的地方。在这个例子中，有 **`2`** 个这样的配对。

**In how many assignment pairs does one range fully contain the other?**

> **有多少个任务的配对满足一个任务范围完全包含另一个的范围？**

Your puzzle answer was `651`.

## Part Two

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that **overlap at all**.

> 似乎仍有相当多的重复工作。进而，精灵们想知道**有重叠**的配对数量。

In the above example, the first two pairs (`2-4,6-8` and `2-3,4-5`) don't overlap, while the remaining four pairs (`5-7,7-9`, `2-8,3-7`, `6-6,4-6`, and `2-6,4-8`) do overlap:

- `5-7,7-9` overlaps in a single section, `7`.
- `2-8,3-7` overlaps all of the sections `3` through `7`.
- `6-6,4-6` overlaps in a single section, `6`.
- `2-6,4-8` overlaps in sections `4`, `5`, and `6`.

> 在上面的例子中，前两对（`2-4,6-8` 和 `2-3,4-5`）没有重叠，而其余四对（`5-7,7-9` , `2-8,3-7`, `6-6,4-6` 和 `2-6,4-8`) 有重叠：
>
> - `5-7,7-9` 有一个区域重叠，`7`。
> - `2-8,3-7` 在 `3` 到 `7` 的所有区域都重叠。
> - `6-6,4-6` 有一个区域重叠，`6`。
> - `2-6,4-8` 在 `4`、`5` 和 `6` 区域重叠。

So, in this example, the number of overlapping assignment pairs is **`4`**.

> 所以，在这个例子中，有重叠任务的配对数量是 **`4`**。

**In how many assignment pairs do the ranges overlap?**

> **有多少个任务的配对满足范围有重叠？**

Your puzzle answer was `956`.

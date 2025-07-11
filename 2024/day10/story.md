# Day 10: Hoof It
> # 第十天：徒步前行

You all arrive at a [Lava Production Facility](https://adventofcode.com/2023/day/15) on a floating island in the sky. As the others begin to search the massive industrial complex, you feel a small nose boop your leg and look down to discover a reindeer wearing a hard hat.
> 你们来到了天空中一座漂浮岛上的熔岩生产设施。当其他人开始搜查这座庞大的工业建筑群时，你感觉有个小鼻子碰了碰你的腿，低头一看，是一只戴着安全帽的驯鹿。

The reindeer is holding a book titled "Lava Island Hiking Guide". However, when you open the book, you discover that most of it seems to have been scorched by lava! As you're about to ask how you can help, the reindeer brings you a blank [topographic map](https://en.wikipedia.org/wiki/Topographic_map) of the surrounding area (your puzzle input) and looks up at you excitedly.
> 驯鹿拿着一本名为《熔岩岛徒步指南》的书。然而，当你翻开这本书时，发现大部分内容似乎都被熔岩烧焦了！正当你准备问如何帮忙时，驯鹿递给你一张空白的地形图（你的谜题输入），兴奋地抬头看着你。

Perhaps you can help fill in the missing hiking trails?
> 也许你可以帮忙补全缺失的徒步路线？

The topographic map indicates the **height** at each position using a scale from `0` (lowest) to `9` (highest). For example:
> 地形图用 `0`（最低）到 `9`（最高）的数字表示每个位置的**高度**。例如：

```
0123
1234
8765
9876
```

Based on un-scorched scraps of the book, you determine that a good hiking trail is **as long as possible** and has an **even, gradual, uphill slope**. For all practical purposes, this means that a **hiking trail** is any path that starts at height `0`, ends at height `9`, and always increases by a height of exactly 1 at each step. Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).
> 根据书中未被烧毁的残页，你确定一条好的徒步路线应该**尽可能长**，并且**均匀、逐步上升**。实际上，这意味着一条**徒步路线**是任意从高度 `0` 开始到高度 `9` 结束，并且每一步高度都恰好增加1的路径。徒步路线不能走对角线——只能上下左右移动（以地图为准）。

You look up from the map and notice that the reindeer has helpfully begun to construct a small pile of pencils, markers, rulers, compasses, stickers, and other equipment you might need to update the map with hiking trails.
> 你抬头离开地图，发现驯鹿已经贴心地为你准备了一堆铅笔、记号笔、尺子、圆规、贴纸和其他你可能需要用来在地图上标记徒步路线的工具。

A **trailhead** is any position that starts one or more hiking trails - here, these positions will always have height `0`. Assembling more fragments of pages, you establish that a trailhead's **score** is the number of `9`-height positions reachable from that trailhead via a hiking trail. In the above example, the single trailhead in the top left corner has a score of `1` because it can reach a single `9` (the one in the bottom left).
> **起点**是指可以出发一条或多条徒步路线的位置——在这里，这些位置总是高度为 `0`。通过拼凑更多残页，你得知一个起点的**得分**就是通过徒步路线从该起点出发可以到达的高度为 `9` 的位置的数量。在上面的例子中，左上角唯一的起点得分为 `1`，因为它只能到达一个 `9`（左下角的那个）。

This trailhead has a score of `2`:
> 这个起点的得分是 `2`：

```
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
```

(The positions marked `.` are impassable tiles to simplify these examples; they do not appear on your actual topographic map.)
> （用 `.` 标记的位置是不可通行的方格，仅用于简化示例；你的实际地形图上不会出现这些。）

This trailhead has a score of `4` because every `9` is reachable via a hiking trail except the one immediately to the left of the trailhead:
> 这个起点的得分是 `4`，因为除了起点左边的那个 `9` 以外，其他所有 `9` 都可以通过徒步路线到达：

```
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
```

This topographic map contains **two** trailheads; the trailhead at the top has a score of `1`, while the trailhead at the bottom has a score of `2`:
> 这张地形图有**两个**起点；顶部的起点得分为 `1`，底部的起点得分为 `2`：

```
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
```

Here's a larger example:
> 这里有一个更大的例子：

```
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
```

This larger example has 9 trailheads. Considering the trailheads in reading order, they have scores of `5`, `6`, `5`, `3`, `1`, `3`, `5`, `3`, and `5`. Adding these scores together, the sum of the scores of all trailheads is **`36`**.
> 这个更大的例子有9个起点。按阅读顺序，这些起点的得分分别为 `5`、`6`、`5`、`3`、`1`、`3`、`5`、`3` 和 `5`。将这些得分相加，所有起点的总得分为 **`36`**。

The reindeer gleefully carries over a protractor and adds it to the pile. **What is the sum of the scores of all trailheads on your topographic map?**
> 驯鹿高兴地又拿来一个量角器放到工具堆里。**你的地形图上所有起点的得分之和是多少？**

Your puzzle answer was `629`.

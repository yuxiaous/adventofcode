# [Day 5: Hydrothermal Venture](https://adventofcode.com/2021/day/5)

> 第5天：海底热泉

You come across a field of [hydrothermal vents](https://en.wikipedia.org/wiki/Hydrothermal_vent) on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

> 你在海底遇到了一片[热液喷口](https://zh.wikipedia.org/wiki/海底热泉)！这些喷口不断地产生大片不透明的烟柱，所以最好尽可能避开它们。

They tend to form in **lines**; the submarine helpfully produces a list of nearby lines of vents ([your puzzle input](day05.txt)) for you to review. For example:

> 它们倾向于按**直线**排列，潜水艇生成了附近热液喷口的直线清单（[你的谜题输入](day05.txt)）供你查看。例如：

```diff
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
```

Each line of vents is given as a line segment in the format `x1,y1 -> x2,y2` where `x1`,`y1` are the coordinates of one end the line segment and `x2`,`y2` are the coordinates of the other end. These line segments include the points at both ends. In other words:

> 每条热液喷口直线都以线段的形式给出，格式为 `x1,y1 -> x2,y2`，其中 `x1`,`y1` 是线段一端的坐标，`x2`,`y2` 是另一端的坐标。这些线段包括两个端点。换句话说：

- An entry like `1,1 -> 1,3` covers points `1,1`, `1,2`, and `1,3`.
- An entry like `9,7 -> 7,7` covers points `9,7`, `8,7`, and `7,7`.

> - 例如 `1,1 -> 1,3` 包含点 `1,1`、`1,2` 和 `1,3`。
> - 例如 `9,7 -> 7,7` 包含点 `9,7`、`8,7` 和 `7,7`。

For now, **only consider horizontal and vertical lines**: lines where either `x1 = x2` or `y1 = y2`.

> 当前，**只考虑水平和垂直的线**，即满足 `x1 = x2` 或 `y1 = y2` 的直线。

So, the horizontal and vertical lines from the above list would produce the following diagram:

> 因此，上面列表中的水平线和垂直线将生成下图：

```diff
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
```

In this diagram, the top left corner is `0,0` and the bottom right corner is `9,9`. Each position is shown as **the number of lines which cover that point** or `.` if no line covers that point. The top-left pair of `1`s, for example, comes from `2,2 -> 2,1`; the very bottom row is formed by the overlapping lines `0,9 -> 5,9` and `0,9 -> 2,9`.

> 在这张图中，左上角的坐标是 `0,0`，右下角的坐标是 `9,9`。每个坐标位置显示**经过该点的直线的数量**，如果没有直线经过该点，则显示 `.`。例如，左上角的两个 `1` 来自于 `2,2 -> 2,1`，最底部的一行由重叠的两条线 `0,9 -> 5,9` 和 `0,9 -> 2,9` 形成。

To avoid the most dangerous areas, you need to determine **the number of points where at least two lines overlap**. In the above example, this is anywhere in the diagram with a `2` or larger - a total of **`5`** points.

> 为了避开最危险的区域，你需要确定**至少两条线重叠的点的数量**。在上面的例子中，表示图表中任何一个拥有 `2` 或更大数字的点--总共有 **`5`** 个点。

Consider only horizontal and vertical lines. **At how many points do at least two lines overlap?**

> 只考虑水平和垂直的直线。**至少两条线重叠的点有多少个？**

Your puzzle answer was `5145`.

## --- Part Two ---

Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider **diagonal lines**.

> 不幸的是，只考虑水平和垂直的直线并不能让你了解到完整的画面。你还需要考虑**对角线**。

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

> 由于热液喷口测绘系统的限制，列表中的直线只可能是水平线、垂直线或者正好 45 度角的对角线。换句话说：

- An entry like `1,1 -> 3,3` covers points `1,1`, `2,2`, and `3,3`.
- An entry like `9,7 -> 7,9` covers points `9,7`, `8,8`, and `7,9`.

> - 例如 `1,1 -> 3,3` 包含点 `1,1`、`2,2` 和 `3,3`。
> - 例如 `9,7 -> 7,9` 包含点 `9,7`、`8,8` 和 `7,9`。

Considering all lines from the above example would now produce the following diagram:

> 考虑上面的例子中的所有行，现在将生成下图：

```diff
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
```

You still need to determine **the number of points where at least two lines overlap**. In the above example, this is still anywhere in the diagram with a `2` or larger - now a total of **`12`** points.

> 你仍然需要确定**至少两条线重叠的点的数量**。在上面的例子中，依然表示图表中任何一个拥有 `2` 或更大数字的点--现在总共有 **`12`** 个点。

Consider all of the lines. **At how many points do at least two lines overlap?**

> 考虑所有的直线。**至少两条线重叠的点有多少个？**

Your puzzle answer was `16518`.

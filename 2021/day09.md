# [Day 9: Smoke Basin](https://adventofcode.com/2021/day/9)

> 第9天：烟雾盆地

These caves seem to be [lava tubes](https://en.wikipedia.org/wiki/Lava_tube). Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

> 这些洞穴似乎是[熔岩管](https://en.wikipedia.org/wiki/Lava_tube)。部分区域甚至还处于火山活动状态，小型热液喷口将烟雾释放到洞穴中，然后像雨一样缓慢沉降。

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you ([your puzzle input](day09.txt)).

> 如果你可以为烟雾如何流经洞穴建模，你也许可以避开它并且使你更加安全。潜水艇为你生成了附近洞穴地面的高度图（[你的谜题输入](day09.txt)）。

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

> 烟雾流向它所在区域的最低点。例如，考虑以下高度图：

```diff
2199943210
3987894921
9856789892
8767896789
9899965678
```

Each number corresponds to the height of a particular location, where `9` is the highest and `0` is the lowest a location can be.

> 每个数字对应于特定位置的高度，其中 `9` 是最高的位置，`0` 是最低的位置。

Your first goal is to find the **low points** - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

> 你的第一个目标是找到**低点** -- 低于任何相邻位置的位置。大多数的位置有四个相邻位置（上、下、左、右），地图边缘或角落上的位置分别具有三个或两个相邻位置。（对角线位置不算相邻。）

In the above example, there are **four** low points, all highlighted: two are in the first row (a `1` and a `0`), one is in the third row (a `5`), and one is in the bottom row (also a `5`). All other locations on the heightmap have some lower adjacent location, and so are not low points.

> 在上面的例子中，有**四个**低点：两个在第一行（一个 `1` 和一个 `0`），一个在第三行（一个 `5`），以及一个在最后一行（也是一个 `5`）。高度图上的所有其他位置都有一些更低的相邻位置，因此不是低点。

The **risk level** of a low point is **1 plus its height**. In the above example, the risk levels of the low points are `2`, `1`, `6`, and `6`. The sum of the risk levels of all low points in the heightmap is therefore **`15`**.

> 低点的**风险水平**是**它的高度加上 1**。 在上面的例子中，低点的风险等级分别是 `2`、`1`、`6` 和 `6`。因此，高度图中所有低点的风险水平总和为 **`15`**。

Find all of the low points on your heightmap. **What is the sum of the risk levels of all low points on your heightmap?**

> 找到高度图上的所有低点。**你的高度图上所有低点的风险等级总和是多少？**

Your puzzle answer was `522`.

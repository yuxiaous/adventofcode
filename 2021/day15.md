# [Day 15: Chiton](https://adventofcode.com/2021/day/15)

> 第15天：石鳖

You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in [chitons](https://en.wikipedia.org/wiki/Chiton), and it would be best not to bump any of them.

> 你很快就要到达了洞穴的出口了，然而洞穴越来越窄。你的潜水艇几乎刚刚可以通过，但主要问题是洞穴的墙壁上布满了[石鳖](https://en.wikipedia.org/wiki/Chiton)，最好不要撞到它们任何一个。

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of **risk level** throughout the cave ([your puzzle input](day15.txt)). For example:

> 洞穴很大，但是顶很低，将你的行动范围限制在了二维平面内。洞穴的形状类似于正方形，快速扫描石鳖密度，生成了整个洞穴的**风险等级**地图（[你的谜题输入](day15.txt)）。例如：

```'
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
```

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its **risk level**; to determine the total risk of an entire path, add up the risk levels of each position you **enter** (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

> 你从左上角开始，你的目的地是右下角，你不能沿对角线移动。每个位置的数字表示它的**风险等级**，要确定整条路径的总风险值，将每个你**进入**位置的风险水平相加（也就是说，除非你进入，否则不用计算你的起始位置的风险水平，离开并不会增加总风险值）。

Your goal is to find a path with the **lowest total risk**. In this example, a path with the lowest total risk is highlighted here:

> 你的目标是找到一条**总风险值最低**的路径。在这个例子中，高亮显示了总风险值最低的一条路径：

```'
.163751742
.381373672
.......328
369493..69
7463417.11
1319128..7
13599124.1
31254216.9
12931385..
231194458.
```

The total risk of this path is **`40`** (the starting position is never entered, so its risk is not counted).

> 这条路径的总风险值为 **`40`**（起始位置从未进入，因此不计算其风险）。

**What is the lowest total risk of any path from the top left to the bottom right?**

> **从左上角到右下角总风险值最低的路径是多少数值？**

Your puzzle answer was `403`.

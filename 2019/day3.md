# [Day 3: Crossed Wires](https://adventofcode.com/2019/day/3)

> 第3天：交叉导线

The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

> 重力助推成功了，你可以顺利到达金星补给站了。在重返地球期间，燃料管理系统没有完整安装，优先级列表中的下一个就是它。

Opening the front panel reveals a jumble of wires. Specifically, **two wires** are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text ([your puzzle input](day3.txt)).

> 打开前面板会发现杂乱的导线。具体来说，**两条导线**连接到中心端口并在网格上向外延伸。你跟踪每根导线离开中心端口时所经过的路径，一根导线用一行文字表示（[你的谜题输入](day3.txt)）。

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to **find the intersection point closest to the central port**. Because the wires are on a grid, use the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

> 导线弯曲并转动，两根导线偶尔会交叉。要修复电路，你需要**找到最靠近中心端口的交点**。由于导线在网格上，因此使用[曼哈顿距离](https://en.wikipedia.org/wiki/Taxicab_geometry)进行此测量。 从技术上讲，尽管导线确实在它们都开始的中心端口处交叉，但这一点不算在内，也算不上与导线本身交叉。

For example, if the first wire's path is `R8,U5,L5,D3`, then starting from the central port (`o`), it goes right `8`, up `5`, left `5`, and finally down `3`:

> 举个例子，如果第一根导线的路径为 `R8，U5，L5，D3`，则从中心端口 (`o`) 开始，它向右 `8` 格，向上 `5` 格，向左 `5` 格，最后再向下 `3` 格：

```diff
...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
```

Then, if the second wire's path is `U7,R6,D4,L4`, it goes up `7`, right `6`, down `4`, and left `4`:

> 接下来，如果第二根导线的路径为 `U7，R6，D4，L4`，则它向上 `7` 格，向右 `6` 格，向下 `4` 格，向左 `4` 格：

```diff
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

These wires cross at two locations (marked `X`), but the lower-left one is closer to the central port: its distance is `3 + 3 = 6`.

> 这些导线在两个位置上交叉（标记为 `X`），但左下角的位置更靠近中心端口：其距离为 `3 + 3 = 6`。

Here are a few more examples:

> 以下是更多例子：

```diff
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
```

```diff
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
```

**What is the Manhattan distance** from the central port to the closest intersection?

> 从中心端口到最近的交叉点的**曼哈顿距离是多少**？

Your puzzle answer was `721`.

## Part Two

It turns out that this circuit is very timing-sensitive; you actually need to **minimize the signal delay**.

> 原来这个电路对时序更敏感，你实际上应该做的是**最小化信号延迟**。

To do this, calculate the **number of steps** each wire takes to reach each intersection; choose the intersection where the **sum of both wires' steps** is lowest. If a wire visits a position on the grid multiple times, use the steps value from the **first** time it visits that position when calculating the total value of a specific intersection.

> 为此，需要计算每根导线到达每个交叉点所需的**步数**，选择**两条导线的步数之和**最少的交叉点。如果一根导线多次经过网格上的某个位置，则使用**第一次**经过该位置的步数来计算交叉点的总步数。

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

> 一根导线所走的步数是导线到达那个位置所经过的格子的总数，包含这个相交点。重新考虑上面的示例：

```diff
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

In the above example, the intersection closest to the central port is reached after `8+5+5+2 = 20` steps by the first wire and `7+6+4+3 = 20` steps by the second wire for a total of `20+20 = 40` steps.

> 在上面的示例中，第一根导线经过 `8+5+5+2 = 20` 步后达到最接近中心端口的交叉点，第二根导线经过 `7+6+4+3 = 20` 步，总共是 `20+20 = 40` 步。

However, the top-right intersection is better: the first wire takes only `8+5+2 = 15` and the second wire takes only `7+6+2 = 15`, a total of `15+15 = 30` steps.

> 事实上，右上角的交叉点会更好一些：第一根导线仅经过 `8+5+2 = 15` 步，第二根导线仅经过 `7+6+2 = 15` 步，总共是 `15+15 = 30` 步。

Here are the best steps for the extra examples from above:

> 这是上面那两个例子的最佳步骤：

```diff
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
```

```diff
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
```

**What is the fewest combined steps the wires must take to reach an intersection?**

> **导线到达交叉点的步数之和最少的是多少？**

Your puzzle answer was `7388`.

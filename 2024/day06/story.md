# Day 6: Guard Gallivant
> # 第六天：守卫巡游

The Historians use their fancy [device](https://adventofcode.com/2024/day/4) again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year [1518](https://adventofcode.com/2018/day/5)! It turns out that having direct access to history is very convenient for a group of historians.
> 历史学家们再次使用他们那台神奇的[设备](https://adventofcode.com/2024/day/4)，这次把你们带到了北极原型服装制造实验室……时间是[1518年](https://adventofcode.com/2018/day/5)！事实证明，能够直接接触历史对一群历史学家来说非常方便。

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single **guard** is patrolling this part of the lab.
> 你们仍然要小心时间悖论，因此在历史学家们寻找首席的过程中，必须避免与1518年的人接触。不幸的是，这片实验室区域有一名**守卫**在巡逻。

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?
> 也许你可以提前推算出守卫的行动路线，这样历史学家们就能安全地搜寻了？

You start by making a map (your puzzle input) of the situation. For example:
> 你首先绘制了一张当前情况的地图（你的谜题输入）。例如：

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

The map shows the current position of the guard with `^` (to indicate the guard is currently facing **up** from the perspective of the map). Any **obstructions** - crates, desks, alchemical reactors, etc. - are shown as `#`.
> 地图上用 `^` 表示守卫当前位置（表示守卫当前朝**上**）。所有**障碍物**——箱子、桌子、炼金反应堆等——都用 `#` 表示。

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
> 1518年的实验室守卫遵循非常严格的巡逻协议，反复执行以下步骤：

- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.
> - 如果正前方有障碍物，则右转90度。
> - 否则，向前迈一步。

Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):
> 按照上述协议，守卫会向上移动几步，直到遇到障碍物（本例中是一堆失败的服装原型）：

```
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:
> 由于守卫前方有障碍物，她会先右转，然后继续沿新方向直行：

```
....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Reaching another obstacle (a spool of several **very** long polymers), she turns right again and continues downward:
> 遇到另一个障碍物（一卷**非常**长的聚合物）后，她再次右转并继续向下：

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
```

This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):
> 这个过程会持续一段时间，但最终守卫会离开地图区域（在经过一罐万能溶剂后）：

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
```

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. **Including the guard's starting position**, the positions visited by the guard before leaving the area are marked with an `X`:
> 通过预测守卫的路线，你可以确定实验室中哪些具体位置会被巡逻经过。**包括守卫的起始位置**，守卫在离开区域前经过的位置都用 `X` 标记：

```
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
```

In this example, the guard will visit **`41`** distinct positions on your map.
> 在这个例子中，守卫会在你的地图上经过 **`41`** 个不同的位置。

Predict the path of the guard. **How many distinct positions will the guard visit before leaving the mapped area?**
> 预测守卫的路径。**在离开地图区域前，守卫会经过多少个不同的位置？**

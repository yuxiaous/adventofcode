# Day 16: Reindeer Maze
> # 第十六天：驯鹿迷宫

It's time again for the [Reindeer Olympics](https://adventofcode.com/2015/day/14)! This year, the big event is the Reindeer Maze, where the Reindeer compete for the **lowest score**.
> 又到了[驯鹿奥运会](https://adventofcode.com/2015/day/14)的时间！今年的重头戏是驯鹿迷宫，驯鹿们要争夺**最低分**。

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?
> 你和历史学家们正好在比赛即将开始时赶来寻找首席。稍微看一会儿也没关系吧？

The Reindeer start on the Start Tile (marked `S`) facing **East** and need to reach the End Tile (marked `E`). They can move forward one tile at a time (increasing their score by `1` point), but never into a wall (`#`). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by `1000` points).
> 驯鹿从起点（`S`）出发，面朝**东**，需要到达终点（`E`）。它们每次可以向前移动一格（得分加`1`），但不能进入墙（`#`）。它们也可以顺时针或逆时针旋转90度（得分加`1000`）。

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:
> 为了找个最佳观赛位置，你先从附近的服务台拿了一张地图（你的谜题输入）。例如：

```
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
```

There are many paths through this maze, but taking any of the best paths would incur a score of only **`7036`**. This can be achieved by taking a total of `36` steps forward and turning 90 degrees a total of `7` times:
> 这个迷宫有很多路径，但走任意一条最佳路径只需得分 **`7036`**。这可以通过总共前进`36`步和旋转90度`7`次实现：

```
###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############
```

Here's a second example:
> 这里有第二个例子：

```
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
```

In this maze, the best paths cost **`11048`** points; following one such path would look like this:
> 在这个迷宫中，最佳路径得分为 **`11048`**；其中一条路径如下：

```
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################
```

Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.
> 注意，上面路径的第一步就是一次90度转向，把驯鹿从面朝东转为面朝北。

Analyze your map carefully. **What is the lowest score a Reindeer could possibly get?**
> 仔细分析你的地图。**驯鹿可能获得的最低分是多少？**

Your puzzle answer was `102488`.

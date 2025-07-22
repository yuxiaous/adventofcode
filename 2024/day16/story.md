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

## Part Two
> ## 第二部分

Now that you know what the best paths look like, you can figure out the best spot to sit.
> 既然你已经知道最佳路径是什么样子了，你就能找出最佳观赛位置。

Every non-wall tile (`S`, `.`, or `E`) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is **whether the tile is on one of the best paths through the maze**. If you sit somewhere else, you'd miss all the action!
> 每个非墙格子（`S`、`.` 或 `E`）的边上都可以坐。虽然决定哪个格子是最佳观赛点要考虑很多因素（座位舒适度、离洗手间远近、是否有柱子挡视线等），但最重要的因素是**这个格子是否在迷宫的某条最佳路径上**。如果你坐在其他地方，就会错过所有精彩瞬间！

So, you'll need to determine which tiles are part of **any** best path through the maze, including the S and E tiles.
> 所以，你需要确定哪些格子属于迷宫的**任意一条最佳路径**，包括 S 和 E 格子。

In the first example, there are **`45`** tiles (marked `O`) that are part of at least one of the various best paths through the maze:
> 在第一个例子中，有 **`45`** 个格子（用 `O` 标记）属于至少一条最佳路径：

```
###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############
```

In the second example, there are **`64`** tiles that are part of at least one of the best paths:
> 在第二个例子中，有 **`64`** 个格子属于至少一条最佳路径：

```
#################
#...#...#...#..O#
#.#.#.#.#.#.#.#O#
#.#.#.#...#...#O#
#.#.#.#.###.#.#O#
#OOO#.#.#.....#O#
#O#O#.#.#.#####O#
#O#O..#.#.#OOOOO#
#O#O#####.#O###O#
#O#O#..OOOOO#OOO#
#O#O###O#####O###
#O#O#OOO#..OOO#.#
#O#O#O#####O###.#
#O#O#OOOOOOO..#.#
#O#O#O#########.#
#O#OOO..........#
#################
```

Analyze your map further. **How many tiles are part of at least one of the best paths through the maze?**
> 进一步分析你的地图。**有多少格子属于至少一条迷宫的最佳路径？**

Your puzzle answer was `559`.

# Day 20: Donut Maze

> 第20天：甜甜圈迷宫

You notice a strange pattern on the surface of Pluto and land nearby to get a closer look. Upon closer inspection, you realize you've come across one of the famous space-warping mazes of the long-lost Pluto civilization!

> 你注意到了冥王星表面的一个奇怪图案，然后降落在它附近仔细观察。通过仔细检查，你意识到你遇上了其中一个著名的跃迁空间迷宫，它是遗失已久的冥王星文明！

Because there isn't much space on Pluto, the civilization that used to live here thrived by inventing a method for folding spacetime. Although the technology is no longer understood, mazes like this one provide a small glimpse into the daily life of an ancient Pluto citizen.

> 因为冥王星上没有太多空间，所以曾经生活在这里的文明通过发明一种折叠时空的方法得以蓬勃发展。尽管这项技术不再为人所知，但像这样的迷宫让我们瞥了一眼古代冥王星公民的日常生活。

This maze is shaped like a [donut](https://en.wikipedia.org/wiki/Torus). Portals along the inner and outer edge of the donut can instantly teleport you from one side to the other. For example:

> 这个迷宫的形状像一个[甜甜圈](https://en.wikipedia.org/wiki/Torus)。穿过甜甜圈内边缘和外边缘的传送门可以将你从一侧立即传送到另一侧。例如：

```'
         A
         A
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z
             Z
```

This map of the maze shows solid walls (`#`) and open passages (`.`). Every maze on Pluto has a start (the open tile next to `AA`) and an end (the open tile next to `ZZ`). Mazes on Pluto also have portals; this maze has three pairs of portals: `BC`, `DE`, and `FG`. When on an open tile next to one of these labels, a single step can take you to the other tile with the same label. (You can only walk on `.` tiles; labels and empty space are not traversable.)

> 这张迷宫地图显示了实心的墙壁（`#`）和开放的通道（`.`）。冥王星上的每个迷宫都有一个起点（`AA` 旁边的开放图块）和一个终点（`ZZ` 旁边的开放图块）。冥王星上的迷宫也有传送门，这个迷宫有三对传送门：`BC`、`DE` 和 `FG`。当站在与这些标签相邻的开放图块上，只需一步就可以将你带到有相同标签的另一端的图块上。（你只能在 `.` 图块上行走，标签和空白区域是无法行走的。）

One path through the maze doesn't require any portals. Starting at `AA`, you could go down 1, right 8, down 12, left 4, and down 1 to reach `ZZ`, a total of 26 steps.

> 一条穿过迷宫的路径是不需要任何传送门的。从 `AA` 开始，你可以向下 1 步，向右 8 步，向下 12 步，向左 4 步，最后向下 1 步到达 `ZZ`，一共 26 步。

However, there is a shorter path: You could walk from `AA` to the inner `BC` portal (4 steps), warp to the outer `BC` portal (1 step), walk to the inner `DE` (6 steps), warp to the outer `DE` (1 step), walk to the outer `FG` (4 steps), warp to the inner `FG` (1 step), and finally walk to `ZZ` (6 steps). In total, this is only **23** steps.

> 但是，存在一条更短的路径：你可以从 `AA` 走到内侧的 `BC` 传送门（4 步），跃迁到外侧的 `BC` 传送门（1 步），走到内侧的 `DE`（6 步），跃迁到外侧的 `DE`（1 步），走到外侧的 `FG`（4 步），跃迁到内侧的 `FG`（1 步），最后走到 `ZZ`（6 步）。总共只要 **23** 步。

Here is a larger example:

> 这有个更大的例子：

```'
                   A
                   A
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C
           U   P   P
```

Here, `AA` has no direct path to `ZZ`, but it does connect to `AS` and `CP`. By passing through `AS`, `QG`, `BU`, and `JO`, you can reach `ZZ` in **58** steps.

> 在这里，从 `AA` 没有直达 `ZZ` 的路径，但它连接了 `AS` 和 `CP`。穿过 `AS`、`QG`、`BU` 和 `JO`，你就能用 **58** 步到达 `ZZ`。

In your maze, **how many steps does it take to get from the open tile marked `AA` to the open tile marked `ZZ`?**

> 在你的迷宫中，**从标记 `AA` 的开放图块到标记 `ZZ` 的开放图块需要走多少步？**

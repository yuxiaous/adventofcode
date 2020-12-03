# Day 3: Toboggan Trajectory

> 第三天：雪橇轨道

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

> 解决了雪橇登录问题后，你出发前往机场。虽然乘坐雪橇旅行可能很容易，但它肯定不安全：雪橇转向角度极小，而且该区域被茂密的树木覆盖。你需要查看哪些角度让你经过最少的树木。

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (`.`) and trees (`#`) you can see. For example:

> 由于当地的地质原因，该区域中的树木仅生长在拥有精确整数坐标的网格中。你制作了一张地图（你的谜题输入），在上面可以看到开放区域（`.`）和树木（`#`）的。例如：

```'
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

> 然而，这些并不是仅有的树木。由于你曾经了解过一些涉及树木遗传学和生物群落稳定性的知识，因此相同的模式会在右侧重复出现多次：

```'
..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

You start on the open square (`.`) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

> 你从左上角的开放区域（`.`）出发，需要到达底部（地图最下方一行）。

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by **counting all the trees** you would encounter for the slope **right 3, down 1**:

> 雪橇只能遵循几个特定的坡度（由于你选择了一个便宜的型号，只适合有理数）。首先统计“右3下1”这个坡度上你会遇到的所有树木：

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

> 从左上角的起始位置开始，检查向右3向下1的位置。然后，从那里继续检查向右3向下1的位置，依此类推，直到到达地图的底部。

The locations you'd check in the above example are marked here with **`O`** where there was an open square and **`X`** where there was a tree:

> 在上面的例子中，你需要检查的位置如果是一个开放区域则标记为 O，如果是一棵树则标记为 `X`：

```'
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

In this example, traversing the map using this slope would cause you to encounter **`7`** trees.

> 在这个例子中，使用这个坡度通过地图，你会遇到 `7` 棵树。

Starting at the top-left corner of your map and following a slope of right 3 and down 1, **how many trees would you encounter?**

> 从你的地图左上角开始，以向右3向下1的坡度出发，你会遇到多少棵树？

Your puzzle answer was `171`.

## --- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

> 是时候检查其余的坡度了，毕竟你需要将树丛阻碍你的可能性降到最低。

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

> 对于以下的各个坡度，如果你从地图左上角开始并笔直穿过地图直到底部，确定将会遇到的树木的数量：

- Right 1, down 1.
- Right 3, down 1. (This is the slope you already checked.)
- Right 5, down 1.
- Right 7, down 1.
- Right 1, down 2.

In the above example, these slopes would find `2`, `7`, `3`, `4`, and `2` tree(s) respectively; multiplied together, these produce the answer **`336`**.

> 在上面的例子中，这些坡度将分别找到 `2`、`7`、`3`、`4` 以及 `2` 棵树，相乘将得到答案 **`336`**。

**What do you get if you multiply together the number of trees encountered on each of the listed slopes?**

> 如果你将每个列出的坡度所遇到的树木数量相乘，会得到什么？

Your puzzle answer was `1206576000`.

# Day 15: Warehouse Woes
> # 第十五天：仓库困境

You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; maybe the Chief has his own submarine down here somewhere as well?
> 你又回到了自己的迷你潜艇里！每位历史学家都驾驶着自己的潜艇朝不同方向前进；也许首席也在这里某处有自己的潜艇？

You look up to see a vast school of [lanternfish](https://adventofcode.com/2021/day/6) swimming past you. On closer inspection, they seem quite anxious, so you drive your mini submarine over to see if you can help.
> 你抬头看到一大群[灯笼鱼](https://adventofcode.com/2021/day/6)游过。仔细一看，它们似乎很焦虑，于是你驾驶潜艇靠近看看能否帮忙。

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. That's why these lanternfish have built elaborate warehouse complexes operated by robots!
> 由于灯笼鱼数量增长很快，它们需要大量食物，而这些食物需要储存。因此，这些灯笼鱼建造了由机器人管理的复杂仓库！

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics or lanternfish inventory management strategies.
> 灯笼鱼们如此焦虑，是因为它们失去了对其中一个最重要仓库机器人的控制！现在，这个机器人在仓库里乱推箱子，完全不顾灯笼鱼的物流和库存管理策略。

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, if you could anticipate the robot's movements, maybe they could find a safe option.
> 现在，没有哪条灯笼鱼敢靠近这个不可预测的机器人去关掉它。不过，如果你能预测机器人的动作，也许它们就能找到安全的解决办法。

The lanternfish already have a map of the warehouse and a list of movements the robot will **attempt** to make (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot difficult to predict.
> 灯笼鱼们已经有了仓库的地图和机器人**尝试**执行的动作列表（你的谜题输入）。问题在于，随着箱子的移动，有些动作会失败，使得机器人的实际动作难以预测。

For example:
> 例如：

```
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
```

As the robot (`@`) attempts to move, if there are any boxes (`O`) in the way, the robot will also attempt to push those boxes. However, if this action would cause the robot or a box to move into a wall (`#`), nothing moves instead, including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish gave you.
> 当机器人（`@`）尝试移动时，如果前方有箱子（`O`），它也会尝试推动这些箱子。但如果这样会导致机器人或箱子撞到墙（`#`），则什么都不会移动，包括机器人。初始位置如灯笼鱼给你的地图顶部所示。

The rest of the document describes the moves (`^` for up, `v` for down, `<` for left, `>` for right) that the robot will attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. Newlines within the move sequence should be ignored.)
> 文档的其余部分描述了机器人将要尝试的动作（`^` 上，`v` 下，`<` 左，`>` 右），按顺序执行。（这些动作实际上是一个很长的序列，分成多行只是为了方便复制粘贴，动作序列中的换行应被忽略。）

Here is a smaller example to get started:
> 下面是一个更小的例子：

```
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
```

Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:
> 如果机器人尝试执行这些动作，箱子的移动过程如下：

```
Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
```

The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:
> 更大的例子有更多动作；机器人完成所有动作后，仓库如下：

```
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
```

The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The **GPS coordinate** of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)
> 灯笼鱼们用自己的货物定位系统（GPS）来追踪箱子的位置。箱子的**GPS坐标**等于其距离地图上边缘的距离乘以100，再加上距离左边缘的距离。（这个距离不受墙体影响，要一直量到地图边缘。）

So, the box shown below has a distance of `1` from the top edge of the map and `4` from the left edge of the map, resulting in a GPS coordinate of `100 * 1 + 4 = 104`.
> 所以下面这个箱子距离地图上边缘`1`格，距离左边缘`4`格，GPS坐标为 `100 * 1 + 4 = 104`。

```
#######
#...O..
#......
```

The lanternfish would like to know the **sum of all boxes' GPS coordinates** after the robot finishes moving. In the larger example, the sum of all boxes' GPS coordinates is **`10092`**. In the smaller example, the sum is **`2028`**.
> 灯笼鱼们想知道机器人完成移动后所有箱子的GPS坐标之和。大例子的总和为 **`10092`**，小例子的总和为 **`2028`**。

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, **what is the sum of all boxes' GPS coordinates?**
> 预测仓库中机器人和箱子的运动。机器人完成移动后，**所有箱子的GPS坐标之和是多少？**

Your puzzle answer was `1465152`.

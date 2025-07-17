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

## Part Two
> ## 第二部分

The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a **second** warehouse's robot is also malfunctioning.
> 灯笼鱼们利用你的信息找到了一个安全时机游过去关闭了失控的机器人！正当它们准备为你举办庆典时，又有消息传来，**第二个**仓库的机器人也失控了。

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is **twice as wide**! The robot's list of movements doesn't change.
> 这个仓库的布局和你刚帮忙的那个非常相似。唯一的关键区别是：除了机器人以外，其他所有东西都**宽度加倍**！机器人的动作列表没有变化。

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:
> 要得到更宽的仓库地图，从原始地图开始，对每个格子做如下修改：

- If the tile is `#`, the new map contains `##` instead.
- If the tile is `O`, the new map contains `[]` instead.
- If the tile is `.`, the new map contains `..` instead.
- If the tile is `@`, the new map contains `@.` instead.
> - 如果是 `#`，新地图用 `##` 替换。
> - 如果是 `O`，新地图用 `[]` 替换。
> - 如果是 `.`，新地图用 `..` 替换。
> - 如果是 `@`，新地图用 `@.` 替换。

This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by `[]`. (The robot does not change size.)
> 这样会生成一张宽度加倍的新仓库地图，宽箱子用 `[]` 表示。（机器人大小不变。）

The larger example from before would now look like this:
> 之前的大例子现在变成这样：

```
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
```

Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:
> 由于箱子现在宽度加倍，但机器人大小和速度不变，箱子可以排列成一次直接推动两个其他箱子的情况。例如：

```
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
```

After appropriately resizing this map, the robot would push around these boxes as follows:
> 按上述方式放大地图后，机器人推动箱子的过程如下：

```
Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
```

This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of `1` from the top edge of the map and `5` from the left edge of the map, resulting in a GPS coordinate of `100 * 1 + 5 = 105`.
> 这个仓库也用GPS定位箱子。对于这些更大的箱子，距离是从地图边缘到箱子最近的边缘。例如，下图中的箱子距离地图上边缘`1`格，距离左边缘`5`格，GPS坐标为 `100 * 1 + 5 = 105`。

```
##########
##...[]...
##........
```

In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:
> 在上述大例子的放大版中，机器人完成所有动作后，仓库如下：

```
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
```

The sum of these boxes' GPS coordinates is **`9021`**.
> 这些箱子的GPS坐标之和为 **`9021`**。

Predict the motion of the robot and boxes in this new, scaled-up warehouse. **What is the sum of all boxes' final GPS coordinates?**
> 预测这个新放大仓库中机器人和箱子的运动。**所有箱子最终的GPS坐标之和是多少？**

Your puzzle answer was `1511259`.

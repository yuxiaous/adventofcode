# [Day 23: Amphipod](https://adventofcode.com/2021/day/23)

> 第23天：端足类动物

A group of [amphipods](https://en.wikipedia.org/wiki/Amphipoda) notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, "surely you can help us with a question that has stumped our best scientists."

> 一群[端足类动物](https://en.wikipedia.org/wiki/Amphipoda)注意到了你花俏的潜水艇，并将你标记下来。“多么令人印象深刻的外壳啊”，一只端足类动物说：“或许你可以帮助我们解决一个困扰我们最优秀科学家多年的问题。”

They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: **Amber** (`A`), **Bronze** (`B`), **Copper** (`C`), and **Desert** (`D`). They live in a burrow that consists of a **hallway** and four **side rooms**. The side rooms are initially full of amphipods, and the hallway is initially empty.

> 他们继续解释说，一群胆小、固执的端足类动物生活在附近的洞穴里。那里生活着四种类型的端足类动物：**琥珀色** (`A`)、**青铜色** (`B`)、**纯铜色** (`C`)和**沙漠色** (`D`)。他们住在由一个**走廊**和四个**侧室**组成的洞穴中。最初，端足类动物们都在侧室里，走廊是空的。

They give you a **diagram of the situation** ([your puzzle input](day23.txt)), including locations of each amphipod (`A`, `B`, `C`, or `D`, each of which is occupying an otherwise open space), walls (`#`), and open space (`.`).

> 他们给你一个**情况示意图**（[你的谜题输入](day23.txt)），包括每个端足类动物的位置（`A`、`B`、`C` 或 `D`，每个它占据的原本是开放的空间）、墙壁（`#`）和开放空间（`.`）。

For example:

> 举个例子：

```'
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
```

The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted `A`-`D` going left to right, like this:

> 端足类动物们想要一种安排每个端足类动物居住侧室的组织方法，每个侧室只包含一种类型的端足类动物，并且类型从左到右按 `A`-`D` 排列，如下所示：

```'
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
```

Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of **energy** to move one step: Amber amphipods require `1` energy per step, Bronze amphipods require `10` energy, Copper amphipods require `100`, and Desert ones require `1000`. The amphipods would like you to find a way to organize the amphipods that requires the **least total energy**.

> 端足类动物可以向上、向下、向左或向右移动，只要它们移动到的是一个无人的开放空间。每种类型的端足类动物移动一步所需要的**能量**不同：琥珀色端足类动物每一步需要 `1` 单位能量，青铜色端足类动物需要 `10` 单位能量，纯铜色端足类动物需要 `100` 单位能量，沙漠色端足类动物需要 `1000` 单位能量。端足类动物们希望你可以找到一种需要**总能量最少**的方法来组织端足类动物们。

However, because they are timid and stubborn, the amphipods have some extra rules:

> 然而，因为这些端足类动物们既胆小又固执，所以它们有一些额外的规则：

- Amphipods will never **stop on the space immediately outside any room**. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)
- Amphipods will never **move from the hallway into a room** unless that room is their destination room **and** that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)
- Once an amphipod stops moving in the hallway, **it will stay in that spot until it can move into a room**. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)

> - 端足类动物们永远不会**在房间门口的空间停留**。只要它们进入这个空间，他们就会持续移动。（具体来说，这个房间门口的空间是指走廊中位于端足类动物们起始位置正上方的四个开放空间。）
> - 端足类动物们永远不会**贸然从走廊进入一个房间**，除非那个房间是它们的目的地，**并且**那个房间没有其他种类的端足类动物。如果一个端足类动物的起始房间不是它的目的地房间，它可以留在那个房间直到它离开房间。（例如，琥珀色端足类动物不会从走廊进入右边的三个房间，并且只有在最左边的房间是空着的时候，或者最左边的房间里只有琥珀色端足类动物时才会进入。）
> - 一旦一只端足类动物在走廊中停止移动，**它将停留在那个位置，直到它可以进入房间**。（也就是说，一旦任何端足类动物开始移动，当前在走廊中的任何其他端足类动物都会停在原地，直到它们可以直接进入房间之前都不会再次移动。）

In the above example, the amphipods can be organized using a minimum of **`12521`** energy. One way to do this is shown below.

> 在上面的例子中，组织这些端足类动物至少需要 **`12521`** 单位能量。一种方法如下所示。

Starting configuration:

> 启动时的配置：

```'
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
```

One Bronze amphipod moves into the hallway, taking 4 steps and using `40` energy:

> 一只青铜色端足类动物进入走廊，走了 4 步，消耗 `40` 单位能量：

```'
#############
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########
```

The only Copper amphipod not in its side room moves there, taking 4 steps and using `400` energy:

> 不在自己的侧室的那只纯铜色端足类动物移动进了它自己的侧室，走了 4 步，消耗 `400` 单位能量：

```'
#############
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########
```

A Desert amphipod moves out of the way, taking 3 steps and using `3000` energy, and then the Bronze amphipod takes its place, taking 3 steps and using `30` energy:

> 一只沙漠色端足类动物移动出来，走了 3 步，消耗 `3000` 单位能量。然后青铜色端足类动物占了它的位置，走了 3 步，消耗 `30` 单位能量：

```'
#############
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########
```

The leftmost Bronze amphipod moves to its room using `40` energy:

> 最左边的青铜色端足类动物消耗 `40` 单位能量移动到了它自己的房间：

```'
#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########
```

Both amphipods in the rightmost room move into the hallway, using `2003` energy in total:

> 最右边房间的两只端足类动物都进入走廊，总共消耗 `2003` 单位能量：

```'
#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########
```

Both Desert amphipods move into the rightmost room using `7000` energy:

> 两只沙漠色端足类动物都进入了最右边的房间，消耗 `7000` 单位能量：

```'
#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########
```

Finally, the last Amber amphipod moves into its room, using `8` energy:

> 最终，最后一只琥珀色端足类动物移动进入它自己的房间，消耗 `8` 单位能量：

```'
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
```

**What is the least energy required to organize the amphipods?**

> **组织这群端足类动物，最少需要多少能量？**

Your puzzle answer was `15365`.

## --- Part Two ---

As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

> 当你准备为端足类动物们提供解决方案时，你注意到它们给你的图表实际上是折叠起来的。当你展开它时，你看见了图表的额外部分。

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:

> 从包含端足类动物的位置开始，在图表文本的第一行和第二行之间，插入以下内容：

```'
  #D#C#B#A#
  #D#B#A#C#
```

So, the above example now becomes:

> 因此，上面的例子现在变为了：

```'
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
```

The amphipods still want to be organized into rooms similar to before:

> 端足类动物们仍然希望组织成类似于之前的房间的样子：

```'
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
```

In this updated example, the least energy required to organize these amphipods is **`44169`**:

> 这次在更新的例子中，组织这些端足类动物最少需要 **`44169`** 单位能量：

```'
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#
  #########

#############
#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#
  #########

#############
#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#
  #########

#############
#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#.#.###
  #D#B#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#A#
  #########

#############
#AA.D.....AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#.#
  #########

#############
#AA.......AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #.#B#C#.#
  #D#B#C#D#
  #A#B#C#D#
  #########

#############
#AA.D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #.#B#C#D#
  #A#B#C#D#
  #########

#############
#A..D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
```

Using the initial configuration from the full diagram, **what is the least energy required to organize the amphipods?**

> 使用完整图表中的初始配置，**组织端足类动物所需的最少能量是多少？**

Your puzzle answer was `52055`.

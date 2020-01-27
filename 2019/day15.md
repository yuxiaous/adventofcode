# Day 15: Oxygen System

> 第15天：氧气系统

Out here in deep space, many things can go wrong. Fortunately, many of those things have indicator lights. Unfortunately, one of those lights is lit: the oxygen system for part of the ship has failed!

> 在太空深处，很多东西容易出问题。幸运的是，其中许多都有指示灯。不幸的是，其中一盏灯亮了 —— 飞船的一部分氧气系统出现了故障！

According to the readouts, the oxygen system must have failed days ago after a rupture in oxygen tank two; that section of the ship was automatically sealed once oxygen levels went dangerously low. A single remotely-operated **repair droid** is your only option for fixing the oxygen system.

> 根据读数，氧气系统一定是在几天前二号氧气罐破裂后产生了故障，一旦氧气含量降低到危险的程度，飞船的那部分便被自动密封。唯一的一台远程操控**维修机器人**是修复氧气系统的唯一选择。

The Elves' care package included an [Intcode](day9.md) program ([your puzzle input](day15.txt)) that you can use to remotely control the repair droid. By running that program, you can direct the repair droid to the oxygen system and fix the problem.

> 精灵的护理包包含了一段 [Intcode](day9.md) 程序（[你的谜题输入](day15.txt)），你可以使用该程序远程控制维修机器人。通过运行该程序，你可以指挥维修机器人到达氧气系统并解决问题。

The remote control program executes the following steps in a loop forever:

- Accept a **movement command** via an input instruction.
- Send the movement command to the repair droid.
- Wait for the repair droid to finish the movement operation.
- Report on the **status** of the repair droid via an output instruction.

> 远程控制程序将不断循环执行以下步骤：
>
> - 通过输入指令接收**移动命令**。
> - 将移动命令发送到维修机器人。
> - 等待维修机器人完成移动操作。
> - 通过输出指令汇报维修机器人的**状态**。

Only four **movement commands** are understood: north (`1`), south (`2`), west (`3`), and east (`4`). Any other command is invalid. The movements differ in direction, but not in distance: in a long enough east-west hallway, a series of commands like `4,4,4,4,3,3,3,3` would leave the repair droid back where it started.

> 只有四种**移动命令**可以识别：北（`1`）、南（`2`）、西（`3`）和东（`4`）。其他命令无效。移动只在方向上有所不同，而不是在距离上：在一条足够长的东西走向的走廊中，例如 `4,4,4,4,3,3,3,3` 这样的一串命令将会让维修机器人返回它开始的位置。

The repair droid can reply with any of the following **status** codes:

- `0`: The repair droid hit a wall. Its position has not changed.
- `1`: The repair droid has moved one step in the requested direction.
- `2`: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.

> 修复机器人可以回复以下任意一个**状态**码：
>
> - `0`：修理机器人撞到了墙。它的位置没有改变。
> - `1`：维修机器人沿要求的方向移动了一步。
> - `2`：修复机器人沿要求的方向移动了一步，它的新位置正处于氧气系统。

You don't know anything about the area around the repair droid, but you can figure it out by watching the status codes.

> 你对修复机器人周围的区域一无所知，但是你可以通过查看状态码来解决。

For example, we can draw the area using `D` for the droid, `#` for walls, `.` for locations the droid can traverse, and empty space for unexplored locations. Then, the initial state looks like this:

> 例如，我们可以使用 `D` 表示机器人，`#` 表示墙，`.` 表示机器人可以通过的地点，以及空白区域表示未探索的地点来绘制这个区域。那么，初始状态如下所示：

```'


   D  


```

To make the droid go north, send it `1`. If it replies with `0`, you know that location is a wall and that the droid didn't move:

> 要让机器人向北移动，则向它发送 `1`。如果回复为 `0`，则说明该地点是一堵墙，机器人没有移动：

```'

   #  
   D  


```

To move east, send `4`; a reply of `1` means the movement was successful:

> 向东移动，发送 `1`； 回复 `1` 表示移动成功：

```'

   #  
   .D


```

Then, perhaps attempts to move north (`1`), south (`2`), and east (`4`) are all met with replies of `0`:

> 接下来，或许向北移动（`1`），向南移动（`2`）和向东移动（`4`）的尝试都得到了 `0` 的回复：

```'

   ##
   .D#
    #

```

Now, you know the repair droid is in a dead end. Backtrack with `3` (which you already know will get a reply of `1` because you already know that location is open):

> 现在，你知道修复机器人走进了死胡同。通过 `3` 返回（你知道这将得到 `1` 的回复，因为你已经知道那个地点是开放的）：

```'

   ##
   D.#
    #

```

Then, perhaps west (`3`) gets a reply of `0`, south (`2`) gets a reply of `1`, south again (`2`) gets a reply of `0`, and then west (`3`) gets a reply of `2`:

> 接下来，或许向西（`3`）得到 `0` 的回复，向南（`2`）得到 `1` 的回复，再次向南（`2`）得到 `0` 的回复，然后向西（`3`）得到 `2` 的回复：

```'

   ##
  #..#
  D.#
   #  
```

Now, because of the reply of `2`, you know you've found the **oxygen system**! In this example, it was only **`2`** moves away from the repair droid's starting position.

> 现在，由于得到了 `2` 的回复，你知道你已经找到了**氧气系统**！在这个例子中，从修复机器人的起始位置到达氧气系统只需要移动 **`2`** 步的距离 。

**What is the fewest number of movement commands** required to move the repair droid from its starting position to the location of the oxygen system?

> 将修理机器人从起始位置移动到氧气系统的位置，**所需的最少移动命令数量是多少**？

Your puzzle answer was `220`.

## Part Two

You quickly repair the oxygen system; oxygen gradually fills the area.

> 你快速修复了氧气系统，氧气逐渐充满了区域。

Oxygen starts in the location containing the repaired oxygen system. It takes **one minute** for oxygen to spread to all open locations that are adjacent to a location that already contains oxygen. Diagonal locations are **not** adjacent.

> 氧气从包含修复后的氧气系统的位置开始。氧气需要花费**一分钟**时间扩散到与已经有氧气的位置相邻的所有开放位置。对角线位置是不相邻的。

In the example above, suppose you've used the droid to explore the area fully and have the following map (where locations that currently contain oxygen are marked `O`):

> 在上面的例子中，假设你已使用机器人探索了全部的区域并且拥有了以下地图（当前含氧气的位置标记为 `O`）：

```'
 ##
#..##
#.#..#
#.O.#
 ###
```

Initially, the only location which contains oxygen is the location of the repaired oxygen system. However, after one minute, the oxygen spreads to all open (`.`) locations that are adjacent to a location containing oxygen:

> 最初，唯一包含氧气的地点是经过修复的氧气系统的地点。然而，在一分钟后，氧气扩散到与含有氧气的地点相邻的所有开放（`.`）地点：

```'
 ##
#..##
#.#..#
#OOO#
 ###
```

After a total of two minutes, the map looks like this:

> 两分钟后，地图如下所示：

```'
 ##
#..##
#O#O.#
#OOO#
 ###
```

After a total of three minutes:

> 三分钟后：

```'
 ##
#O.##
#O#OO#
#OOO#
 ###
```

And finally, the whole region is full of oxygen after a total of four minutes:

> 最后，总共经过四分钟，整个区域都充满了氧气：

```'
 ##
#OO##
#O#OO#
#OOO#
 ###
```

So, in this example, all locations contain oxygen after **`4`** minutes.

> 所以，在这个例子中，所有地点在 **`4`** 分钟后都充满了氧气。

Use the repair droid to get a complete map of the area. **How many minutes will it take to fill with oxygen?**

> 使用修复机器人获取该区域的完整地图。**充满氧气需要多少分钟？**

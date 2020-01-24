# Day 13: Care Package

> 第13天：关爱套装

As you ponder the solitude of space and the ever-increasing three-hour roundtrip for messages between you and Earth, you notice that the Space Mail Indicator Light is blinking. To help keep you sane, the Elves have sent you a care package.

> 你在寂静的深空中沉思，此时往返地球的信息所花费的时间已经增加到了三个小时，你注意到太空邮件指示灯正在闪烁。为了让你保持头脑清晰，精灵发送给你了一个关爱套装。

It's a new game for the ship's [arcade cabinet](https://en.wikipedia.org/wiki/Arcade_cabinet)! Unfortunately, the arcade is **all the way** on the other end of the ship. Surely, it won't be hard to build your own - the care package even comes with schematics.

> 这是一款飞船[街机柜](https://en.wikipedia.org/wiki/Arcade_cabinet)上的新游戏！不幸的是，街机在距离飞船**遥远的**另一头（在地球上）。当然，你自己动手建造一台也并不困难 —— 关爱套装里甚至还附带了原理图。

The arcade cabinet runs [Intcode](day9.md) software like the game the Elves sent ([your puzzle input](day13.txt)). It has a primitive screen capable of drawing square **tiles** on a grid. The software draws tiles to the screen with output instructions: every three output instructions specify the `x` position (distance from the left), `y` position (distance from the top), and `tile id`. The `tile id` is interpreted as follows:

- `0` is an **empty** tile. No game object appears in this tile.
- `1` is a **wall** tile. Walls are indestructible barriers.
- `2` is a **block** tile. Blocks can be broken by the ball.
- `3` is a **horizontal paddle** tile. The paddle is indestructible.
- `4` is a **ball** tile. The ball moves diagonally and bounces off objects.

> 街机柜运行 [Intcode](day9.md) 软件，就像精灵们发送给你的游戏（[你的谜题输入](day13.txt)）一样。它有一块能够在网格上绘制正方形**图块**的原始屏幕。软件通过输出指令在屏幕上绘制图块：每三个输出指令分别指定 `x` 位置（距左侧的距离）、`y` 位置（距顶部的距离）和`图块ID`。`图块ID` 的定义如下：
>
> - `0` 表示一个**空**。没有游戏对象出现在此图块中。
> - `1` 表示一个**墙**。墙是坚不可摧的屏障。
> - `2` 表示一个**障碍**。障碍可以被球击碎。
> - `3` 表示**水平挡板**。挡板是坚不可摧的。
> - `4` 表示**球**。球沿对角线移动并从物体上反弹。

For example, a sequence of output values like `1,2,3,6,5,4` would draw a **horizontal paddle** tile (`1` tile from the left and `2` tiles from the top) and a **ball** tile (`6` tiles from the left and `5` tiles from the top).

> 例如，一串输出值（如 `1,2,3,6,5,4`）将绘制一个**水平挡板**图块（距离左侧 `1` 图块，距离顶部 `2` 图块），以及一个**球**图块（距离左侧 `6` 图块，距离顶部 `5` 图块）。

Start the game. **How many block tiles are on the screen when the game exits?**

> 开始游戏。**当游戏结束时屏幕上有多少个障碍方块？**

Your puzzle answer was `372`.

## Part Two

The game didn't run because you didn't put in any quarters. Unfortunately, you did not bring any quarters. Memory address `0` represents the number of quarters that have been inserted; set it to `2` to play for free.

> 游戏没有运行，因为你没有投入游戏币。不幸的是，你没有带游戏币。内存地址 `0` 代表已投入的游戏币数量，将其设置为 `2` 就可以免费玩了。

The arcade cabinet has a [joystick](https://en.wikipedia.org/wiki/Joystick) that can move left and right. The software reads the position of the joystick with input instructions:

- If the joystick is in the **neutral position**, provide `0`.
- If the joystick is **tilted to the left**, provide `-1`.
- If the joystick is **tilted to the right**, provide `1`.

> 街机柜有一个[操纵杆](https://en.wikipedia.org/wiki/Joystick)可以左右移动。软件通过输入指令读取操纵杆的位置：
>
> - 如果操纵杆在**中间位置**，则得到 `0`。
> - 如果操纵杆**向左边倾斜**，则得到 `-1`。
> - 如果操纵杆**向右边倾斜**，则得到 `1`。

The arcade cabinet also has a [segment display](https://en.wikipedia.org/wiki/Display_device#Segment_displays) capable of showing a single number that represents the player's current score. When three output instructions specify `X=-1, Y=0`, the third output instruction is not a tile; the value instead specifies the new score to show in the segment display. For example, a sequence of output values like `-1,0,12345` would show `12345` as the player's current score.

> 街机柜还具有[段显示](https://en.wikipedia.org/wiki/Display_device#Segment_displays)，能够显示代表玩家当前得分的单个数字。当三个输出指令指定 `X=-1, Y=0` 时，则第三个输出指令不是图块，而是在段显示中显示的新分数。例如，一系列输出值（如 `-1,0,12345`）将显示 `12345` 作为玩家的当前得分。

Beat the game by breaking all the blocks. **What is your score after the last block is broken?**

> 通过打破所有障碍来通关游戏。**当打破最后一个障碍后，你的分数会是多少？**

Your puzzle answer was `19297`.

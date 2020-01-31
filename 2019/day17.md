# Day 17: Set and Forget

> 第17天：设置并忘记

An early warning system detects an incoming [solar flare](https://en.wikipedia.org/wiki/Solar_flare) and automatically activates the ship's electromagnetic shield. Unfortunately, this has cut off the Wi-Fi for many small robots that, unaware of the impending danger, are now trapped on exterior scaffolding on the unsafe side of the shield. To rescue them, you'll have to act quickly!

> 预警系统检测到即将来临的[太阳耀斑](https://en.wikipedia.org/wiki/Solar_flare)并自动激活了飞船的电磁防护罩。不幸的是，这已经切断了许多小型机器人的Wi-Fi，这些机器人没有意识到即将发生的危险，现在被困在防护罩不安全一侧的外部脚手架上。要营救他们，你必须迅速采取行动！

The only tools at your disposal are some wired cameras and a small vacuum robot currently asleep at its charging station. The video quality is poor, but the vacuum robot has a needlessly bright LED that makes it easy to spot no matter where it is.

> 你唯一可以使用的工具是一些有线摄像机和一个小型真空机器人，该机器人目前正在充电站处于睡眠状态。视频质量很差，但是真空机器人有一颗的明亮的 LED，无论在哪里都可以很容易地发现它。

An [Intcode](day9.md) program, the **Aft Scaffolding Control and Information Interface** (ASCII, [your puzzle input](day17.txt)), provides access to the cameras and the vacuum robot. Currently, because the vacuum robot is asleep, you can only access the cameras.

> 一段 [Intcode](day9.md) 程序，**后脚手架控制和信息接口**（ASCII，[你的谜题输入](day17.txt)），可用于接入摄像机和真空机器人。当前，由于真空机器人正处于睡眠状态，你只能接入摄像机。

Running the ASCII program on your Intcode computer will provide the current view of the scaffolds. This is output, purely coincidentally, as [ASCII code](https://simple.wikipedia.org/wiki/ASCII): `35` means `#`, `46` means `.`, `10` starts a [new line](https://en.wikipedia.org/wiki/Newline#In_programming_languages) of output below the current one, and so on. (Within a line, characters are drawn left-to-right.)

> 在 Intcode 计算机上运行 ASCII 程序将提供脚手架的当前图像。非常凑巧的是，图像以 [ASCII 码](https://simple.wikipedia.org/wiki/ASCII)进行输出：`35` 表示 `#`，`46` 表示 `.`，`10` 表示在当前行的下方开始[新的一行](https://en.wikipedia.org/wiki/Newline#In_programming_languages)，依此类推。（在一行中，字符从左到右绘制。）

In the camera output, `#` represents a scaffold and `.` represents open space. The vacuum robot is visible as `^`, `v`, `<`, or `>` depending on whether it is facing up, down, left, or right respectively. When drawn like this, the vacuum robot is **always on a scaffold**; if the vacuum robot ever walks off of a scaffold and begins **tumbling through space uncontrollably**, it will instead be visible as `X`.

> 在摄像机输出中，`#` 代表脚手架，`.` 代表开放空间。真空机器人显示为 `^`、 `v`、 `<` 或 `>`，这取决于机器人面朝的方向（朝上、朝下、朝左或是朝右）。像这样显示时，真空机器人是**一直在脚手架上的**。如果真空机器人在脚手架上踩空，将会**无法控制地滚入太空中**，显示为 `X`。

In general, the scaffold forms a path, but it sometimes loops back onto itself. For example, suppose you can see the following view from the cameras:

> 通常，脚手架形成一条路径，但有时会绕一圈回来与自身交叉。例如，假设你可以从摄像机看到以下图像：

```'
..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..
```

Here, the vacuum robot, `^` is facing up and sitting at one end of the scaffold near the bottom-right of the image. The scaffold continues up, loops across itself several times, and ends at the top-left of the image.

> 此时，真空机器人（`^`）面朝上方，并站在图像右下角附近的脚手架的一端。脚手架持续地向上、转回交叉多次，并在图像的左上方结束。

The first step is to calibrate the cameras by getting the **alignment parameters** of some well-defined points. Locate all **scaffold intersections**; for each, its alignment parameter is the distance between its left edge and the left edge of the view multiplied by the distance between its top edge and the top edge of the view. Here, the intersections from the above image are marked `O`:

> 第一步是通过获取一些定义明确的点作为**校准参数**来校准摄像机。定位所有的**脚手架交叉点**，对于每个交叉点，它的校准参数是其到图像左边边缘的距离乘以其到图像顶部边缘的距离。这里，将上面图像的交叉点标记为 `O`：

```'
..#..........
..#..........
##O####...###
#.#...#...#.#
##O###O###O##
..#...#...#..
..#####...^..
```

For these intersections:

- The top-left intersection is `2` units from the left of the image and `2` units from the top of the image, so its alignment parameter is `2 * 2 = 4`.
- The bottom-left intersection is `2` units from the left and `4` units from the top, so its alignment parameter is `2 * 4 = 8`.
- The bottom-middle intersection is `6` from the left and `4` from the top, so its alignment parameter is `24`.
- The bottom-right intersection's alignment parameter is `40`.

> 对于这些交叉点：
>
> - 左上的交叉点从图像的左边起 `2` 个单位，从图像的顶部起 `2` 个单位，因此它的校准参数为 `2 * 2 = 4`。
> - 左下的交叉点从左边起 `2` 个单位，从顶部起 `4` 个单位，因此它的校准参数为 `2 * 4 = 8`。
> - 底部中间的交叉点从左边起是 `6`，从顶部起 `4`，因此它的校准参数为 `24`。
> - 右下的交叉点的校准参数为 `40`。

To calibrate the cameras, you need the **sum of the alignment parameters**. In the above example, this is **`76`**.

> 要校准摄像机，你需要**对校准参数求和**。在上面的示例中，求和得到 **`76`**。

Run your ASCII program. **What is the sum of the alignment parameters** for the scaffold intersections?

> 运行你的 ASCII 程序。脚手架交叉点的**校准参数的总和是多少**？

Your puzzle answer was `5972`.

## Part Two

Now for the tricky part: notifying all the other robots about the solar flare. The vacuum robot can do this automatically if it gets into range of a robot. However, you can't see the other robots on the camera, so you need to be thorough instead: you need to make the vacuum robot **visit every part of the scaffold at least once**.

> 现在最棘手的部分：通知所有其他机器人关于太阳耀斑的事。如果真空机器人进入另一个机器人的范围，就可以自动执行此操作。但是，你无法在摄像机中看到其他机器人，所以你需要彻底改变想法：你需要让真空机器人**一次性访问脚手架的所有部分**。

The vacuum robot normally wanders randomly, but there isn't time for that today. Instead, you can **override its movement logic** with new rules.

> 真空机器人通常会随机游荡，但是今天没有那个时间了。取而代之的，你可以使用新的规则来**重置它的移动逻辑**。

Force the vacuum robot to wake up by changing the value in your ASCII program at address `0` from `1` to **`2`**. When you do this, you will be automatically prompted for the new movement rules that the vacuum robot should use. The ASCII program will use input instructions to receive them, but they need to be provided as ASCII code; end each line of logic with a single newline, ASCII code `10`.

> 通过将 ASCII 程序中地址 `0` 处的值从 `1` 改为 **`2`**，强制唤醒真空机器人。当你执行此操作时，系统将自动提示你输入真空机器人需要使用的新的移动规则。ASCII 程序将使用输入指令来接收它们，但是需要将它们作为 ASCII 代码提供，用单个换行符 ASCII 码 `10` 结束逻辑的每一行。

First, you will be prompted for the **main movement routine**. The main routine may only call the **movement functions**: `A`, `B`, or `C`. Supply the movement functions to use as ASCII text, separating them with commas (`,`, ASCII code `44`), and ending the list with a newline (ASCII code `10`). For example, to call `A` twice, then alternate between `B` and `C` three times, provide the string `A,A,B,C,B,C,B,C` and then a newline.

> 首先，系统将提示你输入**主移动例程**。主例程只调用**移动函数**：`A`、`B` 或 `C`。以 ASCII 文本格式提供所使用的移动函数，用逗号（`,`，ASCII 码 `44`）分隔它们，并以换行符结束列表（ASCII 码 `10`）。例如，调用 `A` 两次，然后在 `B` 和 `C` 之间交替三次，需要提供字符串 `A,A,B,C,B,C,B,C` 接着是一个换行符。

Then, you will be prompted for each **movement function**. Movement functions may use `L` to **turn left**, `R` to **turn right**, or a number to **move forward** that many units. Movement functions may not call other movement functions. Again, separate the actions with commas and end the list with a newline. For example, to move forward `10` units, turn left, move forward `8` units, turn right, and finally move forward `6` units, provide the string `10,L,8,R,6` and then a newline.

> 接下来，系统将提示你输入各个**移动函数**。移动函数使用 `L` **左转**，`R` **右转**或一个数字表示**向前移动**的单位数量。移动函数不能调用其它的移动函数。同样的，用逗号分隔操作，并以换行符结束列表。例如，向前移动 `10` 个单位，向左转，向前移动 `8` 个单位，向右转，最后向前移动 `6` 个单位，需要提供字符串 `10,L,8,R,6` 接着是一个换行符。

Finally, you will be asked whether you want to see a **continuous video feed**; provide either `y` or `n` and a newline. Enabling the continuous video feed can help you see what's going on, but it also requires a significant amount of processing power, and may even cause your Intcode computer to overheat.

> 最后，系统将会询问你是否需要查看**连续视频反馈**，提供 `y` 或 `n` 以及一个换行符。启用连续视频反馈可以帮助你了解正在发生的情况，但是它也需要大量的处理能力，甚至可能导致你的 Intcode 计算机过热。

Due to the limited amount of memory in the vacuum robot, the ASCII definitions of the main routine and the movement functions may each contain **at most 20 characters**, not counting the newline.

> 由于真空机器人的内存容量有限，每条主例程和移动函数的 ASCII 定义可能包含**最多 20 个字符**，不包括换行符。

For example, consider the following camera feed:

> 例如，考虑以下摄像机的反馈：

```'
#######...#####
#.....#...#...#
#.....#...#...#
......#...#...#
......#...###.#
......#.....#.#
^########...#.#
......#.#...#.#
......#########
........#...#..
....#########..
....#...#......
....#...#......
....#...#......
....#####......
```

In order for the vacuum robot to **visit every part of the scaffold at least once**, one path it could take is:

> 为了使真空机器人**一次性访问脚手架的所有部分**，采取的单行路径是：

```'
R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2
```

Without the memory limit, you could just supply this whole string to function `A` and have the main routine call `A` once. However, you'll need to split it into smaller parts.

> 如果没有内存的限制，你只需将整个字符串提供给函数 `A`，并在主例程中调用 `A` 一次。但是，你需要将它拆分成更小的部分。

One approach is:

> 一种途径是：

- **Main routine: `A,B,C,B,A,C`**
(ASCII input: `65`, `44`, `66`, `44`, `67`, `44`, `66`, `44`, `65`, `44`, `67`, `10`)
- **Function `A`:   `R,8,R,8`**
(ASCII input: `82`, `44`, `56`, `44`, `82`, `44`, `56`, `10`)
- **Function `B`:   `R,4,R,4,R,8`**
(ASCII input: `82`, `44`, `52`, `44`, `82`, `44`, `52`, `44`, `82`, `44`, `56`, `10`)
- **Function `C`:   `L,6,L,2`**
(ASCII input: `76`, `44`, `54`, `44`, `76`, `44`, `50`, `10`)

Visually, this would break the desired path into the following parts:

> 在视觉上，这会将所需的路径分为以下几部分：

```'
A,        B,            C,        B,            A,        C
R,8,R,8,  R,4,R,4,R,8,  L,6,L,2,  R,4,R,4,R,8,  R,8,R,8,  L,6,L,2

CCCCCCA...BBBBB
C.....A...B...B
C.....A...B...B
......A...B...B
......A...CCC.B
......A.....C.B
^AAAAAAAA...C.B
......A.A...C.B
......AAAAAA#AB
........A...C..
....BBBB#BBBB..
....B...A......
....B...A......
....B...A......
....BBBBA......
```

Of course, the scaffolding outside your ship is much more complex.

> 当然，飞船外面的脚手架要比这复杂得多。

As the vacuum robot finds other robots and notifies them of the impending solar flare, it also can't help but leave them squeaky clean, collecting any space dust it finds. Once it finishes the programmed set of movements, assuming it hasn't drifted off into space, the cleaning robot will return to its docking station and report the amount of space dust it collected as a large, non-ASCII value in a single output instruction.

> 当真空机器人找到其他机器人并通知他们即将来临的太阳耀斑时，它也忍不住将它们吱吱作响地清理干净，并收集发现的任何太空尘埃。一旦完成了编程的移动设置（假设它没有漂入太空），清洁机器人将返回它的停靠站，并在单个输出指令中以一个大的非 ASCII 值汇报所收集到的太空尘埃的数量。

After visiting every part of the scaffold at least once, **how much dust does the vacuum robot report it has collected?**

> 在一次性访问脚手架的所有部分之后，**真空机器人汇报它收集了多少尘埃？**

Your puzzle answer was `933214`.

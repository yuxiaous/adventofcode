# Day 11: Space Police

> 第11天：太空警察

On the way to Jupiter, you're [pulled over](https://www.youtube.com/watch?v=KwY28rpyKDE) by the **Space Police**.

> 在前往木星的途中，你被**太空警察**[拦住了](https://www.youtube.com/watch?v=KwY28rpyKDE)。

"Attention, unmarked spacecraft! You are in violation of Space Law! All spacecraft must have a clearly visible **registration identifier**! You have 24 hours to comply or be sent to [Space Jail](https://www.youtube.com/watch?v=BVn1oQL9sWg&t=5)!"

> “注意，无牌飞船！你违反了太空法！所有飞船都必须具有一个清晰可见的**注册编号**！限你24小时内上好牌照，否则你将被送往[太空监狱](https://www.youtube.com/watch?v=BVn1oQL9sWg&t=5)！”

Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for help. Although it takes almost three hours for their reply signal to reach you, they send instructions for how to power up the **emergency hull painting robot** and even provide a small [Intcode program](day9.md) ([your puzzle input](day11.txt)) that will cause it to paint your ship appropriately.

> 你不想被送往太空监狱，所以用无线电向地球上的精灵们寻求帮助。尽管它们的回信需要花费将近三个小时的时间才能到达这里，但他们仍旧发送发给你了如何启动**应急船体涂装机器人**的指令，甚至还提供了一小段的 [Intcode 程序](day9.md)（[你的谜题输入](day11.txt)），这将使它能够正确地喷涂你的飞船。

There's just one problem: you don't have an emergency hull painting robot.

> 不过有一个问题：你没有应急船体涂装机器人。

You'll need to build a new emergency hull painting robot. The robot needs to be able to move around on the grid of square panels on the side of your ship, detect the color of its current panel, and paint its current panel **black** or **white**. (All of the panels are currently **black**.)

> 你需要建造一个新的应急船体涂装机器人。机器人需要能够在飞船侧面的方形面板网格上移动，检测当前面板的颜色，并且将当前面板喷涂成**黑色**或**白色**。（所有面板当前都是**黑色**的。）

The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's camera: provide `0` if the robot is over a **black** panel or `1` if the robot is over a **white** panel. Then, the program will output two values:

- First, it will output a value indicating the **color to paint the panel** the robot is over: `0` means to paint the panel **black**, and `1` means to paint the panel **white**.
- Second, it will output a value indicating the **direction the robot should turn**: `0` means it should turn **left 90 degrees**, and `1` means it should turn **right 90 degrees**.

> Intcode 程序将充当机器人的大脑。程序使用输入指令来访问机器人的摄像机：如果机器人站在**黑色**面板上，则得到`0`；如果机> 器人站在**白色**面板上，则得到`1`。然后，程序将输出两个值：
>
> - 首先，它将输出一个值表示机器人所站的**面板的喷涂颜色**：`0` 表示将面板涂成**黑色**，而 `1` 表示将面板涂成**白色**。
> - 其次，它将输出一个值表示**机器人转动的方向**：`0` 表示**向左旋转90度**，`1` 表示**向右旋转90度**。

After the robot turns, it should always move **forward exactly one panel**. The robot starts facing **up**.

> 当机器人旋转之后，它会**向前移动正好一个面板**。机器人最开始是朝**上**的。

The robot will continue running for a while like this and halt when it is finished drawing. Do not restart the Intcode computer inside the robot during this process.

> 机器人会像这样持续运行一段时间，并在完成绘制后停止。不要在这个过程中重新启动机器人内部的 Intcode 计算机。

For example, suppose the robot is about to start running. Drawing black panels as `.`, white panels as `#`, and the robot pointing the direction it is facing (`< ^ > v`), the initial state and region near the robot looks like this:

> 举个例子，假设机器人即将开始运行。将黑色面板表示为 `.`，将白色面板表示为 `#`，并且机器人面对的方向用（`< ^ > v`）表示，机器人的初始状态和附近区域如下所示：

```'
.....
.....
..^..
.....
.....
```

The panel under the robot (not visible here because a `^` is shown instead) is also black, and so any input instructions at this point should be provided `0`. Suppose the robot eventually outputs `1` (paint white) and then `0` (turn left). After taking these actions and moving forward one panel, the region now looks like this:

> 机器人下方的面板（此处不可见，因为显示了 `^`）也为黑色，所以在这个位置的输入指令会得到 `0`。假设机器人输出了 `1`（涂成白色），然后输出 `0`（左转）。在完成这些动作后向前移动一个面板，该区域现在如下所示：

```'
.....
.....
.<#..
.....
.....
```

Input instructions should still be provided `0`. Next, the robot might output `0` (paint black) and then `0` (turn left):

> 输入指令仍会得到 `0`。接下来，机器人会输出 `0`（涂成黑色），然后是 `0`（左转）：

```'
.....
.....
..#..
.v...
.....
```

After more outputs (`1,0`, `1,0`):

> 之后更多的输出（`1,0`, `1,0`）：

```'
.....
.....
..^..
.##..
.....
```

The robot is now back where it started, but because it is now on a white panel, input instructions should be provided `1`. After several more outputs (`0,1`, `1,0`, `1,0`), the area looks like this:

> 机器人现在又回到了最开始的位置，但是由于它现在站在白色面板上，输入指令会得到 `1`。之后再几个输出（`0,1`, `1,0`, `1,0`），该区域如下所示：

```'
.....
..<#.
...#.
.##..
.....
```

Before you deploy the robot, you should probably have an estimate of the area it will cover: specifically, you need to know the **number of panels it paints at least once**, regardless of color. In the example above, the robot painted **`6` panels** at least once. (It painted its starting panel twice, but that panel is [still only counted once](https://www.youtube.com/watch?v=KjsSvjA5TuE); it also never painted the panel it ended on.)

> 在部署机器人之前，你应该大概估算以下它将覆盖的面积：特别是你需要知道**喷涂过的面板数量**（无论其颜色如何）。在上面的例子中，机器人喷涂了 **`6` 块面板**。（它喷涂了起始面板两次，但该面板[只计一次](https://www.youtube.com/watch?v=KjsSvjA5TuE)，它结束时所站的面板没有喷涂。）

Build a new emergency hull painting robot and run the Intcode program on it. **How many panels does it paint at least once?**

> 建造一个新的应急船体涂装机器人并运行 Intcode 程序。**它喷涂了多少块面板？**

Your puzzle answer was `2088`.

## Part Two

You're not sure what it's trying to paint, but it's definitely not a **registration identifier**. The Space Police are getting impatient.

> 虽然你不确定它到底绘制的是什么东西，但那绝对不是**注册编号**。太空警察有些不耐烦了。

Checking your external ship cameras again, you notice a white panel marked "emergency hull painting robot starting panel". The rest of the panels are **still black**, but it looks like the robot was expecting to **start on a white panel**, not a black one.

> 你再次检查了飞船外部摄像机，你注意到一块白色的面板上面写着：“应急船体涂装机器人起始面板”。其余的面板**仍是黑色**，但看起来机器人是**从白色面板开始的**，而不是黑色面板。

Based on the Space Law Space Brochure that the Space Police attached to one of your windows, a valid registration identifier is always **eight capital letters**. After starting the robot on a single **white panel** instead, **what registration identifier does it paint** on your hull?

> 根据太空警察贴在你的一扇窗户上的《太空法太空手册》，一个有效的注册编号由**八个大写字母**组成。在**白色面板**上启动机器人之后，它在你的飞船在外壳上**涂了什么注册编号**？

Your puzzle answer was `URCAFLCP`.

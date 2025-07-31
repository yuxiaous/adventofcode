# Day 21: Keypad Conundrum
> # 第二十一天：小键盘谜题

As you teleport onto Santa's [Reindeer-class starship](https://adventofcode.com/2019/day/25), The Historians begin to panic: someone from their search party is **missing**. A quick life-form scan by the ship's computer reveals that when the missing Historian teleported, he arrived in another part of the ship.
> 当你传送到圣诞老人[驯鹿级星舰](https://adventofcode.com/2019/day/25)时，历史学家们开始慌乱：他们的队伍里**有人失踪了**。飞船的电脑快速扫描生命体后发现，失踪的历史学家传送到了飞船的另一个区域。

The door to that area is locked, but the computer can't open it; it can only be opened by **physically typing** the door codes (your puzzle input) on the numeric keypad on the door.
> 那个区域的门被锁住了，电脑无法打开；只能通过在门上的数字小键盘**手动输入**门禁码（你的谜题输入）来打开。

The numeric keypad has four rows of buttons: `789`, `456`, `123`, and finally an empty gap followed by `0A`. Visually, they are arranged like this:
> 数字小键盘有四排按钮：`789`、`456`、`123`，最后一排是空格和 `0A`。排列如下：

```
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
```

Unfortunately, the area outside the door is currently **depressurized** and nobody can go near the door. A robot needs to be sent instead.
> 不幸的是，门外区域目前**失压**，没人能靠近门。只能派机器人去。

The robot has no problem navigating the ship and finding the numeric keypad, but it's not designed for button pushing: it can't be told to push a specific button directly. Instead, it has a robotic arm that can be controlled remotely via a **directional keypad**.
> 机器人能顺利找到数字小键盘，但它不是为按键设计的：你不能直接让它按某个按钮。它有一只机械臂，可以通过**方向键盘**远程控制。

The directional keypad has two rows of buttons: a gap / `^` (up) / `A` (activate) on the first row and `<` (left) / `v` (down) / `>` (right) on the second row. Visually, they are arranged like this:
> 方向键盘有两排按钮：第一排是空格、`^`（上）、`A`（激活），第二排是`<`（左）、`v`（下）、`>`（右）。排列如下：

```
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
```

When the robot arrives at the numeric keypad, its robotic arm is pointed at the `A` button in the bottom right corner. After that, this directional keypad remote control must be used to maneuver the robotic arm: the up / down / left / right buttons cause it to move its arm one button in that direction, and the `A` button causes the robot to briefly move forward, pressing the button being aimed at by the robotic arm.
> 机器人到达数字小键盘时，机械臂指向右下角的`A`键。之后，必须用方向键盘遥控机械臂：上下左右按钮让机械臂朝那个方向移动一格，`A`按钮让机器人前移一下，按下机械臂当前指向的按钮。

For example, to make the robot type `029A` on the numeric keypad, one sequence of inputs on the directional keypad you could use is:
> 例如，要让机器人在数字小键盘上输入 `029A`，你可以用如下方向键盘输入序列：

- `<` to move the arm from `A` (its initial position) to `0`.
- `A` to push the `0` button.
- `^A` to move the arm to the `2` button and push it.
- `>^^A` to move the arm to the `9` button and push it.
- `vvvA` to move the arm to the `A` button and push it.
> - `<` 把机械臂从初始的`A`移到`0`。
> - `A` 按下`0`。
> - `^A` 移到`2`并按下。
> - `>^^A` 移到`9`并按下。
> - `vvvA` 移到`A`并按下。

In total, there are three shortest possible sequences of button presses on this directional keypad that would cause the robot to type `029A`: `<A^A>^^AvvvA`, `<A^A^>^AvvvA`, and `<A^A^^>AvvvA`.
> 总共有三种最短的方向键盘按键序列能让机器人输入 `029A`：`<A^A>^^AvvvA`、`<A^A^>^AvvvA` 和 `<A^A^^>AvvvA`。

Unfortunately, the area containing this directional keypad remote control is currently experiencing **high levels of radiation** and nobody can go near it. A robot needs to be sent instead.
> 不幸的是，方向键盘遥控器所在区域**辐射极高**，没人能靠近。只能再派机器人去。

When the robot arrives at the directional keypad, its robot arm is pointed at the `A` button in the upper right corner. After that, a **second, different** directional keypad remote control is used to control this robot (in the same way as the first robot, except that this one is typing on a directional keypad instead of a numeric keypad).
> 机器人到达方向键盘时，机械臂指向右上角的`A`键。之后，用**第二个不同的**方向键盘遥控器控制这个机器人（方式和第一个机器人一样，只不过这次是在方向键盘上按键，而不是数字小键盘）。

There are multiple shortest possible sequences of directional keypad button presses that would cause this robot to tell the first robot to type `029A` on the door. One such sequence is `v<<A>>^A<A>AvA<^AA>A<vAAA>^A`.
> 有多种最短的方向键盘按键序列能让这个机器人指挥第一个机器人在门上输入 `029A`。其中一种是 `v<<A>>^A<A>AvA<^AA>A<vAAA>^A`。

Unfortunately, the area containing this second directional keypad remote control is currently **`-40` degrees**! Another robot will need to be sent to type on that directional keypad, too.
> 不幸的是，第二个方向键盘遥控器所在区域现在**零下40度**！还得再派一个机器人去按那个方向键盘。

There are many shortest possible sequences of directional keypad button presses that would cause this robot to tell the second robot to tell the first robot to eventually type `029A` on the door. One such sequence is `<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A`.
> 有很多最短的方向键盘按键序列能让这个机器人指挥第二个机器人，最终让第一个机器人在门上输入 `029A`。其中一种是 `<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A`。

Unfortunately, the area containing this third directional keypad remote control is currently **full of Historians**, so no robots can find a clear path there. Instead, **you** will have to type this sequence yourself.
> 不幸的是，第三个方向键盘遥控器所在区域**全是历史学家**，没有机器人能过去。只能**你自己**亲自输入这串按键。

Were you to choose this sequence of button presses, here are all of the buttons that would be pressed on your directional keypad, the two robots' directional keypads, and the numeric keypad:
> 如果你选择这串按键，下面是你、两个机器人和数字小键盘上所有被按下的按钮：

```
<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
v<<A>>^A<A>AvA<^AA>A<vAAA>^A
<A^A>^^AvvvA
029A
```

In summary, there are the following keypads:
> 总结一下，有如下几种键盘：

- One directional keypad that **you** are using.
- Two directional keypads that **robots** are using.
- One numeric keypad (on a door) that a **robot** is using.
> - 你用的一个方向键盘。
> - 两个机器人用的方向键盘。
> - 一个机器人用的门上数字小键盘。

It is important to remember that these robots are not designed for button pushing. In particular, if a robot arm is ever aimed at a **gap** where no button is present on the keypad, even for an instant, the robot will **panic** unrecoverably. So, don't do that. All robots will initially aim at the keypad's `A` key, wherever it is.
> 要记住，这些机器人不是为按键设计的。特别是，如果机械臂哪怕一瞬间对准了键盘上的**空格**，机器人就会**彻底崩溃**。所以千万别让这种事发生。所有机器人初始都指向键盘上的A键，无论A键在哪。

To unlock the door, **five** codes will need to be typed on its numeric keypad. For example:
> 要开门，需要在数字小键盘上输入**五组密码**。例如：

```
029A
980A
179A
456A
379A
```

For each of these, here is a shortest sequence of button presses you could type to cause the desired code to be typed on the numeric keypad:
> 对于每组密码，下面是你可以输入的最短按键序列，使机器人最终在数字小键盘上输入目标密码：

```
029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
```

The Historians are getting nervous; the ship computer doesn't remember whether the missing Historian is trapped in the area containing a **giant electromagnet** or **molten lava**. You'll need to make sure that for each of the five codes, you find the **shortest sequence** of button presses necessary.
> 历史学家们越来越紧张；飞船电脑记不清失踪的历史学家到底被困在**巨型电磁铁**区还是**熔岩**区。你必须确保每组密码都找到**最短的按键序列**。

The **complexity** of a single code (like `029A`) is equal to the result of multiplying these two values:
> 单个密码（如 `029A`）的**复杂度**等于以下两项的乘积：

- The **length of the shortest sequence** of button presses you need to type on your directional keypad in order to cause the code to be typed on the numeric keypad; for `029A`, this would be `68`.
- The **numeric part of the code** (ignoring leading zeroes); for `029A`, this would be `29`.
> - 你在方向键盘上输入的**最短按键序列长度**，使机器人最终在数字小键盘上输入目标密码；对于 `029A`，是 `68`。
> - 密码的**数字部分**（忽略前导零）；对于 `029A`，是 `29`。

In the above example, complexity of the five codes can be found by calculating `68 * 29`, `60 * 980`, `68 * 179`, `64 * 456`, and `64 * 379`. Adding these together produces **`126384`**.
> 在上例中，五组密码的复杂度分别为 `68 * 29`、`60 * 980`、`68 * 179`、`64 * 456` 和 `64 * 379`。相加得到 **`126384`**。

Find the fewest number of button presses you'll need to perform in order to cause the robot in front of the door to type each code. **What is the sum of the complexities of the five codes on your list?**
> 找出你需要输入的最少按键次数，使门前的机器人能输入每组密码。**你列表中五组密码的复杂度之和是多少？**

Your puzzle answer was `270084`.

## Part Two
> ## 第二部分

Just as the missing Historian is released, The Historians realize that a **second** member of their search party has also been missing this entire time!
> 就在失踪的历史学家被救出来时，大家才发现其实还有**第二位**队员一直也失踪着！

A quick life-form scan reveals the Historian is also trapped in a locked area of the ship. Due to a variety of hazards, robots are once again dispatched, forming another chain of remote control keypads managing robotic-arm-wielding robots.
> 快速生命体扫描发现，这位历史学家也被困在飞船的另一个锁定区域。由于各种危险，再次派出机器人，形成了另一条遥控键盘和机械臂机器人的链条。

This time, many more robots are involved. In summary, there are the following keypads:
> 这次，涉及的机器人更多。总结如下，有这些键盘：

- One directional keypad that **you** are using.
- **25** directional keypads that **robots** are using.
- One numeric keypad (on a door) that a **robot** is using.
> - 你用的一个方向键盘。
> - **25** 个机器人用的方向键盘。
> - 一个机器人用的门上数字小键盘。

The keypads form a chain, just like before: your directional keypad controls a robot which is typing on a directional keypad which controls a robot which is typing on a directional keypad... and so on, ending with the robot which is typing on the numeric keypad.
> 这些键盘像之前一样形成一条链：你的方向键盘控制一个机器人，这个机器人在另一个方向键盘上输入，那个方向键盘又控制另一个机器人……如此反复，最后一个机器人在数字小键盘上输入。

The door codes are the same this time around; only the number of robots and directional keypads has changed.
> 这次门禁码还是那五组，只是机器人和方向键盘的数量变了。

Find the fewest number of button presses you'll need to perform in order to cause the robot in front of the door to type each code. **What is the sum of the complexities of the five codes on your list?**
> 找出你需要输入的最少按键次数，使门前的机器人能输入每组密码。**你列表中五组密码的复杂度之和是多少？**

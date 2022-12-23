# Day 10: Cathode-Ray Tube

> 第10天：阴极射线管

You avoid the ropes, plunge into the river, and swim to shore.

> 你避开绳索，跳入河中，游到岸边。

The Elves yell something about meeting back up with them upriver, but the river is too loud to tell exactly what they're saying. They finish crossing the bridge and disappear from view.

> 精灵们喊着要在上游与他们汇合，但河水声音太大，听不清他们在说什么。他们过桥后消失在视野中。

Situations like this must be why the Elves prioritized getting the communication system on your handheld device working. You pull it out of your pack, but the amount of water slowly draining from a big crack in its screen tells you it probably won't be of much immediate use.

> 像这样的情况一定是精灵们优先考虑让你的手持设备上的通信系统工作的原因。你把它从背包里拿出来，但从它屏幕上的一条大裂缝中慢慢流出的水量告诉你，它无法立即使用。

**Unless**, that is, you can design a replacement for the device's video system! It seems to be some kind of [cathode-ray tube](https://en.wikipedia.org/wiki/Cathode-ray_tube) screen and simple CPU that are both driven by a precise **clock circuit**. The clock circuit ticks at a constant rate; each tick is called a **cycle**.

> **除非**你能为设备的视频系统设计一个替代品！它应该是某种[阴极射线管](https://en.wikipedia.org/wiki/Cathode-ray_tube)屏幕和简单的 CPU，它们都由精确的**时钟电路**驱动。时钟电路以恒定速率振荡，每次振荡称为一个**周期**。

Start by figuring out the signal being sent by the CPU. The CPU has a single register, `X`, which starts with the value `1`. It supports only two instructions:

- `addx V` takes **two cycles** to complete. **After** two cycles, the `X` register is increased by the value `V`. (`V` can be negative.)
- `noop` takes **one cycle** to complete. It has no other effect.

> 首先确定 CPU 发出的信号。CPU 有一个寄存器“X”，它的值以“1”开始。它只支持两条指令：
>
> - `addx V` 需要**两个周期**完成。在两个周期**之后**，“X”寄存器的值增加“V”。（“V”可以是负数。）
> - `noop` 需要**一个周期**完成。它没有其他作用。

The CPU uses these instructions in a program ([your puzzle input](day10.txt)) to, somehow, tell the screen what to draw.

> CPU 使用程序（[你的谜题输入](day10.txt)）中的这些指令以某种方式告诉屏幕绘制什么。

Consider the following small program:

> 考虑下面的小程序：

```
noop
addx 3
addx -5
```

Execution of this program proceeds as follows:

- At the start of the first cycle, the `noop` instruction begins execution. During the first cycle, `X` is `1`. After the first cycle, the noop instruction finishes execution, doing nothing.
- At the start of the second cycle, the `addx 3` instruction begins execution. During the second cycle, `X` is still `1`.
- During the third cycle, `X` is still `1`. After the third cycle, the `addx 3` instruction finishes execution, setting `X` to `4`.
- At the start of the fourth cycle, the `addx -5` instruction begins execution. During the fourth cycle, `X` is still `4`.
- During the fifth cycle, `X` is still `4`. After the fifth cycle, the `addx -5` instruction finishes execution, setting `X` to `-1`.

> 这个程序的执行过程如下：
>
> - 在第一个周期开始时，“noop” 指令开始执行。在第一个周期中，“X”为 `1`。在第一个周期之后，noop 指令结束执行，什么都没有做。
> - 在第二个周期开始时，“addx 3”指令开始执行。在第二个周期中，“X”仍旧是 `1`。
> - 在第三个周期中，“X”仍旧是 `1`。在第三个周期之后，“addx 3”指令完成执行，设置“X”的值为 `4`。
> - 在第四个周期开始时，“addx -5”指令开始执行。在第四个周期中，“X”仍旧是 `4`。
> - 在第五个周期中，“X”仍旧是 `4`。在第五个周期之后，“addx -5”指令完成执行，设置“X”的值为 `-1`。

Maybe you can learn something by looking at the value of the `X` register throughout execution. For now, consider the **signal strength** (the cycle number multiplied by the value of the X register) **during** the 20th cycle and every 40 cycles after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

> 也许你可以通过在执行过程中查看“X”寄存器的值来了解一些情况。现在，考虑第 20 个周期以及之后的每 40 个周期（即第 20、60、100、140、180 和 220 个周期）的**信号强度**（周期数乘以 X 寄存器的值）。

For example, consider this larger program:

> 举个例子，考虑这个更大的程序

```
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
```

The interesting signal strengths can be determined as follows:

- During the 20th cycle, register `X` has the value `21`, so the signal strength is 20 * 21 = **420**. (The 20th cycle occurs in the middle of the second `addx -1`, so the value of register `X` is the starting value, `1`, plus all of the other `addx` values up to that point: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)
- During the 60th cycle, register `X` has the value `19`, so the signal strength is 60 * 19 = **`1140`**.
- During the 100th cycle, register `X` has the value `18`, so the signal strength is 100 * 18 = **`1800`**.
- During the 140th cycle, register `X` has the value `21`, so the signal strength is 140 * 21 = **`2940`**.
- During the 180th cycle, register `X` has the value `16`, so the signal strength is 180 * 16 = **`2880`**.
- During the 220th cycle, register `X` has the value `18`, so the signal strength is 220 * 18 = **`3960`**.

> 信号强度确定如下：
>
> - 在第 20 个周期中，寄存器 ”X“ 的值为 `21`，因此信号强度为 20 * 21 = **420**。（第 20 个周期发生在第二条“addx -1”指令的中间，因此寄存器“X”的值是初始值“1”加上截至该点的所有其他“addx”值：1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21。）
> - 在第 60 个周期中，寄存器 ”X“ 的值为 `19`，因此信号强度为 60 * 19 = **`1140`**。
> - 在第 100 个周期中，寄存器 ”X“ 的值为 `18`，因此信号强度为 100 * 18 = **`1800`**。
> - 在第 140 个周期中，寄存器 ”X“ 的值为 `21`，因此信号强度为 140 * 21 = **`2940`**。
> - 在第 180 个周期中，寄存器 ”X“ 的值为 `16`，因此信号强度为 180 * 16 = **`2880`**。
> - 在第 220 个周期中，寄存器 ”X“ 的值为 `18`，因此信号强度为 220 * 18 = **`3960`**。

The sum of these signal strengths is **`13140`**.

> 这些信号强度的和为 **`13140`**。

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. **What is the sum of these six signal strengths?**

> 找出第 20、60、100、140、180 以及 220 个周期的信号强度。**这六个信号强度的总和是多少？**

Your puzzle answer was `13720`.

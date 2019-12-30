# [Day 7: Amplification Circuit](https://adventofcode.com/2019/day/7)

> 第7天：放大电路

Based on the navigational maps, you're going to need to send more power to your ship's thrusters to reach Santa in time. To do this, you'll need to configure a series of [amplifiers](https://en.wikipedia.org/wiki/Amplifier) already installed on the ship.

> 根据导航地图，你需要向飞船的推进器发送更多动力，以便及时到达圣诞老人那。为此，你需要配置一系列已经安装在飞船上的[放大器](https://en.wikipedia.org/wiki/Amplifier)。

There are five amplifiers connected in series; each one receives an input signal and produces an output signal. They are connected such that the first amplifier's output leads to the second amplifier's input, the second amplifier's output leads to the third amplifier's input, and so on. The first amplifier's input value is `0`, and the last amplifier's output leads to your ship's thrusters.

> 共有五个放大器串联连接，每个放大器接收一个输入信号并产生一个输出信号。它们的连接方式是，第一个放大器的输出连接到第二个放大器的输入，第二个放大器的输出连接到第三个放大器的输入，依此类推。第一个放大器的输入值为 `0`，最后一个放大器的输出连接到飞船的推进器。

```'
    O-------O  O-------O  O-------O  O-------O  O-------O
0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    O-------O  O-------O  O-------O  O-------O  O-------O
```

The Elves have sent you some **Amplifier Controller Software** ([your puzzle input](day7.txt)), a program that should run on your [existing Intcode computer](day5.md). Each amplifier will need to run a copy of the program.

> 精灵们给你发送了一些**放大器控制器软件**（[你的谜题输入](day7.txt)），该程序应该运行在你[现有的 Intcode 计算机](day5.md)上。每个放大器都需要运行该程序的副本。

When a copy of the program starts running on an amplifier, it will first use an input instruction to ask the amplifier for its current **phase setting** (an integer from `0` to `4`). Each phase setting is used **exactly once**, but the Elves can't remember which amplifier needs which phase setting.

> 当程序的副本开始运行在放大器上时，它将首先使用一条输入指令向放大器询问其当前的**相位设置**（从 `0` 到 `4` 的整数）。每个相位设置**仅能使用一次**，但精灵们不记得哪个放大器需要哪个相位设置了。

The program will then call another input instruction to get the amplifier's input signal, compute the correct output signal, and supply it back to the amplifier with an output instruction. (If the amplifier has not yet received an input signal, it waits until one arrives.)

> 程序接下来将调用另一条输入指令用于获取放大器的输入信号，计算正确的输出信号后，通过一条输出指令提供给放大器。（如果放大器尚未收到输入信号，则一直等待直到收到为止。）

Your job is to **find the largest output signal that can be sent to the thrusters** by trying every possible combination of phase settings on the amplifiers. Make sure that memory is not shared or reused between copies of the program.

> 你的工作是通过尝试所有任何可能的放大器相位设置组合来**寻找可以发送至推进器的最大输出信号**。确保程序副本之间没有共享内存和重复使用内存。

For example, suppose you want to try the phase setting sequence `3,1,2,4,0`, which would mean setting amplifier `A` to phase setting `3`, amplifier `B` to setting `1`, `C` to `2`, `D` to `4`, and `E` to `0`. Then, you could determine the output signal that gets sent from amplifier `E` to the thrusters with the following steps:

- Start the copy of the amplifier controller software that will run on amplifier `A`. At its first input instruction, provide it the amplifier's phase setting, `3`. At its second input instruction, provide it the input signal, `0`. After some calculations, it will use an output instruction to indicate the amplifier's output signal.
- Start the software for amplifier `B`. Provide it the phase setting (`1`) and then whatever output signal was produced from amplifier `A`. It will then produce a new output signal destined for amplifier `C`.
- Start the software for amplifier `C`, provide the phase setting (`2`) and the value from amplifier `B`, then collect its output signal.
- Run amplifier `D`'s software, provide the phase setting (`4`) and input value, and collect its output signal.
- Run amplifier `E`'s software, provide the phase setting (`0`) and input value, and collect its output signal.

> 举个例子，假设你尝试使用相位设置序列 `3,1,2,4,0`，这意味着将放大器 `A` 的相位设置为 `3`，放大器 `B` 设置为 `1`，`C` 设置为 `2`，`D` 设置为 `4`，以及 `E` 设置为 `0`。然后，你可以确定从放大器 `E` 发送到推进器的输出信号，步骤如下：
>
> - 启动位于放大器 `A` 上的放大器控制软件的副本。在第一条输入指令中，提供放大器的相位设置 `3`。在第二条输入指令中，提供输入信号 `0`。经过一些计算后，它将使用一条输出指令表示放大器的输出信号。
> - 启动放大器 `B` 的软件。提供相位设置（`1`）以及从放大器 `A` 处产生的输出信号。接下来它将产生一个新的输出信号，发送给放大器 `C`。
> - 启动放大器 `C` 的软件，提供相位设置（`2`）以及从放大器 `B` 处得到的值，然后获取其输出信号。
> - 运行放大器 `D` 的软件，提供相位设置（`4`）以及输入值，并获取其输出信号。
> - 运行放大器 `E` 的软件，提供相位设置（`0`）以及输入值，并获取其输出信号。

The final output signal from amplifier `E` would be sent to the thrusters. However, this phase setting sequence may not have been the best one; another sequence might have sent a higher signal to the thrusters.

> 来自放大器 `E` 的最终输出信号将被发送到推进器。但是，这组相位设置顺序或许不是最好的，也许存在另一组序列可以向推进器发送更高的信号。

Here are some example programs:

> 以下是一些示例程序：

- Max thruster signal `43210` (from phase setting sequence `4,3,2,1,0`):

> - 最大推力器信号是 `43210`（来自相位设置序列 `4,3,2,1,0`）：

```'
    3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
```

- Max thruster signal `54321` (from phase setting sequence `0,1,2,3,4`):

> - 最大推进器信号是 `54321`（来自相位设置序列 `0,1,2,3,4`）：

```'
    3,23,3,24,1002,24,10,24,1002,23,-1,23,
    101,5,23,23,1,24,23,23,4,23,99,0,0
```

- Max thruster signal `65210` (from phase setting sequence `1,0,4,3,2`):

> - 最大推力器信号是 `65210`（来自相位设置序列 `1,0,4,3,2`）：

```'
    3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
    1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
```

Try every combination of phase settings on the amplifiers. **What is the highest signal that can be sent to the thrusters?**

> 对放大器尝试每种相位设置的组合。**可以发送到推进器的最高信号是多少？**

Your puzzle answer was `272368`.

## Part Two

It's no good - in this configuration, the amplifiers can't generate a large enough output signal to produce the thrust you'll need. The Elves quickly talk you through rewiring the amplifiers into a **feedback loop**:

> 这还不够好 —— 在这种配置下，放大器无法生成一个足够大的输出信号来产生你所需的推力。很快，精灵们告诉你可以通过将放大器重新接线形成一个**反馈回路**：

```'
      O-------O  O-------O  O-------O  O-------O  O-------O
0 -+->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-.
   |  O-------O  O-------O  O-------O  O-------O  O-------O |
   |                                                        |
   '--------------------------------------------------------+
                                                            |
                                                            v
                                                     (to thrusters)
```

Most of the amplifiers are connected as they were before; amplifier `A`'s output is connected to amplifier `B`'s input, and so on. **However**, the output from amplifier `E` is now connected into amplifier `A`'s input. This creates the feedback loop: the signal will be sent through the amplifiers **many times**.

> 多数放大器依旧按照之前的方式进行连接，放大器 `A` 的输出连接到放大器 `B` 的输入，依此类推。**然而**，放大器 `E` 的输出现在将连接到放大器 `A` 的输入。这将形成反馈回路：信号将在放大器之间发送**多次**。

In feedback loop mode, the amplifiers need **totally different phase settings**: integers from `5` to `9`, again each used exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output many times before halting. Provide each amplifier its phase setting at its first input instruction; all further input/output instructions are for signals.

> 在反馈回路模式下，放大器需要**完全不同的相位设置**：从 `5` 到 `9` 的整数，每个整数仅可以使用一次。这些设置将导致放大器控制软件持续的接收输入和产生输出多次，直到程序停止。为每个放大器的第一条输入指令提供相位设置，剩下的其他所有输入/输出指令则用于处理信号。

Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving and sending signals until it halts.

> 在此过程中，不要重启任何放大器上的放大器控制软件。每个放大器都应继续地接收和发送信号，直到程序停止。

All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process, a `0` signal is sent to amplifier `A`'s input **exactly once**.

> 在此过程中，所有发送或接收的信号都将在放大器之间完成，除了最开始和最后的信号。为了启动这个流程，**仅一次**将信号 `0` 发送至放大器 `A` 的输入。

Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the last output signal from amplifier `E` is sent to the thrusters. Your job is to **find the largest output signal that can be sent to the thrusters** using the new phase settings and feedback loop arrangement.

> 最终，放大器上的软件将在处理完最后一次循环后停止运行。此时，放大器 `E` 的最后输出信号将发送到推进器。你的工作是使用新的相位设置和反馈回路布局，**找到可以发送到推进器的最大输出信号**。

Here are some example programs:

> 以下是一些示例程序：

- Max thruster signal `139629729` (from phase setting sequence `9,8,7,6,5`):

> - 最大推力器信号是 `139629729`（来自相位设置序列 `9、8、7、6、5`）：

```'
    3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
```

- Max thruster signal `18216` (from phase setting sequence `9,7,8,5,6`):

> - 最大推进器信号是 `18216`（来自相位设置序列 `9,7,8,5,6`）：

```'
    3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
```

Try every combination of the new phase settings on the amplifier feedback loop. **What is the highest signal that can be sent to the thrusters?**

> 对放大器反馈回路尝试每种新的相位设置组合。**可以发送到推进器的最高信号是多少？**

Your puzzle answer was `19741286`.

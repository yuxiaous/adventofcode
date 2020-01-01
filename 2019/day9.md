# [Day 9: Sensor Boost](https://adventofcode.com/2019/day/9)

> 第9天：传感器增强

You've just said goodbye to the rebooted rover and left Mars when you receive a faint distress signal coming from the asteroid belt. It must be the Ceres monitoring station!

> 你收到了一条从小行星带发来的微弱求救信号，于是你对重启后的漫游车说了再见，并准备离开火星。那一定是谷神星监控站发来的！

In order to lock on to the signal, you'll need to boost your sensors. The Elves send up the latest **BOOST** program - Basic Operation Of System Test.

> 为了锁定信号，你需要增强传感器。精灵们发送了最新的**BOOST**程序给你 —— 系统的基础操作测试程序。

While BOOST ([your puzzle input](day9.txt)) is capable of boosting your sensors, for tenuous safety reasons, it refuses to do so until the computer it runs on passes some checks to demonstrate it is a **complete Intcode computer**.

> 尽管 BOOST（[你的谜题输入](day9.txt)）有能力增强你的传感器，但出于脆弱的安全因素，它拒绝这样做，除非所运行的计算机通过一些检测以证明它是一台**完备的 Intcode 计算机**。

[Your existing Intcode computer](day5.md) is missing one key feature: it needs support for parameters in **relative mode**.

> [你现有的 Intcode 计算机](day5.md)缺少一项关键功能：它需要支持**相对模式**下的参数。

Parameters in mode `2`, **relative mode**, behave very similarly to parameters in **position mode**: the parameter is interpreted as a position. Like position mode, parameters in relative mode can be read from or written to.

> 模式 `2`（相对模式）下的参数与**位置**模式下参数表现非常相似：参数被解释为位置。与位置模式一样，相对模式下的参数可以读取或写入。

The important difference is that relative mode parameters don't count from address `0`. Instead, they count from a value called the **relative base**. The **relative base** starts at `0`.

> 最大的区别是，相对模式的参数不是从地址 `0` 处开始计算的。相反，它们从一个称为**相对基数**的地址开始计算。**相对基数**的初始状态是 `0`。

The address a relative mode parameter refers to is itself **plus** the current **relative base**. When the relative base is `0`, relative mode parameters and position mode parameters with the same value refer to the same address.

> 一个相对模式下的参数所指向的地址是其本身**加上**当前**相对基数**得到的。当相对基数为 `0` 时，相对模式下的参数和位置模式下的参数如果拥有相同的值，则它们指向相同的地址。

For example, given a relative base of `50`, a relative mode parameter of `-7` refers to memory address `50 + -7 = 43`.

> 例如，给定相对基数为 `50`，相对模式下的参数为 `-7`，则指向的是内存地址为 `50 + -7 = 43`。

The relative base is modified with the **relative base offset** instruction:

- Opcode `9` **adjusts the relative base** by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter.

> 相对基数通过**相对基偏移量**指令修改：
>
> - 操作码 `9` 通过其唯一参数值**调整相对基数**。相对基数通过参数值增加（或减小，如果该值为负）。

For example, if the relative base is `2000`, then after the instruction `109,19`, the relative base would be `2019`. If the next instruction were `204,-34`, then the value at address `1985` would be output.

> 例如，如果相对基数是 `2000`，那么在执行指令 `109,19` 之后，相对基数将变为 `2019`。如果下一条指令是 `204,-34`，则将数值输出到地址 `1985` 。

Your Intcode computer will also need a few other capabilities:

- The computer's available memory should be much larger than the initial program. Memory beyond the initial program starts with the value `0` and can be read or written like any other memory. (It is invalid to try to access memory at a negative address, though.)
- The computer should have support for large numbers. Some instructions near the beginning of the BOOST program will verify this capability.

> 你的 Intcode 计算机还需要一些其他功能：
>
> - 计算机的可用内存应比初始程序大很多。超出初始程序内存从 `0` 开始，并且可以像其他内存一样进行读写。（但是，尝试访问一个负地址是无效的。）
> - 计算机需要支持大数。一些靠近 BOOST 程序起始位置的指令将验证此功能。

Here are some example programs that use these features:

- `109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99` takes no input and produces a [copy of itself](https://en.wikipedia.org/wiki/Quine_(computing)) as output.
- `1102,34915192,34915192,7,4,7,99,0` should output a 16-digit number.
- `104,1125899906842624,99` should output the large number in the middle.

> 以下是一些使用这些功能的示例程序：
>
> - `109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99` 不需要输入任何内容并[复制自己](https://en.wikipedia.org/wiki/Quine_(computing))作为输出。
> - `1102,34915192,34915192,7,4,7,99,0` 应该输出一个 16 位的数字。
> - `104,1125899906842624,99` 应该输出指令中间那个大数。

The BOOST program will ask for a single input; run it in test mode by providing it the value `1`. It will perform a series of checks on each opcode, output any opcodes (and the associated parameter modes) that seem to be functioning incorrectly, and finally output a BOOST keycode.

> BOOST 程序将请求一个输入，通过提供 `1` 在测试模式下运行。它将对每个操作码执行一系列检查，输出任何看上去功能不正确的操作码（以及相关的参数模式），最后输出一个 BOOST 关键码。

Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning opcodes when run in test mode; it should only output a single value, the BOOST keycode. **What BOOST keycode does it produce?**

> 一旦你的 Intcode 计算机拥有了完整功能，在测试模式下运行时，BOOST 程序应当不会报告发生故障的操作码，它应该只输出一个值，即 BOOST 关键码。 **它会产生什么 BOOST 关键码？**

Your puzzle answer was `3512778005`.

## Part Two

**You now have a complete Intcode computer.**

> **你现在拥有一台完备的 Intcode 计算机了。**

Finally, you can lock on to the Ceres distress signal! You just need to boost your sensors using the BOOST program.

> 最后，你能够锁定谷神星求救信号了！你只需要使用 BOOST 程序增强传感器。

The program runs in sensor boost mode by providing the input instruction the value `2`. Once run, it will boost the sensors automatically, but it might take a few seconds to complete the operation on slower hardware. In sensor boost mode, the program will output a single value: **the coordinates of the distress signal.**

> 通过为输入指令提供值 `2`，程序以传感器增强模式运行。一旦运行，它将自动增强传感器，但可能需要几秒钟才能在较慢的硬件上完成操作。在传感器增强模式下，程序将输出一个值：**求救信号的坐标。**

Run the BOOST program in sensor boost mode. **What are the coordinates of the distress signal?**

> 在传感器增强模式下运行 BOOST 程序。**求救信号的坐标是什么？**

Your puzzle answer was `35920`.

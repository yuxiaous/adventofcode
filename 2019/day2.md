# Day 2: 1202 Program Alarm

> 第2天：1202程序警报

On the way to your [gravity assist](https://en.wikipedia.org/wiki/Gravity_assist) around the Moon, your ship computer beeps angrily about a "[1202 program alarm](https://www.hq.nasa.gov/alsj/a11/a11.landing.html#1023832)". On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" The ship computer [bursts into flames](https://en.wikipedia.org/wiki/Halt_and_Catch_Fire).

> 在利用月球做重力助推的途中，你的飞船计算机因“1202 程序警报”而发出急促的哔哔声。通过无线电，一只精灵告知了如何处理这种情况：“别担心，那完全是正常现象——” 飞船计算机突然起火了。

You notify the Elves that the computer's [magic smoke](https://en.wikipedia.org/wiki/Magic_smoke) seems to have escaped. "That computer ran **Intcode** programs like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"

> 你告诉精灵计算机冒烟了。 “是那台运行着 **Intcode** 程序（例如它正在运行的重力助推程序）的计算机；当然，那里有足够的备件来建造一台新的 Intcode 计算机！”

An Intcode program is a list of [integers](https://en.wikipedia.org/wiki/Integer) separated by commas (like `1,0,0,3,99`). To run one, start by looking at the first integer (called position `0`). Here, you will find an **opcode** - either `1`, `2`, or `99`. The opcode indicates what to do; for example, `99` means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

> Intcode 程序是一个由逗号分隔的整数列表（例如 `1,0,0,3,99`）。要运行起来，得从第一个整数（称为位置 `0`）开始查看。在这里，你会找到一个**操作码** —— `1`、`2` 或 `99`。操作码指示要做什么；例如，`99` 表示程序已完成，应立即停止。遇到未知的操作码意味着出了点问题。

Opcode `1` **adds** together numbers read from two positions and stores the result in a third position. The three integers **immediately after** the opcode tell you these three positions - the first two indicate the **positions** from which you should read the input values, and the third indicates the **position** at which the output should be stored.

> 操作码 `1` 将从两个位置读取的数字**加**在一起，并将结果存储在第三个位置。**紧跟在**操作码后面的三个整数将告诉你这三个位置 —— 前两个表示你应该从中读取输入值的**位置**，第三个表示用于存储输出值的**位置**。

For example, if your Intcode computer encounters `1,10,20,30`, it should read the values at positions `10` and `20`, add those values, and then overwrite the value at position `30` with their sum.

> 例如，如果您的 Intcode 计算机遇到 `1,10,20,30`，则应读取位置 `10` 和 `20` 的值，将它们相加，然后将它们的和写入位置 `30`。

Opcode `2` works exactly like opcode `1`, except it **multiplies** the two inputs instead of adding them. Again, the three integers after the opcode indicate **where** the inputs and outputs are, not their values.

> 操作码 `2` 的工作方式与操作码 `1` 完全相同，只是它将两个输入值**相乘**而不是相加。同样，操作码后面的三个整数表示输入和输出**在哪里**，而不是它们的值。

Once you're done processing an opcode, **move to the next one** by stepping forward `4` positions.

> 一旦你处理完一个操作码后，向后移动4个位置**进入下一条**。

For example, suppose you have the following program:

> 例如，假设你有如下程序：

`1,9,10,3,2,3,11,0,99,30,40,50`

For the purposes of illustration, here is the same program split into multiple lines:

> 为了便于查看，这里将程序分为多行：

```diff
1,9,10,3,
2,3,11,0,
99,
30,40,50
```

The first four integers, `1,9,10,3`, are at positions `0`, `1`, `2`, and `3`. Together, they represent the first opcode (`1`, addition), the positions of the two inputs (`9` and `10`), and the position of the output (`3`). To handle this opcode, you first need to get the values at the input positions: position `9` contains `30`, and position `10` contains `40`. **Add** these numbers together to get `70`. Then, store this value at the output position; here, the output position (`3`) is **at** position `3`, so it overwrites itself. Afterward, the program looks like this:

> 前四个整数 `1、9、10、3` 位于位置 `0`，`1`，`2` 和 `3`。它们一起代表了第一个操作码（`1`，加法），两个输入的位置（`9` 和 `10`）以及输出的位置（`3`）。要处理此操作码，你首先需要获取输入位置的值：位置 `9` 的值是 `30`，位置 `10` 的值是 `40`。 将这些数字**相加**得到 `70`。然后，将该值存储在输出位置。此处，输出位置（`3`）**位于**位置 `3` 处，所以它将会覆盖它自己。在那之后，程序看上去如下所示：

```diff
1,9,10,70,
2,3,11,0,
99,
30,40,50
```

Step forward `4` positions to reach the next opcode, `2`. This opcode works just like the previous, but it multiplies instead of adding. The inputs are at positions `3` and `11`; these positions contain `70` and `50` respectively. Multiplying these produces `3500`; this is stored at position `0`:

> 向后移动 `4` 个位置到达下一个操作码 `2`。该操作码的工作方式与前一个相同，但是它是相乘而不是相加。输入在位置 `3` 和 `11`；这些位置的值分别是 `70` 和 `50`。将它们相乘得到 `3500`。这存储在位置 `0`：

```diff
3500,9,10,70,
2,3,11,0,
99,
30,40,50
```

Stepping forward `4` more positions arrives at opcode `99`, halting the program.

> 向后移动 `4` 个位置到达操作码 `99`，程序停止。

Here are the initial and final states of a few more small programs:

- `1,0,0,0,99` becomes `2,0,0,0,99` (`1 + 1 = 2`).
- `2,3,0,3,99` becomes `2,3,0,6,99` (`3 * 2 = 6`).
- `2,4,4,5,99,0` becomes `2,4,4,5,99,9801` (`99 * 99 = 9801`).
- `1,1,1,4,99,5,6,0,99` becomes `30,1,1,4,2,5,6,0,99`.

> 以下是一些其他小程序的初始状态和最终状态：
>
> - `1,0,0,0,99` 变为 `2,0,0,0,99` (`1 + 1 = 2`).
> - `2,3,0,3,99` 变为 `2,3,0,6,99` (`3 * 2 = 6`).
> - `2,4,4,5,99,0` 变为 `2,4,4,5,99,9801` (`99 * 99 = 9801`).
> - `1,1,1,4,99,5,6,0,99` 变为 `30,1,1,4,2,5,6,0,99`.

Once you have a working computer, the first step is to restore the gravity assist program ([your puzzle input](day2.txt)) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, **before running the program**, replace position `1` with the value `12` and replace position `2` with the value `2`. **What value is left at position `0`** after the program halts?

一旦你有了一台可用的计算机，第一件事就是将重力助推程序（[你的谜题输入](day2.txt)）恢复到之前的那台着火的计算机的“1202程序警报”状态。为此，**在运行程序之前**，将位置 `1` 的值替换为 `12`，并将位置 `2` 的值替换为 `2`。当程序运行结束后**留在位置 `0` 处的值是什么**？

Your puzzle answer was `3085697`.

## Part Two

"Good, the new computer seems to be working correctly! **Keep it nearby** during this mission - you'll probably use it again. Real Intcode computers support many more features than your new one, but we'll let you know what they are as you need them."

> “很好，新计算机似乎可以正常工作！在执行此任务期间**将其保留在附近** —— 你可能会再次使用它。真正的 Intcode 计算机支持的功能比你这台新计算机多很多，但我们会在你需要它们的时候再告诉你它们是什么。”

"However, your current priority should be to complete your gravity assist around the Moon. For this mission to succeed, we should settle on some terminology for the parts you've already built."

> “然而，你当前的首要任务是完成利用月球的重力助推。为使这项任务成功，我们应该为你制造的零件确定一些术语。”

Intcode programs are given as a list of integers; these values are used as the initial state for the computer's **memory**. When you run an Intcode program, make sure to start by initializing memory to the program's values. A position in memory is called an **address** (for example, the first value in memory is at "address 0").

> Intcode 程序以整数列表的形式提供；这些值作为计算机**内存**的初始状态。当你运行一段 Intcode 程序时，确保先将内存初始化为该程序的值。内存中的位置称为**地址**（例如，内存的第一个值位于“地址0”处）。

Opcodes (like `1`, `2`, or `99`) mark the beginning of an **instruction**. The values used immediately after an opcode, if any, are called the instruction's **parameters**. For example, in the instruction `1,2,3,4`, `1` is the opcode; `2`, `3`, and `4` are the parameters. The instruction `99` contains only an opcode and has no parameters.

> 操作码（如 `1`，`2` 或 `99`）标记一条**指令**的开头。紧挨在操作码后面的值（如有）称为指令的**参数**。例如，在指令 `1,2,3,4` 中，`1`是操作码；`2`，`3` 和 `4` 是参数。指令 `99` 只有一个操作码，没有参数。

The address of the current instruction is called the **instruction pointer**; it starts at `0`. After an instruction finishes, the instruction pointer increases by **the number of values in the instruction**; until you add more instructions to the computer, this is always `4` (`1` opcode + `3` parameters) for the add and multiply instructions. (The halt instruction would increase the instruction pointer by `1`, but it halts the program instead.)

> 当前指令的地址称为**指令指针**，它从 `0` 开始。一条指令完成后，指令指针根据**指令中值的数量**进行增长；直到你向计算机添加更多其他指令类型之前，只有加法和乘法指令的情况下，这个增量都是 `4`（`1` 个操作码 + `3` 个参数）。（停止指令会使指令指针增加 `1`，但它也同时停止了程序。）

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to **determine what pair of inputs produces the output `19690720`**."

> “有了术语，我们就可以继续进行。要完成重力助推，您需要**确定哪两个输入会产生输出 `19690720`**。”

The inputs should still be provided to the program by replacing the values at addresses `1` and `2`, just like before. In this program, the value placed in address `1` is called the **noun**, and the value placed in address `2` is called the **verb**. Each of the two input values will be between `0` and `99`, inclusive.

> 跟之前一样仍然通过替换地址 `1` 和 `2` 中的值来作为输入提供给程序。在这个程序中，位于地址 `1` 中的值称为**名词**，位于地址 `2` 中的值称为**动词**。两个输入的取值都在 `0` 和 `99` 之间（包含）。

Once the program has halted, its output is available at address `0`, also just like before. Each time you try a pair of inputs, make sure you first **reset the computer's memory to the values in the program** ([your puzzle input](day2.txt)) - in other words, don't reuse memory from a previous attempt.

> 也跟之前一样，当程序停止后，它的输出从地址 `0` 处获得。在每次尝试不同的输入时，确保首先**将计算机的内存重置为程序的值**（[你的谜题输入](day2.txt)）—— 换句话说，不要重复使用上一次的内存。

Find the input **noun** and **verb** that cause the program to produce the output `19690720`. **What is `100 * noun + verb`?** (For example, if `noun=12` and `verb=2`, the answer would be `1202`.)

> 找到使程序产生输出 `19690720` 的**名词**和**动词**输入。**计算 `100 * 名词 + 动词` 的值是什么？**（例如，如果 `noun=12`、`verb=2`，则答案为 `1202`。）

Your puzzle answer was `9425`.

# Day 17: Chronospatial Computer
> # 第十七天：时空计算机

The Historians push the button on their strange device, but this time, you all just feel like you're [falling](https://adventofcode.com/2018/day/6).
> 历史学家们按下了他们那台奇怪设备的按钮，但这一次，你们只感觉自己在[下坠](https://adventofcode.com/2018/day/6)。

"Situation critical", the device announces in a familiar voice. "Bootstrapping process failed. Initializing debugger...."
> “情况危急”，设备用熟悉的声音宣布。“引导过程失败。正在初始化调试器……”

The small handheld device suddenly unfolds into an entire computer! The Historians look around nervously before one of them tosses it to you.
> 这台小型手持设备突然展开，变成了一台完整的计算机！历史学家们紧张地四处张望，然后其中一人把它扔给了你。

This seems to be a 3-bit computer: its program is a list of 3-bit numbers (0 through 7), like `0,1,2,3`. The computer also has three **registers** named `A`, `B`, and `C`, but these registers aren't limited to 3 bits and can instead hold any integer.
> 这似乎是一台3位机：它的程序是一串3位数字（0到7），比如 `0,1,2,3`。计算机还有三个**寄存器**，分别叫 `A`、`B` 和 `C`，但这些寄存器不限于3位，可以存储任意整数。

The computer knows **eight instructions**, each identified by a 3-bit number (called the instruction's **opcode**). Each instruction also reads the 3-bit number after it as an input; this is called its **operand**.
> 计算机有**八条指令**，每条指令由一个3位数字（称为**操作码**）标识。每条指令还会读取其后的一个3位数字作为输入，这叫做**操作数**。

A number called the **instruction pointer** identifies the position in the program from which the next opcode will be read; it starts at `0`, pointing at the first 3-bit number in the program. Except for jump instructions, the instruction pointer increases by `2` after each instruction is processed (to move past the instruction's opcode and its operand). If the computer tries to read an opcode past the end of the program, it instead **halts**.
> 有一个叫做**指令指针**的数字，标识下一个要读取操作码的位置；它从0开始，指向程序中的第一个3位数字。除跳转指令外，每条指令执行后，指令指针加2（跳过操作码和操作数）。如果计算机尝试读取超出程序末尾的操作码，则**停止**运行。

So, the program `0,1,2,3` would run the instruction whose opcode is `0` and pass it the operand `1`, then run the instruction having opcode `2` and pass it the operand `3`, then halt.
> 所以，程序 `0,1,2,3` 会先执行操作码为 `0`、操作数为 `1` 的指令，再执行操作码为 `2`、操作数为 `3` 的指令，然后停止。

There are two types of operands; each instruction specifies the type of its operand. The value of a **literal operand** is the operand itself. For example, the value of the literal operand `7` is the number `7`. The value of a **combo operand** can be found as follows:
> 操作数有两种类型；每条指令指定其操作数类型。**字面量操作数**的值就是操作数本身。例如，字面量操作数 `7` 的值就是数字 `7`。**组合操作数**的值如下确定：

- Combo operands `0` through `3` represent literal values `0` through `3`.
- Combo operand `4` represents the value of register `A`.
- Combo operand `5` represents the value of register `B`.
- Combo operand `6` represents the value of register `C`.
- Combo operand `7` is reserved and will not appear in valid programs.
> - 组合操作数 `0` 到 `3` 表示字面值 `0` 到 `3`。
> - 组合操作数 `4` 表示寄存器 `A` 的值。
> - 组合操作数 `5` 表示寄存器 `B` 的值。
> - 组合操作数 `6` 表示寄存器 `C` 的值。
> - 组合操作数 `7` 保留，不会出现在有效程序中。

The eight instructions are as follows:
> 八条指令如下：

The **`adv`** instruction (opcode **`0`**) performs **division**. The numerator is the value in the `A` register. The denominator is found by raising 2 to the power of the instruction's **combo** operand. (So, an operand of `2` would divide `A` by `4` (`2^2`); an operand of `5` would divide `A` by `2^B`.) The result of the division operation is **truncated** to an integer and then written to the `A` register.
> **`adv`** 指令（操作码 `0`）执行**除法**。分子为 `A` 寄存器的值。分母为2的组合操作数次幂。（操作数为 `2` 时，`A` 除以 `4`（`2^2`）；操作数为 `5` 时，`A` 除以 `2^B`。）结果**向下取整**，写回 `A` 寄存器。

The **`bxl`** instruction (opcode **`1`**) calculates the **bitwise XOR** of register `B` and the instruction's **literal** operand, then stores the result in register `B`.
> **`bxl`** 指令（操作码 `1`）计算寄存器 `B` 与指令字面量操作数的**按位异或**，结果写入 `B`。

The **`bst`** instruction (opcode **`2`**) calculates the value of its **combo** operand [modulo](https://en.wikipedia.org/wiki/Modulo) 8 (thereby keeping only its lowest 3 bits), then writes that value to the `B` register.
> **`bst`** 指令（操作码 `2`）计算其组合操作数对8取模（只保留最低3位），结果写入 `B`。

The **`jnz`** instruction (opcode **`3`**) does **nothing** if the `A` register is `0`. However, if the `A` register is **not zero**, it **jumps** by setting the instruction pointer to the value of its **literal** operand; if this instruction jumps, the instruction pointer is **not** increased by `2` after this instruction.
> **`jnz`** 指令（操作码 `3`）如果 `A` 寄存器为 `0` 则**什么都不做**。如果 `A` 不为零，则**跳转**到字面量操作数指定的位置；如果发生跳转，指令指针**不会**在本指令后加2。

The **`bxc`** instruction (opcode **`4`**) calculates the **bitwise XOR** of register `B` and register `C`, then stores the result in register `B`. (For legacy reasons, this instruction reads an operand but **ignores** it.)
> **`bxc`** 指令（操作码 `4`）计算 `B` 和 `C` 的**按位异或**，结果写入 `B`。（出于兼容性原因，这条指令会读取一个操作数但**忽略**它。）

The **`out`** instruction (opcode **`5`**) calculates the value of its **combo** operand modulo 8, then **outputs** that value. (If a program outputs multiple values, they are separated by commas.)
> **`out`** 指令（操作码 `5`）计算其组合操作数对8取模，然后**输出**该值。（如果程序输出多个值，用逗号分隔。）

The **`bdv`** instruction (opcode **`6`**) works exactly like the `adv` instruction except that the result is stored in the **`B` register**. (The numerator is still read from the `A` register.)
> **`bdv`** 指令（操作码 `6`）与 `adv` 指令完全一样，只是结果写入 **`B` 寄存器**。（分子仍然取自 `A` 寄存器。）

The **`cdv`** instruction (opcode **`7`**) works exactly like the `adv` instruction except that the result is stored in the **`C` register**. (The numerator is still read from the `A` register.)
> **`cdv`** 指令（操作码 `7`）与 `adv` 指令完全一样，只是结果写入 **`C` 寄存器**。（分子仍然取自 `A` 寄存器。）

Here are some examples of instruction operation:
> 以下是一些指令操作示例：

- If register `C` contains `9`, the program `2,6` would set register `B` to `1`.
- If register `A` contains `10`, the program `5,0,5,1,5,4` would output `0,1,2`.
- If register `A` contains `2024`, the program `0,1,5,4,3,0` would output `4,2,5,6,7,7,7,7,3,1,0` and leave `0` in register `A`.
- If register `B` contains `29`, the program `1,7` would set register `B` to `26`.
- If register `B` contains `2024` and register `C` contains `43690`, the program `4,0` would set register `B` to `44354`.
> - 如果寄存器 `C` 为 `9`，程序 `2,6` 会把 `B` 设为 `1`。
> - 如果寄存器 `A` 为 `10`，程序 `5,0,5,1,5,4` 会输出 `0,1,2`。
> - 如果寄存器 `A` 为 `2024`，程序 `0,1,5,4,3,0` 会输出 `4,2,5,6,7,7,7,7,3,1,0`，并把 `A` 变为 `0`。
> - 如果寄存器 `B` 为 `29`，程序 `1,7` 会把 `B` 设为 `26`。
> - 如果寄存器 `B` 为 `2024`，`C` 为 `43690`，程序 `4,0` 会把 `B` 设为 `44354`。

The Historians' strange device has finished initializing its debugger and is displaying some **information about the program it is trying to run** (your puzzle input). For example:
> 历史学家们的奇怪设备已经初始化完调试器，正在显示**它要运行的程序的信息**（你的谜题输入）。例如：

```
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
```

Your first task is to **determine what the program is trying to output**. To do this, initialize the registers to the given values, then run the given program, collecting any output produced by `out` instructions. (Always join the values produced by `out` instructions with commas.) After the above program halts, its final output will be **`4,6,3,5,6,3,5,2,1,0`**.
> 你的第一个任务是**确定程序要输出什么**。为此，先用给定值初始化寄存器，然后运行给定程序，收集所有 `out` 指令产生的输出。（始终用逗号连接所有输出值。）上面程序停止后，最终输出为 **`4,6,3,5,6,3,5,2,1,0`**。

Using the information provided by the debugger, initialize the registers to the given values, then run the program. Once it halts, **what do you get if you use commas to join the values it output into a single string?**
> 用调试器提供的信息初始化寄存器，然后运行程序。程序停止后，**用逗号连接所有输出值，结果是多少？**

Your puzzle answer was `6,2,7,2,3,1,6,0,5`.

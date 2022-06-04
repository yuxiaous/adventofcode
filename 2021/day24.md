# [Day 24: Arithmetic Logic Unit](https://adventofcode.com/2021/day/24)

> 第24天：运算逻辑单元

[Magic smoke](https://en.wikipedia.org/wiki/Magic_smoke) starts leaking from the submarine's [arithmetic logic unit](https://en.wikipedia.org/wiki/Arithmetic_logic_unit) (ALU). Without the ability to perform basic arithmetic and logic functions, the submarine can't produce cool patterns with its Christmas lights!

> 潜水艇的[运算逻辑单元](https://en.wikipedia.org/wiki/Arithmetic_logic_unit) (简称 ALU) [冒青烟](https://en.wikipedia.org/wiki/Magic_smoke)了。如果没有执行基础运算和逻辑的能力，潜水艇就无法用圣诞彩灯制作出炫酷的图案！

It also can't navigate. Or run the oxygen system.

> 同样也无法进行导航，或者运行氧气系统。

Don't worry, though - you **probably** have enough oxygen left to give you enough time to build a new ALU.

> 不过别担心 -- 你**大抵**是有充足的氧气的，足够你构建一个新 ALU 的时间了。

The ALU is a four-dimensional processing unit: it has integer variables `w`, `x`, `y`, and `z`. These variables all start with the value `0`. The ALU also supports **six instructions**:

> ALU 是一个四维处理单元：有整数变量 `w`、`x`、`y` 和 `z`，这些变量都以值 `0` 开头的。同时 ALU 还支持**六种指令**：

- `inp a` - Read an input value and write it to variable `a`.
- `add a b` - Add the value of `a` to the value of `b`, then store the result in variable `a`.
- `mul a b` - Multiply the value of `a` by the value of `b`, then store the result in variable `a`.
- `div a b` - Divide the value of `a` by the value of `b`, truncate the result to an integer, then store the result in variable `a`. (Here, "truncate" means to round the value toward zero.)
- `mod a b` - Divide the value of `a` by the value of `b`, then store the **remainder** in variable `a`. (This is also called the [modulo](https://en.wikipedia.org/wiki/Modulo_operation) operation.)
- `eql a b` - If the value of `a` and `b` are equal, then store the value `1` in variable `a`. Otherwise, store the value `0` in variable `a`.

> - `inp a` -- 读取输入值并将其写入变量 `a`。
> - `add a b` -- 将 `a` 的值加上 `b` 的值，然后将结果存储在变量 `a` 中。
> - `mul a b` -- 将 `a` 的值乘以 `b` 的值，然后将结果存储在变量 `a` 中。
> - `div a b` -- 将 `a` 的值除以 `b` 的值，对结果取整，然后将结果存储在变量`a`中。（这里，“取整”是使用去尾法取整。）
> - `mod a b` -- 将 `a` 的值除以 `b` 的值，然后将**余数**存储在变量 `a` 中。（这也称为[模](https://en.wikipedia.org/wiki/Modulo_operation)操作。）
> - `eql a b` -- 如果 `a` 和 `b` 的值相等，则将值 `1` 存储在变量 `a` 中。否则，将值 `0` 存储在变量 `a` 中。

In all of these instructions, `a` and `b` are placeholders; `a` will always be the variable where the result of the operation is stored (one of `w`, `x`, `y`, or `z`), while `b` can be either a variable or a number. Numbers can be positive or negative, but will always be integers.

> 在这些指令中，`a` 和 `b` 是占位符。`a` 始终作为操作结果的存储变量（`w`、`x`、`y` 或 `z` 之一）。而 `b` 可以是变量或者数字，数字可以是正数或负数，但必须是整数。

The ALU has no **jump** instructions; in an ALU program, every instruction is run exactly once in order from top to bottom. The program halts after the last instruction has finished executing.

> ALU 没有**跳转**指令。在 ALU 程序中，每条指令按从上到下的顺序依次运行。程序在最后一条指令执行完成后停止。

(Program authors should be especially cautious; attempting to execute `div` with `b=0` or attempting to execute `mod` with `a<0` or `b<=0` will cause the program to crash and might even damage the ALU. These operations are never intended in any serious ALU program.)

> （程序作者应特别小心，试图在 `b=0` 时执行 `div`，或者在 `a<0` 或 `b<=0` 时执行 `mod` 会导致程序崩溃甚至损坏 ALU。这些操作不应用于任何严谨的 ALU 程序。）

For example, here is an ALU program which takes an input number, negates it, and stores it in `x`:

> 例如，这是一个 ALU 程序，它接受一个输入数字，将其取反，并将其存储在 `x` 中：

```'
inp x
mul x -1
```

Here is an ALU program which takes two input numbers, then sets `z` to `1` if the second input number is three times larger than the first input number, or sets `z` to `0` otherwise:

> 这是一个 ALU 程序，它接受两个输入数字，如果第二个输入数字是第一个输入数字的三倍，则将 `z` 设置为 `1`，否则将 `z` 设置为 `0`：

```'
inp z
inp x
mul z 3
eql z x
```

Here is an ALU program which takes a non-negative integer as input, converts it into binary, and stores the lowest (1's) bit in `z`, the second-lowest (2's) bit in `y`, the third-lowest (4's) bit in `x`, and the fourth-lowest (8's) bit in `w`:

> 这是一个 ALU 程序，它以非负整数作为输入，将其转换为二进制，并将最低位（1）存储在 `z` 中，第二低位（2）存储在 `y` 中，第三低位（4）存储在 `x` 中，第四低位（8）存储在 `w` 中：

```'
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
```

Once you have built a replacement ALU, you can install it in the submarine, which will immediately resume what it was doing when the ALU failed: validating the submarine's **model number**. To do this, the ALU will run the MOdel Number Automatic Detector program (MONAD, [your puzzle input](day24.txt)).

> 一旦你构建了一个替换的 ALU，你可以将它安装在潜水艇上，它需要立即恢复之前故障的 ALU 所做的事情：验证潜水艇的**型号**。为此，ALU 将运行型号自动检测程序（简称 MONAD，[你的谜题输入](day24.txt)）。

Submarine model numbers are always **fourteen-digit numbers** consisting only of digits `1` through `9`. The digit `0` **cannot** appear in a model number.

> 潜水艇的型号是一个**十四位数字**，仅由数字 `1` 到 `9` 组成，数字 `0` **不能**出现在型号中。

When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen separate `inp` instructions, each expecting a **single digit** of the model number in order of most to least significant. (So, to check the model number `13579246899999`, you would give `1` to the first `inp` instruction, `3` to the second `inp` instruction, `5` to the third `inp` instruction, and so on.) This means that when operating MONAD, each input instruction should only ever be given an integer value of at least `1` and at most `9`.

> 假设当 MONAD 检查一个 14 位数字的型号时，它使用 14 条单独的 `inp` 指令，每条指令都获得型号的**一位**，按照从高到低的顺序排列。（所以，要检查型号 `13579246899999`，你需要给第一个 `inp` 指令 `1`，给第二个 `inp` 指令 `3`，给第三个 `inp` 指令 `5`，依此类推。) 这意味着在操作 MONAD 时，每条输入指令都只能给予一个从 `1` 到 `9` 的整数值。

Then, after MONAD has finished running all of its instructions, it will indicate that the model number was **valid** by leaving a `0` in variable `z`. However, if the model number was **invalid**, it will leave some other non-zero value in `z`.

> 然后，在 MONAD 运行完所有指令后，如果型号是**有效的**，将在变量 `z` 中存储 `0`。但如果型号是**无效的**，则会在 `z` 中存储其他的非零值。

MONAD imposes additional, mysterious restrictions on model numbers, and legend says the last copy of the MONAD documentation was eaten by a [tanuki](https://en.wikipedia.org/wiki/Japanese_raccoon_dog). You'll need to **figure out what MONAD does** some other way.

> 据说 MONAD 对型号还有些额外的、神秘的限制，但 MONAD 的最后一份文档被[日本狸猫](https://en.wikipedia.org/wiki/Japanese_raccoon_dog)吃掉了。你需要 用其他方式**弄明白 MONAD 做了什么**。

To enable as many submarine features as possible, find the largest valid fourteen-digit model number that contains no `0` digits. **What is the largest model number accepted by MONAD?**

> 要尽可能多地恢复潜水艇功能，请找到不包含数字 `0` 的、最大的且有效的十四位数字型号。**MONAD 接受的最大型号是多少？**

Your puzzle answer was `12996997829399`.

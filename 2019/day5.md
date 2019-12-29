# [Day 5: Sunny with a Chance of Asteroids](https://adventofcode.com/2019/day/5)

> 第5天：充满阳光的小行星

You're starting to sweat as the ship makes its way toward Mercury. The Elves suggest that you get the air conditioner working by upgrading your ship computer to support the Thermal Environment Supervision Terminal.

> 在飞船行驶向水星路途中，你开始汗流浃背。精灵们建议你通过升级飞船计算机的热环境监督终端来使空调工作。

The Thermal Environment Supervision Terminal (TEST) starts by running a **diagnostic program** ([your puzzle input](day5.txt)). The TEST diagnostic program will run on [your existing Intcode computer](day2.md) after a few modifications:

> 热环境监督终端（TEST）通过运行**诊断程序**（[你的谜题输入](day5.txt)）启动。经过一些修改，TEST 诊断程序将在[你现有的 Intcode 计算机](day2.md)上运行：

**First**, you'll need to add **two new instructions**:

- Opcode `3` takes a single integer as **input** and saves it to the position given by its only parameter. For example, the instruction `3,50` would take an input value and store it at address `50`.
- Opcode `4` **outputs** the value of its only parameter. For example, the instruction `4,50` would output the value at address `50`.

> **首先**，你需要添加**两个新指令**：
>
> - 操作码 `3` 将一个整数作为**输入**，并将该输入保存到它唯一的参数所指定的位置。例如，指令 `3,50` 将获取一个输入值并将其存储在地址 `50` 中。
> - 操作码 `4` **输出**它唯一的参数的值。例如，指令 `4,50` 将在数值输出到地址 `50` 处。

Programs that use these instructions will come with documentation that explains what should be connected to the input and output. The program `3,0,4,0,99` outputs whatever it gets as input, then halts.

> 使用这些指令的程序将与说明文档一起使用，说明文档中指明了什么应该与输入和输出相连接。程序 `3,0,4,0,99` 输出从输入那得到的任意内容，然后停止。

**Second**, you'll need to add support for **parameter modes**:

Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already understands parameter mode `0`, **position mode**, which causes the parameter to be interpreted as a **position** - if the parameter is `50`, its value is **the value stored at address `50` in memory**. Until now, all parameters have been in position mode.

> **其次**，你需要增加对**参数模式**的支持：
>
> 一条指令的每个参数均基于其参数的模式进行处理。现在，你的飞船计算机已经可以理解参数模式 `0`（**位置模式**）了，它将参数解释为**位置** —— 如果参数为 `50`，则其值为**存储在内存中地址 `50` 的值**。到目前为止，所有参数都处于位置模式。

Now, your ship computer will also need to handle parameters in mode `1`, **immediate mode**. In immediate mode, a parameter is interpreted as a **value** - if the parameter is `50`, its value is simply `50`.

> 现在，你的飞船计算机也将需要处理模式 `1`（**立即模式**）下的参数。在立即模式下，参数被解释为**数值** —— 如果参数为 `50`，那它的值直接就是 `50`。

Parameter modes are stored in the same value as the instruction's opcode. The opcode is a two-digit number based only on the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value in an instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are `0`.

> 参数的模式与指令的操作码存储在同一个数值中。操作码是基于数值的个位和十位的两位数，即操作码是指令中第一个数值的最右边两位数。参数的模式只占一位数，每个参数对应一位，从操作码的右向左读取：即第一个参数的模式在百位上，第二个参数的模式在千位上，第三个参数的模式在万位上，依此类推。任何缺少的模式均视为 `0`。

For example, consider the program `1002,4,3,4,33`.

The first instruction, `1002,4,3,4`, is a **multiply** instruction - the rightmost two digits of the first value, `02`, indicate opcode `2`, multiplication. Then, going right to left, the parameter modes are `0` (hundreds digit), `1` (thousands digit), and `0` (ten-thousands digit, not present and therefore zero):

```diff
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
```

> 举个例子，思考程序 `1002,4,3,4,33`。
>
> 第一条指令 `1002,4,3,4` 是一条**乘法**指令 —— 第一个数值的最右边两位数（`02`）表示操作码 `2`，即乘法。然后，从右到左，参数的模式依次为 `0`（百位），`1`（千位）和 `0`（万位，不存在，因此为零）：
>
> ```!
> ABCDE
>  1002
>
> DE - 两位操作码，     02 == 操作码 2
>  C - 第一个参数的模式，0 == 位置模式
>  B - 第二个参数的模式，1 == 立即模式
>  A - 第三个参数的模式，0 == 位置模式，
>                            由于为零而被省略
> ```

This instruction multiplies its first two parameters. The first parameter, `4` in position mode, works like it did before - its value is the value stored at address `4` (`33`). The second parameter, `3` in immediate mode, simply has value `3`. The result of this operation, `33 * 3 = 99`, is written according to the third parameter, `4` in position mode, which also works like it did before - `99` is written to address `4`.

> 这条指令将它的前两个参数相乘。第一个参数 `4` 工作在位置模式下，与以前一样 —— 它的值存储在地址 `4`（`33`）中。第二个参数 `3` 工作在立即模式下，直接取它的值 `3`。这个操作的结果（`33 * 3 = 99`）根据第三个参数 `4` 工作在位置模式下，它的工作方式也与之前一样 —— 将 `99` 写入地址 `4`。

Parameters that an instruction writes to will **never be in immediate mode**.

> 写指令的参数**永远不会处于立即模式**。

**Finally**, some notes:

- It is important to remember that the instruction pointer should increase by **the number of values in the instruction** after the instruction finishes. Because of the new instructions, this amount is no longer always `4`.
- Integers can be negative: `1101,100,-1,4,0` is a valid program (find `100 + -1`, store the result in position `4`).

> **最后**，一些注意事项：
>
> - 这点非常重要，需要记住，当指令完成后，指令的指针需要根据**指令中值的数量**而增加。由于多出了新的指令，该数值不再总是 `4`。
> - 整数可以为负：`1101,100,-1,4,0` 是一段有效的程序（计算 `100 + -1`，将结果存储在位置 `4` 处）。

The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an **input** instruction - provide it `1`, the ID for the ship's air conditioner unit.

> TEST 诊断程序将通过运行**输入**指令从用户那里请求系统的ID进行测试 —— 提供 `1`，它是飞船空调单元的ID。

It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like parameter modes, function correctly. For each test, it will run an **output** instruction indicating how far the result of the test was from the expected value, where `0` means the test was successful. Non-zero outputs mean that a function is not working correctly; check the instructions that were run before the output instruction to see which one failed.

> 接下来它将执行一系列诊断测试，以确认 Intcode 计算机的各个部分（如参数模式）的功能是否正常。对于每个测试，它将运行一条**输出**指令，指示测试结果与预期值的差距，其中 `0` 表示测试成功。非零输出表示该功能无法正常工作，检查这条输出指令之前运行的指令，看看哪一条出错了。

Finally, the program will output a **diagnostic code** and immediately halt. This final output isn't an error; an output followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.

> 最后，程序将输出**诊断代码**并立即停止。最后的这条输出不是一个错误，输出后立即停止意味着程序已完成。排除诊断代码，如果所有的输出都为零，则诊断程序运行成功。

After providing `1` to the only input instruction and passing all the tests, **what diagnostic code does the program produce?**

> 提供 `1` 给唯一的输入指令之后，并通过所有测试，**程序会产生什么诊断代码？**

Your puzzle answer was `5182797`.

## Part Two

The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship **warmer**.

> 空调上线了！它的冷气让人感觉很好，但不一会 TEST 警报开始响起。由于空调无法将热量散发到别出去，只能又回到了飞船，因此实际上会使飞船内的空气**更暖**。

Instead, you'll need to use the TEST to extend the [thermal radiators](https://en.wikipedia.org/wiki/Spacecraft_thermal_control). Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

> 相反，你需要使用 TEST 来扩展[散热器](https://en.wikipedia.org/wiki/Spacecraft_thermal_control)。幸运的是，诊断程序（你的谜题输入）已经配备这项功能。不幸的是，你的 Intcode 计算机没有。

Your computer is only missing a few opcodes:

- Opcode `5` is **jump-if-true**: if the first parameter is **non-zero**, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
- Opcode `6` is **jump-if-false**: if the first parameter **is zero**, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
- Opcode `7` is **less than**: if the first parameter is **less than** the second parameter, it stores `1` in the position given by the third parameter. Otherwise, it stores `0`.
- Opcode `8` is **equals**: if the first parameter is **equal to** the second parameter, it stores `1` in the position given by the third parameter. Otherwise, it stores `0`.

> 你的计算机只是缺少了一些操作码：
>
> - 操作码 `5` 是**如果真则跳转**：如果第一个参数为**非零**，则将指令指针设置为第二个参数的值，否则什么都不做。
> - 操作码 `6` 是**如果假则跳转**：如果第一个参数为**零**，则将指令指针设置为第二个参数的值，否则什么都不做。
> - 操作码 `7` 是**小于**：如果第一个参数**小于**第二个参数，则将 `1` 存储在第三个参数给定的位置，否则存储 `0`。
> - 操作码 `8` 是**等于**：如果第一个参数**等于**第二个参数，则将 `1` 存储在第三个参数给定的位置，否则存储 `0`。

Like all instructions, these instructions need to support **parameter modes** as described above.

> 像所有指令一样，这些指令也需要支持**参数模式**，如上所述。

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. **However**, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is **not automatically increased**.

> 通常，一条指令完成后，指令指针会增加该指令中值的数量。**但是**，如果指令修改了指令指针，则会直接使用这个数值，**不会自动增加**。

For example, here are several programs that take one input, compare it to the value `8`, and then produce one output:

- `3,9,8,9,10,9,4,9,99,-1,8` - Using **position mode**, consider whether the input is **equal to** `8`; output `1` (if it is) or `0` (if it is not).
- `3,9,7,9,10,9,4,9,99,-1,8` - Using **position mode**, consider whether the input is **less than** `8`; output `1` (if it is) or `0` (if it is not).
- `3,3,1108,-1,8,3,4,3,99` - Using **immediate mode**, consider whether the input is **equal to** `8`; output `1` (if it is) or `0` (if it is not).
- `3,3,1107,-1,8,3,4,3,99` - Using **immediate mode**, consider whether the input is **less than** `8`; output `1` (if it is) or `0` (if it is not).

> 例如，以下几个程序接受一个输入值，将其与 `8` 进行比较，然后产生一个输出值：
>
> - `3,9,8,9,10,9,4,9,99,-1,8` —— 使用**位置模式**，判断输入值是否**等于** `8`，如果是则输出 `1`，否则输出 `0`。
> - `3,9,7,9,10,9,4,9,99,-1,8` —— 使用**位置模式**，判断输入值是否**小于** `8`，如果是则输出 `1`，否则输出 `0`。
> - `3,3,1108,-1,8,3,4,3,99` —— 使用**立即模式**，判断输入值是否**等于** `8`，如果是则输出 `1`，否则输出 `0`。
> - `3,3,1107,-1,8,3,4,3,99` —— 使用**立即模式**，判断输入值是否**小于** `8`，如果是则输出 `1`，否则输出 `0`。

Here are some jump tests that take an input, then output `0` if the input was zero or `1` if the input was non-zero:

- `3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9` (using **position mode**)
- `3,3,1105,-1,9,1101,0,0,12,4,12,99,1` (using **immediate mode**)

> 以下几个跳转测试接受一个输入值，如果输入值为零则输出 `0`，如果输入值为非零则输出 `1`：
>
> - `3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9`（使用**位置模式**）
> - `3,3,1105,-1,9,1101,0,0,12,4,12,99,1`（使用**立即模式**）

Here's a larger example:

> 这是一个更大的示例：

```!
3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
```

The above example program uses an input instruction to ask for a single number. The program will then output `999` if the input value is below `8`, output `1000` if the input value is equal to `8`, or output `1001` if the input value is greater than `8`.

> 上面的示例程序使用一条输入指令请求一个数字。然后，如果输入值小于 `8` 则输出 `999`，如果输入值等于 `8` 则将输出 `1000`，如果输入值大于 `8` 则将输出 `1001`。

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, **provide it `5`**, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the **diagnostic code**.

> 这一次，当 TEST 诊断程序运行其输入指令获取测试系统的 ID 时，**为其提供 `5`**，即飞船散热控制器的 ID。此诊断测试套件将输出一个数字，即**诊断代码**。

**What is the diagnostic code for system ID `5`?**

> **系统 ID 为 `5` 的诊断代码是什么？**

Your puzzle answer was `12077198`.

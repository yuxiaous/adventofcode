# Day 8: Handheld Halting

> 第八天：终止掌机

Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.

> 你乘坐的飞往主航空枢纽的飞机达到了巡航高度，没有发生任何事故。当你正考虑看一下飞机上的菜单中是否有一种带有小伞的饮料时，你被领座的小孩打断了。

Their [handheld game console](https://en.wikipedia.org/wiki/Handheld_game_console) won't turn on! They ask if you can take a look.

> 他们的[掌上游戏机](https://en.wikipedia.org/wiki/Handheld_game_console)无法开机！他们请求你帮忙看看。

You narrow the problem down to a strange **infinite loop** in the boot code ([your puzzle input](day08.txt)) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.

> 在设备的启动代码中（[你的谜题输入](day08.txt)），你将问题的范围缩小到了一个奇怪的“无限循环”中。你应该能够修复它，但是首先你需要对代码进行隔离运行。

The boot code is represented as a text file with one **instruction** per line of text. Each instruction consists of an **operation** (`acc`, `jmp`, or `nop`) and an **argument** (a signed number like `+4` or `-20`).

> 启动代码写在一个文本文件中，每行一条指令。每条指令都由一个操作符（`acc`、`jmp` 或 `nop`）和一个参数（一个带符号的数字，例如 `+4` 或 `-20`）组成。

- `acc` increases or decreases a single global value called the **accumulator** by the value given in the argument. For example, `acc +7` would increase the accumulator by 7. The accumulator starts at `0`. After an `acc` instruction, the instruction immediately below it is executed next.
- `jmp` **jumps** to a new instruction relative to itself. The next instruction to execute is found using the argument as an **offset** from the `jmp` instruction; for example, `jmp +2` would skip the next instruction, `jmp +1` would continue to the instruction immediately below it, and `jmp -20` would cause the instruction 20 lines above to be executed next.
- `nop` stands for **No OPeration** - it does nothing. The instruction immediately below it is executed next.

> - `acc` 通过参数中给定的值，增加或减少一个称为“累加器”的全局值。例如，`acc +7` 会使累加器增加 7。累加器从 `0` 开始。在执行一条 `acc` 指令后，紧接着执行下一条指令。
> - `jmp` 跳转到一条相对于自身的新指令。下一条将要执行的指令通过 `jmp` 指令中的 offset 参数来找到。例如，`jmp +2` 将跳过下一条指令，`jmp +1` 将继续执行它的下一条指令，而 `jmp -20` 将在之后执行 20 行之前的指令。
> - `nop` 表示无操作——它什么也不做。紧接着执行下一条指令。

For example, consider the following program:

> 举个例子，考虑下面的程序：

```'
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```

These instructions are visited in this order:

> 这些指令将按照以下顺序访问：

```'
nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
```

First, the `nop +0` does nothing. Then, the accumulator is increased from 0 to 1 (`acc +1`) and `jmp +4` sets the next instruction to the other `acc +1` near the bottom. After it increases the accumulator from 1 to 2, `jmp -4` executes, setting the next instruction to the only `acc +3`. It sets the accumulator to 5, and `jmp -3` causes the program to continue back at the first `acc +1`.

> 首先，`nop +0` 什么都不做。然后，累加器从 0 增加到 1（`acc +1`），`jmp +4` 将下一条指令设置为底部附近的另一条 `acc +1`。在将累加器从 1 增加到 2 之后，执行 `jmp -4`，将下一条指令设置为唯一的 `acc +3`。它将累加器设置为 5，接着 `jmp -3` 使程序从新回到第一个 `acc +1` 处。

This is an **infinite loop**: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

> 这是一个“无限循环”：按照这种跳跃顺序，程序将永远运行下去。一旦程序尝试第二次运行任何指令，你就知道它永远不会终止了。

Immediately **before** the program would run an instruction a second time, the value in the accumulator is **`5`**.

> 在程序将要第二次运行一条指令之前，累加器中的值为 **`5`**。

Run your copy of the boot code. Immediately before any instruction is executed a second time, **what value is in the accumulator?**

> 运行你的启动代码副本。在第二次执行某条指令之前，累加器中的值是多少？

Your puzzle answer was `1446`.

## --- Part Two ---

After some careful analysis, you believe that **exactly one instruction is corrupted**.

> 经过一些仔细的分析，你确定有一条指令被损坏了。

Somewhere in the program, **either** a `jmp` is supposed to be a `nop`, **or** a `nop` is supposed to be a `jmp`. (No `acc` instructions were harmed in the corruption of this boot code.)

> 在程序中的某个地方，要么有一个 `jmp` 原本应该是 `nop`，要么有一个 `nop` 原本应该是 `jmp`。（在这段启动代码的损坏中，没有 `acc` 指令受到损害。）

The program is supposed to terminate by **attempting to execute an instruction immediately after the last instruction in the file**. By changing exactly one `jmp` or `nop`, you can repair the boot code and make it terminate correctly.

> 该程序应该通过尝试在文件中的最后一条指令之后再执行一条指令来终止。通过只更改一个 `jmp` 或 `nop`，你可以修复启动代码并使它正确终止。

For example, consider the same program from above:

> 举个例子，考虑与上面相同的程序：

```'
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```

If you change the first instruction from `nop +0` to `jmp +0`, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the `jmp` instructions, the program will still eventually find another `jmp` instruction and loop forever.

> 如果你将第一条指令从 `nop +0` 修改为 `jmp +0`，则会创建一个单指令无限循环，再也无法离开那条指令。如果你修改了其他任意一条 `jmp` 指令，该程序最终仍将找到另一条 `jmp` 指令并永远循环。

However, if you change the second-to-last instruction (from `jmp -4` to `nop -4`), the program terminates! The instructions are visited in this order:

> 但是，如果你修改倒数第二条指令（从 `jmp -4` 修改为 `nop -4`），程序将会终止！这些指令将按照以下顺序访问：

```'
nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
```

After the last instruction (`acc +6`), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value **`8`** (`acc +1`, `acc +1`, `acc +6`).

> 在最后一条指令（`acc +6`）之后，程序会在运行完文件中最后一条指令之后终止。经过这个修改，程序终止后，累加器的值为 **`8`**（`acc +1`、`acc +1`、`acc +6`）。

Fix the program so that it terminates normally by changing exactly one `jmp` (to `nop`) or `nop` (to `jmp`). **What is the value of the accumulator after the program terminates?**

> 修复程序，使其通过修改一个 `jmp`（改为 `nop`）或 `nop`（改为 `jmp`）能够正常终止。程序终止后，累加器的值是多少？

Your puzzle answer was `1403`.

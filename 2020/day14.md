# Day 14: Docking Data

> 第十四天：对接数据

As your ferry approaches the sea port, the captain asks for your help again. The computer system that runs this port isn't compatible with the docking program on the ferry, so the docking parameters aren't being correctly initialized in the docking program's memory.

> 当你的渡轮接近海港时，船长再次请求你的帮助。这个港口运行的计算机系统与渡轮上的停靠程序不兼容，因此停靠程序的内存中停靠参数未被正确初始化。

After a brief inspection, you discover that the sea port's computer system uses a strange [bitmask](https://en.wikipedia.org/wiki/Mask_(computing)) system in its initialization program. Although you don't have the correct decoder chip handy, you can emulate it in software!

> 简单检查后，你发现海港的计算机系统在它的初始化程序中使用了一套奇怪的 [位掩码](https://en.wikipedia.org/wiki/Mask_(computing)) 系统。尽管你手头上没有正确的解码器芯片，但是可以在软件中进行仿真！

The initialization program ([your puzzle input](day14.txt)) can either update the bitmask or write a value to memory. Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, a line like `mem[8] = 11` would write the value `11` to memory address `8`.

> 初始化程序（[你的谜题输入](day14.txt)）既可以更新位掩码又可以在内存中写入值。值和内存地址都是 36 位无符号整数。例如，暂时忽略位掩码，类似 `mem[8] = 11` 这样一行会将值 `11` 写入内存地址 `8` 中。

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing `2^35`) on the left and the least significant bit (`2^0`, that is, the `1`s bit) on the right. The current bitmask is applied to values immediately before they are written to memory: a `0` or `1` overwrites the corresponding bit in the value, while an `X` leaves the bit in the value unchanged.

> 位掩码始终以 36 位的字符串的形式给出，最高位（表示为 `2^35`）在左侧以及最低位（`2^0`，即数值 `1` 的位）在右边。当前的位掩码会在值写入内存之前应用在这些值上：`0` 或 `1` 会重写值中相应的位，而 `X` 则会保持值中相应的位不变。

For example, consider the following program:

> 举个例子，考虑下面的程序：

```'
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
```

This program starts by specifying a bitmask (`mask = ....`). The mask it specifies will overwrite two bits in every written value: the `2`s bit is overwritten with `0`, and the `64`s bit is overwritten with `1`.

> 这段程序从指定一个位掩码（`mask = ....`）开始。指定的掩码将在每个写入的值中重写两位：`2` 的位被 `0` 重写，而 `64` 的位被 `1` 重写。

The program then attempts to write the value `11` to memory address `8`. By expanding everything out to individual bits, the mask is applied as follows:

> 然后程序尝试将值 `11` 写入内存地址 `8` 中。通过将数值内容转化为二进制位，掩码按以下方式应用：

```'
value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)
```

So, because of the mask, the value `73` is written to memory address `8` instead. Then, the program tries to write `101` to address `7`:

> 因此，由于存在掩码，便将值 `73` 写入了内存地址 `8` 中。然后，程序尝试将 `101` 写入地址 `7` 中：

```'
value:  000000000000000000000000000001100101  (decimal 101)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001100101  (decimal 101)
```

This time, the mask has no effect, as the bits it overwrote were already the values the mask tried to set. Finally, the program tries to write `0` to address `8`:

> 这次，掩码没有起效，因为它被重写的位与掩码尝试设置的值相同。最后，程序尝试将 `0` 写入地址 `8` 中。

```'
value:  000000000000000000000000000000000000  (decimal 0)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001000000  (decimal 64)
```

`64` is written to address `8` instead, overwriting the value that was there previously.

> `64` 被写入了地址 `8`，重写了之前的值。

To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization program completes. (The entire 36-bit address space begins initialized to the value `0` at every address.) In the above example, only two values in memory are not zero - `101` (at address `7`) and `64` (at address `8`) - producing a sum of **`165`**.

> 要初始化你的轮渡的停靠程序，你需要在初始化程序完成后计算内存中所有值的总和。（开始时，整个 36 位的地址空间中的所有地址都将被初始化为 `0`。）在上面的例子中，内存中只有两个值不为零：`101`（位于地址 `7`）和 `64`（位于地址 `8`），得到的总和为 **`165`**。

Execute the initialization program. **What is the sum of all values left in memory after it completes?**

> 执行初始化程序，完成后内存中的所有的值的总和为多少？

Your puzzle answer was `17934269678453`.

## --- Part Two ---

For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using **version 2** of the decoder chip!

> 由于某些原因，海港的计算机系统仍旧无法与渡轮的停靠程序进行通信。必须使用版本为 2 的解码器芯片！

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a [memory address decoder](https://www.youtube.com/watch?v=PvfhANgLrm4). Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination **memory address** in the following way:

- If the bitmask bit is `0`, the corresponding memory address bit is **unchanged**.
- If the bitmask bit is `1`, the corresponding memory address bit is **overwritten with** **`1`**.
- If the bitmask bit is `X`, the corresponding memory address bit is **floating**.

> 版本为 2 的解码器芯片完全不修改写入的值。相反，它变成了[内存地址解码器](https://www.youtube.com/watch?v=PvfhANgLrm4)。在值写入内存之前，位掩码中的每个位都将使用以下方法修改目标内存地址的对应位：
>
> - 如果位掩码位为 `0`，则对应的内存地址位是不变的。
> - 如果位掩码位为 `1`，则对应的内存地址位重写为 `1`。
> - 如果位掩码位为 `X`，则对应的内存地址位是浮动的。

A **floating** bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on **all possible values**, potentially causing many memory addresses to be written all at once!

> 一个浮动位没有连接任何东西，可能发生不可预测的波动。实际上，这意味着浮动位将可能是任何值，有可能导致一次写入多个存储器地址！

For example, consider the following program:

> 举个例子，考虑下面的程序：

```'
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
```

When this program goes to write to memory address `42`, it first applies the bitmask:

> 当这段程序准备写入内存地址 `42` 时，它先应用了位掩码：

```'
address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X
```

After applying the mask, four bits are overwritten, three of which are different, and two of which are **floating**. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

> 应用掩码后，四个位被重写了，其中三个是不同的，其中两个是浮动的。浮动位代表所有可能值的组合，两个浮动位，可以写入四个实际的内存地址：

```'
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)
```

Next, the program is about to write to memory address `26` with a different bitmask:

> 接下来，程序将使用另一个位掩码写入内存地址 `26`：

```'
address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX
```

This results in an address with three floating bits, causing writes to **eight** memory addresses:

> 这导致一个具有三个浮动位的地址，从而对应写入八个内存地址：

```'
000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
```

The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is **`208`**.

> 整个 36 位的地址空间在开始时仍旧将每个地址的值都初始化为 0，并且你仍然需要在程序完成后计算内存中所有值的总和。在这个例子中，总和为 **`208`**。

Execute the initialization program using an emulator for a version 2 decoder chip. **What is the sum of all values left in memory after it completes?**

> 使用解码器芯片版本为 2 的仿真器执行初始化程序。完成后内存中所有的值的总和是多少？

Your puzzle answer was `3440662844064`.

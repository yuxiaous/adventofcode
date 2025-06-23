# Day 3: Mull It Over
> 第三天：再三思考

"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the [North Pole Toboggan Rental Shop](https://adventofcode.com/2020/day/2). The Historians head out to take a look.
> “我们的电脑出了点问题，所以我也不知道我们是否还有首席历史学家的存货！不过你可以去仓库看看。”北极雪橇租赁店的店主有些慌乱地说道。历史学家们于是前去查看。

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"
> 店主转向你说：“你能帮忙看看我们的电脑为什么又出问题了吗？”

The computer appears to be trying to run a program, but its memory (your puzzle input) is **corrupted**. All of the instructions have been jumbled up!
> 电脑似乎正在尝试运行一个程序，但它的内存（你的谜题输入）已经**损坏**。所有指令都被打乱了！

It seems like the goal of the program is just to **multiply some numbers**. It does that with instructions like `mul(X,Y)`, where X and Y are each 1-3 digit numbers. For instance, `mul(44,46)` multiplies `44` by `46` to get a result of 2024. Similarly, `mul(123,4)` would multiply `123` by `4`.
> 这个程序的目标似乎只是**将一些数字相乘**。它通过类似`mul(X,Y)`的指令实现，其中X和Y都是1到3位的数字。例如，`mul(44,46)`表示用44乘以46，结果为2024。同样，`mul(123,4)`表示用123乘以4。

However, because the program's memory has been corrupted, there are also many invalid characters that should be **ignored**, even if they look like part of a `mul` instruction. Sequences like `mul(4*`, `mul(6,9!`, `?(12,34)`, or `mul ( 2 , 4 )` do **nothing**.
> 但是，由于程序内存已损坏，其中还有许多无效字符需要**忽略**，即使它们看起来像是`mul`指令的一部分。像`mul(4*`、`mul(6,9!`、`?(12,34)`或`mul ( 2 , 4 )`这样的序列都**不会有任何作用**。

For example, consider the following section of corrupted memory:
> 例如，考虑下面这段损坏的内存：

`xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`

Only the four highlighted sections are real `mul` instructions. Adding up the result of each instruction produces **`161`** `(2*4 + 5*5 + 11*8 + 8*5)`.
> 只有其中四段高亮部分是真正的`mul`指令。将每条指令的结果相加得到 **`161`**`（2*4 + 5*5 + 11*8 + 8*5）`。

Scan the corrupted memory for uncorrupted mul instructions. **What do you get if you add up all of the results of the multiplications?**
> 扫描损坏的内存，查找未损坏的mul指令。**将所有乘法结果相加，你会得到多少？**

Your puzzle answer was `174960292`.

## Part Two

As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.
> 当你扫描损坏的内存时，你注意到有些条件语句依然完好无损。如果你能处理程序中未损坏的条件语句，或许能得到更准确的结果。

There are two new instructions you'll need to handle:
> 你需要处理两条新指令：

- The `do()` instruction **enables** future `mul` instructions.
- The `don't()` instruction **disables** future `mul` instructions.
> - `do()` 指令会**启用**后续的 `mul` 指令。
> - `don't()` 指令会**禁用**后续的 `mul` 指令。

Only the **most recent** `do()` or `don't()` instruction applies. At the beginning of the program, mul instructions are **enabled**.
> 只有**最近的** `do()` 或 `don't()` 指令有效。程序开始时，mul 指令是**启用**的。

For example:
> 例如：

`xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`

This corrupted memory is similar to the example from before, but this time the `mul(5,5)` and `mul(11,8)` instructions are **disabled** because there is a `don't()` instruction before them. The other `mul` instructions function normally, including the one at the end that gets re-**enabled** by a `do()` instruction.
> 这段损坏的内存与之前的例子类似，但这次 `mul(5,5)` 和 `mul(11,8)` 指令被**禁用**，因为它们前面有一个 `don't()` 指令。其他的 `mul` 指令正常执行，包括最后一个被 `do()` 指令重新**启用**的 `mul`。

This time, the sum of the results is **`48`** `(2*4 + 8*5)`.
> 这一次，结果之和是 **`48`**（2*4 + 8*5）。

Handle the new instructions; **what do you get if you add up all of the results of just the enabled multiplications?**
> 处理这些新指令；**只将启用状态下的乘法结果相加，你会得到多少？**

Your puzzle answer was `56275602`.

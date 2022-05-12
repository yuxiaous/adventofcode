# [Day 3: Binary Diagnostic](https://adventofcode.com/2021/day/3)

> 第3天：二进制诊断

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

> 潜水艇发出了一些奇怪的吱吱声，所以你要求它生成一份诊断报告以防万一。

The diagnostic report ([your puzzle input](day03.txt)) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the **power consumption**.

> 诊断报告（[你的谜题输入](day03.txt)）包含一份二进制数字的列表，如果正确解码，可以告诉你许多有关潜艇状况的有用信息。第一个要检查的参数是**功耗**。

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the **gamma rate** and the **epsilon rate**). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

> 你需要使用诊断报告中的二进制数来生成两个新的二进制数（称为**伽玛率**和**依普西隆率**）。然后可以通过将伽玛率与依普西隆率相乘来得到功耗。

Each bit in the gamma rate can be determined by finding the **most common bit in the corresponding position** of all numbers in the diagnostic report. For example, given the following diagnostic report:

> 在诊断报告中，通过在所有数字的相应位置中找到最多的那个值的方法，可以确定伽玛率中的每个位的值。例如，给定以下诊断报告：

```diff
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

Considering only the first bit of each number, there are five `0` bits and seven `1` bits. Since the most common bit is `1`, the first bit of the gamma rate is `1`.

> 只考虑每个数字的第一位，有五个 `0` 和七个 `1`。由于最多的是 `1`，所以伽玛率的第一位是 `1`。

The most common second bit of the numbers in the diagnostic report is `0`, so the second bit of the gamma rate is `0`.

> 在诊断报告中，第二位最多的数字是 `0`，所以伽玛率的第二位是 `0`。

The most common value of the third, fourth, and fifth bits are `1`, `1`, and `0`, respectively, and so the final three bits of the gamma rate are `110`.

> 第三、第四和第五位最多的值分别是 `1`、`1` 和 `0`，所以伽玛率的后三位是 `110`。

So, the gamma rate is the binary number `10110`, or **`22`** in decimal.

> 因此，伽玛率是二进制数 `10110`，或十进制数 **`22`**。

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is `01001`, or **`9`** in decimal. Multiplying the gamma rate (`22`) by the epsilon rate (`9`) produces the power consumption, **`198`**.

> 依普西隆率的计算方法相似，不是使用最多的位，而是每个位置中使用最少的位。因此，依普西隆率是 `01001`，或十进制数 **`9`**。 将伽玛率 (`22`) 乘以依普西隆率 (`9`) 会得到功耗 **`198`**。

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. **What is the power consumption of the submarine?** (Be sure to represent your answer in decimal, not binary.)

> 使用诊断报告中的二进制数来计算伽玛率和依普西隆率，然后将它们相乘。**潜水艇的功耗是多少？**（请务必使用十进制来表示你的答案，而不是二进制。）

Your puzzle answer was `4160394`.

## --- Part Two ---

Next, you should verify the **life support rating**, which can be determined by multiplying the **oxygen generator rating** by the **CO2 scrubber rating**.

> 接下来，你应该验证**生命维持额定值**，可以通过**氧气发生器额定值**和**二氧化碳清除器额定值**的乘积来确定。

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and **consider just the first bit** of those numbers. Then:

> 氧气发生器额定值和二氧化碳清除器额定值的值都可以在诊断报告中找到--找到它们是一件棘手的事。这两个值都使用类似的过程来确定，该过程涉及过滤出唯一剩下的值。要找出这两个额定值，得先从诊断报告中包含所有二进制数的列表开始，首先判断这些数的**第一位**：

- Keep only numbers selected by the **bit criteria** for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
- If you only have one number left, stop; this is the rating value for which you are searching.
- Otherwise, repeat the process, considering the next bit to the right.

> - 对于你正在查找的额定值类型，仅保留符合**位规则**的数字，丢弃不符合位规则的数字。
> - 如果你只剩下一个数了，停下来。这就是你正在查找的额定值。
> - 否则，重复这个过程，判断右边的下一位。

The **bit criteria** depends on which type of rating value you want to find:

> **位规则**取决于你要查找的额定值类型：

- To find **oxygen generator rating**, determine the **most common** value (`0` or `1`) in the current bit position, and keep only numbers with that bit in that position. If `0` and `1` are equally common, keep values with a **`1`** in the position being considered.
- To find **CO2 scrubber rating**, determine the **least common** value (`0` or `1`) in the current bit position, and keep only numbers with that bit in that position. If `0` and `1` are equally common, keep values with a **`0`** in the position being considered.

> - 要查找**氧气发生器额定值**，先确定当前位中的**最多的**值（`0` 或 `1`），并只保留该位中带有该值的数字。如果 `0` 和 `1` 数量相同，则保留该位中带有 **`1`** 的数字。
> - 要查找**二氧化碳清除器额定值**，先确定当前位中的**最少的**值（`0` 或 `1`），并只保留该位中带有该值的数字。如果 `0` 和 `1` 数量相同，则保留该位中带有 **`0`** 的数字。

For example, to determine the **oxygen generator rating** value using the same example diagnostic report from above:

> 举个例子，使用上面同一个例子中的诊断报告来确定**氧气发生器额定值**：

- Start with all 12 numbers and consider only the first bit of each number. There are more `1` bits (7) than `0` bits (5), so keep only the 7 numbers with a `1` in the first position: `11110`, `10110`, `10111`, `10101`, `11100`, `10000`, and `11001`.
- Then, consider the second bit of the 7 remaining numbers: there are more `0` bits (4) than `1` bits (3), so keep only the 4 numbers with a `0` in the second position: `10110`, `10111`, `10101`, and `10000`.
- In the third position, three of the four numbers have a `1`, so keep those three: `10110`, `10111`, and `10101`.
- In the fourth position, two of the three numbers have a `1`, so keep those two: `10110` and `10111`.
- In the fifth position, there are an equal number of `0` bits and `1` bits (one each). So, to find the **oxygen generator rating**, keep the number with a `1` in that position: `10111`.
- As there is only one number left, stop; the **oxygen generator rating** is `10111`, or **`23`** in decimal.

> - 从所有的 12 个数字开始，只判断每个数字的第一位。值为 `1` 的位（7个）比值为 `0` 的位（5个）多，所以只保留第一位中带有 `1` 的 7 个数字：`11110`、`10110`、`10111`、`10101` 、`11100`、`10000` 和 `11001`。
> - 然后，判断剩余 7 个数字的第二位：值为 `0` 的位（4个）比值为 `1` 的位（3个）多，所以只保留第二位中带有 `0` 的 4 个数字：`10110`、`10111`、`10101` 和 `10000`。
> - 在第三位中，四个数字有三个是 `1`，所以保留这三个数：`10110`、`10111` 和 `10101`。
> - 在第四位中，三个数字有两个是 `1`，所以保留这两个数：`10110` 和 `10111`。
> - 在第五位中，有相同数量的 `0` 和 `1`（各一个）。因此，为了找出**氧气发生器额定值**，需要保留该位中带有 `1` 的数字：`10111`。
> - 由于只剩下一个数字了，所以停止继续查找。**氧气发生器额定值**为 `10111`，或十进制数 **`23`**。

Then, to determine the **CO2 scrubber rating** value from the same example above:

> 接下来，从上面的同一个例子中确定**二氧化碳清除器额定值**：

- Start again with all 12 numbers and consider only the first bit of each number. There are fewer `0` bits (5) than `1` bits (7), so keep only the 5 numbers with a `0` in the first position: `00100`, `01111`, `00111`, `00010`, and `01010`.
- Then, consider the second bit of the 5 remaining numbers: there are fewer `1` bits (2) than `0` bits (3), so keep only the 2 numbers with a `1` in the second position: `01111` and `01010`.
- In the third position, there are an equal number of `0` bits and `1` bits (one each). So, to find the **CO2 scrubber rating**, keep the number with a `0` in that position: `01010`.
- As there is only one number left, stop; the **CO2 scrubber rating** is `01010`, or **`10`** in decimal.

> - 重新从所有的 12 个数字开始，只判断每个数字的第一位。值为 `0` 的位（5个）比值为 `1` 的位（7个）少，所以只保留第一位中带有 `0` 的 5 个数字：`00100`、`01111`、`00111`、`00010` 和 `01010`。
> - 然后，判断剩余 5 个数字的第二位：值为 `1` 的位（2个）比值为 `0` 的位（3个）少，所以只保留第二位中带有 `1` 的 2 个数字：`01111` 和 `01010`。
> - 在第三位中，有相同数量的 `0` 和 `1`（各一个）。因此，为了找出**二氧化碳清除器额定值**，需要保留该位中带有 `0` 的数字：`01010`。
> - 由于只剩下一个数字了，所以停止继续查找。**二氧化碳清除器额定值**为 `01010`，或十进制数 **`10`**。

Finally, to find the life support rating, multiply the oxygen generator rating (`23`) by the CO2 scrubber rating (`10`) to get **`230`**.

> 最后，为了得到生命维持额定值，将氧气发生器额定值(`23`)与二氧化碳清除器额定值(`10`)相乘得到 **`230`**。

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. **What is the life support rating of the submarine?** (Be sure to represent your answer in decimal, not binary.)

使用诊断报告中的二进制数来计算氧气发生器额定值和二氧化碳清除器额定值，然后将它们相乘。**潜艇的生命维持额定值是多少？**（请务必使用十进制来表示你的答案，而不是二进制。）

Your puzzle answer was `4125600`.

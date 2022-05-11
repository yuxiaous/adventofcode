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

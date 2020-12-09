# Day 9: Encoding Error

> 第九天：编码错误

With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen in the seat in front of you.

> 在你的领座愉快地享受他们的电子游戏时，你将注意力转移到了一个开放数据端口上，它位于你前方座位后的小屏幕上。

Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips. Upon connection, the port outputs a series of numbers ([your puzzle input](day09.txt)).

> 尽管该端口是非标准的，但你还是巧妙地通过使用多个回形针将其连接到了你的计算机。连接后，端口输出了一系列数字（[你的谜题输入](day09.txt)）。

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.

> 数据似乎通过交换掩码加法系统（XMAS）进行了加密，它是一个具有重大缺陷的旧加密算法，破解它对于你来说得心应手。

XMAS starts by transmitting a **preamble** of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.

> XMAS 首先发送一个 25 个数字的前文。之后，你收到的每个数字都应该是前面的 25 个数字中任意两个数字的总和。这两个数字具有不同的值，并且这样的数对可能不止一个。

For example, suppose your preamble consists of the numbers `1` through `25` in a random order. To be valid, the next number must be the sum of two of those numbers:

- `26` would be a **valid** next number, as it could be `1` plus `25` (or many other pairs, like `2` and `24`).
- `49` would be a **valid** next number, as it is the sum of `24` and `25`.
- `100` would **not** be valid; no two of the previous 25 numbers sum to `100`.
- `50` would also **not** be valid; although `25` appears in the previous 25 numbers, the two numbers in the pair must be different.

> 举个例子，假设你的前文由数字 `1` 到 `25` 以随机顺序组成。为了有效，后续数字必须是这些数字其中两个的总和：
>
> - `26` 是一个有效的后续数字，因为它可能是 `1` 加 `25`（或其他数对，例如 `2` 和 `24`）。
> - `49` 是一个有效的后续数字，因为它是 `24` 和 `25` 的和。
> - `100` 是无效的，前 25 个数字中没有加起来等于 `100` 的两个数字。
> - `50` 也是无效的，尽管在之前 25 个数字中出现了 `25`，但数对中的两个数字必须是不同。

Suppose the 26th number is `45`, and the first number (no longer an option, as it is more than 25 numbers ago) was `20`. Now, for the next number to be valid, there needs to be some pair of numbers among `1`-`19`, `21`-`25`, or `45` that add up to it:

- `26` would still be a **valid** next number, as `1` and `25` are still within the previous 25 numbers.
- `65` would **not** be valid, as no two of the available numbers sum to it.
- `64` and `66` would both be **valid**, as they are the result of `19+45` and `21+45` respectively.

> 假设第 26 个数字是 `45`，第 1 个数字（不再可选了，因为它在前 25 个数字之外）是 `20`。现在，为了使后续数字有效，需要在`1`-`19`、`21`-`25` 以及 `45` 这些数字中选择两个加起来：
>
> - `26` 仍旧是一个有效的后续数字，因为 `1` 和 `25` 仍在前 25 个数字之中。
> - `65` 是无效的，因为没有可以相加得到它的两个可用的数字。
> - `64` 和 `66` 都是有效的，因为它们分别是 `19+45` 和 `21+45` 的结果。

Here is a larger example which only considers the previous **5** numbers (and has a preamble of length 5):

> 这是一个更大的例子，它只考虑前面的 5 数字（并且前文的长度为 5）：

```'
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
```

In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is **`127`**.

> 在这个例子中，在 5 个数字的前文之后，几乎每个数字都是前 5 个数字中的两个之和，唯一不遵循此规则的数字是 **`127`**。

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. **What is the first number that does not have this property?**

> 攻击 XMAS 数据的弱点的第一步是在列表中找到第一个不满足条件的数字（在前文之后），即它不是前 25 个数字中任意两个数字的和。第一个没有此属性的数字是什么？

Your puzzle answer was `1930745883`.

## --- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must **find a contiguous set of at least two numbers** in your list which sum to the invalid number from step 1.

> 破解 XMAS 加密的最后一步依赖于你刚刚找到的无效数字：你必须在列表中找到一个至少包含两个数字的连续集合，这些数字加起来就是步骤 1 中的无效数字。

Again consider the above example:

> 再次考虑上面的例子：

```'
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
```

In this list, adding up all of the numbers from `15` through `40` produces the invalid number from step 1, `127`. (Of course, the contiguous set of numbers in your actual list might be much longer.)

> 在这个列表中，将 `15` 到 `40` 中的所有数字相加会得到步骤 1 中的无效数字 `127`。（当然，实际列表中的数字连续集合可能会长很多。）

To find the **encryption weakness**, add together the **smallest** and **largest** number in this contiguous range; in this example, these are `15` and `47`, producing **`62`**.

> 要找出加密弱点，将这个连续范围内的最小和最大数字相加，在这个例子中，它们是 `15` 和 `47`，得到 **`62`**。

**What is the encryption weakness in your XMAS-encrypted list of numbers?**

> 在 XMAS 加密的数字列表中，加密弱点是什么？

Your puzzle answer was `268878261`.

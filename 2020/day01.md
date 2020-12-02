# [Day 1: Report Repair](https://adventofcode.com/2020/day/1)

> 第一天：报告维修

After saving Christmas [five years in a row](https://adventofcode.com/events), you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

> 在连续五年拯救圣诞节后，你决定找一个不错的热带岛屿度假村度假。当然，即使你不在圣诞节也不会停下来。

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them **stars**. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

> 这个热带岛屿有它自己的货币，并且完全只用现金。那里使用的金币上有一幅海星的图案，当地人就称它们为星币。似乎没有一家货币交易所听说过这种货币，但是不管如何，在你来到这里之前，你需要找到五十枚这种金币，以便可以支付房间的定金。

To save your vacation, you need to get all **fifty stars** by December 25th.

> 为了拯救你的度假，你需要在12月25日之前获得全部的五十枚星币。

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

> 你可以通过解决谜题来收集星币。圣诞倒数日历中的每一天都会有两个谜题被激活，当完成第一个谜题后，第二个谜题便会解锁。每个谜题都会授予一枚星币。祝你好运！

Before you leave, the Elves in accounting just need you to fix your **expense report** (your puzzle input); apparently, something isn't quite adding up.

> 在你离开之前，会计精灵需要你修复你的账单（[你的谜题输入](day01.txt)）。显然，这些东西并没有加起来。

Specifically, they need you to **find the two entries that sum to `2020`** and then multiply those two numbers together.

> 具体来说，他们需要你找到两个总和为 `2020` 的条目，然后将这两个数字相乘。

For example, suppose your expense report contained the following:

> 举个例子，假设你的账单包含如下条目：

```'
1721
979
366
299
675
1456
```

In this list, the two entries that sum to `2020` are `1721` and `299`. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is **`514579`**.

> 在这个列表中，可以相加得到 `2020` 的两个条目分别是 `1721` 和 `299` 。将它们相乘会得到 `1721 * 299 = 514579`，因此正确答案是 **`514579`**。

Of course, your expense report is much larger. **Find the two entries that sum to `2020`; what do you get if you multiply them together?**

> 当然，你的账单要长得多。找到两个总和为 `2020` 的条目，将它们相乘会得到什么？

Your puzzle answer was `776064`.

## --- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find **three** numbers in your expense report that meet the same criteria.

> 会计精灵为了感谢你的帮助，其中一个精灵给了你一枚上次度假时剩下来的海星金币。如果你可以在账单中找到满足相同条件的三个数字，他们会给你第二枚金币。

Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`. Multiplying them together produces the answer, **`241861950`**.

> 再次使用上面的例子，相加得到 `2020` 的三个条目分别为 `979`、`366` 和 `675`。将它们相乘得到答案 **`241861950`**。

In your expense report, **what is the product of the three entries that sum to `2020`?**

> 在你的账单中，相加可以得到 `2020` 的三个条目的乘积是多少？

Your puzzle answer was `6964490`.

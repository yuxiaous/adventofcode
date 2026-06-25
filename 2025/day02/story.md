# Day 2: Gift Shop

> 第二天：礼品店

You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

> 你走进大楼，乘坐电梯来到它唯一的另一个停靠点：礼品店。"感谢您光临北极！"附近的一块牌子兴高采烈地写道。你不确定到底谁有资格访问北极，但你知道通过这里可以进入大厅，再从大厅进入北极基地的其他区域。

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

> 当你在出乎意料地丰富的商品中穿行时，一位店员认出了你，并向你寻求帮助。

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

> 原来，一位年轻精灵在礼品店的电脑上玩耍时，不小心往礼品店数据库里添加了一大堆无效的产品 ID！对你来说，帮他们找出这些无效的产品 ID 应该不成问题吧？

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

> 他们已经检查了大部分产品 ID 范围；只剩下少数几个产品 ID 范围（你的谜题输入）需要你来检查。例如：

```
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
```

(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

> （这里为了可读性对 ID 范围做了换行；在你的输入中，它们会显示在一行中。）

The ranges are separated by commas (`,`); each range gives its **first ID** and **last ID** separated by a dash (`-`).

> 范围之间用逗号（`,`）分隔；每个范围用短划线（`-`）分隔其**第一个 ID** 和**最后一个 ID**。

Since the young Elf was just doing silly patterns, you can find the **invalid IDs** by looking for any ID which is made only of some sequence of digits repeated twice. So, `55` (`5` twice), `6464` (`64` twice), and `123123` (`123` twice) would all be invalid IDs.

> 由于年轻精灵只是在做傻傻的图案游戏，你可以通过查找那些仅由某个数字序列重复两次组成的 ID 来找到**无效 ID**。因此，`55`（`5` 重复两次）、`6464`（`64` 重复两次）和 `123123`（`123` 重复两次）都是无效 ID。

None of the numbers have leading zeroes; `0101` isn't an ID at all. (`101` is a **valid** ID that you would ignore.)

> 所有数字都没有前导零；`0101` 根本不算 ID。（`101` 是你会忽略的**有效** ID。）

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

> 你的任务是找出给定范围内出现的所有无效 ID。在上面的例子中：

- `11-22` has two invalid IDs, **`11`** and **`22`**.
- `95-115` has one invalid ID, **`99`**.
- `998-1012` has one invalid ID, **`1010`**.
- `1188511880-1188511890` has one invalid ID, **`1188511885`**.
- `222220-222224` has one invalid ID, **`222222`**.
- `1698522-1698528` contains no invalid IDs.
- `446443-446449` has one invalid ID, **`446446`**.
- `38593856-38593862` has one invalid ID, **`38593859`**.
- The rest of the ranges contain no invalid IDs.

> - `11-22` 有两个无效 ID，**`11`** 和 **`22`**。
> - `95-115` 有一个无效 ID，**`99`**。
> - `998-1012` 有一个无效 ID，**`1010`**。
> - `1188511880-1188511890` 有一个无效 ID，**`1188511885`**。
> - `222220-222224` 有一个无效 ID，**`222222`**。
> - `1698522-1698528` 没有无效 ID。
> - `446443-446449` 有一个无效 ID，**`446446`**。
> - `38593856-38593862` 有一个无效 ID，**`38593859`**。
> - 其余范围没有无效 ID。

Adding up all the invalid IDs in this example produces **`1227775554`**.

> 把例子中所有无效 ID 相加，得到 **`1227775554`**。

**What do you get if you add up all of the invalid IDs?**

> **把所有无效 ID 相加，你会得到什么？**

Your puzzle answer was `19605500130`.

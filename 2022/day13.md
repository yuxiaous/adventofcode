# Day 13: Distress Signal
> 第13天：遇险信号

You climb the hill and again try contacting the Elves. However, you instead receive a signal you weren't expecting: a **distress signal**.
> 你爬上山再次尝试联系精灵们。然而，你却收到了一个意想不到的信号：**遇险信号**。

Your handheld device must still not be working properly; the packets from the distress signal got decoded **out of order**. You'll need to re-order the list of received packets ([your puzzle input](day13.txt)) to decode the message.
> 你的手持设备似乎仍然无法正常工作；遇险信号的数据包被**解码顺序混乱**。你需要重新排序收到的数据包列表（[你的谜题输入](day13.txt)）以解码消息。

Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify **how many pairs of packets are in the right order**.
> 你的列表由一对对数据包组成；每对之间用空行分隔。你需要确定**有多少对数据包顺序是正确的**。

For example:
> 例如：

```
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
```

Packet data consists of lists and integers. Each list starts with `[`, ends with `]`, and contains zero or more comma-separated values (either integers or other lists). Each packet is always a list and appears on its own line.
> 数据包内容由列表和整数组成。每个列表以`[`开头，以`]`结尾，包含零个或多个逗号分隔的值（可以是整数或其他列表）。每个数据包总是一个列表，并单独占一行。

When comparing two values, the first value is called **left** and the second value is called **right**. Then:
> 比较两个值时，第一个值称为**左侧**，第二个值称为**右侧**。然后：

- If **both values are integers**, the **lower integer** should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
- If **both values are lists**, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
- If **exactly one value is an integer**, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing `[0,0,0]` and `2`, convert the right value to `[2]` (a list containing `2`); the result is then found by instead comparing `[0,0,0]` and `[2]`.
> - 如果**两个值都是整数**，则**较小的整数**应排在前面。如果左侧整数小于右侧整数，则顺序正确。如果左侧整数大于右侧整数，则顺序不正确。如果两个整数相同，则继续比较下一个部分。
> - 如果**两个值都是列表**，则依次比较每个列表的第一个值、第二个值等。如果左侧列表先耗尽元素，则顺序正确。如果右侧列表先耗尽元素，则顺序不正确。如果两个列表长度相同且没有比较出顺序，则继续比较下一个部分。
> - 如果**只有一个值是整数**，则将该整数转换为只包含该整数的列表，然后重新比较。例如，比较`[0,0,0]`和`2`时，将右侧值转换为`[2]`（只包含2的列表）；然后比较`[0,0,0]`和`[2]`。

Using these rules, you can determine which of the pairs in the example are in the right order:
> 使用这些规则，你可以判断示例中的哪些数据包对顺序是正确的：

```
== Pair 1 ==
- Compare [1,1,3,1,1] vs [1,1,5,1,1]
  - Compare 1 vs 1
  - Compare 1 vs 1
  - Compare 3 vs 5
    - Left side is smaller, so inputs are in the right order

== Pair 2 ==
- Compare [[1],[2,3,4]] vs [[1],4]
  - Compare [1] vs [1]
    - Compare 1 vs 1
  - Compare [2,3,4] vs 4
    - Mixed types; convert right to [4] and retry comparison
    - Compare [2,3,4] vs [4]
      - Compare 2 vs 4
        - Left side is smaller, so inputs are in the right order

== Pair 3 ==
- Compare [9] vs [[8,7,6]]
  - Compare 9 vs [8,7,6]
    - Mixed types; convert left to [9] and retry comparison
    - Compare [9] vs [8,7,6]
      - Compare 9 vs 8
        - Right side is smaller, so inputs are not in the right order

== Pair 4 ==
- Compare [[4,4],4,4] vs [[4,4],4,4,4]
  - Compare [4,4] vs [4,4]
    - Compare 4 vs 4
    - Compare 4 vs 4
  - Compare 4 vs 4
  - Compare 4 vs 4
  - Left side ran out of items, so inputs are in the right order

== Pair 5 ==
- Compare [7,7,7,7] vs [7,7,7]
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Right side ran out of items, so inputs are not in the right order

== Pair 6 ==
- Compare [] vs [3]
  - Left side ran out of items, so inputs are in the right order

== Pair 7 ==
- Compare [[[]]] vs [[]]
  - Compare [[]] vs []
    - Right side ran out of items, so inputs are not in the right order

== Pair 8 ==
- Compare [1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]
  - Compare 1 vs 1
  - Compare [2,[3,[4,[5,6,7]]]] vs [2,[3,[4,[5,6,0]]]]
    - Compare 2 vs 2
    - Compare [3,[4,[5,6,7]]] vs [3,[4,[5,6,0]]]
      - Compare 3 vs 3
      - Compare [4,[5,6,7]] vs [4,[5,6,0]]
        - Compare 4 vs 4
        - Compare [5,6,7] vs [5,6,0]
          - Compare 5 vs 5
          - Compare 6 vs 6
          - Compare 7 vs 0
            - Right side is smaller, so inputs are not in the right order
```

What are the indices of the pairs that are already **in the right order**? (The first pair has index 1, the second pair has index 2, and so on.) In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is **`13`**.
> 哪些数据包对的顺序已经**正确**？（第一对的索引为1，第二对为2，依此类推。）在上面的例子中，顺序正确的对是1、2、4和6；这些索引的和是**`13`**。

Determine which pairs of packets are already in the right order. **What is the sum of the indices of those pairs?**
> 判断哪些数据包对的顺序已经正确。**这些对的索引之和是多少？**

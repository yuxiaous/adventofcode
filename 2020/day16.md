# Day 16: Ticket Translation

> 第十六天：车票翻译

As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

> 当你步行到另一趟转机航班时，你注意到重新规划的路线中接下来的一段是乘坐高速火车。但是，你的火车票上写着你不懂的语言。因此在接下来的航班抵达火车站之前，你最好能弄明白上面说的是什么。

Unfortunately, you can't actually **read** the words on the ticket. You can, however, read the numbers, and so you figure out **the fields these tickets must have** and **the valid ranges** for values in those fields.

> 不幸的是，你实在是无法看懂车票上的文字。但是，你可以看懂数字，因此你可以弄明白这些车票有哪些字段以及这些字段中数值的有效范围。

You collect the **rules for ticket fields**, the **numbers on your ticket**, and the **numbers on other nearby tickets** for the same train service (via the airport security cameras) together into a single document you can reference ([your puzzle input](day16.txt)).

> 你收集了同一个票务服务中的车票字段规则、你的车票上的数字以及附近其他车票上的数字（通过机场安全摄像机），并将它们保存在一个文档中（[你的谜题输入](day16.txt)）。

The **rules for ticket fields** specify a list of fields that exist **somewhere** on the ticket and the **valid ranges of values** for each field. For example, a rule like `class: 1-3 or 5-7` means that one of the fields in every ticket is named `class` and can be any value in the ranges `1-3` or `5-7` (inclusive, such that `3` and `5` are both valid in this field, but `4` is not).

> 车票字段规则指定了一个字段的列表，包含车票上所有字段以及每个字段中数字的有效范围。例如， `class: 1-3 or 5-7` 这样一条规则表示车票中有一个字段命名为 `class`，并且可取范围 `1-3` 或 `5-7` 中的任意值。（诸如 `3` 和 `5` 之类的数字都是这个字段的有效值，但 `4` 无效）。

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

> 每张车票都可以由一行逗号分隔开的数字表示。这些数字就是车票上显示的数字，并按照它们出现的顺序排列，每张车票的格式都是相同。例如，考虑下面这张车票：

```'
.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
```

Here, `?` represents text in a language you don't understand. This ticket might be represented as `101,102,103,104,301,302,303,401,402,403`; of course, the actual train tickets you're looking at are **much** more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

> 在这里，`?` 代表你看不懂的文字。这张车票可以表示为 `101,102,103,104,301,302,303,401,402,403`，当然，你实际正在查看的火车票要比这个复杂得多。无论如何，你只需要用这种方法提取数字：从某个相同位置的特定字段取第一个数字，从另一个不同位置的特定字段取第二个数字，依此类推。你只是不知道每个位置的实际意思是什么！

Start by determining which tickets are **completely invalid**; these are tickets that contain values which **aren't valid for any field**. Ignore **your ticket** for now.

> 首先确定哪些车票是完全无效的，这些车票包含不属于任何字段的无效数字。先忽略你的车票。

For example, suppose you have the following notes:

> 举个例子，假设你有以下的记录：

```'
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
```

It doesn't matter which position corresponds to which field; you can identify invalid **nearby tickets** by considering only whether tickets contain **values that are not valid for any field**. In this example, the values on the first **nearby ticket** are all valid for at least one field. This is not true of the other three **nearby tickets**: the values `4`, `55`, and `12` are are not valid for any field. Adding together all of the invalid values produces your **ticket scanning error rate**: `4 + 55 + 12` = **`71`**.

> 哪个位置对应哪个字段都没有关系；你可以通过分析附近的车票是否包含对某个字段无效的数字来验证车票是否无效。在这个例子中，第一张附近的车票上的数字都至少对应一个有效字段。对于其它三张附近的车票，情况就不是这样了：数字 `4`、`55` 和 `12` 对任意一个字段均无效。将所有无效值相加得出你的车票扫描错误率：`4 + 55 + 12` = **`71`**。

Consider the validity of the **nearby tickets** you scanned. **What is your ticket scanning error rate?**

> 考虑你扫描的附近车票的有效性。你的车票扫描错误率是多少？

Your puzzle answer was `21071`.

## --- Part Two ---

Now that you've identified which tickets contain invalid values, **discard those tickets entirely**. Use the remaining valid tickets to determine which field is which.

> 现在，你已经确定了哪些车票包含无效值，统统丢掉这些车票。使用剩下的有效车票确定哪个字段是什么。

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if `seat` is the third field, it is the third field on every ticket, including **your ticket**.

> 使用每个字段的有效范围，确定车票上字段的显示顺序。所有车票的字段顺序是一致的：如果 `seat` 是第三个字段，则每张车票的第三个字段都是它，包括你的车票。

For example, suppose you have the following notes:

> 举个例子，假设你有以下的记录：

```'
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
```

Based on the **nearby tickets** in the above example, the first position must be `row`, the second position must be `class`, and the third position must be `seat`; you can conclude that in **your ticket**, `class` is `12`, `row` is `11`, and `seat` is `13`.

> 根据上面例子中的附近车票，第一个位置必定是 `row`，第二个位置必定是 `class`，第三个位置必定是 `seat`。所以你能断定，在你的车票中，`class` 是 `12`，`row` 是 `11`，以及 `seat` 是 `13`。

Once you work out which field is which, look for the six fields on **your ticket** that start with the word `departure`. **What do you get if you multiply those six values together?**

> 一旦你确定哪个字段是什么后，在你的车票上找出以 `departure` 开头的六个字段。将这六个值相乘会得到什么？

Your puzzle answer was `3429967441937`.

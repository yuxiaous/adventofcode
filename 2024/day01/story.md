# Day 1: Historian Hysteria
> 第一天：历史学家的狂想

The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.
> 首席历史学家每年都会出席盛大的圣诞雪橇发射仪式，但近几个月却无人见过他！最后的消息是他正在探访对北极具有历史意义的地点。一群资深历史学家请你协助他们调查最可能的首席历史学家去向。

As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.
> 每检查一个地点，他们会在清单上用星号标记。他们认为首席历史学家一定在他们要查看的前五十个地方之一，所以为了拯救圣诞节，你需要在圣诞老人12月25日出发前帮助他们在清单上获得五十颗星。

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
> 通过解谜来收集星星。降临节日历中的每一天都会提供两个谜题；完成第一个谜题后会解锁第二个。每个谜题可获得一颗星。祝你好运！

You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently empty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.
> 你们还没出发，精灵资深历史学家们就遇到了问题：他们要检查的地点清单目前是空的。最终，有人决定首先要检查的最佳地点应该是首席历史学家的办公室。

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?
> 当大家涌入办公室时，所有人都确认首席历史学家确实不在这里。相反，精灵们发现了各种笔记和具有历史意义地点的清单！这似乎是首席历史学家离开前的计划。也许这些笔记可以用来确定要搜索哪些地点？

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.
> 在首席的办公室里，具有历史意义的地点不是用名字列出，而是用一个叫做地点ID的唯一编号。为了确保不遗漏任何信息，历史学家们分成两组，各自搜索办公室并试图创建自己的完整地点ID清单。

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?
> 只有一个问题：当把两份清单并排放在一起（你的谜题输入）时，很快就会发现这两份清单并不相似。也许你能帮助历史学家们协调他们的清单？

For example:
> 例如：

```
3   4
4   3
2   5
1   3
3   9
3   3
```

Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.
> 也许这两份清单只是有些许差异！要找出差距，将数字配对并测量它们之间的距离。将左侧清单中最小的数字与右侧清单中最小的数字配对，然后将左侧第二小的数字与右侧第二小的数字配对，依此类推。

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
> 在每一对中，计算两个数字之间的距离；你需要把所有这些距离加起来。例如，如果你将左侧清单中的3与右侧清单中的7配对，距离是4；如果将9与3配对，距离是6。

In the example list above, the pairs and distances would be as follows:
- The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
- The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
- The third-smallest number in both lists is 3, so the distance between them is 0.
- The next numbers to pair up are 3 and 4, a distance of 1.
- The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
- Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
> - 左侧清单中最小的数字是1，右侧清单中最小的数字是3。它们之间的距离是2。
> - 左侧清单中第二小的数字是2，右侧清单中第二小的数字还是3。它们之间的距离是1。
> - 两份清单中第三小的数字都是3，所以它们之间的距离是0。
> - 接下来配对的数字是3和4，距离为1。
> - 每份清单中第五小的数字分别是3和5，距离为2。
> - 最后，左侧清单中最大的数字是4，右侧清单中最大的数字是9；它们之间的距离是5。

To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is `2 + 1 + 0 + 1 + 2 + 5`, a total distance of `11`!
> 要找出左右两份清单之间的总距离，将所有配对的距离加起来。在上面的例子中，这就是 `2 + 1 + 0 + 1 + 2 + 5`，总距离为 `11`！

Your actual left and right lists contain many location IDs. What is the total distance between your lists?
> 你实际的左右清单包含许多地点ID。你的清单之间的总距离是多少？

Your puzzle answer was `2344935`.

## Part Two

> 第二部分

Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.
> 你的分析只证实了大家的担忧：这两份地点ID清单确实非常不同。

Or are they?
> 真的如此吗？

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.
> 历史学家们无法达成一致，不知道是哪一组出错了，也无法辨认大部分首席的笔迹，但在混乱中你注意到一个有趣的细节：许多地点ID在两份清单中都出现了！也许其他数字根本不是地点ID，而是误读的笔迹。

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
> 这一次，你需要准确计算左侧清单中每个数字在右侧清单中出现的次数。将左侧清单中的每个数字乘以它在右侧清单中出现的次数，然后将这些结果相加，得到总相似度分数。

Here are the same example lists again:
> 下面还是相同的示例清单：

```
3   4
4   3
2   5
1   3
3   9
3   3
```

For these example lists, here is the process of finding the similarity score:
> 对于这些示例清单，计算相似度分数的过程如下：

- The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
- The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
- The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
- The fourth number, 1, also does not appear in the right list.
- The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
- The last number, 3, appears in the right list three times; the similarity score again increases by 9.
> - 左侧清单中的第一个数字是3。它在右侧清单中出现了三次，所以相似度分数增加了3 * 3 = 9。
> - 左侧清单中的第二个数字是4。它在右侧清单中出现了一次，所以相似度分数增加了4 * 1 = 4。
> - 左侧清单中的第三个数字是2。它没有出现在右侧清单中，所以相似度分数不变（2 * 0 = 0）。
> - 第四个数字1也没有出现在右侧清单中。
> - 第五个数字3在右侧清单中出现了三次；相似度分数增加了9。
> - 最后一个数字3在右侧清单中出现了三次；相似度分数再次增加了9。

So, for these example lists, the similarity score at the end of this process is `31` (`9 + 4 + 0 + 0 + 9 + 9`).
> 所以，对于这些示例清单，最终的相似度分数是 `31`（`9 + 4 + 0 + 0 + 9 + 9`）。

Once again consider your left and right lists. What is their similarity score?
> 再次考虑你的左右清单。它们的相似度分数是多少？

Your puzzle answer was `27647262`.

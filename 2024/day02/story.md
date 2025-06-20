# Day 2: Red-Nosed Reports
> 第二天：红鼻子报告

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.
> 幸运的是，历史学家们要搜索的第一个地点离首席历史学家的办公室不远。

While the [Red-Nosed Reindeer nuclear fusion/fission](https://adventofcode.com/2015/day/19) plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.
> 虽然红鼻子驯鹿核聚变/裂变工厂里似乎没有首席历史学家的踪迹，但工程师们一见到你就跑了过来。显然，他们还在谈论鲁道夫通过单个电子分子合成被拯救的那次经历。

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.
> 他们赶紧补充说——既然你已经来了——他们非常希望你能帮忙分析红鼻子反应堆的一些异常数据。你回头看看历史学家们是否在等你，但他们似乎已经分组，正在设施的每个角落搜寻。你于是答应帮忙分析这些异常数据。

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:
> 这些异常数据（你的谜题输入）由许多报告组成，每行一份报告。每份报告是一组用空格分隔的数字，称为等级。例如：

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

This example data contains six reports each containing five levels.
> 这个示例数据包含六份报告，每份报告有五个等级。

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:
> 工程师们正在试图找出哪些报告是安全的。红鼻子反应堆的安全系统只能容忍等级逐渐递增或递减的情况。因此，只有同时满足以下两个条件的报告才算安全：

- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.
> - 等级要么全部递增，要么全部递减。
> - 任意两个相邻等级的差值至少为1，至多为3。

In the example above, the reports can be found safe or unsafe by checking those rules:
> 在上面的示例中，可以通过检查这些规则判断报告是否安全：

- `7 6 4 2 1`: **Safe** because the levels are all decreasing by 1 or 2.
- `1 2 7 8 9`: **Unsafe** because `2 7` is an increase of 5.
- `9 7 6 2 1`: **Unsafe** because `6 2` is a decrease of 4.
- `1 3 2 4 5`: **Unsafe** because `1 3` is increasing but `3 2` is decreasing.
- `8 6 4 4 1`: **Unsafe** because `4 4` is neither an increase or a decrease.
- `1 3 6 7 9`: **Safe** because the levels are all increasing by 1, 2, or 3.
> - `7 6 4 2 1`：**安全**，因为所有等级都在递减，且每次递减1或2。
> - `1 2 7 8 9`：**不安全**，因为`2 7`增加了5。
> - `9 7 6 2 1`：**不安全**，因为`6 2`减少了4。
> - `1 3 2 4 5`：**不安全**，因为`1 3`递增但`3 2`递减。
> - `8 6 4 4 1`：**不安全**，因为`4 4`既不是递增也不是递减。
> - `1 3 6 7 9`：**安全**，因为所有等级都递增1、2或3。

So, in this example, `2` reports are **safe**.
> 所以，在这个例子中，有`2`份报告是**安全**的。

Analyze the unusual data from the engineers. **How many reports are safe?**
> 分析工程师们的异常数据。**有多少份报告是安全的？**

Your puzzle answer was `287`.

## Part Two

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.
> 工程师们对安全报告数量之少感到惊讶，直到他们意识到忘了告诉你有关“问题阻尼器”的事情。

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!
> 问题阻尼器是一个安装在反应堆上的模块，它允许安全系统在本应安全的报告中容忍一个异常等级。就好像这个异常等级从未出现过一样！

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
> 现在，规则和之前一样，只是如果从一份不安全的报告中移除一个等级后能使其变为安全，则该报告也算作安全。

More of the above example's reports are now safe:
> 上述示例中的更多报告现在变得安全了：

- `7 6 4 2 1`: **Safe** without removing any level.
- `1 2 7 8 9`: **Unsafe** regardless of which level is removed.
- `9 7 6 2 1`: **Unsafe** regardless of which level is removed.
- `1 3 2 4 5`: **Safe** by removing the second level, 3.
- `8 6 4 4 1`: **Safe** by removing the third level, 4.
- `1 3 6 7 9`: **Safe** without removing any level.
> - `7 6 4 2 1`：**安全**，无需移除任何等级。
> - `1 2 7 8 9`：**不安全**，无论移除哪个等级都不安全。
> - `9 7 6 2 1`：**不安全**，无论移除哪个等级都不安全。
> - `1 3 2 4 5`：**安全**，移除第二个等级3后安全。
> - `8 6 4 4 1`：**安全**，移除第三个等级4后安全。
> - `1 3 6 7 9`：**安全**，无需移除任何等级。

Thanks to the Problem Dampener, `4` reports are actually **safe**!
> 多亏了问题阻尼器，实际上有`4`份报告是**安全**的！

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
> 更新你的分析，考虑问题阻尼器可以从不安全报告中移除一个等级的情况。现在有多少份报告是安全的？

Your puzzle answer was `354`.

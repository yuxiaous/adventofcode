# Day 4: Ceres Search
> 第四天：谷神星搜寻

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the [Ceres monitoring station](https://adventofcode.com/2019/day/10)!
> “看来首席不在这里。下一个！”一位历史学家拿出一个设备，按下唯一的按钮。短暂的闪光后，你认出这里是谷神星监测站的内部！

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her **word search** (your puzzle input). She only has to find one word: `XMAS`.
> 当寻找首席的行动继续时，住在站里的一个小精灵拉了拉你的衣服；她想知道你能否帮她完成**单词搜索**（你的谜题输入）。她只需要找到一个单词：`XMAS`。

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of `XMAS` - you need to find **all of them**. Here are a few ways `XMAS` might appear, where irrelevant characters have been replaced with `.`:
> 这个单词搜索允许单词以横向、纵向、对角线、反向甚至重叠其他单词的方式出现。不过有点特别，你不仅要找到一个 `XMAS`，而是要找到**所有的**。下面是 `XMAS` 可能出现的几种方式，无关字符已被替换为 `.`：

```
..X...
.SAMX.
.A..A.
XMAS.S
.X....
```

The actual word search will be full of letters instead. For example:
> 实际的单词搜索将全部由字母组成。例如：

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

In this word search, `XMAS` occurs a total of `18` times; here's the same word search again, but where letters not involved in any XMAS have been replaced with `.`:
> 在这个单词搜索中，`XMAS` 总共出现了 `18` 次；下面是同样的单词搜索，但未参与任何 XMAS 的字母已被替换为 `.`：

```
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
```

Take a look at the little Elf's word search. **How many times does XMAS appear?**
> 看看小精灵的单词搜索。**XMAS 出现了多少次？**

Your puzzle answer was `2483`.

## Part Two

The Elf looks quizzically at you. Did you misunderstand the assignment?
> 小精灵看着你。你误解了任务吗？

Looking for the instructions, you flip over the word search to find that this isn't actually an `XMAS` puzzle; it's an `X-MAS` puzzle in which you're supposed to find two `MAS` in the shape of an `X`. One way to achieve that is like this:
> 你翻到单词搜索的背面寻找说明，发现这其实不是一个 `XMAS` 谜题；而是一个 `X-MAS` 谜题，你需要找到以 `X` 形状排列的两个 `MAS`。实现方式之一如下：

```
M.S
.A.
M.S
```

Irrelevant characters have again been replaced with `.` in the above diagram. Within the `X`, each `MAS` can be written forwards or backwards.
> 上图中无关字符再次被替换为 `.`。在这个 `X` 形中，每个 `MAS` 可以正向或反向书写。

Here's the same example from before, but this time all of the `X-MAS`es have been kept instead:
> 下面是之前的同一个例子，但这次只保留了所有的 `X-MAS`：

```
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
```

In this example, an `X-MAS` appears `9` times.
> 在这个例子中，`X-MAS` 出现了 `9` 次。

Flip the word search from the instructions back over to the word search side and try again. **How many times does an X-MAS appear?**
> 把单词搜索翻回正面再试一次。**X-MAS 出现了多少次？**
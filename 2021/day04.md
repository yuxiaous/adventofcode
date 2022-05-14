# [Day 4: Giant Squid](https://adventofcode.com/2021/day/4)

> 第4天：巨型鱿鱼

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you **can** see, however, is a giant squid that has attached itself to the outside of your submarine.

> 你已经下潜到海面以下将近 1.5 公里（差不多一英里）了，深到看不到任何阳光。但是，你**可以**看到一条巨型鱿鱼，它吸附在你的潜艇外部。

Maybe it wants to play [bingo](https://en.wikipedia.org/wiki/Bingo_(American_version))?

> 也许它想玩[宾果游戏](https://zh.wikipedia.org/wiki/美式宾果)？

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is **marked** on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board **wins**. (Diagonals don't count.)

> 宾果游戏在一组由 5x5 个数字组成的网格棋盘上进行。数字随机被选择，在所有出现了被选择数字的棋盘上，将该数字进行**标记**。（数字可能不会出现在所有棋盘上。）如果棋盘上的任何一行或一列的所有数字都被标记了，则该棋盘**获胜**。（对角线不算。）

The submarine has a **bingo subsystem** to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards ([your puzzle input](day04.txt)). For example:

> 潜水艇有一个**宾果游戏子系统**来帮助乘客（目前是你和巨型鱿鱼）打发时间。它会自动生成一组随机顺序的数字用来抽取以及一组随机棋盘（[你的谜题输入](day04.txt)）。例如：

```diff
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
```

After the first five numbers are drawn (`7`, `4`, `9`, `5`, and `11`), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

> 在抽取出前五个数字后（`7`、`4`、`9`、`5` 和 `11`），没有获胜者，棋盘标记如下（这里并排显示以节省空间）：

```diff
22  13  17  11*  0         3  15   0   2  22        14  21  17  24   4*
 8   2  23   4* 24         9* 18  13  17   5*       10  16  15   9* 19
21   9* 14  16   7*       19   8   7* 25  23        18   8  23  26  20
 6  10   3  18   5*       20  11* 10  24   4*       22  11* 13   6   5*
 1  12  20  15  19        14  21  16  12   6         2   0  12   3   7*
```

After the next six numbers are drawn (`17`, `23`, `2`, `0`, `14`, and `21`), there are still no winners:

> 在抽取出接下来的六个数字后（`17`、`23`、`2`、`0`、`14` 和 `21`），仍然没有获胜者：

```diff
22  13  17* 11*  0*        3  15   0*  2* 22        14* 21* 17* 24   4*
 8   2* 23*  4* 24         9* 18  13  17*  5*       10  16  15   9* 19
21*  9* 14* 16   7*       19   8   7* 25  23*       18   8  23* 26  20
 6  10   3  18   5*       20  11* 10  24   4*       22  11* 13   6   5*
 1  12  20  15  19        14* 21* 16  12   6         2*  0* 12   3   7*
 ```

Finally, `24` is drawn:

> 最后，抽取出了`24`：

```diff
22  13  17* 11*  0*        3  15   0*  2* 22        14* 21* 17* 24*  4*
 8   2* 23*  4* 24*        9* 18  13  17*  5*       10  16  15   9* 19
21*  9* 14* 16   7*       19   8   7* 25  23*       18   8  23* 26  20
 6  10   3  18   5*       20  11* 10  24*  4*       22  11* 13   6   5*
 1  12  20  15  19        14* 21* 16  12   6         2*  0* 12   3   7*
 ```

At this point, the third board **wins** because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: **`14 21 17 24 4`**).

> 就在此刻，第三个棋盘**获胜**了，因为它至少有一个完整的标记了数字的行或列（在这个例子中，顶层的整行数字都被标记了：**`14 21 17 24 4`**）。

The **score** of the winning board can now be calculated. Start by finding the **sum of all unmarked numbers** on that board; in this case, the sum is 188. Then, multiply that sum by **the number that was just called** when the board won, 24, to get the final score, `188 * 24 =` **`4512`**.

> 现在可以计算获胜棋盘的**分数**。首先，算出该棋盘上所有未标记数字的**总和**，在这个例子中总和是 188。然后，将该总和与**棋盘获胜时所叫到的数字**(24)相乘，得到最终得分，`188 * 24 =` **`4512`**。

To guarantee victory against the giant squid, figure out which board will win first. **What will your final score be if you choose that board?**

> 为了确保战胜巨型鱿鱼，先弄清楚哪块棋盘将获得获胜。**如果你选择这块棋盘，你的最终得分是多少？**

Your puzzle answer was `60368`.

## --- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

> 另一方面，尝试不同的策略可能是明智的：让巨型鱿鱼获胜。

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to **figure out which board will win last** and choose that one. That way, no matter which boards it picks, it will win for sure.

> 你不确定一只巨型鱿鱼可以同时玩多少个宾果棋盘，所以与其浪费时间数它的触手，更安全的做法是**弄清楚哪个棋盘会最后获胜**，并且选择那个棋盘。这样，无论它选择哪块棋盘，它都会赢。

In the above example, the second board is the last to win, which happens after `13` is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to `148` for a final score of `148 * 13 =` **`1924`**.

> 在上面的例子中，当 `13` 被叫到时，第二块棋盘中间那列被完全标记，最终它是最后一个获胜的棋盘。如果你一直玩到这一刻，第二块棋盘的未标记数字的总和是 `148`，最终得分为 `148 * 13 =` **`1924`**。

Figure out which board will win last. **Once it wins, what would its final score be?**

> 找出哪个棋盘最后获胜。**一旦获胜，它的最终得分是多少？**

Your puzzle answer was `17435`.

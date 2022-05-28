# [Day 21: Dirac Dice](https://adventofcode.com/2021/day/21)

> 第21天：狄拉克骰子

There's not much to do as you slowly descend to the bottom of the ocean. The submarine computer challenges you to a nice game of **Dirac Dice**.

> 你慢慢的向海底下降，此时无事可做。潜水艇计算机向你发起**狄拉克骰子**的游戏挑战。

This game consists of a single [die](https://en.wikipedia.org/wiki/Dice), two [pawns](https://en.wikipedia.org/wiki/Glossary_of_board_games#piece), and a game board with a circular track containing ten spaces marked `1` through `10` clockwise. Each player's **starting space** is chosen randomly ([your puzzle input](day21.txt)). Player 1 goes first.

> 这个游戏由一个[骰子](https://en.wikipedia.org/wiki/Dice)、两个[棋子](https://en.wikipedia.org/wiki/Glossary_of_board_games#piece)和一个带有圆形轨道的游戏棋盘组成，其中包含顺时针标记为 `1` 到 `10` 的十个空格。每个玩家的**起始位置**是随机选择的（[你的谜题输入](day21.txt)）。玩家 1 先开始。

Players take turns moving. On each player's turn, the player rolls the die **three times** and adds up the results. Then, the player moves their pawn that many times **forward** around the track (that is, moving clockwise on spaces in order of increasing value, wrapping back around to `1` after `10`). So, if a player is on space `7` and they roll `2`, `2`, and `1`, they would move forward 5 times, to spaces `8`, `9`, `10`, `1`, and finally stopping on `2`.

> 玩家轮流移动。在每个玩家的回合中，玩家掷 **3 次**骰子并将结果相加。然后，玩家在轨道上**向前**移动他们的棋子相应次数（即，在顺时针方向上按数字从小到大移动，越过 `10` 之后返回到 `1`）。因此，如果一个玩家在位置 `7` 上，并且他掷了 `2`、`2` 和 `1`，他将向前移动 5 次，经过位置 `8`、`9`、`10`、`1`，最后停在位置 `2` 上。

After each player moves, they increase their **score** by the value of the space their pawn stopped on. Players' scores start at `0`. So, if the first player starts on space `7` and rolls a total of `5`, they would stop on space `2` and add `2` to their score (for a total score of `2`). The game immediately ends as a win for any player whose score reaches **at least `1000`**.

> 在每个玩家移动之后，将他们的棋子停留的位置的值增加到他们的**得分**里。玩家的分数从 `0` 开始。因此，如果第一个玩家从位置 `7` 开始并总共掷出了 `5`，他将停在位置 `2` 上，并将他的得分加 `2`（总得分为 `2`）。当任何一个玩家的得分率先达到 **`1000`** 分时，他将赢得游戏并结束游戏。

Since the first game is a practice game, the submarine opens a compartment labeled **deterministic dice** and a 100-sided die falls out. This die always rolls `1` first, then `2`, then `3`, and so on up to `100`, after which it starts over at `1` again. Play using this die.

> 由于第一场游戏是练习游戏，潜水艇开了一个标有**确定性骰子**的房间，掉出了一个 100 面的骰子。这个骰子会先掷出 `1`，然后是 `2`，接着是 `3`，依此类推直到 `100`，之后又从 `1` 重新开始。这场先用这个骰子玩。

For example, given these starting positions:

> 例如，给定这样的起始位置：

```'
Player 1 starting position: 4
Player 2 starting position: 8
```

This is how the game would go:

> 这就是游戏的进行过程：

- Player 1 rolls `1`+`2`+`3` and moves to space `10` for a total score of `10`.
- Player 2 rolls `4`+`5`+`6` and moves to space `3` for a total score of `3`.
- Player 1 rolls `7`+`8`+`9` and moves to space `4` for a total score of `14`.
- Player 2 rolls `10`+`11`+`12` and moves to space `6` for a total score of `9`.
- Player 1 rolls `13`+`14`+`15` and moves to space `6` for a total score of `20`.
- Player 2 rolls `16`+`17`+`18` and moves to space `7` for a total score of `16`.
- Player 1 rolls `19`+`20`+`21` and moves to space `6` for a total score of `26`.
- Player 2 rolls `22`+`23`+`24` and moves to space `6` for a total score of `22`.

> - 玩家 1 掷出 `1`+`2`+`3` 并移动到位置 `10`，总得分为 `10`。
> - 玩家 2 掷出 `4`+`5`+`6` 并移动到位置 `3`，总得分为 `3`。
> - 玩家 1 掷出 `7`+`8`+`9` 并移动到位置 `4`，总得分为 `14`。
> - 玩家 2 掷出 `10`+`11`+`12` 并移动到位置 `6`，总得分为 `9`。
> - 玩家 1 掷出 `13`+`14`+`15` 并移动到位置 `6`，总得分为 `20`。
> - 玩家 2 掷出 `16`+`17`+`18` 并移动到位置 `7`，总得分为 `16`。
> - 玩家 1 掷出 `19`+`20`+`21` 并移动到位置 `6`，总得分为 `26`。
> - 玩家 2 掷出 `22`+`23`+`24` 并移动到位置 `6`，总得分为 `22`。

...after many turns...

> ……转许多回合之后……

- Player 2 rolls `82`+`83`+`84` and moves to space `6` for a total score of `742`.
- Player 1 rolls `85`+`86`+`87` and moves to space `4` for a total score of `990`.
- Player 2 rolls `88`+`89`+`90` and moves to space `3` for a total score of `745`.
- Player 1 rolls `91`+`92`+`93` and moves to space `10` for a final score, `1000`.

> - 玩家 2 掷出 `82`+`83`+`84` 并移动到位置 `6`，总得分为 `742`。
> - 玩家 1 掷出 `85`+`86`+`87` 并移动到位置 `4`，总得分为 `990`。
> - 玩家 2 掷出 `88`+`89`+`90` 并移动到位置 `3`，总得分为 `745`。
> - 玩家 1 掷出 `91`+`92`+`93` 并移动到位置 `10` 获得最终得分：`1000`。

Since player 1 has at least `1000` points, player 1 wins and the game ends. At this point, the losing player had `745` points and the die had been rolled a total of `993` times; `745 * 993 =` **`739785`**.

> 由于玩家 1 拥有至少 `1000` 分，所以玩家 1 获胜并且结束游戏。此时，输家有 `745` 分，骰子总共掷了 `993` 次： `745 * 993 =` **`739785`**。

Play a practice game using the deterministic 100-sided die. The moment either player wins, **what do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?**

> 使用 100 面的确定性骰子玩一场练习游戏。当任一玩家获胜时，**如果将失败玩家的分数乘以游戏中掷骰子的次数，你会得到什么？**

Your puzzle answer was `918081`.

# Day 2: Rock Paper Scissors

> 第2天：剪刀石头布

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant [Rock Paper Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) tournament is already in progress.

> 精灵们开始在海滩上安营扎寨。为了决定谁的帐篷离点心储藏室最近，一场巨大的[剪刀石头布](https://en.wikipedia.org/wiki/Rock_paper_scissors)比赛正在进行中。

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

> 剪刀石头布是两个玩家之间的游戏。每次游戏包含多个回合，在每一回合中，每个玩家同时使用手的形状选择石头、布或剪刀中的一个。然后，选出该回合的获胜者：石头打败剪刀，剪刀打败布，布打败石头。如果两位玩家选择相同的形状，则该回合以平局结束。

Appreciative of your help yesterday, one Elf gives you an **encrypted strategy guide** ([your puzzle input](day02.txt)) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

> 为了感谢你昨天的帮助，一个精灵给了你一份**加密的策略指南**（[你的谜题输入](day02.txt)），他们说这一定会帮助你获胜。 “第一列是你的对手将要出的东西：A 是石头，B 是布，C 是剪刀。第二列——” 突然，这个精灵被叫去帮忙搭其他人的帐篷了。

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

> 第二列，你想，一定是你应该出的对策：X 是石头，Y 是布，Z 是剪刀。每次都赢将会很可疑，所以对策必须经过仔细选择的。

The winner of the whole tournament is the player with the highest score. Your **total score** is the sum of your scores for each round. The score for a single round is the score for the **shape you selected** (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the **outcome of the round** (0 if you lost, 3 if the round was a draw, and 6 if you won).

> 整场比赛的获胜者是得分最高的玩家。你的**总分**是你每回合得分的总和。单个回合的分数是**你选择的形状**的分数（石头是 1 分，布是 2 分，剪刀是 3 分）加上**该回合结果**的分数（输了是 0 分, 平局是 3 分，赢了是 6 分）。

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

> 由于你无法确定那个精灵是想帮助你还是欺骗你，因此你应该计算按照策略指南会得到的分数。

For example, suppose you were given the following strategy guide:

举个例子，假设你获得的策略指南如下：

```'
A Y
B X
C Z
```

This strategy guide predicts and recommends the following:

- In the first round, your opponent will choose Rock (`A`), and you should choose Paper (`Y`). This ends in a win for you with a score of **8** (2 because you chose Paper + 6 because you won).
- In the second round, your opponent will choose Paper (`B`), and you should choose Rock (`X`). This ends in a loss for you with a score of **1** (1 + 0).
- The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = **6**.

> 本战略指南预测并推荐以下内容：
>
> - 在第一回合中，你的对手会选择石头（`A`），而你应该选择布（`Y`）。你将赢得 **8** 分（2 分因为你选择了布 + 6 分因为你赢了）。
> - 在第二回合中，你的对手会选择布（`B`），你应该选择石头（`X`）。结果是你输了，得 **1** 分(1 + 0)。
> - 第三回合平局，双方都选择剪刀，得分为 3 + 3 = **6**。

In this example, if you were to follow the strategy guide, you would get a total score of **`15`** (8 + 1 + 6).

> 在这个例子中，如果你遵循策略指南，你将获得 **`15`** (8 + 1 + 6) 的总分。

**What would your total score be if everything goes exactly according to your strategy guide?**

**如果一切都完全按照你的策略指南进行，你的总分是多少？**

Your puzzle answer was `15422`.

## Part Two

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: `X` means you need to lose, `Y` means you need to end the round in a draw, and `Z` means you need to win. Good luck!"

> 精灵完成了搭帐篷的帮助然后偷偷回到你身边。“不管怎样，第二列说明了本回合比赛需要如何结束：`X` 表示你需要输，`Y` 表示你需要以平局结束本回合比赛，而 `Z` 表示你需要获胜。祝你好运！“

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

- In the first round, your opponent will choose Rock (`A`), and you need the round to end in a draw (`Y`), so you also choose Rock. This gives you a score of 1 + 3 = **4**.
- In the second round, your opponent will choose Paper (`B`), and you choose Rock so you lose (`X`) with a score of 1 + 0 = **1**.
- In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = **7**.

> 仍然以相同的方式计算总分，但现在你需要弄清楚要选择什么形状，以便按照指示结束回合。上面的例子现在是这样的：
>
> - 在第一回合中，你的对手会选择石头（`A`），而你需要以平局结束（`Y`），所以你也选择石头。你的得分是 1 + 3 = **4**。
> - 在第二回合中，你的对手将选择布 (`B`)，所以你选择石头，你将输掉(`X`)并得 1 + 0 = **1** 分 。
> - 在第三回合中，你将以石头击败对手的剪刀，得 1 + 6 = **7** 分。

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of **`12`**.

> 现在你已经正确解密了超绝密攻略，你将获得 **`12`** 分的总分。

Following the Elf's instructions for the second column, **what would your total score be if everything goes exactly according to your strategy guide?**

> 按照精灵关于第二列的解释，**如果一切都完全按照你的策略指南进行，你的总分是多少？**

Your puzzle answer was `15442`.

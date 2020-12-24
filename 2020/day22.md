# Day 22: Crab Combat

> 第二十二天：螃蟹战斗

It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of [space cards](https://adventofcode.com/2019/day/22)! You'd like to play a game of **Combat**, and there's even an opponent available: a small crab that climbed aboard your raft before you left.

> 木筏在海洋上航行了几个小时后，你便陷入了无聊之中。幸运的是，你带来了一组[太空卡](https://adventofcode.com/2019/day/22)！你打算玩一个战斗游戏，这时甚至还出现了一个对手：一条小螃蟹爬上了木筏。

Fortunately, it doesn't take long to teach the crab the rules.

> 幸运的是，你没花多长时间就教会螃蟹游戏规则。

Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of **rounds**: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.

> 在游戏开始之前，先将分发卡牌，所以每个玩家都有自己的牌组（你的谜题输入）。然后，游戏由一系列的回合组成：两名玩家都亮出自己最上方的牌，牌面点数大的一方将赢得本轮。获胜者拿走两张牌，将它们放在自己牌组的底部，所以获胜者的牌会比对手多。当一个玩家获得了所有卡牌时他就赢了，并且游戏结束。

For example, consider the following starting decks:

> 举个例子，假设有下列初始牌组：

```'
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
```

This arrangement means that player 1's deck contains 5 cards, with `9` on top and `1` on the bottom; player 2's deck also contains 5 cards, with `5` on top and `10` on the bottom.

> 这表示玩家 1 的牌组中有 5 张牌，`9` 在顶部 `1` 在底部。玩家 2 的牌组也有 5 张牌，`5` 在顶部，`10` 底部。

The first round begins with both players drawing the top card of their decks: `9` and `5`. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that `9` is above `5`. In total, it takes 29 rounds before a player has all of the cards:

> 第一回合开始时，两个玩家都出了自己牌组最上面一张牌：`9` 和 `5`。玩家 1 的牌面点数较大，因此两张卡牌都收至玩家 1 的牌组底部，并且 `9` 在上方，`5` 在下方。总共经过 29 回合后，一个玩家获得了所有卡牌：

```'
-- Round 1 --
Player 1's deck: 9, 2, 6, 3, 1
Player 2's deck: 5, 8, 4, 7, 10
Player 1 plays: 9
Player 2 plays: 5
Player 1 wins the round!

-- Round 2 --
Player 1's deck: 2, 6, 3, 1, 9, 5
Player 2's deck: 8, 4, 7, 10
Player 1 plays: 2
Player 2 plays: 8
Player 2 wins the round!

-- Round 3 --
Player 1's deck: 6, 3, 1, 9, 5
Player 2's deck: 4, 7, 10, 8, 2
Player 1 plays: 6
Player 2 plays: 4
Player 1 wins the round!

-- Round 4 --
Player 1's deck: 3, 1, 9, 5, 6, 4
Player 2's deck: 7, 10, 8, 2
Player 1 plays: 3
Player 2 plays: 7
Player 2 wins the round!

-- Round 5 --
Player 1's deck: 1, 9, 5, 6, 4
Player 2's deck: 10, 8, 2, 7, 3
Player 1 plays: 1
Player 2 plays: 10
Player 2 wins the round!

...several more rounds pass...

-- Round 27 --
Player 1's deck: 5, 4, 1
Player 2's deck: 8, 9, 7, 3, 2, 10, 6
Player 1 plays: 5
Player 2 plays: 8
Player 2 wins the round!

-- Round 28 --
Player 1's deck: 4, 1
Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
Player 1 plays: 4
Player 2 plays: 9
Player 2 wins the round!

-- Round 29 --
Player 1's deck: 1
Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
Player 1 plays: 1
Player 2 plays: 7
Player 2 wins the round!


== Post-game results ==
Player 1's deck: 
Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1
```

Once the game ends, you can calculate the winning player's **score**. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:

> 游戏结束后，你需要计算获胜者的得分。牌组中最下面的一张牌的分值等于该牌的点数乘以 1，倒数第二张牌的分值等于该牌的点数乘以 2，依此类推。对于 10 张卡牌，最上面的卡牌的分值等于卡牌的点数乘以 10。在这个例子中，获胜者的得分为：

```'
   3 * 10
+  2 *  9
+ 10 *  8
+  6 *  7
+  8 *  6
+  5 *  5
+  9 *  4
+  4 *  3
+  7 *  2
+  1 *  1
= 306
```

So, once the game ends, the winning player's score is **`306`**.

> 因此，当游戏结束后，获胜玩家的得分是 **`306`**。

Play the small crab in a game of Combat using the two decks you just dealt. **What is the winning player's score?**

> 使用你刚刚处理过的两组卡牌跟小螃蟹一起玩战斗游戏。获胜玩家的得分是多少？

Your puzzle answer was `33010`.

--- Part Two ---

You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of **Recursive Combat**.

> 你输给了小螃蟹！幸运的是，螃蟹并不擅长递归。为了捍卫你作为竹筏船长的荣誉，你向小螃蟹发起**递归战斗**的游戏挑战。

Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of **rounds** with a few changes:

- Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the **game** instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
- Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
- If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
- Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.

> 递归战斗仍然是通过将牌分为两组开始的（你可以像之前一样使用相同的起始牌组进行游戏——这很公平）。然后，游戏由一系列的回合组成，但有一些变化：
>
> - 在玩家出牌之前，如果之前某一轮游戏的牌组恰好与当前牌组满足条件：相同的玩家、相同的顺序、相同的卡牌，则玩家 1 胜利，游戏立即结束。这里不考虑其他某次的游戏。（这是为了防止了无止境的递归战斗，但是每个人都认为这是一个坏主意。）
> - 否则，该回合的卡牌必须是全新的组合。回合开始后，玩家每回合都按照正常方式抽出牌组中最上面的卡牌。
> - 如果两个玩家牌组中剩余的卡牌数量都同时大于等于自己刚出的牌的点数，则该轮的获胜者通过玩一局新的递归战斗游戏来确定（见下文）。
> - 否则，如果至少一名玩家的牌堆中没有足够的卡牌来递归，则该回合的获胜者是出牌点数较高的玩家。

As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again so that the winner's card is above the other card). Note that the winner's card might be **the lower-valued of the two cards** if they won the round due to winning a sub-game. If collecting cards by winning the round causes a player to have all of the cards, they win, and the game ends.

> 与战斗游戏一样，回合的获胜者（即使他是通过赢得子游戏而赢得这个回合的）将在回合开始时获得两张牌，并将它们放在自己牌组的底部（同样，优胜者的卡牌位于另一张卡牌的上方）。注意，如果获胜者是通过赢得了子游戏而赢得回合的，则他的卡牌有可能是两张卡牌中点数较小的那张。当玩家赢得了所有卡牌时就获胜了，然后游戏结束。

Here is an example of a small game that would loop forever without the infinite game prevention rule:

> 这是一个小游戏的例子，如果没有无限游戏预防规则，它将永久循环下去：

```'
Player 1:
43
19

Player 2:
2
29
14
```

During a round of Recursive Combat, if both players have at least as many cards in their own decks as the number on the card they just dealt, the winner of the round is determined by recursing into a sub-game of Recursive Combat. (For example, if player 1 draws the `3` card, and player 2 draws the `7` card, this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left, not counting the `3` and `7` cards that were drawn.)

> 在一回合的递归战斗中，如果两个玩家牌组中剩余的卡牌数量都同时大于等于自己刚出的牌的点数，则该轮的获胜者将通过进入递归战斗子游戏来确定。（例如，如果玩家 1 出牌 `3`，玩家 2 出牌 `7`，在不包含刚出牌的 `3` 和 `7` 的情况下，玩家 1 至少有 3 张牌，玩家 2 至少有 7 张牌。）

To play a sub-game of Recursive Combat, each player creates a new deck by making a **copy** of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be **copies** of the next three cards in their deck.)

> 玩递归战斗的子游戏，每位玩家通过复制自己牌组中剩余的卡牌来创建一个新牌组（复制的卡牌数量等于他们出牌后触发子游戏时的卡牌数量）。进行子游戏时，触发它的主游戏处于暂停状态，并且完全不受子游戏影响。子游戏结束后不会从玩家的牌组中移除任何卡牌。（例如，如果玩家 1 出牌 3，则子游戏中的牌组将是当前牌组中剩下的三张卡牌的副本。）

Here is a complete example of gameplay, where `Game 1` is the primary game of Recursive Combat:

> 这是一个完整的游戏例子，其中 `Game 1` 是递归战斗的主游戏：

```'
=== Game 1 ===

-- Round 1 (Game 1) --
Player 1's deck: 9, 2, 6, 3, 1
Player 2's deck: 5, 8, 4, 7, 10
Player 1 plays: 9
Player 2 plays: 5
Player 1 wins round 1 of game 1!

-- Round 2 (Game 1) --
Player 1's deck: 2, 6, 3, 1, 9, 5
Player 2's deck: 8, 4, 7, 10
Player 1 plays: 2
Player 2 plays: 8
Player 2 wins round 2 of game 1!

-- Round 3 (Game 1) --
Player 1's deck: 6, 3, 1, 9, 5
Player 2's deck: 4, 7, 10, 8, 2
Player 1 plays: 6
Player 2 plays: 4
Player 1 wins round 3 of game 1!

-- Round 4 (Game 1) --
Player 1's deck: 3, 1, 9, 5, 6, 4
Player 2's deck: 7, 10, 8, 2
Player 1 plays: 3
Player 2 plays: 7
Player 2 wins round 4 of game 1!

-- Round 5 (Game 1) --
Player 1's deck: 1, 9, 5, 6, 4
Player 2's deck: 10, 8, 2, 7, 3
Player 1 plays: 1
Player 2 plays: 10
Player 2 wins round 5 of game 1!

-- Round 6 (Game 1) --
Player 1's deck: 9, 5, 6, 4
Player 2's deck: 8, 2, 7, 3, 10, 1
Player 1 plays: 9
Player 2 plays: 8
Player 1 wins round 6 of game 1!

-- Round 7 (Game 1) --
Player 1's deck: 5, 6, 4, 9, 8
Player 2's deck: 2, 7, 3, 10, 1
Player 1 plays: 5
Player 2 plays: 2
Player 1 wins round 7 of game 1!

-- Round 8 (Game 1) --
Player 1's deck: 6, 4, 9, 8, 5, 2
Player 2's deck: 7, 3, 10, 1
Player 1 plays: 6
Player 2 plays: 7
Player 2 wins round 8 of game 1!

-- Round 9 (Game 1) --
Player 1's deck: 4, 9, 8, 5, 2
Player 2's deck: 3, 10, 1, 7, 6
Player 1 plays: 4
Player 2 plays: 3
Playing a sub-game to determine the winner...

=== Game 2 ===

-- Round 1 (Game 2) --
Player 1's deck: 9, 8, 5, 2
Player 2's deck: 10, 1, 7
Player 1 plays: 9
Player 2 plays: 10
Player 2 wins round 1 of game 2!

-- Round 2 (Game 2) --
Player 1's deck: 8, 5, 2
Player 2's deck: 1, 7, 10, 9
Player 1 plays: 8
Player 2 plays: 1
Player 1 wins round 2 of game 2!

-- Round 3 (Game 2) --
Player 1's deck: 5, 2, 8, 1
Player 2's deck: 7, 10, 9
Player 1 plays: 5
Player 2 plays: 7
Player 2 wins round 3 of game 2!

-- Round 4 (Game 2) --
Player 1's deck: 2, 8, 1
Player 2's deck: 10, 9, 7, 5
Player 1 plays: 2
Player 2 plays: 10
Player 2 wins round 4 of game 2!

-- Round 5 (Game 2) --
Player 1's deck: 8, 1
Player 2's deck: 9, 7, 5, 10, 2
Player 1 plays: 8
Player 2 plays: 9
Player 2 wins round 5 of game 2!

-- Round 6 (Game 2) --
Player 1's deck: 1
Player 2's deck: 7, 5, 10, 2, 9, 8
Player 1 plays: 1
Player 2 plays: 7
Player 2 wins round 6 of game 2!
The winner of game 2 is player 2!

...anyway, back to game 1.
Player 2 wins round 9 of game 1!

-- Round 10 (Game 1) --
Player 1's deck: 9, 8, 5, 2
Player 2's deck: 10, 1, 7, 6, 3, 4
Player 1 plays: 9
Player 2 plays: 10
Player 2 wins round 10 of game 1!

-- Round 11 (Game 1) --
Player 1's deck: 8, 5, 2
Player 2's deck: 1, 7, 6, 3, 4, 10, 9
Player 1 plays: 8
Player 2 plays: 1
Player 1 wins round 11 of game 1!

-- Round 12 (Game 1) --
Player 1's deck: 5, 2, 8, 1
Player 2's deck: 7, 6, 3, 4, 10, 9
Player 1 plays: 5
Player 2 plays: 7
Player 2 wins round 12 of game 1!

-- Round 13 (Game 1) --
Player 1's deck: 2, 8, 1
Player 2's deck: 6, 3, 4, 10, 9, 7, 5
Player 1 plays: 2
Player 2 plays: 6
Playing a sub-game to determine the winner...

=== Game 3 ===

-- Round 1 (Game 3) --
Player 1's deck: 8, 1
Player 2's deck: 3, 4, 10, 9, 7, 5
Player 1 plays: 8
Player 2 plays: 3
Player 1 wins round 1 of game 3!

-- Round 2 (Game 3) --
Player 1's deck: 1, 8, 3
Player 2's deck: 4, 10, 9, 7, 5
Player 1 plays: 1
Player 2 plays: 4
Playing a sub-game to determine the winner...

=== Game 4 ===

-- Round 1 (Game 4) --
Player 1's deck: 8
Player 2's deck: 10, 9, 7, 5
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 1 of game 4!
The winner of game 4 is player 2!

...anyway, back to game 3.
Player 2 wins round 2 of game 3!

-- Round 3 (Game 3) --
Player 1's deck: 8, 3
Player 2's deck: 10, 9, 7, 5, 4, 1
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 3 of game 3!

-- Round 4 (Game 3) --
Player 1's deck: 3
Player 2's deck: 9, 7, 5, 4, 1, 10, 8
Player 1 plays: 3
Player 2 plays: 9
Player 2 wins round 4 of game 3!
The winner of game 3 is player 2!

...anyway, back to game 1.
Player 2 wins round 13 of game 1!

-- Round 14 (Game 1) --
Player 1's deck: 8, 1
Player 2's deck: 3, 4, 10, 9, 7, 5, 6, 2
Player 1 plays: 8
Player 2 plays: 3
Player 1 wins round 14 of game 1!

-- Round 15 (Game 1) --
Player 1's deck: 1, 8, 3
Player 2's deck: 4, 10, 9, 7, 5, 6, 2
Player 1 plays: 1
Player 2 plays: 4
Playing a sub-game to determine the winner...

=== Game 5 ===

-- Round 1 (Game 5) --
Player 1's deck: 8
Player 2's deck: 10, 9, 7, 5
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 1 of game 5!
The winner of game 5 is player 2!

...anyway, back to game 1.
Player 2 wins round 15 of game 1!

-- Round 16 (Game 1) --
Player 1's deck: 8, 3
Player 2's deck: 10, 9, 7, 5, 6, 2, 4, 1
Player 1 plays: 8
Player 2 plays: 10
Player 2 wins round 16 of game 1!

-- Round 17 (Game 1) --
Player 1's deck: 3
Player 2's deck: 9, 7, 5, 6, 2, 4, 1, 10, 8
Player 1 plays: 3
Player 2 plays: 9
Player 2 wins round 17 of game 1!
The winner of game 1 is player 2!


== Post-game results ==
Player 1's deck: 
Player 2's deck: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3
```

After the game, the winning player's score is calculated from the cards they have in their original deck using the same rules as regular Combat. In the above game, the winning player's score is **`291`**.

> 游戏结束后，获胜者的得分是根据他们在原始牌组中拥有的卡牌计算得出的，使用的规则与常规战斗相同。在上面的游戏中，获胜玩家的分数是 **`291`**。

Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same two decks as before. **What is the winning player's score?**

> 为了捍卫你作为竹筏船长的荣誉，使用与以前相同的两个牌组跟小螃蟹进行递归战斗游戏。获胜玩家的得分是多少？

Your puzzle answer was `32769`.

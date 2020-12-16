# Day 15: Rambunctious Recitation

> 第十五天：夸张报数

You catch the airport shuttle and try to book a new flight to your vacation island. Due to the storm, all direct flights have been cancelled, but a route is available to get around the storm. You take it.

> 你乘坐机场班车，然后尝试预订前往度假岛的新航班。由于暴风雨，所有直飞航班都已取消，但是你觉得还有一条路线可以绕过暴风雨。

While you wait for your flight, you decide to check in with the Elves back at the North Pole. They're playing a **memory game** and are ever so excited to explain the rules!

> 在等待航班的同时，你决定向返回北极的精灵们报平安。他们正在玩一种记忆游戏，非常兴奋向你解释游戏规则！

In this game, the players take turns saying **numbers**. They begin by taking turns reading from a list of **starting numbers** ([your puzzle input](day15.txt)). Then, each turn consists of considering the **most recently spoken number**:

- If that was the **first** time the number has been spoken, the current player says **`0`**.
- Otherwise, the number had been spoken before; the current player announces **how many turns apart** the number is from when it was previously spoken.

> 在这个游戏中，玩家轮流说数字。他们首先从一串含有起始数字（[你的谜题输入](day15.txt)）的列表中开始轮流读数。然后，每个回合考虑最近一次的读数：
>
> - 如果这个数是第一次出现，当前玩家应当说 **`0`**。
> - 如果这个数之前已经说过了，当前玩家应当说出上一次说这个数时与现在所间隔的回合数。

So, after the starting numbers, each turn results in that player speaking aloud either **`0`** (if the last number is new) or an **age** (if the last number is a repeat).

> 所以，在起始数字之后，每个回合的结果是当前玩家大声说出 **`0`**（如果上一个数字是第一次出现）或 **年龄**（如果上一个数字已经出现过了）。

For example, suppose the starting numbers are `0,3,6`:

- **Turn 1**: The `1`st number spoken is a starting number, **`0`**.
- **Turn 2**: The `2`nd number spoken is a starting number, **`3`**.
- **Turn 3**: The `3`rd number spoken is a starting number, **`6`**.
- **Turn 4**: Now, consider the last number spoken, `6`. Since that was the first time the number had been spoken, the `4`th number spoken is **`0`**.
- **Turn 5**: Next, again consider the last number spoken, `0`. Since it **had** been spoken before, the next number to speak is the difference between the turn number when it was last spoken (the previous turn, `4`) and the turn number of the time it was most recently spoken before then (turn `1`). Thus, the 5th number spoken is `4 - 1`, **`3`**.
- **Turn 6**: The last number spoken, `3` had also been spoken before, most recently on turns `5` and `2`. So, the `6`th number spoken is `5 - 2`, **`3`**.
- **Turn 7**: Since `3` was just spoken twice in a row, and the last two turns are `1` turn apart, the `7`th number spoken is **`1`**.
- **Turn 8**: Since `1` is new, the `8`th number spoken is **`0`**.
- **Turn 9**: `0` was last spoken on turns `8` and `4`, so the `9`th number spoken is the difference between them, **`4`**.
- **Turn 10**: `4` is new, so the `10`th number spoken is **`0`**.

> 举个例子，假设起始数字为 `0,3,6`：
>
> - 第 1 回合：第 1 个说出的数字是一个起始数字 **`0`**。
> - 第 2 回合：第 2 个说出的数字是一个起始数字 **`3`**。
> - 第 3 回合：第 3 个说出的数字是一个起始数字 **`6`**。
> - 第 4 回合：现在，考虑上一个说出的数字 `6`。由于这是第一次说出该数字，所以第 4 个说出的数字是 **`0`**。
> - 第 5 回合：接下来，再次考虑上一个说出的数字 `0`。由于之前已经说过了，因此下一个要说的数字是最近一次说出的回合数（上一回合 `4`）与这之前一次说出的回合数（回合 `1`）之间的差值。因此，第 5 个说出的数字是 `4 - 1`，即 **`3`**。
> - 第 6 回合：上一个说出的数字 `3`，之前也已经说过了，最近的回合数是 `5` 和 `2`。所以第 6 个说出的数字是 `5 - 2`，即 **`3`**。
> - 第 7 回合：由于 `3` 连续说了两次，而且最后两回合的间隔是 `1` 回合，所以第 7 个说出的数字是 **`1`**。
> - 第 8 回合：由于 `1` 是新的，所以第 8 个说出的数字是 **`0`**。
> - 第 9 回合：`0` 最近说出的回合数是 `8` 和 `4`，因此第 9 个说出的数字是两者之间的差值，即 **`4`**。
> - 第 10 回合：`4` 是新的，因此第 10 个说出的数字是 **`0`**。

(The game ends when the Elves get sick of playing or dinner is ready, whichever comes first.)

> （游戏将在精灵玩累了或晚餐准备好了时结束，这取决于哪个先到。）

Their question for you is: what will be the **`2020`th** number spoken? In the example above, the `2020`th number spoken will be `436`.

> 他们给你的问题是：第 2020 个说出的数字是多少？在上面的例子中，第 2020 个说出的数字是 `436`。

Here are a few more examples:

- Given the starting numbers `1,3,2`, the `2020`th number spoken is `1`.
- Given the starting numbers `2,1,3`, the `2020`th number spoken is `10`.
- Given the starting numbers `1,2,3`, the `2020`th number spoken is `27`.
- Given the starting numbers `2,3,1`, the `2020`th number spoken is `78`.
- Given the starting numbers `3,2,1`, the `2020`th number spoken is `438`.
- Given the starting numbers `3,1,2`, the `2020`th number spoken is `1836`.

> 这里有一些更多的例子：
>
> - 给定起始数字 `1,3,2`，则第 2020 个说出的数字是 `1`。
> - 给定起始数字 `2,1,3`，则第 2020 个说出的数字是 `10`。
> - 给定起始数字 `1,2,3`，则第 2020 个说出的数字是 `27`。
> - 给定起始数字 `2,3,1`，则第 2020 个说出的数字是 `78`。
> - 给定起始数字 `3,2,1`，则第 2020 个说出的数字是 `438`。
> - 给定起始数字 `3,1,2`，则第 2020 个说出的数字是 `1836`。

Given your starting numbers, **what will be the `2020`th number spoken?**

> 使用给你的起始数字，第 `2020` 个说出的数字是什么？

Your puzzle answer was `1373`.

## --- Part Two ---

Impressed, the Elves issue you a challenge: determine the `30000000`th number spoken. For example, given the same starting numbers as above:

- Given `0,3,6`, the `30000000`th number spoken is `175594`.
- Given `1,3,2`, the `30000000`th number spoken is `2578`.
- Given `2,1,3`, the `30000000`th number spoken is `3544142`.
- Given `1,2,3`, the `30000000`th number spoken is `261214`.
- Given `2,3,1`, the `30000000`th number spoken is `6895259`.
- Given `3,2,1`, the `30000000`th number spoken is `18`.
- Given `3,1,2`, the `30000000`th number spoken is `362`.

> 令人深刻的是，精灵给你留下了一个挑战：确定第 30000000 个说出的数字。例如，给定与上面相同的起始数字：
>
> - 给定 `0,3,6`，则第 30000000 个说出的数字是 `175594`。
> - 给定 `1,3,2`，则第 30000000 个说出的数字是 `2578`。
> - 给定 `2,1,3`，则第 30000000 个说出的数字是 `3544142`。
> - 给定 `1,2,3`，则第 30000000 个说出的数字是 `261214`。
> - 给定 `2,3,1`，则第 30000000 个说出的数字是 `6895259`。
> - 给定 `3,2,1`，则第 30000000 个说出的数字是 `18`。
> - 给定 `3,1,2`，则第 30000000 个说出的数字是 `362`。

Given your starting numbers, **what will be the `30000000`th number spoken?**

> 使用给你的起始数字，第 `30000000` 个说出的数字是什么？

Your puzzle answer was `112458`.

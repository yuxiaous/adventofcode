# Day 13: Claw Contraption
> # 第十三天：抓娃娃机装置

Next up: the [lobby](https://adventofcode.com/2020/day/24) of a resort on a tropical island. The Historians take a moment to admire the hexagonal floor tiles before spreading out.
> 下一站：热带岛屿度假村的[大厅](https://adventofcode.com/2020/day/24)。历史学家们先欣赏了一下六边形地砖，然后分头行动。

Fortunately, it looks like the resort has a new [arcade](https://en.wikipedia.org/wiki/Amusement_arcade)! Maybe you can win some prizes from the [claw machines](https://en.wikipedia.org/wiki/Claw_machine)?
> 幸运的是，这家度假村新开了一家[游戏厅](https://en.wikipedia.org/wiki/Amusement_arcade)！也许你可以在[抓娃娃机](https://en.wikipedia.org/wiki/Claw_machine)里赢点奖品？

The claw machines here are a little unusual. Instead of a joystick or directional buttons to control the claw, these machines have two buttons labeled `A` and `B`. Worse, you can't just put in a token and play; it costs **3 tokens** to push the `A` button and **1 token** to push the `B` button.
> 这里的抓娃娃机有点特别。没有摇杆或方向键，只有两个按钮，分别标着 `A` 和 `B`。更糟糕的是，你不能只投币就玩；按一次 `A` 按钮要花 **3 个代币**，按一次 `B` 按钮要花 **1 个代币**。

With a little experimentation, you figure out that each machine's buttons are configured to move the claw a specific amount to the **right** (along the `X` axis) and a specific amount **forward** (along the `Y` axis) each time that button is pressed.
> 经过一点试验，你发现每台机器的按钮都被设置为每按一次就让爪子在 `X` 轴（向右）和 `Y` 轴（向前）上移动特定的距离。

Each machine contains one **prize**; to win the prize, the claw must be positioned **exactly** above the prize on both the `X` and `Y` axes.
> 每台机器里都有一个**奖品**；要赢得奖品，爪子必须在 `X` 和 `Y` 轴上都**精确**对准奖品的位置。

You wonder: what is the smallest number of tokens you would have to spend to win as many prizes as possible? You assemble a list of every machine's button behavior and prize location (your puzzle input). For example:
> 你想知道：要赢得尽可能多的奖品，最少需要花多少代币？你整理了每台机器的按钮行为和奖品位置列表（你的谜题输入）。例如：

```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
```

This list describes the button configuration and prize location of four different claw machines.
> 这个列表描述了四台不同抓娃娃机的按钮配置和奖品位置。

For now, consider just the first claw machine in the list:
> 现在，只考虑列表中的第一台抓娃娃机：

- Pushing the machine's `A` button would move the claw `94` units along the `X` axis and `34` units along the `Y` axis.
- Pushing the `B` button would move the claw `22` units along the `X` axis and `67` units along the `Y` axis.
- The prize is located at `X=8400`, `Y=5400`; this means that from the claw's initial position, it would need to move exactly `8400` units along the `X` axis and exactly `5400` units along the `Y` axis to be perfectly aligned with the prize in this machine.
> - 按下 `A` 按钮会让爪子在 `X` 轴上移动 `94` 单位，在 `Y` 轴上移动 `34` 单位。
> - 按下 `B` 按钮会让爪子在 `X` 轴上移动 `22` 单位，在 `Y` 轴上移动 `67` 单位。
> - 奖品位于 `X=8400`, `Y=5400`；这意味着从爪子的初始位置，必须在 `X` 轴上正好移动 `8400` 单位，在 `Y` 轴上正好移动 `5400` 单位，才能与奖品完全对齐。

The cheapest way to win the prize is by pushing the `A` button `80` times and the `B` button `40` times. This would line up the claw along the `X` axis (because `80*94 + 40*22 = 8400`) and along the `Y` axis (because `80*34 + 40*67 = 5400`). Doing this would cost `80*3` tokens for the `A` presses and `40*1` for the `B` presses, a total of **`280`** tokens.
> 赢得奖品的最便宜方法是按 `A` 按钮 `80` 次，按 `B` 按钮 `40` 次。这样爪子在 `X` 轴上正好对齐（`80*94 + 40*22 = 8400`），在 `Y` 轴上也正好对齐（`80*34 + 40*67 = 5400`）。这样需要 `80*3` 个代币用于 `A`，`40*1` 个代币用于 `B`，总共 **`280`** 个代币。

For the second and fourth claw machines, there is no combination of A and B presses that will ever win a prize.
> 对于第二台和第四台抓娃娃机，无论怎么组合按A和B都无法赢得奖品。

For the third claw machine, the cheapest way to win the prize is by pushing the `A` button `38` times and the `B` button `86` times. Doing this would cost a total of **`200`** tokens.
> 对于第三台抓娃娃机，最便宜的获胜方法是按 `A` 按钮 `38` 次，按 `B` 按钮 `86` 次。这样总共需要 **`200`** 个代币。

So, the most prizes you could possibly win is two; the minimum tokens you would have to spend to win all (two) prizes is **`480`**.
> 所以你最多能赢得两个奖品；赢得所有（两个）奖品所需的最少代币数是 **`480`**。

You estimate that each button would need to be pressed **no more than `100` times** to win a prize. How else would someone be expected to play?
> 你估算每个按钮最多需要按 **100** 次就能赢得奖品。否则谁还会玩呢？

Figure out how to win as many prizes as possible. **What is the fewest tokens you would have to spend to win all possible prizes?**
> 算算怎么才能赢得最多的奖品。**赢得所有可能奖品所需的最少代币是多少？**

Your puzzle answer was `36758`.

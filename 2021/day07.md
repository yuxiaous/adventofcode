# [Day 7: The Treachery of Whales](https://adventofcode.com/2021/day/7)

A giant [whale](https://en.wikipedia.org/wiki/Sperm_whale) has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

> 一条巨[鲸](https://en.wikipedia.org/wiki/Sperm_whale)决定将你的潜水艇作为它的下一餐，而且它比你快得多，你无处可逃！

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a **massive underground cave system** just beyond where they're aiming!

> 突然，一群螃蟹（每只都在自己的小潜艇中--否则这里对它们来说太深了）来营救你！他们似乎正准备在海底炸一个洞。传感器显示出一个**巨大的地下洞穴系统**，就在他们瞄准的地方之后！

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

> 螃蟹潜水艇需要排列整齐后才有足够的能量炸出一个足够大的洞让你的潜水艇通过。然而，在鲸鱼抓住你之前，它们看起来不会对齐！也许你能帮忙？

There's one major catch - crab submarines can only move horizontally.

> 有一个主要问题 -- 螃蟹潜水艇只能横向移动。

You quickly make a list of **the horizontal position of each crab** ([your puzzle input](day07.txt)). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

> 你快速列出**每只螃蟹的水平位置**（[你的谜题输入](day07.txt)）。螃蟹潜水艇的燃料有限，所以你需要找到一种方法，使它们的所有水平位置都匹配，同时要求它们消耗尽可能少的燃料。

For example, consider the following horizontal positions:

> 例如，考虑以下水平位置：

`16,1,2,0,4,2,7,1,2,14`

This means there's a crab with horizontal position `16`, a crab with horizontal position `1`, and so on.

> 这意味着有一个水平位置为 `16` 的螃蟹，一个水平位置为 `1` 的螃蟹，以此类推。

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position `2`:

> 在水平位置上，一只螃蟹每移动 1 步需要消耗 1 点燃料。你可以让它们全部对齐在任何一个水平位置，但耗油最少的是水平位置是 `2`：

- Move from `16` to `2`: `14` fuel
- Move from `1` to `2`: `1` fuel
- Move from `2` to `2`: `0` fuel
- Move from `0` to `2`: `2` fuel
- Move from `4` to `2`: `2` fuel
- Move from `2` to `2`: `0` fuel
- Move from `7` to `2`: `5` fuel
- Move from `1` to `2`: `1` fuel
- Move from `2` to `2`: `0` fuel
- Move from `14` to `2`: `12` fuel

> - 从 `16` 移动到 `2`：需要 `14` 点燃料
> - 从 `1` 移动到 `2`：需要 `1` 点燃料
> - 从 `2` 移动到 `2`：需要 `0` 点燃料
> - 从 `0` 移动到 `2`：需要 `2` 点燃料
> - 从 `4` 移动到 `2`：需要 `2` 点燃料
> - 从 `2` 移动到 `2`：需要 `0` 点燃料
> - 从 `7` 移动到 `2`：需要 `5` 点燃料
> - 从 `1` 移动到 `2`：需要 `1` 点燃料
> - 从 `2` 移动到 `2`：需要 `0` 点燃料
> - 从 `14` 移动到 `2`：需要 `12` 点燃料

This costs a total of **`37`** fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position `1` (`41` fuel), position `3` (`39` fuel), or position `10` (`71` fuel).

> 这总共需要 **`37`** 点燃料。这是最便宜的结果，更昂贵的结果包括在位置 `1`（需要 `41` 点燃料）、位置 `3`（需要  `39` 点燃料）或位置 `10`（需要 `71` 点燃料）对齐。

Determine the horizontal position that the crabs can align to using the least fuel possible. **How much fuel must they spend to align to that position?**

> 确定螃蟹在哪个水平位置对齐可以使用尽可能少的燃料。**他们必须花费多少燃料才能与该位置对齐？**

Your puzzle answer was `352254`.

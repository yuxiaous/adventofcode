# Day 7: Bridge Repair
> # 第七天：桥梁修复

The Historians take you to a familiar [rope bridge](https://adventofcode.com/2022/day/9) over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?
> 历史学家们带你来到丛林中一座熟悉的吊桥上，桥下是一条河。不过，首席并不在桥的这一边；也许他在另一边？

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.
> 当你准备过桥时，你注意到一群工程师正在修理桥梁。（显然，这座桥经常坏。）在修好之前你无法通过。

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and **stole all the operators** from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).
> 你问工程师们还需要多久；他们说只剩下最后的校准工作，但有几只小象在附近玩耍，并且从校准方程中**把所有运算符都偷走了**！如果有人能判断出哪些测试值可以通过在校准方程（你的谜题输入）中插入任意组合的运算符得到，他们就能完成校准。

For example:
> 例如：

```
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.
> 每一行代表一个方程。冒号前面的数字是测试值；你的任务是判断剩下的数字能否通过插入运算符组合得到该测试值。

Operators are **always evaluated left-to-right**, **not** according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: **add** (`+`) and **multiply** (`*`).
> 运算符**总是从左到右**计算，**不**遵循优先级规则。此外，方程中的数字不能重新排列。你瞥见丛林里有小象拿着两种运算符：**加法**（`+`）和**乘法**（`*`）。

Only three of the above equations can be made true by inserting operators:
> 上述方程中，只有三个可以通过插入运算符使其成立：

- `190: 10 19` has only one position that accepts an operator: between `10` and `19`. Choosing `+` would give `29`, but choosing `*` would give the test value (`10 * 19 = 190`).
- `3267: 81 40 27` has two positions for operators. Of the four possible configurations of the operators, **two** cause the right side to match the test value: `81 + 40 * 27` and `81 * 40 + 27` both equal `3267` (when evaluated left-to-right)!
- `292: 11 6 16 20` can be solved in exactly one way: `11 + 6 * 16 + 20`.
> - `190: 10 19` 只有一个可以插入运算符的位置：`10` 和 `19` 之间。选择 `+` 得到 `29`，但选择 `*` 就能得到测试值（`10 * 19 = 190`）。
> - `3267: 81 40 27` 有两个插入运算符的位置。四种运算符组合中，有**两种**能使右侧等于测试值：`81 + 40 * 27` 和 `81 * 40 + 27`（从左到右计算时）都等于3267！
> - `292: 11 6 16 20` 只有一种方式成立：`11 + 6 * 16 + 20`。

The engineers just need the **total calibration result**, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is **`3749`**.
> 工程师们只需要**总校准结果**，即所有可能成立的方程的测试值之和。在上面的例子中，这三个方程的测试值之和为 **`3749`**。

Determine which equations could possibly be true. **What is their total calibration result?**
> 判断哪些方程有可能成立。**它们的总校准结果是多少？**

Your puzzle answer was `3119088655389`.

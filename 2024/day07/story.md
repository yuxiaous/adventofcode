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

## Part Two
> ## 第二部分

The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.
> 工程师们看起来很担心；你给出的总校准结果远远不在安全容差范围内。就在这时，你发现了自己的错误：有些藏得很好的小象手里拿着第三种运算符。

The [concatenation](https://en.wikipedia.org/wiki/Concatenation) operator (`||`) combines the digits from its left and right inputs into a single number. For example, `12 || 345` would become `12345`. All operators are still evaluated left-to-right.
> 连接运算符（`||`）会把左侧和右侧输入的数字拼接成一个新数字。例如，`12 || 345` 会变成 `12345`。所有运算符依然从左到右计算。

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:
> 现在，除了之前只能用加法和乘法成立的三个方程，上述例子还有三个方程可以通过插入运算符成立：

- `156: 15 6` can be made true through a single concatenation: `15 || 6 = 156`.
- `7290: 6 8 6 15` can be made true using `6 * 8 || 6 * 15`.
- `192: 17 8 14` can be made true using `17 || 8 + 14`.
> - `156: 15 6` 可以通过一次拼接成立：`15 || 6 = 156`。
> - `7290: 6 8 6 15` 可以用 `6 * 8 || 6 * 15` 得到。
> - `192: 17 8 14` 可以用 `17 || 8 + 14` 得到。

Adding up all six test values (the three that could be made before using only `+` and `*` plus the new three that can now be made by also using `||`) produces the new **total calibration result** of **`11387`**.
> 把所有六个测试值（之前只能用 `+` 和 `*` 得到的三个，加上现在也能用 `||` 得到的三个）相加，得到新的**总校准结果**为 **`11387`**。

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. **What is their total calibration result?**
> 利用你对小象藏身之处的新发现，判断哪些方程有可能成立。**它们的总校准结果是多少？**

Your puzzle answer was `264184041398847`.

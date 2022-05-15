# [Day 6: Lanternfish](https://adventofcode.com/2021/day/6)

> 第6天：灯笼鱼

The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

> 海底越来越陡峭。 也许雪橇钥匙是这样携带的？

A massive school of glowing [lanternfish](https://en.wikipedia.org/wiki/Lanternfish) swims past. They must spawn quickly to reach such large numbers - maybe **exponentially** quickly? You should model their growth rate to be sure.

> 一大群发光的 [灯笼鱼](https://en.wikipedia.org/wiki/Lanternfish) 游过。它们必须快速繁殖才能达到如此大的数量 -- 也许有**指数级**那么快？你应该为他们的增长率建模。

Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every **7** days.

> 尽管你对这种特定种类的灯笼鱼一无所知，但你对它们的属性进行了一些猜测。可以确定的是，每条灯笼鱼每 **7** 天会繁殖出一条新的灯笼鱼。

However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents **the number of days until it creates a new lanternfish**.

> 然而，这个过程并不是在每条灯笼鱼间同步的 -- 例如一条灯笼鱼距离繁殖出另一条灯笼鱼可能还剩 2 天，而另一条可能还有 4 天。因此，你可以将每条鱼建模为一个数字，表示**直到它繁殖出一条新的灯笼鱼所剩的天数**。

Furthermore, you reason, a **new** lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

> 此外，你还推理，一条**新出生的**灯笼鱼必定需要稍长的时间才能开始繁殖更多的灯笼鱼：第一个繁殖周期会比之后的多两天。

So, suppose you have a lanternfish with an internal timer value of `3`:

> 因此，假设你有一条计时器为 `3` 的灯笼鱼：

- After one day, its internal timer would become `2`.
- After another day, its internal timer would become `1`.
- After another day, its internal timer would become `0`.
- After another day, its internal timer would reset to `6`, and it would create a **new** lanternfish with an internal timer of `8`.
- After another day, the first lanternfish would have an internal timer of `5`, and the second lanternfish would have an internal timer of `7`.
  
> - 一天后，它的计时器变为 `2`。
> - 又过了一天，它的计时器变为 `1`。
> - 又过了一天，它的计时器变为 `0`。
> - 又过了一天，它的计时器重置为 `6`，它会繁殖出一条计时器为 `8` 的**新**灯笼鱼。
> - 又过了一天，第一条灯笼鱼的计时器变为 `5`，第二条灯笼鱼的计时器变为 `7`。

A lanternfish that creates a new fish resets its timer to `6`, **not `7`** (because `0` is included as a valid timer value). The new lanternfish starts with an internal timer of `8` and does not start counting down until the next day.

> 繁殖出一条新鱼的灯笼鱼会将其计时器重置为 `6`，**而不是 `7`**（因为 `0` 也是计时器的有效值）。新的灯笼鱼的计时器从 `8` 开始，在第二天开始倒计时。

Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish ([your puzzle input](day06.txt)). For example, suppose you were given the following list:

> 由于意识到你正在尝试做什么，潜水艇自动生成了一个列表，包含附近数百条灯笼鱼的年龄（[你的谜题输入](day06.txt)）。例如，假设你获得了以下列表：

`3,4,3,1,2`

This list means that the first fish has an internal timer of `3`, the second fish has an internal timer of `4`, and so on until the fifth fish, which has an internal timer of `2`. Simulating these fish over several days would proceed as follows:

> 这个列表  意味着  第一条鱼的计时器为 `3`，第二条鱼的计时器为 `4`，依此类推，直到第五条鱼的计时器为 `2`。模拟这些鱼在这几天内的情况如下：

```diff
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
```

Each day, a `0` becomes a `6` and adds a new `8` to the end of the list, while each other number decreases by 1 if it was present at the start of the day.

> 每天，由 `0` 变成 `6` 的会在列表末尾添加一个新的 `8`，而其他数字则会在每天开始时减 1。

In this example, after 18 days, there are a total of `26` fish. After 80 days, there would be a total of **`5934`**.

> 在这个例子中，18 天后，总共有 `26` 条鱼。80 天后，总共会有 **`5934`** 条鱼。

Find a way to simulate lanternfish. **How many lanternfish would there be after 80 days?**

> 找到一种模拟灯笼鱼的方法。**80天后会有多少条灯笼鱼？**

Your puzzle answer was `379114`.

## --- Part Two ---

Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

> 假设灯笼鱼长生不老，并且拥有无限的食物和空间。他们会占领整个海洋吗？

After 256 days in the example above, there would be a total of **`26984457539`** lanternfish!

> 在上面的例子中，256 天后总共会有 **`26984457539`** 条灯笼鱼！

**How many lanternfish would there be after 256 days?**

> **256天后会有多少条灯笼鱼？**

Your puzzle answer was `1702631502303`.

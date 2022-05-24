# [Day 18: Snailfish](https://adventofcode.com/2021/day/18)

> 第18天：蜗牛鱼

You descend into the ocean trench and encounter some [snailfish](https://en.wikipedia.org/wiki/Snailfish). They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his **math homework**.

> 你潜入海沟并遇到一些[蜗牛鱼](https://en.wikipedia.org/wiki/Snailfish)。它们说它们看见过雪橇钥匙！如果你帮助其中一条小蜗牛鱼完成数学家庭作业，它们甚至会告诉你钥匙的方向。

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a **pair** - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

> 蜗牛鱼的数字不像常规的数字。相反，每个蜗牛鱼数字都是一个**对子** -- 有序的两个元素。对子中的每个元素可以是一个常规数字或者另一个对子。

Pairs are written as `[x,y]`, where `x` and `y` are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

> 对子以 `[x,y]` 的形式表示，其中 `x` 和 `y` 是对子的元素。以下是一些蜗牛鱼数字的例子，每行一个蜗牛鱼数字：

```'
[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
```

This snailfish homework is about **addition**. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, `[1,2]` + `[[3,4],5]` becomes `[[1,2],[[3,4],5]]`.

> 这个蜗牛鱼作业是关于**加法**的。计算两个蜗牛鱼数字的和，是将加法运算符的左值和右值组成一个对子。例如，`[1,2]` + `[[3,4],5]` 变为 `[[1,2],[[3,4],5]]`。

There's only one problem: **snailfish numbers must always be reduced**, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

> 这里有一个问题：**蜗牛鱼数字必须始终保持精简**，将两个蜗牛鱼数字相加得到的结果需要被精简。

To **reduce a snailfish number**, you must repeatedly do the first action in this list that applies to the snailfish number:

> 要**精简一个蜗牛鱼数字**，你必须在下面的操作方法中由上至下地执行第一个可用的操作，并反复执行：

- If any pair is **nested inside four pairs**, the leftmost such pair **explodes**.
- If any regular number is **10 or greater**, the leftmost such regular number **splits**.

> - 如果有任何对子**被嵌套在四层之内**，则将满足条件的最左侧的对子进行**分解操作**。
> - 如果有任何常规数字**大于等于 10**，则将满足条件的最左侧的常规数字进行**拆分操作**。

Once no action in the above list applies, the snailfish number is reduced.

> 直到没有操作可以执行了，蜗牛鱼数字就精简完成了。

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if **split** produces a pair that meets the **explode** criteria, that pair **explodes** before other **splits** occur.

> 在精简期间，一次最多只能执行一个操作，之后回到操作方法的顶部重新开始。例如，当**拆分操作**产生一个满足**分解操作**的对子时，则该对子优先进行**分解操作**。

To **explode** a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number `0`.

> 要分解一个对子，则该对子的左值被增加到它左侧的第一个常规数字中（如果有），该对子的右值被增加到它右侧的第一个常规数字中（如果有）。分解的对子必须是由两个常规数字组成。然后，将被分解掉的对子替换为常规数字 `0`。

Here are some examples of a single explode action:

> 以下是一些单步分解操作的例子：

- `[[[[[9,8],1],2],3],4]` becomes `[[[[0,9],2],3],4]` (the `9` has no regular number to its left, so it is not added to any regular number).
- `[7,[6,[5,[4,[3,2]]]]]` becomes `[7,[6,[5,[7,0]]]]` (the `2` has no regular number to its right, and so it is not added to any regular number).
- `[[6,[5,[4,[3,2]]]],1]` becomes `[[6,[5,[7,0]]],3]`.
- `[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]` becomes `[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]` (the pair `[3,2]` is unaffected because the pair `[7,3]` is further to the left; `[3,2]` would explode on the next action).
- `[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]` becomes `[[3,[2,[8,0]]],[9,[5,[7,0]]]]`.

> - `[[[[[9,8],1],2],3],4]` 变为 `[[[[0,9],2],3],4]`（`9` 的左边没有常规数字，因此它不会添加到任何常规数字中）。
> - `[7,[6,[5,[4,[3,2]]]]]` 变为 `[7,[6,[5,[7,0]]]]`（`2` 的右边没有常规数字，因此它不会添加到任何常规数字中）。
> - `[[6,[5,[4,[3,2]]]],1]` 变为 `[[6,[5,[7,0]]],3]`。
> - `[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]` 变为 `[[3,[2,[ 8,0]]],[9,[5,[4,[3,2]]]]]`（`[3,2]` 对不受影响，因为 `[7,3]` 离左侧更远，`[3,2]` 将在下一次操作时分解）。
> - `[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]` 变为 `[[3,[2,[8,0] ]],[9,[5,[7,0]]]]`。

To **split** a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded **down**, while the right element of the pair should be the regular number divided by two and rounded **up**. For example, `10` becomes `[5,5]`, `11` becomes `[5,6]`, `12` becomes `[6,6]`, and so on.

> 要**拆分**一个常规数字，则将其替换为一个对子。对子的左元素为该常规数字除以二并**向下**取整后的数，对子的右元素为该常规数字除以二并**向上**取整后的数。例如，`10` 变成 `[5,5]`，`11` 变成 `[5,6]`，`12` 变成 `[6,6]`，以此类推。

Here is the process of finding the reduced result of `[[[[4,3],4],4],[7,[[8,4],9]]]` + `[1,1]`:

> 下面是求 `[[[[4,3],4],4],[7,[[8,4],9]]]` + `[1,1]` 精简结果的过程：

```'
after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
```

Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]`.

> 一旦没有精简操作可以执行，剩下的蜗牛鱼数字就是加法运算的实际结果：`[[[[0,7],4],[[7,8],[6,0]]],[8 ,1]]`。

The homework assignment involves adding up a **list of snailfish numbers** ([your puzzle input](day18.txt)). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

> 这份家庭作业涉及合计一份**蜗牛鱼数字列表**（[你的谜题输入](day18.txt)）。每个蜗牛鱼数字分别列在单独的一行上。将第一个和第二个蜗牛鱼数字相加，然后将其结果和第三个相加，接着将其结果和第四个相加，依此类推，直到列表中的所有数字都使用过一次。

For example, the final sum of this list is `[[[[1,1],[2,2]],[3,3]],[4,4]]`:

> 例如，这个列表的最终总和是 `[[[[1,1],[2,2]],[3,3]],[4,4]]`：

```'
[1,1]
[2,2]
[3,3]
[4,4]
```

The final sum of this list is `[[[[3,0],[5,3]],[4,4]],[5,5]]`:

> 这个列表的最终总和是 `[[[[3,0],[5,3]],[4,4]],[5,5]]`：

```'
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
```

The final sum of this list is `[[[[5,0],[7,4]],[5,5]],[6,6]]`:

> 这个列表的最终总和是 `[[[[5,0],[7,4]],[5,5]],[6,6]]`：

```'
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
```

Here's a slightly larger example:

> 这是一个稍微大一点的例子：

```'
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
```

The final sum `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` is found after adding up the above snailfish numbers:

> 把上面所有的蜗牛鱼数字合计后得到的最终总和是 `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]], [8,7]]]`：

```'
  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
```

To check whether it's the right answer, the snailfish teacher only checks the **magnitude** of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

> 为了检查它是否是正确的答案，蜗牛鱼老师只检查最终总和的**量级**。一个对子的量级是其左元素量级的 3 倍加上其右元素量级的 2 倍。常规数字的量级就是它自己。

For example, the magnitude of `[9,1]` is `3*9 + 2*1 =` **`29`**; the magnitude of `[1,9]` is `3*1 + 2*9 =` **`21`**. Magnitude calculations are recursive: the magnitude of `[[9,1],[1,9]]` is `3*29 + 2*21 =` **`129`**.

> 例如，`[9,1]` 的量级为 `3*9 + 2*1 =` **`29`**，`[1,9]` 的量级是 `3*1 + 2*9 =` **`21`**。量级的计算是递归的：`[[9,1],[1,9]]` 的量级是 `3*29 + 2*21 =` **`129`**。

Here are a few more magnitude examples:

> 这里有一些量级的例子：

- `[[1,2],[[3,4],5]]` becomes **`143`**.
- `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]` becomes **`1384`**.
- `[[[[1,1],[2,2]],[3,3]],[4,4]]` becomes **`445`**.
- `[[[[3,0],[5,3]],[4,4]],[5,5]]` becomes **`791`**.
- `[[[[5,0],[7,4]],[5,5]],[6,6]]` becomes **`1137`**.
- `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` becomes **`3488`**.

> - `[[1,2],[[3,4],5]]` 得到 **`143`**。
> - `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]` 得到 **`1384`**。
> - `[[[[1,1],[2,2]],[3,3]],[4,4]]` 得到 **`445`**。
> - `[[[[3,0],[5,3]],[4,4]],[5,5]]` 得到 **`791`**。
> - `[[[[5,0],[7,4]],[5,5]],[6,6]]` 得到 **`1137`**。
> - `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8 ,7]]]` 得到 **`3488`**。

So, given this example homework assignment:

> 因此，给定这个例子作为家庭作业：

```'
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
```

The final sum is:

> 最终的总和是：

```'
[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
```

The magnitude of this final sum is **`4140`**.

> 这个最终总和的量级是 **`4140`**。

Add up all of the snailfish numbers from the homework assignment in the order they appear. **What is the magnitude of the final sum?**

> 按照列出的顺序，将家庭作业中所有的蜗牛鱼数字求和。**最终总和的量级是多少？**

Your puzzle answer was `3647`.

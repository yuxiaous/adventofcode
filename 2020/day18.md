# Day 18: Operation Order

> 第十八天：运算顺序

As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

> 你看着窗外，凝望着一片植被茂盛的大陆从地平线上缓缓出现，此时邻座的孩子打断了你。他们好奇地问你是否可以帮助他们完成数学作业。

Unfortunately, it seems like this "math" [follows different rules](https://www.youtube.com/watch?v=3QtRK7Y2pPU&t=15) than you remember.

> 不幸的是，这东西似乎跟你记忆中的数学[规则不同](https://www.youtube.com/watch?v=3QtRK7Y2pPU&t=15)。

The homework ([your puzzle input](day18.txt)) consists of a series of expressions that consist of addition (`+`), multiplication (`*`), and parentheses (`(...)`). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

> 这个作业（[你的谜题输入](day18.txt)）由一系列表达式组成，这些表达式包括加法（`+`），乘法（`*`）和括号（`(...)`）。就像普通的数学运算一样，括号表示必须先对其内部进行求值，周围的表达式才能使用它。加法运算仍旧是求出运算符号两边的数字之和，乘法运算仍旧是求出乘积。

However, the rules of **operator precedence** have changed. Rather than evaluating multiplication before addition, the operators have the **same precedence**, and are evaluated left-to-right regardless of the order in which they appear.

> 但是，运算符优先级规则更改了。相较先乘法后加法的推导方法，这里的运算符之间具有相同的优先级，按照从左到右的顺序进行推导。

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are as follows:

> 举个例子，推导表达式 `1 + 2 * 3 + 4 * 5 + 6` 的步骤如下：

```'
1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
```

Parentheses can override this order; for example, here is what happens if parentheses are added to form `1 + (2 * 3) + (4 * (5 + 6))`:

> 括号可以改变该顺序。例如，如果将上面的表达式添加上括号 `1 + (2 * 3) + (4 * (5 + 6))`，会发生以下改变：

```'
1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
```

Here are a few more examples:

> 这里有一些更多的例子：

- `2 * 3 + (4 * 5)` becomes **`26`**.
- `5 + (8 * 3 + 9 + 3 * 4 * 3)` becomes **`437`**.
- `5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))` becomes **`12240`**.
- `((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2` becomes **`13632`**.

Before you can help with the homework, you need to understand it yourself. **Evaluate the expression on each line of the homework; what is the sum of the resulting values?**

> 在你帮助作业之前，你需要先了解它。推导作业中每一行的表达式，结果值的总和是多少？

Your puzzle answer was `23507031841020`.

## --- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: **advanced** math.

> 你设法回答了孩子们的问题，他们完成了家庭作业的第一部分，但是当他们开始下一部分时又陷入了困境：高级数学。

Now, addition and multiplication have **different** precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated **before** multiplication.

> 现在，加法和乘法具有不同的优先级，但是跟你所熟悉的优先级不是一回事儿，取而代之的是先加法后加法。

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are now as follows:

> 举个例子，推导表达式 `1 + 2 * 3 + 4 * 5 + 6` 的步骤如下：

```'
1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
```

Here are the other examples from above:

> 这里上面规则的另一些例子：

- `1 + (2 * 3) + (4 * (5 + 6))` still becomes **`51`**.
- `2 * 3 + (4 * 5)` becomes **`46`**.
- `5 + (8 * 3 + 9 + 3 * 4 * 3)` becomes **`1445`**.
- `5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))` becomes **`669060`**.
- `((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2` becomes **`23340`**.

**What do you get if you add up the results of evaluating the homework problems using these new rules?**

> 如果你使用这些新规则将作业上的问题推导出的结果加起来，会得到什么？

Your puzzle answer was `218621700997826`.

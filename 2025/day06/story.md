# Day 6: Trash Compactor

> 第六天：垃圾压缩机

After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

> 在帮助了厨房里的精灵们之后，你正在休息，帮他们重演一个电影场景，结果你过于兴奋地跳进了垃圾滑道！

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

> 短暂的坠落之后，你发现自己身处一个垃圾粉碎机中。不幸的是，门被磁力密封了。

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her [math homework](https://adventofcode.com/2021/day/18).

> 当你试图寻找出路时，一队头足类动物走近了你！他们很确定能把门打开，但需要一些时间。在你等待的时候，他们好奇你是否能帮最小的头足类动物完成她的[数学作业](https://adventofcode.com/2021/day/18)。

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of **problems**; each problem has a group of numbers that need to be either **added** (`+`) or **multiplied** (`*`) together.

> 头足类动物的数学看起来和普通数学没什么不同。数学练习卷（你的谜题输入）包含一个**题目**列表；每个题目有一组数字需要**相加**（`+`）或**相乘**（`*`）。

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

> 不过，这些题目的排列有点奇怪；它们似乎是紧挨着排在一个很长的水平列表中。例如：

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

> 每个题目的数字是垂直排列的；题目底部是需要执行的操作符号。题目之间由一整列空格分隔。每个题目内数字的左右对齐方式可以忽略。

So, this worksheet contains four problems:

> 因此，这份练习卷包含四个题目：

- `123` * `45` * `6` = **`33210`**
- `328` + `64` + `98` = **`490`**
- `51` * `387` * `215` = **`4243455`**
- `64` + `23` + `314` = **`401`**

> - `123` * `45` * `6` = **`33210`**
> - `328` + `64` + `98` = **`490`**
> - `51` * `387` * `215` = **`4243455`**
> - `64` + `23` + `314` = **`401`**

To check their work, cephalopod students are given the **grand total** of adding together all of the answers to the individual problems. In this worksheet, the grand total is `33210` + `490` + `4243455` + `401` = **`4277556`**.

> 为了检查他们的作业，头足类学生需要将所有单独题目的答案相加得到**总和**。在这份练习卷中，总和为 `33210` + `490` + `4243455` + `401` = **`4277556`**。

Of course, the actual worksheet is **much** wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

> 当然，实际的练习卷要**宽得多**。你需要确保把它完全展开，这样才能清楚地阅读题目。

Solve the problems on the math worksheet. **What is the grand total found by adding together all of the answers to the individual problems?**

> 解决数学练习卷上的题目。**将所有单独题目的答案相加得到的总和是多少？**

Your puzzle answer was `5335495999141`.

## Part Two

The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

> 大个头足类动物回来了，想看看情况如何。当他们发现你的总和与练习卷预期的结果不符时，才意识到忘了解释如何阅读头足类动物的数学。

Cephalopod math is written **right-to-left in columns**. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

> 头足类动物的数学是**按列从右到左**书写的。每个数字独占一列，最高位在上，最低位在下。（题目之间仍然由一整列空格分隔，题目底部的符号仍然是要使用的运算符。）

Here's the example worksheet again:

> 以下是同样的示例练习卷：

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

Reading the problems right-to-left one column at a time, the problems are now quite different:

> 按列从右到左阅读题目，题目现在完全不同了：

- The rightmost problem is `4` + `431` + `623` = **`1058`**
- The second problem from the right is `175` * `581` * `32` = **`3253600`**
- The third problem from the right is `8` + `248` + `369` = **`625`**
- Finally, the leftmost problem is `356` * `24` * `1` = **`8544`**

> - 最右边的题目是 `4` + `431` + `623` = **`1058`**
> - 从右数第二个题目是 `175` * `581` * `32` = **`3253600`**
> - 从右数第三个题目是 `8` + `248` + `369` = **`625`**
> - 最后，最左边的题目是 `356` * `24` * `1` = **`8544`**

Now, the grand total is `1058` + `3253600` + `625` + `8544` = **`3263827`**.

> 现在，总和为 `1058` + `3253600` + `625` + `8544` = **`3263827`**。

Solve the problems on the math worksheet again. **What is the grand total found by adding together all of the answers to the individual problems?**

> 再次解决数学练习卷上的题目。**将所有单独题目的答案相加得到的总和是多少？**

Your puzzle answer was `10142723156431`.

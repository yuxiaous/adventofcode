# Day 4: Printing Department

> 第四天：印刷部门

You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

> 你乘坐自动扶梯下到印刷部门。他们显然正在为圣诞节做准备；到处都是一卷卷巨大的纸张，角落里甚至有一台巨型打印机（用来处理那些真正的大打印任务）。

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

> 在这里装饰很容易：他们可以自己做装饰品。你真正需要的是在电梯离线时找到一条通往北极基地更深处的方法。

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

> "事实上，也许我们可以帮上忙，"当你寻求帮助时，一位精灵回答道。"我们很确定后墙的另一边有一间餐厅。如果我们能打通那堵墙，你就可以继续前进了。可惜我们所有的叉车都在忙着搬运那些大纸卷。"

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

> 如果你能优化叉车的工作，也许它们就能腾出时间来打通那堵墙。

The rolls of paper (`@`) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

> 纸卷（`@`）排列在一个大网格上；精灵们甚至有一张有用的示意图（你的谜题输入），标明了所有东西的位置。

For example:

> 例如：

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

The forklifts can only access a roll of paper if there are **fewer than four rolls of paper** in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

> 叉车只有在八个相邻位置中**少于四个纸卷**时才能取到该纸卷。如果你能找出哪些纸卷是叉车可以取到的，它们就能少花时间在寻找上，从而有更多的时间来拆通向餐厅的墙。

In this example, there are **`13`** rolls of paper that can be accessed by a forklift (marked with `x`):

> 在这个例子中，有 **`13`** 个纸卷可以被叉车取到（用 `x` 标记）：

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

Consider your complete diagram of the paper roll locations. **How many rolls of paper can be accessed by a forklift?**

> 考虑你的完整纸卷位置图。**有多少纸卷可以被叉车取到？**

Your puzzle answer was `1533`.

## Part Two

Now, the Elves just need help accessing as much of the paper as they can.

> 现在，精灵们需要帮助来尽可能多地取到纸卷。

Once a roll of paper can be accessed by a forklift, it can be **removed**. Once a roll of paper is removed, the forklifts might be able to access **more** rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

> 一旦一个纸卷可以被叉车取到，它就可以被**移除**。一旦一个纸卷被移除，叉车可能就能取到**更多**的纸卷，而这些纸卷也同样可以被移除。如果不断重复这个过程，精灵们总共能移除多少个纸卷？

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted **`@`** to indicate that a roll of paper is about to be removed, and using `x` to indicate that a roll of paper was just removed:

> 从上面相同的例子开始，以下是一种尽可能多地移除纸卷的方法，用高亮的 **`@`** 表示即将被移除的纸卷，用 `x` 表示刚刚被移除的纸卷：

```
Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@...xx
..@@@@....
.x.@@@@...
..@@@@@..
...@.@.@@x
..@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
```

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of **`43`** rolls of paper can be removed.

> 当没有更多纸卷可以被叉车取到时停止。在这个例子中，总共可以移除 **`43`** 个纸卷。

Start with your original diagram. **How many rolls of paper in total can be removed by the Elves and their forklifts?**

> 从你的原始布局图开始。**精灵们和他们的叉车总共可以移除多少个纸卷？**

Your puzzle answer was `9206`.

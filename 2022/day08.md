# Day 8: Treetop Tree House

> 第8天：树顶树屋

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a [tree house](https://en.wikipedia.org/wiki/Tree_house).

> 探险队遇到一片奇特的高大树木，所有这些树木都被精心种植在网格中。精灵们解释说，以前的探险队种植这些树是为了重新造林。现在，他们很好奇这里是否适合建造[树屋](https://en.wikipedia.org/wiki/Tree_house)。

First, determine whether there is enough tree cover here to keep a tree house **hidden**. To do this, you need to count the number of trees that are **visible from outside the grid** when looking directly along a row or column.

> 首先，确定这里是否有足够的树用来遮蔽树屋，使树屋保持**隐秘**。为此，你需要**从网格之外**对行或列观察  并统计**可见的**树木的数量。

The Elves have already launched a [quadcopter](https://en.wikipedia.org/wiki/Quadcopter) to generate a map with the height of each tree ([your puzzle input](day08.txt)). For example:

> 精灵们派出了一架[无人机](https://en.wikipedia.org/wiki/Quadcopter)来生成一张包含每棵树高度的地图（[你的谜题输入](day08.txt)）。 例如：

```
30373
25512
65332
33549
35390
```

Each tree is represented as a single digit whose value is its height, where `0` is the shortest and `9` is the tallest.

> 每棵树都用一个数字表示，值是它的高度，其中“0”是最矮的，“9”是最高的。

A tree is **visible** if all of the other trees between it and an edge of the grid are **shorter** than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

> 如果一棵树与网格边缘之间的所有其它树都比这棵树**矮**，则这棵树是**可见的**。只考虑同一行或同一列的树，也就是说，只能从这棵树的上下左右四个方向看。

All of the trees around the edge of the grid are **visible** - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the **interior nine trees** to consider:

- The top-left `5` is **visible** from the left and top. (It isn't visible from the right or bottom since other trees of height `5` are in the way.)
- The top-middle `5` is **visible** from the top and right.
- The top-right `1` is not visible from any direction; for it to be visible, there would need to only be trees of height **`0`** between it and an edge.
- The left-middle `5` is **visible**, but only from the right.
- The center `3` is not visible from any direction; for it to be visible, there would need to be only trees of at most height `2` between it and an edge.
- The right-middle `3` is **visible** from the right.
- In the bottom row, the middle `5` is **visible**, but the `3` and `4` are not.

> 围绕网格边缘的一圈树木都是**可见**，因为它们已经在边缘了，没有树木挡住视线。在这个例子中，只剩下**内部九棵树**需要考虑：
>
> - 顶部左侧的 “5” 从左侧和顶部是**可见的**。（从右边或底部看不到它，因为其他高度为 “5” 的树挡住了视线。）
> - 顶部中间的 “5” 从顶部和右侧是**可见的**。
> - 顶部右侧的 “1” 从任何方向都是不可见的。为了能够看见它，它和边缘之间需要高度为 **“0”** 的树。
> - 左侧中间的 “5” 是**可见的**，但只能从右侧才能看到。
> - 中心的 “3” 从任何方向都是不可见的，为了能够看见，它和边缘之间需要高度为 “2” 的树。
> - 右侧中间的 “3” 从右侧看是**可见的**。
> - 在底下一行，中间的 “5” 是**可见的**，但 “3” 和 “4” 是不可见的。

With 16 trees visible on the edge and another 5 visible in the interior, a total of **`21`** trees are visible in this arrangement.

> 在边缘的 16 棵树可见，另外在内部的 5 棵树可见，在这种排列中总共有 **“21”** 棵树可见。

Consider your map; **how many trees are visible from outside the grid?**

> 考虑你的地图，**从网格外可以看到多少棵树？**

Your puzzle answer was `1845`.

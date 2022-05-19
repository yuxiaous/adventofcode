# [Day 13: Transparent Origami](https://adventofcode.com/2021/day/13)

> 第13天：透明折纸

You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

> 你到达了洞穴的另一部分，这里处于火山活跃状态。如果你可以进行某种热成像，这样你就可以提前判断哪些洞穴太热了而无法安全进入。

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

> 幸运的是，这艘潜水艇似乎配备了热成像仪！当你激活它时，你看到欢迎词：

```'
Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
```

> ```'
> 感谢您的购买！要激活此红外热成像相机系统，请输入手册第 1 页上的代码。
> ```

Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of [transparent paper](https://en.wikipedia.org/wiki/Transparency_(projection))! The transparent paper is marked with random dots and includes instructions on how to fold it up ([your puzzle input](day13.txt)). For example:

> 显然，精灵从来没有使用过这个功能。令你兴奋的是，你终于找到了手册。当你打开它时，第 1 页掉了出来。这是一大张[透明纸](https://en.wikipedia.org/wiki/Transparency_(projection))！透明纸上标有随机点，并包含有关如何折叠它的说明（[你的谜题输入](day13.txt)）。例如：

```'
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
```

The first section is a list of dots on the transparent paper. `0,0` represents the top-left coordinate. The first value, `x`, increases to the right. The second value, `y`, increases downward. So, the coordinate `3,0` is to the right of `0,0`, and the coordinate `0,7` is below `0,0`. The coordinates in this example form the following pattern, where `#` is a dot on the paper and `.` is an empty, unmarked position:

> 第一部分是透明纸上点的列表。`0,0` 表示左上角坐标。第一个值 `x` 向右增加。第二个值 `y` 向下增加。因此，坐标 `3,0` 位于 `0,0` 的右侧，坐标 `0,7` 位于 `0,0` 的下方。这个例子中的坐标形成以下图案，其中 `#` 是纸上的一个点，而 `.` 是一个空的、未标记的位置：

```'
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
```

Then, there is a list of **fold instructions**. Each instruction indicates a line on the transparent paper and wants you to fold the paper **up** (for horizontal `y=...` lines) or **left** (for vertical `x=...` lines). In this example, the first fold instruction is `fold along y=7`, which designates the line formed by all of the positions where `y` is `7` (marked here with `-`):

> 接下来，有一个**折叠指令**列表。每条指令都在透明纸上表示一条直线，并希望你将纸**向上**折叠（在水平线 `y=...` 的位置）或**向左**折叠（在垂直线 `x=...` 的位置）。在这个例子中，第一个折叠指令是 `沿 y=7 折叠`，它表示所有由 `y` 等于 `7` 的位置组成的直线（这里用 `-` 标记）：

```'
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
```

Because this is a horizontal line, fold the bottom half **up**. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

> 因为这是一条水平线，所以将下半部分**向上**折叠。折叠完成后，可能会导致一些点重叠，但点永远不会刚好出现在折线上。执行这条折叠指令后的结果如下所示：

```'
#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
```

Now, only `17` dots are visible.

> 现在，只能看见 `17` 个点了。

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at `0,0` and `0,1`). Because the paper is transparent, the dot just below them in the result (at `0,3`) remains visible, as it can be seen through the transparent paper.

> 注意折叠之前的左下角那两个点，在折叠完成后，这些点出现在了左上角（`0,0` 和 `0,1`）。因为纸是透明的，所以它们正下方的点（`0,3`）仍然可以透过透明纸被看见。

Also notice that some dots can end up **overlapping**; in this case, the dots merge together and become a single dot.

> 同样需要注意，有些点可能会**重叠**。在这种情况下，这些点合并在一起并成为一个点。

The second fold instruction is `fold along x=5`, which indicates this line:

> 第二个折叠指令是 `沿 x=5 折叠`，它表示这条直线：

```'
#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
```

Because this is a vertical line, fold **left**:

> 因为这是一条垂直线，所以**向左**折叠：

```'
#####
#...#
#...#
#...#
#####
.....
.....
```

The instructions made a square!

> 这些指令得到了一个正方形！

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, **`17`** dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

> 透明纸非常大，所以现在把注意力放回第一次折叠。在上面的例子中，第一次折叠之后，只能看见 **`17`** 个点了 -- 因为折叠完成后，重叠的点只能计为一个点。

**How many dots are visible after completing just the first fold instruction on your transparent paper?**

> **在你的透明纸上完成第一个折叠指令后，可以看到多少个点？**

Your puzzle answer was `682`.

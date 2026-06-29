# Day 9: Movie Theater

> 第九天：电影院

You slide down the [firepole](https://en.wikipedia.org/wiki/Fireman%27s_pole) in the corner of the playground and land in the North Pole base movie theater!

> 你顺着游乐场角落的[消防滑杆](https://en.wikipedia.org/wiki/Fireman%27s_pole)滑下，降落在北极基地的电影院里！

The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are **red**; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

> 电影院有一块铺着有趣图案的大瓷砖地板。这里的精灵正在重新装修影院，替换大网格中的一些方形瓷砖。有些瓷砖是**红色**的；精灵们想找出最大的矩形，使得矩形的两个对角都是红色瓷砖。他们甚至有一张红色瓷砖在网格中位置的列表（你的谜题输入）。

For example:

> 例如：

```
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
```

Showing red tiles as `#` and other tiles as `.`, the above arrangement of red tiles would look like this:

> 将红色瓷砖显示为 `#`，其他瓷砖显示为 `.`，上述红色瓷砖的排列如下所示：

```
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
```

You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

> 你可以选择任意两个红色瓷砖作为矩形的对角；你的目标是找到可能的最大矩形。

For example, you could make a rectangle (shown as `O`) with an area of `24` between `2,5` and `9,7`:

> 例如，你可以在 `2,5` 和 `9,7` 之间画出一个面积为 `24` 的矩形（用 `O` 表示）：

```
..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............
```

Or, you could make a rectangle with area `35` between `7,1` and `11,7`:

> 或者，你可以在 `7,1` 和 `11,7` 之间画出一个面积为 `35` 的矩形：

```
..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............
```

You could even make a thin rectangle with an area of only `6` between `7,3` and `2,3`:

> 你甚至可以在 `7,3` 和 `2,3` 之间画出一个面积仅为 `6` 的细长矩形：

```
..............
.......#...#..
..............
..OOOOOO......
..............
..#......#....
..............
.........#.#..
..............
```

Ultimately, the largest rectangle you can make in this example has area **`50`**. One way to do this is between `2,5` and `11,1`:

> 最终，在这个例子中你能画出的最大矩形面积为 **`50`**。其中一种方式是在 `2,5` 和 `11,1` 之间：

```
..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............
```

Using two red tiles as opposite corners, **what is the largest area of any rectangle you can make?**

> 以两个红色瓷砖作为对角，**你能画出的最大矩形面积是多少？**

Your puzzle answer was `4739623064`.

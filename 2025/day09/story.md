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

## Part Two

The Elves just remembered: they can only switch out tiles that are **red** or **green**. So, your rectangle can only include red or green tiles.

> 精灵们刚刚想起：他们只能替换**红色**或**绿色**的瓷砖。也就是说，你的矩形只能包含红色或绿色的瓷砖。

In your list, every red tile is connected to the red tile before and after it by a straight line of **green tiles**. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

> 在你的列表中，每个红色瓷砖与列表中前后的红色瓷砖之间通过一条由**绿色瓷砖**组成的直线相连。列表首尾相接，因此第一个红色瓷砖也与最后一个红色瓷砖相连。列表中相邻的瓷砖总是位于同一行或同一列。

Using the same example as before, the tiles marked `X` would be green:

> 使用和之前相同的例子，标有 `X` 的瓷砖为绿色：

```
..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............
```

In addition, all of the tiles **inside** this loop of red and green tiles are **also** green. So, in this example, these are the green tiles:

> 此外，这个红色和绿色瓷砖围绕起来的**内部**所有瓷砖**也**是绿色的。因此，在这个例子中，绿色瓷砖如下所示：

```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

The remaining tiles are never red nor green.

> 剩余的瓷砖既不是红色也不是绿色。

The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

> 你选择的矩形仍需以红色瓷砖作为对角，但其中包含的任何其他瓷砖现在必须是红色或绿色。这大大限制了你的选择。

For example, you could make a rectangle out of red and green tiles with an area of `15` between `7,3` and `11,1`:

> 例如，你可以在 `7,3` 和 `11,1` 之间用红色和绿色瓷砖拼出一个面积为 `15` 的矩形：

```
..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

Or, you could make a thin rectangle with an area of `3` between `9,7` and `9,5`:

> 或者，你可以在 `9,7` 和 `9,5` 之间画出一个面积为 `3` 的细长矩形：

```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXXOXX..
.........OXX..
.........OX#..
..............
```

The largest rectangle you can make in this example using only red and green tiles has area **`24`**. One way to do this is between `9,5` and `2,3`:

> 在这个例子中，仅用红色和绿色瓷砖能拼出的最大矩形面积为 **`24`**。其中一种方式是在 `9,5` 和 `2,3` 之间：

```
..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............
```

Using two red tiles as opposite corners, **what is the largest area of any rectangle you can make using only red and green tiles?**

> 以两个红色瓷砖作为对角，**仅用红色和绿色瓷砖，你能画出的最大矩形面积是多少？**

Your puzzle answer was `1654141440`.

# Day 12: Garden Groups
> # 第十二天：花园分区

Why not search for the Chief Historian near the [gardener](https://adventofcode.com/2023/day/5) and his [massive farm](https://adventofcode.com/2023/day/21)? There's plenty of food, so The Historians grab something to eat while they search.
> 为什么不在园丁和他那巨大的农场附近找找首席历史学家呢？这里有充足的食物，所以历史学家们一边搜寻一边顺便吃点东西。

You're about to settle near a complex arrangement of garden plots when some Elves ask if you can lend a hand. They'd like to set up fences around each region of garden plots, but they can't figure out how much fence they need to order or how much it will cost. They hand you a map (your puzzle input) of the garden plots.
> 你正准备在一片复杂的花园地块旁安顿下来，这时有些精灵来问你能否帮忙。他们想要围住每个花园区域，但不知道该订购多少篱笆，也不知道费用是多少。他们递给你一张花园地块的地图（你的谜题输入）。

Each garden plot grows only a single type of plant and is indicated by a single letter on your map. When multiple garden plots are growing the same type of plant and are touching (horizontally or vertically), they form a **region**. For example:
> 每块花园地只种一种植物，在你的地图上用一个字母表示。当多块地种着同一种植物并且相邻（上下或左右），它们就组成一个**区域**。例如：

```
AAAA
BBCD
BBCC
EEEC
```

This 4x4 arrangement includes garden plots growing five different types of plants (labeled `A`, `B`, `C`, `D`, and `E`), each grouped into their own region.
> 这个4x4的布局包含五种不同的植物（`A`、`B`、`C`、`D`、`E`），每种都分成了自己的区域。

In order to accurately calculate the cost of the fence around a single region, you need to know that region's **area** and **perimeter**.
> 要准确计算围住某个区域所需篱笆的费用，你需要知道该区域的**面积**和**周长**。

The **area** of a region is simply the number of garden plots the region contains. The above map's type `A`, `B`, and `C` plants are each in a region of area `4`. The type `E` plants are in a region of area `3`; the type `D` plants are in a region of area `1`.
> 区域的**面积**就是该区域包含的地块数量。上面地图中`A`、`B`、`C`区域的面积都是`4`，`E`区域面积为`3`，`D`区域面积为`1`。

Each garden plot is a square and so has **four sides**. The **perimeter** of a region is the number of sides of garden plots in the region that do not touch another garden plot in the same region. The type `A` and `C` plants are each in a region with perimeter `10`. The type `B` and `E` plants are each in a region with perimeter `8`. The lone `D` plot forms its own region with perimeter `4`.
> 每块地是一个正方形，有**四条边**。区域的**周长**是该区域内所有地块与区域外接触的边数。`A`和`C`区域的周长都是`10`，`B`和`E`区域的周长都是`8`，单独的`D`区域周长为`4`。

Visually indicating the sides of plots in each region that contribute to the perimeter using `-` and `|`, the above map's regions' perimeters are measured as follows:
> 用 `-` 和 `|` 直观表示每个区域贡献周长的边，上面地图的各区域周长如下：

```
+-+-+-+-+
|A A A A|
+-+-+-+-+     +-+
              |D|
+-+-+   +-+   +-+
|B B|   |C|
+   +   + +-+
|B B|   |C C|
+-+-+   +-+ +
          |C|
+-+-+-+   +-+
|E E E|
+-+-+-+
```

Plants of the same type can appear in multiple separate regions, and regions can even appear within other regions. For example:
> 同种植物可以出现在多个独立区域，区域甚至可以嵌套。例如：

```
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
```

The above map contains **five** regions, one containing all of the `O` garden plots, and the other four each containing a single `X` plot.
> 上面这张地图包含**五个**区域，一个区域包含所有的O地块，另外四个区域各包含一个X地块。

The four `X` regions each have area `1` and perimeter `4`. The region containing `21` type `O` plants is more complicated; in addition to its outer edge contributing a perimeter of `20`, its boundary with each `X` region contributes an additional `4` to its perimeter, for a total perimeter of `36`.
> 四个`X`区域面积都是`1`，周长都是`4`。包含`21`个`O`的区域更复杂，除了外圈贡献`20`的周长外，每个与`X`接壤的地方还多贡献`4`，总周长为`36`。

Due to "modern" business practices, the **price** of fence required for a region is found by **multiplying** that region's area by its perimeter. The **total price** of fencing all regions on a map is found by adding together the price of fence for every region on the map.
> 由于“现代”商业做法，某个区域所需篱笆的**价格**等于该区域面积乘以周长。地图上所有区域的篱笆**总价**就是所有区域价格之和。

In the first example, region `A` has price `4 * 10 = 40`, region `B` has price `4 * 8 = 32`, region `C` has price `4 * 10 = 40`, region `D` has price `1 * 4 = 4`, and region `E` has price `3 * 8 = 24`. So, the total price for the first example is **`140`**.
> 在第一个例子中，`A`区价格为 `4 * 10 = 40`，`B`区为 `4 * 8 = 32`，`C`区为 `4 * 10 = 40`，`D`区为 `1 * 4 = 4`，`E`区为 `3 * 8 = 24`。所以总价为 **`140`**。

In the second example, the region with all of the `O` plants has price `21 * 36 = 756`, and each of the four smaller X regions has price `1 * 4 = 4`, for a total price of **`772`** (`756 + 4 + 4 + 4 + 4`).
> 在第二个例子中，所有`O`的区域价格为 `21 * 36 = 756`，四个小`X`区域各为 `1 * 4 = 4`，总价为 **`772`**（`756 + 4 + 4 + 4 + 4`）。

Here's a larger example:
> 这里有一个更大的例子：

```
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
```

It contains:
> 其中包括：

- A region of `R` plants with price `12 * 18 = 216`.
- A region of `I` plants with price `4 * 8 = 32`.
- A region of `C` plants with price `14 * 28 = 392`.
- A region of `F` plants with price `10 * 18 = 180`.
- A region of `V` plants with price `13 * 20 = 260`.
- A region of `J` plants with price `11 * 20 = 220`.
- A region of `C` plants with price `1 * 4 = 4`.
- A region of `E` plants with price `13 * 18 = 234`.
- A region of `I` plants with price `14 * 22 = 308`.
- A region of `M` plants with price `5 * 12 = 60`.
- A region of `S` plants with price `3 * 8 = 24`.
> - 一个R区，价格 `12 * 18 = 216`。
> - 一个I区，价格 `4 * 8 = 32`。
> - 一个C区，价格 `14 * 28 = 392`。
> - 一个F区，价格 `10 * 18 = 180`。
> - 一个V区，价格 `13 * 20 = 260`。
> - 一个J区，价格 `11 * 20 = 220`。
> - 一个C区，价格 `1 * 4 = 4`。
> - 一个E区，价格 `13 * 18 = 234`。
> - 一个I区，价格 `14 * 22 = 308`。
> - 一个M区，价格 `5 * 12 = 60`。
> - 一个S区，价格 `3 * 8 = 24`。

So, it has a total price of **`1930`**.
> 所以总价为 **`1930`**。

**What is the total price of fencing all regions on your map?**
> **你地图上所有区域的篱笆总价是多少？**

Your puzzle answer was `1473408`.

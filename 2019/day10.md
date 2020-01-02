# [Day 10: Monitoring Station](https://adventofcode.com/2019/day/10)

> 第10天：监测站

You fly into the asteroid belt and reach the Ceres monitoring station. The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.

> 你飞入小行星带，到达了谷神星监测站。这里的精灵有一个紧急情况：他们在追踪所有小行星时遇到了麻烦，无法确定它们的安全性。

The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region ([your puzzle input](day10.txt)).

> 精灵们想在附近的太空区域建立一个新的监测站，他们向你提供了一份该地区所有小行星的地图（你的谜题输入）。

The map indicates whether each position is empty (`.`) or contains an asteroid (`#`). The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be described with `X,Y` coordinates where `X` is the distance from the left edge and `Y` is the distance from the top edge (so the top-left corner is `0,0` and the position immediately to its right is `1,0`).

> 地图指示了每个位置是否为空（`.`）或是否包含小行星（`#`）。小行星比它们在地图上显示的要小得多，每个小行星都恰好位于其标记位置的中心。可以使用 `X,Y` 坐标来描述小行星，其中 `X` 是到左边缘的距离，而 `Y` 是到上边缘的距离（因此左上角的坐标是 `0,0`，紧靠其右的坐标是 `1,0`）。

Your job is to figure out which asteroid would be the best place to build a **new monitoring station**. A monitoring station can **detect** any asteroid to which it has **direct line of sight** - that is, there cannot be another asteroid **exactly** between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The **best** location is the asteroid that can **detect** the largest number of other asteroids.

> 你的工作是确定哪个小行星是建造**新监测站**的最佳场所。监测站可以**探测**到任何拥有**直接视线**的小行星 —— 也就是说，不可能**恰好**有另一个小行星在它们之间。该视线可以任何角度，而不仅仅是与网格对齐或对角线对齐的线。**最佳**位置是可以探测到最多数量的其他小行星的小行星。

For example, consider the following map:

> 例如，考虑以下地图：

```'
.#..#
.....
#####
....#
...##
```

The best location for a new monitoring station on this map is the highlighted asteroid at `3,4` because it can detect `8` asteroids, more than any other location. (The only asteroid it cannot detect is the one at `1,0`; its view of this asteroid is blocked by the asteroid at `2,2`.) All other asteroids are worse locations; they can detect `7` or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:

> 在这张地图上，新的监测站的最佳位置是 `3,4` 处的小行星，因为它可以探测到 `8` 颗小行星，比其他任何位置都多。（它唯一无法探测到的是 `1,0` 这颗小行星；它的视线被 `2,2` 处的小行星挡住了。）所有其他小行星的位置都不如这个，他们只能探测到 `7` 颗或是更少的其他小行星。以下是如果在各个小行星上建造监测站所能探测到的其他小行星的数量情况：

```'
.7..7
.....
67775
....7
...87
```

Here is an asteroid (`#`) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be blocked and could not be detected:

> 这是一颗小行星（`#`）以及可能会挡住视线的示例。如果在大写字母的位置有一颗小行星，则标有对应小写字母的位置将被遮挡，无法探测到：

```'
#.........
...A......
...B..a...
.EDCG....a
..F.c.b...
.....c....
..efd.c.gb
.......c..
....f...c.
...e..d..c
```

Here are some larger examples:

> 这是一个更大的示例：

- Best is `5,8` with `33` other asteroids detected:

> - 最好的位置是 `5,8`，可以探测到 `33` 颗其他小行星：

```'
    ......#.#.
    #..#.#....
    ..#######.
    .#.#.###..
    .#..#.....
    ..#....#.#
    #..#....#.
    .##.#..###
    ##...#..#.
    .#....####
```

- Best is `1,2` with `35` other asteroids detected:

> - 最好的位置是 `1,2`，可以探测到 `35` 颗其他小行星：

```'
    #.#...#.#.
    .###....#.
    .#....#...
    ##.#.#.#.#
    ....#.#.#.
    .##..###.#
    ..#...##..
    ..##....##
    ......#...
    .####.###.
```

- Best is `6,3` with `41` other asteroids detected:

> - 最好的位置是 `6,3`，可以探测到 `41` 颗其他小行星：

```'
    .#..#..###
    ####.###.#
    ....###.#.
    ..###.##.#
    ##.##.#.#.
    ....###..#
    ..#.#..#.#
    #..#.#.###
    .##...##.#
    .....#.#..
```

- Best is `11,13` with `210` other asteroids detected:

> - 最好的位置是 `11,13`，可以探测到 `210` 颗其他小行星：

```'
    .#..##.###...#######
    ##.############..##.
    .#.######.########.#
    .###.#######.####.#.
    #####.##.#.##.###.##
    ..#####..#.#########
    ####################
    #.####....###.#.#.##
    ##.#################
    #####.##.###..####..
    ..######..##.#######
    ####.##.####...##..#
    .#####..#.######.###
    ##...#.##########...
    #.##########.#######
    .####.#.###.###.#.##
    ....##.##.###..#####
    .#.#.###########.###
    #.#.#.#####.####.###
    ###.##.####.##.#..##
```

Find the best location for a new monitoring station. **How many other asteroids can be detected from that location?**

> 找出新监测站的最佳位置。**从该位置可以探测到多少颗其他小行星？**

Your puzzle answer was `299`.

## Part Two

Once you give them the coordinates, the Elves quickly deploy an Instant Monitoring Station to the location and discover the worst: there are simply too many asteroids.

> 当你给出坐标后，精灵们迅速在该处部署了一座即时监测站，然后发现事情并没有那么简单：小行星简直太多了。

The only solution is **complete vaporization by giant laser**.

> 唯一的解决方案就是**用巨型激光器完全蒸发它们**。

Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating laser perfect for vaporizing asteroids. The laser starts by pointing **up** and always rotates **clockwise**, vaporizing any asteroid it hits.

> 幸运的是，除小行星扫描器外，新的监测站还配备了一台巨型旋转激光器，非常适合蒸发小行星。激光器一开始指向**上方**，并且只能**顺时针**旋转，蒸发任何接触到的小行星。

If multiple asteroids are **exactly** in line with the station, the laser only has enough power to vaporize **one** of them before continuing its rotation. In other words, the same asteroids that can be **detected** can be vaporized, but if vaporizing one asteroid makes another one detectable, the newly-detected asteroid won't be vaporized until the laser has returned to the same position by rotating a full 360 degrees.

> 如果有多个小行星与监测站**精确**的在同一条直线上，激光器在旋转经过的时候只有足够的能量来汽化其中的**一个**。换句话说，只有可以被**探测到**的小行星才能被汽化，如果一颗小行星被汽化掉后能让另一颗小行星被探测到，则新探测到的小行星不会立刻被汽化掉，而是要等到激光器旋转360度后回到相同位置。

For example, consider the following map, where the asteroid with the new monitoring station (and laser) is marked `X`:

> 例如，考虑以下地图，建有新监测站（和激光器）的小行星标记为 `X`：

```'
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
```

The first nine asteroids to get vaporized, in order, would be:

> 依次汽化掉的前九颗小行星是：

```'
.#....###24...#..
##...##.13#67..9#
##...#...5.8####.
..#.....X...###..
..#.#.....#....##
```

Note that some asteroids (the ones behind the asteroids marked `1`, `5`, and `7`) won't have a chance to be vaporized until the next full rotation. The laser continues rotating; the next nine to be vaporized are:

> 注意那些小行星（藏在标有 `1`，`5` 和 `7` 的小行星后面）只有在下一次旋转回来后才有机会被汽化掉。激光器继续旋转，接下来九颗被汽化掉的小行星是：

```'
.#....###.....#..
##...##...#.....#
##...#......1234.
..#.....X...5##..
..#.9.....8....76
```

The next nine to be vaporized are then:

> 接下来九颗被汽化掉的小行星是：

```'
.8....###.....#..
56...9#...#.....#
34...7...........
..2.....X....##..
..1..............
```

Finally, the laser completes its first full rotation (`1` through `3`), a second rotation (`4` through `8`), and vaporizes the last asteroid (`9`) partway through its third rotation:

> 最后，激光器完成了第一次完整的旋转（从 `1` 到 `3`），第二次旋转（从 `4` 到 `8`），并在第三次旋转中汽化掉了最后一颗小行星（`9`）：

```'
......234.....6..
......1...5.....7
.................
........X....89..
.................
```

In the large example above (the one with the best monitoring station location at `11,13`):

- The 1st asteroid to be vaporized is at `11,12`.
- The 2nd asteroid to be vaporized is at `12,1`.
- The 3rd asteroid to be vaporized is at `12,2`.
- The 10th asteroid to be vaporized is at `12,8`.
- The 20th asteroid to be vaporized is at `16,0`.
- The 50th asteroid to be vaporized is at `16,9`.
- The 100th asteroid to be vaporized is at `10,16`.
- The 199th asteroid to be vaporized is at `9,6`.
- **The 200th asteroid to be vaporized is at `8,2`.**
- The 201st asteroid to be vaporized is at `10,9`.
- The 299th and final asteroid to be vaporized is at `11,1`.

> 在上面的大型示例中（监测站最好的位置是 `11,13`）：
>
> - 第1颗被汽化掉的小行星位于 `11,12`。
> - 第2颗被汽化掉的小行星位于 `12,1`。
> - 第3颗被汽化掉的小行星位于 `12,2`。
> - 第10颗被汽化掉的小行星位于 `12,8`。
> - 第20颗被汽化掉的小行星位于 `16,0`。
> - 第50颗被汽化掉的小行星位于 `16,9`。
> - 第100颗被汽化掉的小行星位于 `10,16`。
> - 第199颗被汽化掉的小行星位于 `9,6`。
> - **第200颗被汽化掉的小行星位于 `8,2`。**
> - 第201颗被汽化掉的小行星位于 `10,9`。
> - 第299颗也是最后一颗被汽化掉的小行星位于 `11,1`。

The Elves are placing bets on which will be the **200th** asteroid to be vaporized. Win the bet by determining which asteroid that will be; **what do you get if you multiply its X coordinate by `100` and then add its Y coordinate?** (For example, `8,2` becomes `802`.)

> 精灵们开始押注哪颗是**第200颗**被汽化掉的小行星，猜中的人将赢得赌注。**如果将其 X 坐标值乘以100，然后加上其 Y 坐标值，你会得到什么？**（例如，`8,2` 变为 `802`）。

Your puzzle answer was `1419`.

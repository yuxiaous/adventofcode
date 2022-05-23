# [Day 17: Trick Shot](https://adventofcode.com/2021/day/17)

> 第17天：策略射击

You finally decode the Elves' message. `HI`, the message says. You continue searching for the sleigh keys.

> 你终于解码了精灵的信息，消息是“`嗨`”。你开始继续寻找雪橇钥匙。

Ahead of you is what appears to be a large [ocean trench](https://en.wikipedia.org/wiki/Oceanic_trench). Could the keys have fallen into it? You'd better send a probe to investigate.

> 前方似乎是一条巨大的[海沟](https://en.wikipedia.org/wiki/Oceanic_trench)。钥匙掉进去吗？ 你最好派探测器去调查一下。

The probe launcher on your submarine can fire the probe with any [integer](https://en.wikipedia.org/wiki/Integer) velocity in the `x` (forward) and `y` (upward, or downward if negative) directions. For example, an initial `x,y` velocity like `0,10` would fire the probe straight up, while an initial velocity like `10,-1` would fire the probe forward at a slight downward angle.

> 潜水艇上的探测器发射装置能够以任何[整数](https://en.wikipedia.org/wiki/Integer)速度发射探测器，速度使用 `x`（向前）和 `y`（向上或向下）表示。例如，像 `0,10` 这样的初始速度（`x,y`）会向正上方发射探测器，而像 `10,-1` 这样的初始速度会以略微向下的角度向前发射探测器。

The probe's `x,y` position starts at `0,0`. Then, it will follow some trajectory by moving in **steps**. On each step, these changes occur in the following order:

> 探测器的 `x,y` 位置从 `0,0` 开始。然后，它将沿着轨道以**步**为间隔来移动。在每一步中，位置按照以下顺序改变：

- The probe's `x` position increases by its `x` velocity.
- The probe's `y` position increases by its `y` velocity.
- Due to drag, the probe's `x` velocity changes by `1` toward the value `0`; that is, it decreases by `1` if it is greater than `0`, increases by `1` if it is less than `0`, or does not change if it is already `0`.
- Due to gravity, the probe's `y` velocity decreases by `1`.

> - 探测器的 `x` 位置以 `x` 速度增加。
> - 探测器的 `y` 位置以 `y` 速度增加。
> - 由于阻力，探测器的 `x` 速度朝着 `0` 变化 `1`。也就是说，如果速度大于 `0` 则减少 `1`，如果速度小于 `0` 则增加 `1`，或者如果速度已经为 `0` 时则不改变。
> - 由于重力，探测器的 `y` 速度减少 `1`。

For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be within a **target area** after any step. The submarine computer has already calculated this target area ([your puzzle input](day17.txt)). For example:

> 为了使探测器成功进入海沟，探测器必须沿着某条轨道，在若干步之后到达**目标区域**内。潜水艇计算机已经计算出了这个目标区域（[你的拼图输入](day17.txt)）。例如：

```'
target area: x=20..30, y=-10..-5
```

This target area means that you need to find initial `x,y` velocity values such that after any step, the probe's `x` position is at least `20` and at most `30`, **and** the probe's `y` position is at least `-10` and at most `-5`.

> 这个目标区域意味着你需要算出 `x,y` 初始速度，这样在若干步之后，探测器的 `x` 位置最少是 `20` 最多是 `30`，**并且**探测器的 `y` 位置最少是 `-10` 最多是 `-5`。

Given this target area, one initial velocity that causes the probe to be within the target area after any step is `7,2`:

> 经过若干步之后，可以使探测器进入这个给定的目标区域的其中一个初始速度是 `7,2`：

```'
.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
...........................#...
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
```

In this diagram, `S` is the probe's initial position, `0,0`. The `x` coordinate increases to the right, and the `y` coordinate increases upward. In the bottom right, positions that are within the target area are shown as `T`. After each step (until the target area is reached), the position of the probe is marked with `#`. (The bottom-right `#` is both a position the probe reaches and a position in the target area.)

> 在这张图中，`S` 是探测器的初始位置：`0,0`。`x` 坐标向右增加，`y` 坐标向上增加。在右下角，目标区域内的位置显示为 `T`。在每一步之后（到达目标区域之前），探测器的位置都用 `#` 标记。（右下角的 `#` 既是探测器到达的位置，也是目标区域内的位置。）

Another initial velocity that causes the probe to be within the target area after any step is `6,3`:

> 经过若干步之后，可以使探测器进入目标区域的另一个初始速度是 `6,3`：

```'
...............#..#............
...........#........#..........
...............................
......#..............#.........
...............................
...............................
S....................#.........
...............................
...............................
...............................
.....................#.........
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................T#TTTTTTTTT
....................TTTTTTTTTTT
```

Another one is `9,0`:

> 还有一个是 `9,0`：

```'
S........#.....................
.................#.............
...............................
........................#......
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTT#
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
```

One initial velocity that **doesn't** cause the probe to be within the target area after any step is `17,-4`:

> 经过若干步之后，**不会**使探测器进入目标区域内的一个初始速度是 `17,-4`：

```'
S..............................................................
...............................................................
...............................................................
...............................................................
.................#.............................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT................................
....................TTTTTTTTTTT..#.............................
....................TTTTTTTTTTT................................
...............................................................
...............................................................
...............................................................
...............................................................
................................................#..............
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
...............................................................
..............................................................#
```

The probe appears to pass through the target area, but is never within it after any step. Instead, it continues down and to the right - only the first few steps are shown.

> 经过若干步之后，探测器似乎穿过了目标区域，没有进入其中，反而向右下方继续移动 -- 这里只显示前几步。

If you're going to fire a highly scientific probe out of a super cool probe launcher, you might as well do it with **style**. How high can you make the probe go while still reaching the target area?

> 如果你打算用超酷的探测器发射装置来发射一个高度科学的探测器，你不妨秀出你的**风格**。在仍然可以到达目标区域的情况下，你能够使探头走多高？

In the above example, using an initial velocity of `6,9` is the best you can do, causing the probe to reach a maximum `y` position of **`45`**. (Any higher initial `y` velocity causes the probe to overshoot the target area entirely.)

> 在上面的例子中，使用 `6,9` 的初始速度能让你做到最好，使探测器达到最大 **`45`** 的 `y` 位置。（任何更高的初始 `y` 速度都会导致探测器完全越过目标区域。）

Find the initial velocity that causes the probe to reach the highest `y` position and still eventually be within the target area after any step. **What is the highest `y` position it reaches on this trajectory?**

> 找出能够使探测器到达最高 `y` 位置并且最终在若干步之后仍然可以进入目标区域内的初始速度。**它在这条轨道上达到的最高 `y` 位置是多少？**

Your puzzle answer was `14535`.

--- Part Two ---

Maybe a fancy trick shot isn't the best idea; after all, you only have one probe, so you had better not miss.

> 或许一个花哨的策略射击并不是最好的主意。毕竟你只有一个探测器，所以你最好不要弄丢了。

To get the best idea of what your options are for launching the probe, you need to find **every initial velocity** that causes the probe to eventually be within the target area after any step.

> 为了更好地配置探测器的发射选项，你需要找出**每一个初始速度**，这些初始速度会使探测器在若干步之后最终进入目标区域。

In the above example, there are **`112`** different initial velocity values that meet these criteria:

> 在上面的例子中，有 **`112`** 个不同的初始速度值满足这些条件：

```'
23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7
```

**How many distinct initial velocity values cause the probe to be within the target area after any step?**

> **有多少个不同的初始速度值能够使探测器在若干步之后进入目标区域？**

Your puzzle answer was `2270`.

# Day 18: RAM Run
> # 第十八天：内存逃亡

You and The Historians look a lot more pixelated than you remember. You're [inside a computer](https://adventofcode.com/2017/day/2) at the North Pole!
> 你和历史学家们看起来比记忆中更像像素块。你们现在在北极的[一台计算机内部](https://adventofcode.com/2017/day/2)！

Just as you're about to check out your surroundings, a program runs up to you. "This region of memory isn't safe! The User misunderstood what a [pushdown automaton](https://en.wikipedia.org/wiki/Pushdown_automaton) is and their algorithm is pushing whole bytes down on top of us! Run!"
> 正当你准备打量四周时，一个程序跑过来对你说：“这片内存区域不安全！用户误解了[下推自动机](https://en.wikipedia.org/wiki/Pushdown_automaton)的概念，他们的算法正把整个字节压到我们头上！快跑！”

The algorithm is fast - it's going to cause a byte to fall into your memory space once every [nanosecond](https://www.youtube.com/watch?v=9eyFDBPk4Yw)! Fortunately, you're **faster**, and by quickly scanning the algorithm, you create a **list of which bytes will fall** (your puzzle input) in the order they'll land in your memory space.
> 算法很快——每[纳秒](https://www.youtube.com/watch?v=9eyFDBPk4Yw)就有一个字节掉进你的内存空间！幸运的是，你**更快**，通过快速扫描算法，你得到了一个**即将落下的字节列表**（你的谜题输入），按它们落地顺序排列。

Your memory space is a two-dimensional grid with coordinates that range from `0` to `70` both horizontally and vertically. However, for the sake of example, suppose you're on a smaller grid with coordinates that range from `0` to `6` and the following list of incoming byte positions:
> 你的内存空间是一个二维网格，横纵坐标都从 `0` 到 `70`。不过，为了举例，假设你在一个更小的网格上，坐标范围是 `0` 到 `6`，并有如下即将落下的字节位置列表：

```
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
```

Each byte position is given as an `X,Y` coordinate, where `X` is the distance from the left edge of your memory space and `Y` is the distance from the top edge of your memory space.
> 每个字节位置用 `X,Y` 坐标表示，`X` 是距离内存空间左边缘的距离，`Y` 是距离上边缘的距离。

You and The Historians are currently in the top left corner of the memory space (at `0,0`) and need to reach the exit in the bottom right corner (at `70,70` in your memory space, but at `6,6` in this example). You'll need to simulate the falling bytes to plan out where it will be safe to run; for now, simulate just the first few bytes falling into your memory space.
> 你和历史学家们现在在内存空间的左上角（`0,0`），需要到达右下角的出口（你的空间是 `70,70`，本例是 `6,6`）。你需要模拟字节的落下，规划安全的逃生路线；现在只模拟前几个字节落入内存空间。

As bytes fall into your memory space, they make that coordinate **corrupted**. Corrupted memory coordinates cannot be entered by you or The Historians, so you'll need to plan your route carefully. You also cannot leave the boundaries of the memory space; your only hope is to reach the exit.
> 字节落入你的内存空间后，会使该坐标**损坏**。损坏的内存坐标你和历史学家们都不能进入，所以你需要仔细规划路线。你也不能离开内存空间的边界；你们唯一的希望就是到达出口。

In the above example, if you were to draw the memory space after the first `12` bytes have fallen (using `.` for safe and `#` for corrupted), it would look like this:
> 在上面的例子中，如果前 `12` 个字节落下后画出内存空间（`.` 表示安全，`#` 表示损坏），会是这样：

```
...#...
..#..#.
....#..
...#..#
..#..#.
.#..#..
#.#....
```

You can take steps up, down, left, or right. After just 12 bytes have corrupted locations in your memory space, the shortest path from the top left corner to the exit would take **`22`** steps. Here (marked with `O`) is one such path:
> 你可以向上、下、左、右移动一步。在只有12个字节损坏内存空间后，从左上角到出口的最短路径需要 **`22`** 步。下面（用 `O` 标记）是其中一条路径：

```
OO.#OOO
.O#OO#O
.OOO#OO
...#OO#
..#OO#.
.#.O#..
#.#OOOO
```

Simulate the first kilobyte (`1024` bytes) falling onto your memory space. Afterward, **what is the minimum number of steps needed to reach the exit?**
> 模拟前1KB（`1024`字节）落入你的内存空间。之后，**到达出口所需的最少步数是多少？**

Your puzzle answer was `308`.

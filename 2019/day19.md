# Day 19: Tractor Beam

> 第19天：牵引光束

Unsure of the state of Santa's ship, you borrowed the tractor beam technology from Triton. Time to test it out.

> 由于不确定圣诞老人的飞船情况，因此你从崔顿（海卫一）借来了牵引光束技术。是时候测试一下了。

When you're safely away from anything else, you activate the tractor beam, but nothing happens. It's hard to tell whether it's working if there's nothing to use it on. Fortunately, your ship's drone system can be configured to deploy a drone to specific coordinates and then check whether it's being pulled. There's even an [Intcode](day9.md) program ([your puzzle input](day19.txt)) that gives you access to the drone system.

> 当你与所有物体都保持了安全距离后，你激活了牵引光束，但是什么也没有发生。如果没有东西可以用于牵引光束，很难说它是否正常工作。幸运的是，你的飞船的无人机系统可以进行配置，部署无人机到特定坐标，然后检查它是否被拉动。甚至还有一段 [Intcode](day9.md) 程序（[你的谜题输入](day19.txt)）用于访问无人机系统。

The program uses two input instructions to request the **X and Y position** to which the drone should be deployed. Negative numbers are invalid and will confuse the drone; all numbers should be **zero or positive**.

> 程序使用两条输入指令来请求将无人机部署到的 **X 和 Y 位置**。负数无效，这会扰乱无人机，所有数字应该是**零或者正数**。

Then, the program will output whether the drone is **stationary** (`0`) or **being pulled by something** (`1`). For example, the coordinate X=`0`, Y=`0` is directly in front of the tractor beam emitter, so the drone control program will always report `1` at that location.

> 然后，程序将输出无人机是**静止的**（`0`）还是**被什么东西拉动了**（`1`）。例如，坐标 X=`0`，Y=`0` 直接位于牵引光束发射器的前面，因此在那个位置无人机控制程序将始终报告 `1`。

To better understand the tractor beam, it is important to **get a good picture** of the beam itself. For example, suppose you scan the 10x10 grid of points closest to the emitter:

> 为了更好地理解牵引光束，**拥有一张好的示意图**是非常重要的。例如，假设你扫描了最接近发射器的 10x10 个网格的点：

```'
       X
  0->      9
 0#.........
 |.#........
 v..##......
  ...###....
  ....###...
Y .....####.
  ......####
  ......####
  .......###
 9........##
```

In this example, the **number of points affected by the tractor beam** in the 10x10 area closest to the emitter is **`27`**.

> 在这个例子中，在最接近发射器的 10x10 区域中，**受牵引光束影响的点的数量为 `27`**。

However, you'll need to scan a larger area to **understand the shape** of the beam. **How many points are affected by the tractor beam in the 50x50 area closest to the emitter?** (For each of X and Y, this will be `0` through `49`.)

> 事实上，你需要扫描一块更大的区域以便**了解光束的形态**。**在最接近发射器的 50x50 区域中，多少个点会被牵引光束影响？**（对于坐标轴 X 和 Y，它的区间是 `0` 到 `49`。）

Your puzzle answer was `144`.

## Part Two

You aren't sure how large Santa's ship is. You aren't even sure if you'll need to use this thing on Santa's ship, but it doesn't hurt to be prepared. You figure Santa's ship might fit in a **100x100** square.

> 你不确定圣诞老人的飞船有多大。你甚至不确定是否需要在圣诞老人的飞船上使用这个东西，但做好准备是没有坏处的。你揣测圣诞老人的飞船可能有 **100x100** 的正方形区域这么大。

The beam gets wider as it travels away from the emitter; you'll need to be a minimum distance away to fit a square of that size into the beam fully. (Don't rotate the square; it should be aligned to the same axes as the drone grid.)

> 光束离开发射器越远就变得越宽，你需要一个最小的距离使那个尺寸的正方形可以完全地切合光束。（不要旋转正方形，它应该与无人机网格的轴对齐。）

For example, suppose you have the following tractor beam readings:

> 例如，假设你具有以下牵引光束读数：

```'
#.......................................
.#......................................
..##....................................
...###..................................
....###.................................
.....####...............................
......#####.............................
......######............................
.......#######..........................
........########........................
.........#########......................
..........#########.....................
...........##########...................
...........############.................
............############................
.............#############..............
..............##############............
...............###############..........
................###############.........
................#################.......
.................########OOOOOOOOOO.....
..................#######OOOOOOOOOO#....
...................######OOOOOOOOOO###..
....................#####OOOOOOOOOO#####
.....................####OOOOOOOOOO#####
.....................####OOOOOOOOOO#####
......................###OOOOOOOOOO#####
.......................##OOOOOOOOOO#####
........................#OOOOOOOOOO#####
.........................OOOOOOOOOO#####
..........................##############
..........................##############
...........................#############
............................############
.............................###########
```

In this example, the **10x10** square closest to the emitter that fits entirely within the tractor beam has been marked `O`. Within it, the point closest to the emitter (the only highlighted **`O`**) is at X=`25`, Y=`20`.

> 在这个例子中，最接近发射器且完全切合牵引光束的 **10x10** 正方形标记为 `O`。其中，最接近发射器的点（唯一高亮显示的 **`O`**）位于 X=`25`，Y=`20` 处。

Find the **100x100** square closest to the emitter that fits entirely within the tractor beam; within that square, find the point closest to the emitter. **What value do you get if you take that point's X coordinate, multiply it by `10000`, then add the point's Y coordinate?** (In the example above, this would be `250020`.)

> 找到最接近发射器且完全切合牵引光束的 **100x100** 正方形。在那个正方形内，找到最接近发射器的点。**如果采用该点的 X 坐标值乘以10000，然后加上该点的 Y 坐标值，你会得到什么值？**（在上面的例子中，这个值是 `250020`）。

Your puzzle answer was `13561537`.

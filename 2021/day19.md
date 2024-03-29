# [Day 19: Beacon Scanner](https://adventofcode.com/2021/day/19)

> 第19天：信标扫描器

As your [probe](https://adventofcode.com/2021/day/17) drifted down through this area, it released an assortment of **beacons** and **scanners** into the water. It's difficult to navigate in the pitch black open waters of the ocean trench, but if you can build a map of the trench using data from the scanners, you should be able to safely reach the bottom.

> 当你的[探测器](https://adventofcode.com/2021/day/17)下沉并穿过这片区域时，它会释放一种**信标**和**扫描器**到水中。在海沟的漆黑开阔水域中导航是非常困难的，但如果你能够使用来自扫描器的数据绘制一副海沟地图，你应该能够安全地到达海底。

The beacons and scanners float motionless in the water; they're designed to maintain the same position for long periods of time. Each scanner is capable of detecting all beacons in a large cube centered on the scanner; beacons that are at most 1000 units away from the scanner in each of the three axes (`x`, `y`, and `z`) have their precise position determined relative to the scanner. However, scanners cannot detect other scanners. The submarine has automatically summarized the relative positions of beacons detected by each scanner ([your puzzle input](day19.txt)).

> 信标和扫描器都悬浮在水中，它们被设计来可以长时间保持在同一个位置。每个扫描器都能够侦测以扫描器为中心的大立方空间内的所有信标，分别在三个轴（`x`、`y` 和 `z`）上，扫描器都可以精确定位 1000 个距离单位内的所有信标的相对位置。但是，扫描器无法侦测到其他扫描器。潜艇自动汇总了每个扫描器侦测到的信标的相对位置（[你的谜题输入](day19.txt)）。

For example, if a scanner is at `x,y,z` coordinates `500,0,-500` and there are beacons at `-500,1000,-1500` and `1501,0,-500`, the scanner could report that the first beacon is at `-1000,1000,-1000` (relative to the scanner) but would not detect the second beacon at all.

> 例如，如果一个扫描器位于 `x,y,z` 坐标 `500,0,-500` 处，并且信标位于 `-500,1000,-1500` 和 `1501,0,-500` 两处，则扫描器可以侦测到第一个信标的相对位置是 `-1000,1000,-1000`，但无法侦测到第二个信标。

Unfortunately, while each scanner can report the positions of all detected beacons relative to itself, **the scanners do not know their own position**. You'll need to determine the positions of the beacons and scanners yourself.

> 不幸的是，虽然每个扫描器都可以汇报所有侦测到的信标的相对位置，但**扫描器不知道它自己的位置**。你需要自己确定信标和扫描器的位置。

The scanners and beacons map a single contiguous 3d region. This region can be reconstructed by finding pairs of scanners that have overlapping detection regions such that there are **at least 12 beacons** that both scanners detect within the overlap. By establishing 12 common beacons, you can precisely determine where the scanners are relative to each other, allowing you to reconstruct the beacon map one scanner at a time.

> 扫描器和信标之间映射了一个独立且连续的 3d 区域。可以通过两个具有重叠侦察区域的扫描器来重构该区域，这两个扫描器需要在重叠区域内同时侦察到**至少 12 个信标**。通过建立 12 个常规信标，你可以精确地确定扫描器之间的相对位置，从而让你一次性重构出基于某个扫描器的信标地图。

For a moment, consider only two dimensions. Suppose you have the following scanner reports:

> 先暂时只考虑两个坐标维度。假设你有以下的扫描器报告：

```'
--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1
```

Drawing `x` increasing rightward, `y` increasing upward, scanners as `S`, and beacons as `B`, scanner `0` detects this:

> 绘制地图，`x` 轴向右增加，`y` 轴向上增加，扫描器为 `S`，信标为 `B`，`0` 号扫描器侦测到这幅图：

```'
...B.
B....
....B
S....
```

Scanner `1` detects this:

> `1` 号扫描器侦测到这幅图：

```'
...B..
B....S
....B.
```

For this example, assume scanners only need 3 overlapping beacons. Then, the beacons visible to both scanners overlap to produce the following complete map:

> 对于这个例子，假设扫描器只需要 3 个重叠的信标。然后，将两个扫描器同时可见的信标重叠后生成以下完整地图：

```'
...B..
B....S
....B.
S.....
```

Unfortunately, there's a second problem: the scanners also don't know their **rotation or facing direction**. Due to magnetic alignment, each scanner is rotated some integer number of 90-degree turns around all of the `x`, `y`, and `z` axes. That is, one scanner might call a direction positive `x`, while another scanner might call that direction negative `y`. Or, two scanners might agree on which direction is positive `x`, but one scanner might be upside-down from the perspective of the other scanner. In total, each scanner could be in any of 24 different orientations: facing positive or negative `x`, `y`, or `z`, and considering any of four directions "up" from that facing.

> 不幸的是，还有第二个问题：扫描器也不知道它们自己的**旋转或朝向**。由于磁对准，每个扫描器都围绕着 `x`、`y` 和 `z` 轴旋转了若干整数倍的 90 度角。也就是说，一个扫描器可能称一个方向为正 `x`，而是另一个扫描器可能称该方向为负 `y`。或者，两个扫描器可能正 `x` 的方向相同，但从另一个扫描器的角度来看一台扫描器可能是上下颠倒的。总的来说，每个扫描器都有 24 种不同的朝向：考虑一下，如果朝向正或负的 `x`、`y` 或 `z`，从该朝向来看，其余四个方向中的哪一个是“上方”。

For example, here is an arrangement of beacons as seen from a scanner in the same position but in different orientations:

> 例如，以下是一个扫描器在相同位置但不同朝向时所看到的信标阵列：

```'
--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7

--- scanner 0 ---
1,-1,1
2,-2,2
3,-3,3
2,-1,3
-5,4,-6
-8,-7,0

--- scanner 0 ---
-1,-1,-1
-2,-2,-2
-3,-3,-3
-1,-3,-2
4,6,5
-7,0,8

--- scanner 0 ---
1,1,-1
2,2,-2
3,3,-3
1,3,-2
-4,-6,5
7,0,8

--- scanner 0 ---
1,1,1
2,2,2
3,3,3
3,1,2
-6,-4,-5
0,7,-8
```

By finding pairs of scanners that both see at least 12 of the same beacons, you can assemble the entire map. For example, consider the following report:

> 通过找到能够同时看到至少 12 个相同信标的两个扫描器，你就可以组合出整个地图。例如，考虑以下报告：

```'
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
```

Because all coordinates are relative, in this example, all "absolute" positions will be expressed relative to scanner `0` (using the orientation of scanner `0` and as if scanner `0` is at coordinates `0,0,0`).

> 因为所有的坐标都是相对的，所以在这个例子中，所有的“绝对”位置都将相对于 `0` 号扫描器来表示的（即使用 `0` 号扫描器的朝向，并且将 `0` 号扫描器的坐标视为 `0,0,0` ）。

Scanners `0` and `1` have overlapping detection cubes; the 12 beacons they both detect (relative to scanner `0`) are at the following coordinates:

> `0` 号扫描器和 `1` 号扫描器有重叠的侦测空间，它们都可以侦测到的 12 个信标（相对于 `0` 号扫描器）位于以下坐标：

```'
-618,-824,-621
-537,-823,-458
-447,-329,318
404,-588,-901
544,-627,-890
528,-643,409
-661,-816,-575
390,-675,-793
423,-701,434
-345,-311,381
459,-707,401
-485,-357,347
```

These same 12 beacons (in the same order) but from the perspective of scanner `1` are:

> 这 12 个信标（按相同的顺序）从 `1` 号扫描器的角度来看是这样的：

```'
686,422,578
605,423,415
515,917,-361
-336,658,858
-476,619,847
-460,603,-452
729,430,532
-322,571,750
-355,545,-477
413,935,-424
-391,539,-444
553,889,-390
```

Because of this, scanner `1` must be at `68,-1246,-43` (relative to scanner `0`).

> 因此，相对于 `0` 号扫描器，`1` 号扫描器就位于 `68,-1246,-43`。

Scanner `4` overlaps with scanner `1`; the 12 beacons they both detect (relative to scanner `0`) are:

> `4` 号扫描器与 `1` 号扫描器重叠，它们能同时侦测到的 12 个信标（相对于 `0` 号扫描器）位于：

```'
459,-707,401
-739,-1745,668
-485,-357,347
432,-2009,850
528,-643,409
423,-701,434
-345,-311,381
408,-1815,803
534,-1912,768
-687,-1600,576
-447,-329,318
-635,-1737,486
```

So, scanner `4` is at `-20,-1133,1061` (relative to scanner `0`).

> 因此，`4` 号扫描器位于 `-20,-1133,1061`（相对于 `0` 扫描器）。

Following this process, scanner `2` must be at `1105,-1205,1229` (relative to scanner `0`) and scanner `3` must be at `-92,-2380,-20` (relative to scanner `0`).

>经过一番观察之后，`2` 号扫描器位于 `1105,-1205,1229`（相对于 `0` 号扫描器），`3` 扫描器位于 `-92,-2380,-20`（相对于 `0` 号扫描器）。

The full list of beacons (relative to scanner `0`) is:

> 所有信标（相对于 `0` 号扫描器）如下：

```'
-892,524,684
-876,649,763
-838,591,734
-789,900,-551
-739,-1745,668
-706,-3180,-659
-697,-3072,-689
-689,845,-530
-687,-1600,576
-661,-816,-575
-654,-3158,-753
-635,-1737,486
-631,-672,1502
-624,-1620,1868
-620,-3212,371
-618,-824,-621
-612,-1695,1788
-601,-1648,-643
-584,868,-557
-537,-823,-458
-532,-1715,1894
-518,-1681,-600
-499,-1607,-770
-485,-357,347
-470,-3283,303
-456,-621,1527
-447,-329,318
-430,-3130,366
-413,-627,1469
-345,-311,381
-36,-1284,1171
-27,-1108,-65
7,-33,-71
12,-2351,-103
26,-1119,1091
346,-2985,342
366,-3059,397
377,-2827,367
390,-675,-793
396,-1931,-563
404,-588,-901
408,-1815,803
423,-701,434
432,-2009,850
443,580,662
455,729,728
456,-540,1869
459,-707,401
465,-695,1988
474,580,667
496,-1584,1900
497,-1838,-617
527,-524,1933
528,-643,409
534,-1912,768
544,-627,-890
553,345,-567
564,392,-477
568,-2007,-577
605,-1665,1952
612,-1593,1893
630,319,-379
686,-3108,-505
776,-3184,-501
846,-3110,-434
1135,-1161,1235
1243,-1093,1063
1660,-552,429
1693,-557,386
1735,-437,1738
1749,-1800,1813
1772,-405,1572
1776,-675,371
1779,-442,1789
1780,-1548,337
1786,-1538,337
1847,-1591,415
1889,-1729,1762
1994,-1805,1792
```

In total, there are **`79`** beacons.

> 总共有 **`79`** 个信标。

Assemble the full map of beacons. **How many beacons are there?**

> 组合出完整的信标地图。**有多少个信标？**

Your puzzle answer was `491`.

## --- Part Two ---

Sometimes, it's a good idea to appreciate just how big the ocean is. Using the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry), how far apart do the scanners get?

> 有时候，感受海洋的广大也是个好主意。使用[曼哈顿](https://en.wikipedia.org/wiki/Taxicab_geometry)距离，扫描器的距离有多远？

In the above example, scanners `2` (`1105,-1205,1229`) and `3` (`-92,-2380,-20`) are the largest Manhattan distance apart. In total, they are `1197 + 1175 + 1249 =` **`3621`** units apart.

> 在上面的例子中，`2` 号扫描器（`1105,-1205,1229`）和 `3` 号扫描器（`-92,-2380,-20`）之间的曼哈顿距离是最大的。总的来说，它们的距离是 `1197 + 1175 + 1249 =` **`3621`** 个单位。

**What is the largest Manhattan distance between any two scanners?**

> **任意两个扫描器之间的最大曼哈顿距离是多少？**

Your puzzle answer was `13374`.

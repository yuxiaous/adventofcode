# Day 20: Jurassic Jigsaw

> 第二十天：侏罗纪拼图

The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

> 高速火车离开森林，带着你一路向南。你可以看到远方的沙漠！由于你有一些空闲时间，你准备顺便看一下神话情报局的卫星所捕获的图像中是否包含有趣的东西。

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's **camera array**. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image **tiles** that need to be **reassembled back into a single image**.

> 卫星消息解码后，你发现数据中实际包含了许多由卫星相机阵列所拍摄的小图像。摄像机阵列由许多摄像机组成，它们会生成许多较小的正方形图像块，并将它们重新组合为一个完整的图像，而不是直接生成一个完整的正方形图像。

Each camera in the camera array returns a single monochrome **image tile** with a random unique **ID number**. The tiles ([your puzzle input](day20.txt)) arrived in a random order.

> 相机阵列中的每个相机都会返回一个单色的图像块，并带有一个随机的唯一 ID 号码。图像块（[你的谜题输入](day20.txt)）以随机顺序接收。

Worse yet, the camera array appears to be malfunctioning: each image tile has been **rotated and flipped to a random orientation**. Your first task is to reassemble the original image by orienting the tiles so they fit together.

> 糟糕的是，摄像头阵列似乎出现了故障：每个图像块都被旋转并翻转到了随机方向。你的首要任务是通过调整图像块的方向来重新组装原始图像，使其契合在一起。

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

> 为了显示如何重新组装图块，每个图块的数据都包含一个边框，并与相邻图块精确对齐。所有图块都有边框，并且当图块之间的方向正确时，边框就会精确对齐。图像边缘的图块也具有边框，但是最外面的边缘不会与任何其他图块对齐。

For example, suppose you have the following nine tiles:

> 举个例子，假设你有如下的九个图块：

```'
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
```

By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

> 通过旋转、翻转和重新排列，你可以找到使所有邻边都对齐的正方形排列：

```'
#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
```

For reference, the IDs of the above tiles are:

> 仅供参考，以上图块的 ID 分别为：

```'
1951    2311    3079
2729    1427    2473
2971    1489    1171
```

To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get `1951 * 3079 * 2971 * 1171` = **`20899048083289`**.

> 要检查你是否正确拼装了图像，需要将四个顶角的图块 ID 相乘。如果使用上面例子中所拼装图块进行计算，将得到 `1951 * 3079 * 2971 * 1171` = **`20899048083289`**。

Assemble the tiles into an image. **What do you get if you multiply together the IDs of the four corner tiles?**

> 将图块拼装成图像。将四个顶角的图块 ID 相乘，你会得到什么？

Your puzzle answer was `8581320593371`.

## --- Part Two ---

Now, you're ready to **check the image for sea monsters**.

> 现在，你准备检查图像中是否有海怪了。

The borders of each tile are not part of the actual image; start by removing them.

> 每个图块的边框都不是图像的一部分，先去掉它。

In the example above, the tiles become:

> 在上面的例子中，图块变成了这样：

```'
.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###
```

Remove the gaps to form the actual image:

> 移除间隙得到实际的图像：

```'
.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
```

Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

> 现在，你准备好寻找海怪了！因为你的图像是单色的，所以海怪看起来像这样：

```'
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
```

When looking for this pattern in the image, **the spaces can be anything**; only the `#` need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, **after flipping and rotating it** to the appropriate orientation, there are `two` sea monsters (marked with **`O`**):

> 在图像中寻找这个图案时，空格无关紧要，只需要匹配 `#`。另外，在正确定位图像之前，你可能需要旋转或翻转图像才能找到海怪。在上面的图像中，翻转并旋转到适当的方向后，可以发现两个海怪（标记为 **`O`**）：

```'
.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
```

Determine how rough the waters are in the sea monsters' habitat by counting the number of `#` that are **not** part of a sea monster. In the above example, the habitat's water roughness is **`273`**.

> 通过统计不属于海怪身体的 `#` 的数目，确定海怪栖息地的水域有多汹涌。在上面的例子中，栖息地水域的汹涌值为 **`273`**。

**How many `#` are not part of a sea monster?**

> 有多少个 `#` 不是海怪身体的一部分？

# [Day 20: Trench Map](https://adventofcode.com/2021/day/20)

> 第20天：海沟地图

With the scanners fully deployed, you turn their attention to mapping the floor of the ocean trench.

> 扫描器完全部署后，你将注意力转移到绘制海沟底部的地图上。

When you get back the image from the scanners, it seems to just be random noise. Perhaps you can combine an image enhancement algorithm and the input image ([your puzzle input](day20.txt)) to clean it up a little.

> 当你从扫描器里取回图像时，它似乎只是一些随机的噪点。也许你可以结合使用图像增强算法对输入图像（[你的谜题输入](day20.txt)）稍微消除一些噪点。

For example:

> 举个例子：

```'
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
```

The first section is the **image enhancement algorithm**. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the **input image**, a two-dimensional grid of **light pixels** (`#`) and **dark pixels** (`.`).

> 第一部分是**图像增强算法**。它通常在单行中给出，但在这个例子中为了便于阅读，已将其换成多行。第二部分是**输入图像**，一个由**亮像素**（`#`）和**暗像素**（`.`）组成的二维网格。

The image enhancement algorithm describes how to enhance an image by **simultaneously** converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the **image enhancement algorithm** string.

> 图像增强算法描述了如何将输入图像中的所有像素**同时**转换为输出图像来增强一副图像。通过查看输入图像中对应的像素为中心的 3x3 正方形像素区域来确定输出图像的每个像素。因此，想要确定输出图像中 (5,10) 处像素的值，需要考虑输入图像中的 9 个像素：(4,9), (4,10), (4,11), (5,9)、(5,10)、(5,11)、(6,9)、(6,10) 和 (6,11)。这九个输入像素组合成一个二进制数，用作**图像增强算法**字符串中的索引。

For example, to determine the output pixel that corresponds to the very middle pixel of the input image, the nine pixels marked by `[...]` would need to be considered:

> 例如，要确定对应于输入图像正中间像素的输出像素，需要考虑用 `[...]` 标记的九个像素：

```'
# . . # .
#[. . .].
#[# . .]#
.[. # .].
. . # # #
```

Starting from the top-left and reading across each row, these pixels are `...`, then `#..`, then `.#.`; combining these forms `...#...#.`. By turning dark pixels (`.`) into `0` and light pixels (`#`) into `1`, the binary number `000100010` can be formed, which is `34` in decimal.

> 从左上角开始读取每一行，这些像素是 `...`，然后是 `#..`，最后是 `.#.`，结合起来是这样的 `...#...#.`。将暗像素（`.`）换成 `0`，将亮像素（`#`）换成 `1`，可以形成二进制数 `000100010`，即十进制的 `34`。

The image enhancement algorithm string is exactly 512 characters long, enough to match every possible 9-bit binary number. The first few characters of the string (numbered starting from zero) are as follows:

> 图像增强算法字符串正好有 512 个字符长，足以匹配所有可能的 9 位二进制数。字符串的前几个字符（从零开始编号）如下：

```'
0         10        20        30  34    40        50        60        70
|         |         |         |   |     |         |         |         |
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
```

In the middle of this first group of characters, the character at index 34 can be found: `#`. So, the output pixel in the center of the output image should be `#`, a **light pixel**.

> 在第一组字符的中间，可以找到索引为 34 的字符：`#`。所以，输出图像中心的像素应该是 `#`，一个**亮像素**。

This process can then be repeated to calculate every pixel of the output image.

> 然后可以重复此过程，用以计算输出图像的每个像素。

Through advances in imaging technology, the images being operated on here are **infinite** in size. **Every** pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (`.`). For the purposes of the example, to save on space, only a portion of the infinite-sized input and output images will be shown.

> 由于成像技术的发展，这里处理的图像在尺寸上是**无限的**。无限输出图像的**每个**像素都需要根据输入图像的相关像素进行精确计算。你拥有的小输入图像只是实际的无限输入图像的一小部分，输入图像的其余部分由暗像素（`.`）组成。出于演示的目的，为了节省空间，这里只显示无限大小的输入和输出图像的一部分。

The starting input image, therefore, looks something like this, with more dark pixels (`.`) extending forever in every direction not shown here:

> 因此，起始输入图像看起来是这样的，还有更多的暗像素（`.`）在此处未显示，它们向每个方向上无限延伸：

```'
...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............
```

By applying the image enhancement algorithm to every pixel simultaneously, the following output image can be obtained:

> 通过对每个像素同时应用图像增强算法，可以得到如下输出图像：

```'
...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............
```

Through further advances in imaging technology, the above output image can also be used as an input image! This allows it to be enhanced **a second time**:

> 由于成像技术的进一步发展，上面的输出图像也同样可以作为输入图像！这允许它被增强**第二次**：

```'
...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............
```

Truly incredible - now the small details are really starting to come through. After enhancing the original input image twice, **`35`** pixels are lit.

> 真是不可思议 -- 现在微小的细节开始逐步显现了。将原始输入图像增强两次后，有 **`35`** 个像素被点亮。

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. **How many pixels are lit in the resulting image?**

> 从原始输入图像开始，应用两次图像增强算法，注意图像是无限大小的。**生成的图像中有多少像素被点亮？**

Your puzzle answer was `5486`.

## --- Part Two ---

You still can't quite make out the details in the image. Maybe you just didn't [enhance](https://en.wikipedia.org/wiki/Kernel_(image_processing)) it enough.

> 你仍然无法完全识别图像中的细节。也许你只是没有[增强](https://en.wikipedia.org/wiki/Kernel_(image_processing))到位。

If you enhance the starting input image in the above example a total of **50** times, **`3351`** pixels are lit in the final output image.

> 如果你将上面例子中的初始图像总共增强 **50** 次，在最终输出图像中将会有 **`3351`** 个像素被点亮。

Start again with the original input image and apply the image enhancement algorithm 50 times. **How many pixels are lit in the resulting image?**

> 从原始输入图像重新开始，应用 50 次图像增强算法。**生成的图像中有多少像素被点亮？**

Your puzzle answer was `20210`.

# Day 9: Disk Fragmenter
> # 第九天：磁盘碎片整理器

Another push of the button leaves you in the familiar hallways of some friendly [amphipods](https://adventofcode.com/2021/day/23)! Good thing you each somehow got your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.
> 又按了一下按钮，你们来到了那些友好的甲壳虫熟悉的走廊！还好你们每个人都莫名其妙地有了自己的迷你潜艇。历史学家们驾驶着潜艇去寻找首席，大多时候直接撞在墙上。

While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you offer to help.
> 当历史学家们很快学会如何驾驶潜艇时，你注意到角落里有只甲壳虫正苦恼地摆弄着他的电脑。他正试图通过整理所有文件来获得更多连续的空闲空间，但他的程序无法正常工作；你主动提出帮忙。

He shows you the **disk map** (your puzzle input) he's already generated. For example:
> 他给你看了他已经生成的**磁盘映射**（你的谜题输入）。例如：

```
2333133121414131402
```

The disk map uses a dense format to represent the layout of **files** and **free space** on the disk. The digits alternate between indicating the length of a file and the length of free space.
> 磁盘映射采用紧凑格式表示磁盘上的**文件**和**空闲空间**布局。数字交替表示文件长度和空闲空间长度。

So, a disk map like `12345` would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like `90909` would represent three nine-block files in a row (with no free space between them).
> 例如，`12345` 表示一个1块的文件、2块空闲、3块文件、4块空闲、5块文件。`90909` 表示连续三个9块的文件（中间没有空闲空间）。

Each file on disk also has an **ID number** based on the order of the files as they appear **before** they are rearranged, starting with ID `0`. So, the disk map `12345` has three files: a one-block file with ID `0`, a three-block file with ID `1`, and a five-block file with ID `2`. Using one character for each block where digits are the file ID and `.` is free space, the disk map `12345` represents these individual blocks:
> 每个文件在磁盘上的**ID号**由文件在重排**前**出现的顺序决定，从 `0` 开始。因此，`12345` 有三个文件：一个1块的文件ID为0，一个3块的文件ID为1，一个5块的文件ID为 `2`。用每个块一个字符表示，数字为文件ID，`.` 为空闲空间，`12345` 表示如下：

```
0..111....22222
```

The first example above, `2333133121414131402`, represents these individual blocks:
> 上面第一个例子 `2333133121414131402` 表示如下：

```
00...111...2...333.44.5555.6666.777.888899
```

The amphipod would like to **move file blocks one at a time** from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks). For the disk map `12345`, the process looks like this:
> 甲壳虫希望**每次将一个文件块**从磁盘末尾移动到最左侧的空闲块（直到文件块之间没有空隙）。对于磁盘映射 `12345`，过程如下：

```
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
```

The first example requires a few more steps:
> 第一个例子需要更多步骤：

```
00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............
```

The final step of this file-compacting process is to update the **filesystem checksum**. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position `0`. If a block contains free space, skip it instead.
> 文件整理过程的最后一步是更新**文件系统校验和**。计算方法是：将每个块的位置乘以其包含的文件ID，然后求和。最左侧的块位置为 `0`。如果某个块是空闲空间，则跳过。

Continuing the first example, the first few blocks' position multiplied by its file ID number are `0 * 0 = 0`, `1 * 0 = 0`, `2 * 9 = 18`, `3 * 9 = 27`, `4 * 8 = 32`, and so on. In this example, the checksum is the sum of these, **`1928`**.
> 以第一个例子为例，前几个块的位置乘以文件ID分别为 `0 * 0 = 0`，`1 * 0 = 0`，`2 * 9 = 18`，`3 * 9 = 27`，`4 * 8 = 32`，以此类推。这个例子的校验和为这些结果之和，即 **`1928`**。

Compact the amphipod's hard drive using the process he requested. **What is the resulting filesystem checksum?** (Be careful copy/pasting the input for this puzzle; it is a single, very long line.)
> 按照甲壳虫的要求整理硬盘。**最终的文件系统校验和是多少？**（复制/粘贴本题输入时要小心；它是一行非常长的字符串。）

Your puzzle answer was `6283404590840`.

## Part Two
> ## 第二部分

Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that [file system fragmentation](https://en.wikipedia.org/wiki/File_system_fragmentation) was a bad idea?
> 完成后，马上有两件事变得很明显。首先，磁盘确实拥有了更多连续的空闲空间，正如甲壳虫所希望的那样。其次，电脑运行得更慢了！也许引入这么多文件系统碎片并不是个好主意？

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving **whole files** instead.
> 积极的甲壳虫已经有了新计划：这次他不想再移动单个块，而是想尝试通过移动**整个文件**来整理磁盘。

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of **decreasing file ID number** starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.
> 这一次，尝试将整个文件移动到最左侧、能够容纳该文件的空闲块区间。按照**文件ID号递减**的顺序，每个文件只尝试移动一次，从ID号最大的文件开始。如果文件左侧没有足够大的空闲区间，则该文件不移动。

The first example from above now proceeds differently:
> 上面第一个例子的过程现在变成这样：

```
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
```

The process of updating the filesystem checksum is the same; now, this example's checksum would be **`2858`**.
> 文件系统校验和的计算方法不变；现在，这个例子的校验和是 **`2858`**。

Start over, now compacting the amphipod's hard drive using this new method instead. **What is the resulting filesystem checksum?**
> 重新开始，这次用这种新方法整理甲壳虫的硬盘。**最终的文件系统校验和是多少？**

Your puzzle answer was `6304576012713`.

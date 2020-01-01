# [Day 8: Space Image Format](https://adventofcode.com/2019/day/8)

> 第8天：空间图像格式

The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, and so they are curious if you would spend a brief sojourn on Mars. You land your ship near the rover.

> 当精灵意识到你有机会重启其中一辆火星漫游者时，它们的精神振奋了，因此它们希望你能在火星上进行短暂的逗留。你将飞船降落在漫游者附近。

When you reach the rover, you discover that it's already in the process of rebooting! It's just waiting for someone to enter a [BIOS](https://en.wikipedia.org/wiki/BIOS) password. The Elf responsible for the rover takes a picture of the password ([your puzzle input](day8.txt)) and sends it to you via the Digital Sending Network.

> 当你抵达漫游者时，你发现它已经准备好重新启动了！它只是在等待有人输入一个[BIOS](https://en.wikipedia.org/wiki/BIOS)密码。负责漫游者的精灵拍摄了一张密码照片（[你的谜题输入](day8.txt)），然后通过数字发送网络发送给你。

Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why this is the case. They send you the instructions to decode it.

> 不幸的是，通过数字发送网络发送的图像未使用任何常规编码进行编码。相反，它们以一种特殊的空间图像格式进行编码。精灵们似乎都不明白为什么会这样。他们向你发出指令以对其进行解码。

Images are sent as a series of digits that each represent the color of a single pixel. The digits fill each row of the image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is filled.

> 图像以一串数字进行发送，每个数字代表一个像素的颜色。这些数字从左到右填充图像的每一行，然后向下移动到下一行，从上到下填充行，直到填充了图像的所有像素。

Each image actually consists of a series of identically-sized **layers** that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.

> 每幅图像实际上都由一系列大小相同的**图层**组成，它们都以这种方式进行填充。因此，第一个数字对应第一层左上的像素，第二个数字对应同一层它右边的像素，依此类推，直到最后一个数字对应最后一层右下的像素。

For example, given an image `3` pixels wide and `2` pixels tall, the image data `123456789012` corresponds to the following image layers:

> 举个例子，假设图像宽 `3` 像素，高 `2` 像素，则图像数据 `123456789012` 对应以下图层：

```'
Layer 1: 123
         456

Layer 2: 789
         012
```

The image you received is **`25` pixels wide and `6` pixels tall**.

> 你收到的图像是 **`25` 像素宽和 `6` 像素高**。

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the **fewest `0` digits**. On that layer, what is **the number of `1` digits multiplied by the number of `2` digits?**

> 为了确保图像在传输过程中没有损坏，精灵希望你找到包含数字 `0` 最少的图层。在该层上，**数字 `1` 的数量乘以数字 `2` 的数量**是多少？

Your puzzle answer was `1965`.

## Part Two

Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: `0` is black, `1` is white, and `2` is transparent.

> 现在，你准备好解码图像了。通过堆叠图层并对齐每层中相同位置的像素来渲染图像。数字表示像素的颜色：`0` 代表黑色，`1` 代表白色，以及 `2` 代表透明。

The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a **black** pixel at that position.

> 渲染图层时，第一层在前面，最后一层在后面。所以，如果在给定的位置上，第一层和第二层各有一个透明像素，第三层有一个黑色像素，第四层有一个白色像素，则最终图像在该位置上将是**黑色**像素。

For example, given an image `2` pixels wide and `2` pixels tall, the image data `0222112222120000` corresponds to the following image layers:

举个例子，假设图像宽 `2` 像素，高 `2` 像素，则图像数据 `0222112222120000` 对应于以下图像层：

```'
Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
```

Then, the full image can be found by determining the top visible pixel in each position:

- The top-left pixel is **black** because the top layer is `0`.
- The top-right pixel is **white** because the top layer is `2` (transparent), but the second layer is `1`.
- The bottom-left pixel is **white** because the top two layers are `2`, but the third layer is `1`.
- The bottom-right pixel is **black** because the only visible pixel in that position is `0` (from layer `4`).

> 然后，可以通过判断每个位置的顶部可见像素来确定完整的图像：
>
> - 左上角的像素为**黑色**，因为顶层为 `0`。
> - 右上角的像素为**白色**，因为顶层为 `2`（透明），而第二层为 `1`。
> - 左下角的像素为**白色**，因为上面两层为 `2`，而第三层为 `1`。
> - 右下角的像素为**黑色**，因为该位置唯一可见的像素为 `0`（来自图层 `4`）。

So, the final image looks like this:

> 因此，最终图像看上去是这样的：

```'
01
10
```

**What message is produced after decoding your image?**

> **解码图像后会产生什么消息？**

Your puzzle answer was `GZKJY`.

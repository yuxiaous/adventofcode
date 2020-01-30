# Day 16: Flawed Frequency Transmission

> 第16天：缺陷频率传输

You're 3/4ths of the way through the [gas giants](https://en.wikipedia.org/wiki/Gas_giant). Not only do roundtrip signals to Earth take five hours, but the signal quality is quite bad as well. You can clean up the signal with the Flawed Frequency Transmission algorithm, or **FFT**.

> 你经过[气体巨人](https://en.wikipedia.org/wiki/Gas_giant)路程的四分之三。此时往返地球的信号不仅要花费 5 个小时，而且信号质量还非常差。 你可以使用缺陷频率传输算法（**FFT**）处理信号。

As input, FFT takes a list of numbers. In the signal you received ([your puzzle input](day16.txt)), each number is a single digit: data like `15243` represents the sequence `1`, `5`, `2`, `4`, `3`.

> 作为输入，FFT 需要一串数字列表。在你接收到的信号中（[你的谜题输入](day16.txt)），每个数字都是一个数位：例如 `15243` 这样的数据表示序列 `1`, `5`, `2`, `4`, `3`。

FFT operates in repeated **phases**. In each phase, a new list is constructed with the same length as the input list. This new list is also used as the input for the next phase.

> FFT 以重复的**阶段**进行操作。在每个阶段中，都会构造一个长度与输入列表相同的新列表。这个新列表也用作下一个阶段的输入。

Each element in the new list is built by multiplying every value in the input list by a value in a repeating **pattern** and then adding up the results. So, if the input list were `9, 8, 7, 6, 5` and the pattern for a given element were `1, 2, 3`, the result would be `9*1 + 8*2 + 7*3 + 6*1 + 5*2` (with each input element on the left and each value in the repeating pattern on the right of each multiplication). Then, only the ones digit is kept: `38` becomes `8`, `-17` becomes `7`, and so on.

> 通过将输入列表中的每个值乘以重复的**模**中的值，然后将结果相加来构建新列表中的每个元素。所以，如果输入列表为 `9, 8, 7, 6, 5`，给定元素的模为 `1, 2, 3`，则结果为 `9*1 + 8*2 + 7*3 + 6*1 + 5*2`（其中每个乘法运算的左侧是输入元素，右侧是重复的模中的值）。然后，只保留一个数位：`38` 变为 `8`，`-17` 变为 `7`，依此类推。

While each element in the output array uses all of the same input array elements, the actual repeating pattern to use depends on **which output element** is being calculated. The base pattern is `0, 1, 0, -1`. Then, repeat each value in the pattern a number of times equal to the **position in the output list** being considered. Repeat once for the first element, twice for the second element, three times for the third element, and so on. So, if the third element of the output list is being calculated, repeating the values would produce: `0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1`.

> 虽然输出数组中的每个元素都使用相同的输入数组中的元素，但是实际要使用的重复的模是什么取决于正在计算的是**哪个输出元素**。当基础的模为 `0, 1, 0, -1` 时，然后将模中的每个值重复多次，重复的次数等于所考虑的数字在**输出列表中的位置**。 对第一个元素重复一次，对第二个元素重复两次，对第三个元素重复三次，依此类推。因此，如果正在计算输出列表的第三个元素，则重复这些值将产生：`0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1`。

When applying the pattern, skip the very first value exactly once. (In other words, offset the whole pattern left by one.) So, for the second element of the output list, the actual pattern used would be: `0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1, ...`.

> 当应用模时，跳过整个模的第一个（换句话说，将整个模向左偏移一位）。因此，对于输出列表的第二个元素，实际所使用的模将是：`0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1, ...`。

After using this process to calculate each element of the output list, the phase is complete, and the output list of this phase is used as the new input list for the next phase, if any.

> 使用这个过程计算输出列表的每个元素之后，这个阶段就完成了，这个阶段的输出列表将用作下一个阶段的新输入列表（如果有）。

Given the input signal `12345678`, below are four phases of FFT. Within each phase, each output digit is calculated on a single line with the result at the far right; each multiplication operation shows the input digit on the left and the pattern value on the right:

> 给定输入信号 `12345678`，以下是 FFT 的四个阶段。在每个阶段内，每个输出数位在一行上计算，结果在最右边。每个乘法运算操作的左侧是输入数位，右侧是模的值：

```'
Input signal: 12345678

1*1  + 2*0  + 3*-1 + 4*0  + 5*1  + 6*0  + 7*-1 + 8*0  = 4
1*0  + 2*1  + 3*1  + 4*0  + 5*0  + 6*-1 + 7*-1 + 8*0  = 8
1*0  + 2*0  + 3*1  + 4*1  + 5*1  + 6*0  + 7*0  + 8*0  = 2
1*0  + 2*0  + 3*0  + 4*1  + 5*1  + 6*1  + 7*1  + 8*0  = 2
1*0  + 2*0  + 3*0  + 4*0  + 5*1  + 6*1  + 7*1  + 8*1  = 6
1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*1  + 7*1  + 8*1  = 1
1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*1  + 8*1  = 5
1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*0  + 8*1  = 8

After 1 phase: 48226158

4*1  + 8*0  + 2*-1 + 2*0  + 6*1  + 1*0  + 5*-1 + 8*0  = 3
4*0  + 8*1  + 2*1  + 2*0  + 6*0  + 1*-1 + 5*-1 + 8*0  = 4
4*0  + 8*0  + 2*1  + 2*1  + 6*1  + 1*0  + 5*0  + 8*0  = 0
4*0  + 8*0  + 2*0  + 2*1  + 6*1  + 1*1  + 5*1  + 8*0  = 4
4*0  + 8*0  + 2*0  + 2*0  + 6*1  + 1*1  + 5*1  + 8*1  = 0
4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*1  + 5*1  + 8*1  = 4
4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*1  + 8*1  = 3
4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*0  + 8*1  = 8

After 2 phases: 34040438

3*1  + 4*0  + 0*-1 + 4*0  + 0*1  + 4*0  + 3*-1 + 8*0  = 0
3*0  + 4*1  + 0*1  + 4*0  + 0*0  + 4*-1 + 3*-1 + 8*0  = 3
3*0  + 4*0  + 0*1  + 4*1  + 0*1  + 4*0  + 3*0  + 8*0  = 4
3*0  + 4*0  + 0*0  + 4*1  + 0*1  + 4*1  + 3*1  + 8*0  = 1
3*0  + 4*0  + 0*0  + 4*0  + 0*1  + 4*1  + 3*1  + 8*1  = 5
3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*1  + 3*1  + 8*1  = 5
3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*1  + 8*1  = 1
3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*0  + 8*1  = 8

After 3 phases: 03415518

0*1  + 3*0  + 4*-1 + 1*0  + 5*1  + 5*0  + 1*-1 + 8*0  = 0
0*0  + 3*1  + 4*1  + 1*0  + 5*0  + 5*-1 + 1*-1 + 8*0  = 1
0*0  + 3*0  + 4*1  + 1*1  + 5*1  + 5*0  + 1*0  + 8*0  = 0
0*0  + 3*0  + 4*0  + 1*1  + 5*1  + 5*1  + 1*1  + 8*0  = 2
0*0  + 3*0  + 4*0  + 1*0  + 5*1  + 5*1  + 1*1  + 8*1  = 9
0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*1  + 1*1  + 8*1  = 4
0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*1  + 8*1  = 9
0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*0  + 8*1  = 8

After 4 phases: 01029498
```

Here are the first eight digits of the final output list after 100 phases for some larger inputs:

> 对于一些较大的输入，这是 100 个阶段后最终输出列表的前八位数字：

- `80871224585914546619083218645595` becomes `24176176`.
- `19617804207202209144916044189917` becomes `73745418`.
- `69317163492948606335995924319873` becomes `52432133`.

After **100** phases of FFT, **what are the first eight digits in the final output list?**

> 经过 **100** 个 FFT 阶段后，**最终输出列表中的前八位是什么？**

Your puzzle answer was `73127523`.

## Part Two

Now that your FFT is working, you can decode the **real signal**.

> 现在你的 FFT 可以正常工作了，你可以解码**真实信号**了。

The real signal is [your puzzle input](day16.txt) **repeated 10000 times**. Treat this new signal as a single input list. Patterns are still calculated as before, and 100 phases of FFT are still applied.

> 真正的信号是将[你的谜题输入](day16.txt)**重复 10000 次**。将这个新信号作为单个输入列表对待。模仍旧像之前一样计算，并且仍然应用 100 个阶段的 FFT。

The **first seven digits** of your initial input signal also represent the **message offset**. The message offset is the location of the eight-digit message in the final output list. Specifically, the message offset indicates **the number of digits to skip** before reading the eight-digit message. For example, if the first seven digits of your initial input signal were `1234567`, the eight-digit message would be the eight digits after skipping 1,234,567 digits of the final output list. Or, if the message offset were `7` and your final output list were `98765432109876543210`, the eight-digit message would be `21098765`. (Of course, your real message offset will be a seven-digit number, not a one-digit number like `7`.)

> 你的初始输入信号的**前七个数位**也代表**信息偏移量**。信息偏移量是指在最终输出列表中八位信息的位置。具体来说，信息偏移量表示在读取八位信息之前**所要跳过的位数**。例如，如果你的初始输入信号的前七位数字是 `1234567`，则该八位数字信息将是跳过最终输出列表中的 1,234,567 位数字之后的八位数字。又或者，如果信息偏移量是 `7`，并且最终输出列表是 `98765432109876543210`，则八位数信息将是 `21098765`。（当然，你的实信息偏移量将是一个七位数，而不是像 `7` 这样的一位数。）

Here is the eight-digit message in the final output list after 100 phases. The message offset given in each input has been highlighted. (Note that the inputs given below are repeated 10000 times to find the actual starting input lists.)

> 这是 100 个阶段后最终输出列表中的八位数信息。每个输入中给出的信息偏移量已突出显示。（请注意，下面给出的输入需要重复 10000 次以得到实际的起始输入列表。）

- **`0303673`**`2577212944063491565474664` becomes `84462026`.
- **`0293510`**`9699940807407585447034323` becomes `78725270`.
- **`0308177`**`0884921959731165446850517` becomes `53553731`.

After repeating your input signal 10000 times and running 100 phases of FFT, **what is the eight-digit message embedded in the final output list?**

> 在重复输入信号 10000 次并运行 100 个阶段的 FFT 之后，**最终输出列表中嵌入的八位数信息是什么？**

Your puzzle answer was `80284420`.

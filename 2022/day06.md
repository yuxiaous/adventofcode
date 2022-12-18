# Day 6: Tuning Trouble

> 第6天：调整麻烦

The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the **star** fruit grove.

> 准备工作终于完成了，你和精灵们步行离开营地，开始前往星状水果树林。

As you move through the dense undergrowth, one of the Elves gives you a handheld **device**. He says that it has many fancy features, but the most important one to set up right now is the **communication system**.

> 当你穿过茂密的灌木丛时，一个精灵给了你一个手持**设备**。他说它有很多花哨的功能，但当下一个最有用的功能是**通讯系统**。

However, because he's heard you have [significant](https://adventofcode.com/2016/day/6) [experience](https://adventofcode.com/2016/day/25) [dealing](https://adventofcode.com/2019/day/7) [with](https://adventofcode.com/2019/day/9) [signal-based](https://adventofcode.com/2019/day/16) [systems](https://adventofcode.com/2021/day/25), he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.

> 其实，是因为他听说你[对于](https://adventofcode.com/2016/day/6)[处理](https://adventofcode.com/2016/day/25)[基于信号的](https://adventofcode.com/2019/day/7)[系统](https://adventofcode.com/2019/day/9)[有丰富的](https://adventofcode.com/2019/day/16)[经验](https://adventofcode.com/2021/day/25)，因此他说服了其他精灵，让他们允许给你一台故障的设备 —— 你毫无疑问可以修好它。


As if inspired by comedic timing, the device emits a few colorful sparks.

> 或许是因为这一刻过于喜剧，这个设备发出了一些五颜六色的火花。

To be able to communicate with the Elves, the device needs to **lock on to their signal**. The signal is a series of seemingly-random characters that the device receives one at a time.

> 为了能够与精灵们通讯，设备需要**锁定他们的信号**。信号是一串看似随机的字符，设备一次接收一条。

To fix the communication system, you need to add a subroutine to the device that detects a **start-of-packet marker** in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of **four characters that are all different**.

> 为了修复通信系统，你需要向设备添加一段子程序，用以检测数据流的**包开始标记**。精灵们使用的协议中，数据包的开始由一串 **四个完全不同的字符** 表示。

The device will send your subroutine a datastream buffer ([your puzzle input](day06.txt)); your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.

> 设备将向你的子程序发送一个数据流缓冲（[你的谜题输入](day06.txt)），你的子程序需要确定第一个出现四个完全不同字符的位置。具体来说，它需要报告从缓冲区开始到第一个这样的四字符标记结尾的字符数量。

For example, suppose you receive the following datastream buffer:

> 举个例子，假设你接收了以下数据流缓冲：

```
mjqjpqmgbljsphdztnvjfqwrcgsmlb
```

After the first three characters (`mjq`) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters `mjqj`. Because `j` is repeated, this isn't a marker.

> 收到前三个字符 (`mjq`) 时，还不足以组成标记。第一次可能出现标记的情况是在收到第四个字符之后，四个字符成为 `mjqj`。因为 `j` 是重复的，所以这不是标记。

The first time a marker appears is after the **seventh** character arrives. Once it does, the last four characters received are `jpqm`, which are all different. In this case, your subroutine should report the value **`7`**, because the first start-of-packet marker is complete after 7 characters have been processed.

> 第一次出现标记是在**第七个**字符时，收到的后四个字符是 `jpqm`，它们都是不同的。在这种情况下，你的子程序应该报告数值 **`7`**，因为第一个包开始标记在处理完 7 个字符后找到。

Here are a few more examples:

- `bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character **`5`**
- `nppdvjthqldpwncqszvftbrmjlhg`: first marker after character **`6`**
- `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character **`10`**
- `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character **`11`**

> 这里还有一些更多的例子：
>
> - `bvwbjplbgvbhsrlpgdmjqwftvncz`：第一个标记出现在 **`5`** 个字符后
> - `nppdvjthqldpwncqszvftbrmjlhg`：第一个标记出现在 **`6`** 个字符后
> - `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`：第一个标记出现在 **`10`** 字符后
> - `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`：第一个标记出现在 **`11`** 字符后

**How many characters need to be processed before the first start-of-packet marker is detected?**

**在检测到第一个数据包开始标记前，需要处理多少个字符？**

Your puzzle answer was `1175`.

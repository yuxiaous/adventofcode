# [Day 8: Seven Segment Search](https://adventofcode.com/2021/day/8)

> 第8天：七段搜索

You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

> 鲸鱼撞击着洞口，这里快坍塌了，你需要尽快到达洞穴的安全地带。传感器指示这个洞穴的另一个出口在更深的地方，所以你别无选择，只能继续前进。

As your submarine slowly makes its way through the cave system, you notice that the four-digit [seven-segment displays](https://en.wikipedia.org/wiki/Seven-segment_display) in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

> 当你的潜水艇慢慢地穿过洞穴系统时，你注意到潜艇中的四位数字的[七段显示器](https://en.wikipedia.org/wiki/Seven-segment_display)出现了故障，他们一定在逃跑过程中损坏了。没有他们你会遇到很多麻烦，所以你最好找出问题所在。

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named `a` through `g`:

> 通过打开或关闭名为 `a` 到 `g` 的七个段中的一部分，七段显示器可以显示不同的数字：

```diff
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
```

So, to render a `1`, only segments `c` and `f` would be turned on; the rest would be off. To render a `7`, only segments `a`, `c`, and `f` would be turned on.

> 因此，要显示 `1`，只需要将 `c` 和 `f` 打开，其余的关闭。要显示 `7`，只需要将 `a`、`c` 和 `f` 打开。

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires `a` through `g`, but those wires are connected to segments **randomly**. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits **within** a display use the same connections, though.)

> 现在的问题是每个显示器上的控制段的信号被打乱了。潜水艇仍在尝试在信号线 `a` 到 `g` 上，通过生成的输出来显示数字，但这些线是**随机**连接到段上的。更糟糕的是，每个四位数字显示器的线/段连接是被单独打乱的！（不过，显示器**中的**所有数字都使用相同的连接。）

So, you might know that only signal wires `b` and `g` are turned on, but that doesn't mean **segments** `b` and `g` are turned on: the only digit that uses two segments is `1`, so it must mean segments `c` and `f` are meant to be on. With just that information, you still can't tell which wire (`b`/`g`) goes to which segment (`c`/`f`). For that, you'll need to collect more information.

> 因此，你如果看到信号线 `b` 和 `g` 是打开的，但这并不意味着**段** `b` 和 `g` 被打开：唯一使用两个段的数字是 `1`，所以它只能意味着是要打开段 `c` 和 `f`。仅凭这些信息，你仍然无法分辨哪条线 (`b`/`g`) 连接到哪个段(`c`/`f`)。为此，你需要收集更多信息。

For each display, you watch the changing signals for a while, make a note of **all ten unique signal patterns** you see, and then write down a single **four digit output value** ([your puzzle input](day08.txt)). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

> 对于每个显示，你观察了变化的信号一段时间，记下了你看到的**全部十个不重样的信号图案**，然后写下一个**四位数字输出值**（[你的谜题输入](day08.txt)）。使用信号图案，你应该能够推测出哪个模式对应哪个数字。

For example, here is what you might see in a single entry in your notes:

> 例如，在你的笔记里，你看到的每一条单独的条目看上去会是以下的样子：

```diff
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
```

(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

> （在这是为了适配屏幕宽度，这里将这个条目拆分成了两行。在你的笔记中，它们都将是一行的。）

Each entry consists of ten **unique signal patterns**, a `|` delimiter, and finally the **four digit output value**. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because `7` is the only digit that uses three segments, `dab` in the above example means that to render a `7`, signal lines `d`, `a`, and `b` are on. Because `4` is the only digit that uses four segments, `eafb` means that to render a `4`, signal lines `e`, `a`, `f`, and `b` are on.

> 每个条目由十个**不重样的信号图案**、一个 `|` 分隔符以及最终的**四位数字输出值**组成。在同一个条目内，使用的线/段连接是相同的（但你不知道实际应该连接是哪一个）。使用当前的这套线/段连接，不重样的信号图案对应于十种不同的数字显示方式。因为 `7` 是唯一使用三个段的数字，所以上面例子中的 `dab` 意味着要显示 `7`，信号线 `d`、`a` 和 `b` 是打开的。因为 `4` 是唯一使用四个段的数字，`eafb` 意味着要显示 `4`，信号线 `e`、`a`、`f` 和 `b` 是打开的。

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (`cdfeb fcadb cdfeb cdbaf`) use five segments and are more difficult to deduce.

> 根据这个信息，你应该能够推测出与十位数字中的每一个数字相对应的信号线组合。然后，你可以解码四位输出值。不幸的是，在上面的例子中，输出值（`cdfeb fcadb cdfeb cdbaf`）中的所有数字都使用了五个段，并且很难推断。

For now, **focus on the easy digits**. Consider this larger example:

> 现在，**将注意力集中在简单的数字上**。考虑这个更大的例子：

```diff
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
```

Because the digits `1`, `4`, `7`, and `8` each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting **only digits in the output values** (the part after `|` on each line), in the above example, there are **`26`** instances of digits that use a unique number of segments (highlighted above).

> 因为 `1`、`4`、`7` 和 `8` 这几个数中，每一个使用的段的数量都是唯一的，所以你应该能够分辨出哪些信号组合对应于这些数字。统计出**输出值中仅有的那个数字**（在每行 `|` 之后的部分），在上面的例子中，有 **`26`** 个数字实例使用的段的数量是唯一的。

**In the output values, how many times do digits `1`, `4`, `7`, or `8` appear?**

**在输出值中，数字 `1`、`4`、`7` 和 `8` 出现了多少次？**

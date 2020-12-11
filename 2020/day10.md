# Day 10: Adapter Array

> 第十天：适配器组

Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!

> 为飞机的数据端口打好补丁后，你发现天气预报正在播报一场强烈的热带风暴。但在你准备弄清楚这是否会影响你的度假计划之前，你的设备突然关机了！

Its battery is dead.

> 电池没电了。

You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of **jolts**. Always prepared, you make a list of all of the joltage adapters in your bag.

> 你需要将它插上电源。但有一个问题：座位附近的充电插座提供了错误脉冲数。由于早有准备，于是你列出了背包里的所有脉冲适配器。

Each of your joltage adapters is rated for a specific **output joltage** ([your puzzle input](day10.txt)). Any given adapter can take an input `1`, `2`, or `3` jolts **lower** than its rating and still produce its rated output joltage.

> 你的每个脉冲适配器有特定的输出脉冲频率（[您的谜题输入](day10.txt)）。任何给定的适配器都可以接受比其额定频率低 `1`、`2` 或 `3` 的脉冲输入，并且仍会产生其额定输出脉冲。

In addition, your device has a built-in joltage adapter rated for **`3`** **jolts higher** than the highest-rated adapter in your bag. (If your adapter list were `3`, `9`, and `6`, your device's built-in adapter would be rated for `12` jolts.)

> 此外，你的设备具有一个内置的脉冲适配器，其额定频率比你的包中的额定频率最高的适配器要高 **`3`** 脉冲。（如果你的适配器列表为 `3`、`9` 和 `6`，则你设备的内置适配器的额定频率为 `12` 脉冲。）

Treat the charging outlet near your seat as having an effective joltage rating of `0`.

> 将你的座椅附近的充电插座的有效脉冲额定频率视为 `0`。

Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort and realize you can't even charge your device!

> 由于你还有一些时间闲着没事做，你不妨试一下你所有的适配器。你可不想等到了度假地才意识到没有办法为你的设备充电！

If you **use every adapter in your bag** at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?

> 如果你包中的每个适配器只能使用一次，该如何分配充电插座、适配器和设备之间的脉冲差异？

For example, suppose that in your bag, you have adapters with the following joltage ratings:

> 举个例子，假设在你的包中，你有以下脉冲频率的适配器：

```'
16
10
15
5
1
11
7
19
6
12
4
```

With these adapters, your device's built-in joltage adapter would be rated for `19 + 3 = 22` jolts, 3 higher than the highest-rated adapter.

> 对于这些适配器，你设备的内置脉冲适配器的额定脉冲频率为 `19 + 3 = 22`，比最高频率的适配器高 3 脉冲。

Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter, you'd need to choose them like this:

- The charging outlet has an effective rating of `0` jolts, so the only adapters that could connect to it directly would need to have a joltage rating of `1`, `2`, or `3` jolts. Of these, only one you have is an adapter rated `1` jolt (difference of **`1`**).
- From your `1`-jolt rated adapter, the only choice is your `4`-jolt rated adapter (difference of **`3`**).
- From the `4`-jolt rated adapter, the adapters rated `5`, `6`, or `7` are valid choices. However, in order to not skip any adapters, you have to pick the adapter rated `5` jolts (difference of **`1`**).
- Similarly, the next choices would need to be the adapter rated `6` and then the adapter rated `7` (with difference of **`1`** and **`1`**).
- The only adapter that works with the `7`-jolt rated adapter is the one rated `10` jolts (difference of **`3`**).
- From `10`, the choices are `11` or `12`; choose `11` (difference of **`1`**) and then `12` (difference of **`1`**).
- After `12`, only valid adapter has a rating of `15` (difference of **`3`**), then `16` (difference of **`1`**), then `19` (difference of **`3`**).
- Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is `22` jolts (always a difference of **`3`**).

因为适配器只能连接到比其额定频率低 1-3 脉冲的信号源，所以为了用到每一个适配器，你需要像这样选择它们：

- 充电插座的有效脉冲频率为 `0`，因此唯一可以直接连接到其上的适配器的额定脉冲频率为`1`、`2` 或 `3`。在这些适配器中，你只有一个脉冲频率为 `1` 的适配器（差值为 **`1`**）。
- 继 `1` 脉冲频率的适配器之后，唯一的选择是 `4` 脉冲频率的适配器（差值为 **`3`**）。
- 继 `4` 脉冲频率的适配器之后，频率为 `5`、`6` 或 `7` 的适配器都是可选的。但是，为了不跳过任何适配器，你必须选择脉冲频率为 `5` 的适配器（差值为 **`1`**）。
- 类似地，接下来的选择将是频率为 `6` 的适配器，然后是频率为 `7` 的适配器（差值分别为 **`1`** 和 **`1`**）。
- 唯一可以连接 `7` 脉冲频率适配器一起工作的 是一个脉冲频率为 `10` 的适配器（差值为 **`3`**）。
- 从 `10` 开始，接下来的选择是 `11` 或 `12`，先选 `11`（差值为 **`1`**），然后选 `12`（差值为 **`1`**）。
- 在 `12` 之后，唯一有效的适配器的频率为 `15`（差值为 **`3`**），然后是 `16`（差值为 **`1`**），然后是 `19`（差值为 **`3`**）。
- 最后，因为你设备的内置适配器比最高的适配器高 3，因此它的脉冲频率为 `22`（差值始终为相 **`3`**）。

In this example, when using every adapter, there are **`7`** differences of 1 jolt and **`5`** differences of 3 jolts.

> 在这个例子中，当使用了每一个适配器，有 **`7`** 个差值为 1 脉冲，以及有 **`5`** 个差值为 3 脉冲。

Here is a larger example:

> 这是一个更大的例子：

```'
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
```

In this larger example, in a chain that uses all of the adapters, there are **`22`** differences of 1 jolt and **`10`** differences of 3 jolts.

> 在这个更大的例子中，将所有的适配器连成一串，有 **`22`** 个差值为 1 脉冲，以及有 **`10`** 个差值为 3 脉冲。

Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage differences between the charging outlet, the adapters, and your device. **What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?**

> 将你所有的适配器连成一串，连接充电插座和你的设备内置适配器，并统计充电插座、适配器和你的设备之间的脉冲差值。将差值为 1 脉冲的数量和差值为 3 脉冲的数量相乘得到的值是多少？

Your puzzle answer was `2484`.

## --- Part Two ---

To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.

> 为了完全确定你是否有足够的适配器，你需要弄清楚它们有多少种不同的排列方式 每种排列方式都需要将充电插座连接至设备。之前的关于适配器如何可以成功连接的规则仍然适用。

The first example above (the one that starts with `16`, `10`, `15`) supports the following arrangements:

> 上面的第一个例子（从 `16`, `10`, `15` 开始的那个）支持以下几种排列方式：

```'
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
```

(The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is **`8`**.

> （括号中显示了充电插座和设备的内置适配器。）给定第一个例子中的适配器，将充电插座连接到设备的排列方式总共有 **`8`** 种。

The second example above (the one that starts with `28`, `33`, `18`) has many arrangements. Here are a few:

> 上面的第二个例子（从 `28`, `33`, `18` 开始的那个）有很多的排列方式，这里是其中一部分：

```'
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, (52)
```

In total, this set of adapters can connect the charging outlet to your device in **`19208`** distinct arrangements.

> 总体而言，这组适配器有 **`19208`** 种不同的排列方式将充电插座连接到设备上。

You glance back down at your bag and try to remember why you brought so many adapters; there must be **more than a trillion** valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

> 你回头瞥了一眼你的包，尝试回忆你为什么要带这么多适配器，这一定有超过一兆种有效方法来排列它们！当然，必须有一种有效的方法来统计排列方式。

**What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?**

> 总共有多少种不同的排列适配器的方式可以将充电插座连接到设备？

Your puzzle answer was `15790581481472`.

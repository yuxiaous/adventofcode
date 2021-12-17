# [Day 1: Sonar Sweep](https://adventofcode.com/2021/day/1)

> 第1天：声纳扫描

You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

> 你正在海上的船里处理着自己的事情，突然落水警报响起了！你赶紧看看能不能帮上忙。原来是一个精灵绊倒了，不小心将雪橇的钥匙掉进了大海！

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 **stars**.

> 当你回过神来时，你已经在一艘潜水艇里了，精灵们早就为这种情况做好了准备。它被覆盖着圣诞彩灯（这是理所当然的），它甚至还有一根实验型天线，只要你能将它的信号强度提高到足够高，它应该能够跟踪到那把钥匙。有一块小仪表用来指示天线的信号强度，它可以显示 0-50 颗**星**  。

Your instincts tell you that in order to save Christmas, you'll need to get all **fifty stars** by December 25th.

> 你的直觉告诉你，为了拯救圣诞节，你需要在 12 月 25 日之前获得所有 **五十颗星**。

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

> 通过解决谜题来收集星星。降临节日历中的每一天都会开启两个谜题，当你完成第一个谜题时，第二个谜题会被解锁。每个谜题都会奖励**一颗星**。祝你好运！

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report ([your puzzle input](day01.txt)) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

> 当潜艇下沉到海底表面时，它开始自动对附近的海底进行声纳扫描。在一块小屏幕上，出现了声纳扫描报告（[你的谜题输入](day01.txt)）：每行都是一个海底深度的测量值，由上至下表示扫描距离潜水艇越来越远。

For example, suppose you had the following report:

> 举个例子，加上你获得了以下报告：

```diff
199
200
208
210
200
207
240
269
260
263
```

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of `199`, `200`, `208`, `210`, and so on.

> 这份报告表明，从潜水艇向外扫描，声纳扫描检测出深度为 `199`、`200`、`208`、`210` 等。

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

> 第一件事是弄清楚深度增加的速度有多快，这样你就知道下一步该做什么了————你不确定钥匙是否会被洋流或鱼或其他东西带到更深的水中。

To do this, count **the number of times a depth measurement increases** from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

> 为此需要统计深度测量值比前一个**测量值增加的次数**（在第一个测量值之前没有数据）。在上面的例子中，变化如下：

```diff
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```

In this example, there are **`7`** measurements that are larger than the previous measurement.

> 在这个例子中，有 **`7`** 个测量值大于前一个测量值。

**How many measurements are larger than the previous measurement?**

> **有多少个测量值比前一个测量值大？**

Your puzzle answer was `1564`.

## --- Part Two ---

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a **three-measurement sliding window**. Again considering the above example:

```diff
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
```

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked `A` (`199`, `200`, `208`); their sum is `199 + 200 + 208 = 607`. The second window is marked `B` (`200`, `208`, `210`); its sum is `618`. The sum of measurements in the second window is larger than the sum of the first, so this first comparison **increased**.

Your goal now is to count **the number of times the sum of measurements in this sliding window increases** from the previous sum. So, compare `A` with `B`, then compare `B` with `C`, then `C` with `D`, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

```diff
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
```

In this example, there are **`5`** sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. **How many sums are larger than the previous sum?**

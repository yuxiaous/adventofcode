# [Day 25: Sea Cucumber](https://adventofcode.com/2021/day/25)

> 第25天：海参

This is it: the bottom of the ocean trench, the last place the sleigh keys could be. Your submarine's experimental antenna **still isn't boosted enough** to detect the keys, but they **must** be here. All you need to do is **reach the seafloor** and find them.

> 就是这里，海沟的底部，最后一个可能找到雪橇钥匙的地方。潜水艇的实验型天线**仍然没有增强到**足以侦测到钥匙，但它们**肯定**在这里。你需要做的就是**抵达海底**并找到它们。

At least, you'd touch down on the seafloor if you could; unfortunately, it's completely covered by two large herds of [sea cucumbers](https://en.wikipedia.org/wiki/Sea_cucumber), and there isn't an open space large enough for your submarine.

> 你尝试着陆在海底，但很可惜，海底被两大群[海参](https://en.wikipedia.org/wiki/Sea_cucumber)完全覆盖了，没有足够大的开放空间容纳你的潜水艇。

You suspect that the Elves must have done this before, because just then you discover the phone number of a deep-sea marine biologist on a handwritten note taped to the wall of the submarine's cockpit.

> 就在这时，你在潜水艇驾驶舱的墙壁上发现了一张手写便条，上面写着一位深海海洋生物学家的电话号码。你猜测是精灵们之前留在这里的。

"Sea cucumbers? Yeah, they're probably hunting for food. But don't worry, they're predictable critters: they move in perfectly straight lines, only moving forward when there's space to do so. They're actually quite polite!"

> “海参？啊，它们可能是在觅食。不过别担心，它们是可以预测的生物：它们会沿着完美的直线移动，只要有空间就会向前移动。它们实际上非常有礼貌！ "

You explain that you'd like to predict when you could land your submarine.

> 你解释说，你想要预测什么时候可以降落潜水艇。

"Oh that's easy, they'll eventually pile up and leave enough space for-- wait, did you say submarine? And the only place with that many sea cucumbers would be at the very bottom of the Mariana--" You hang up the phone.

> “哦，这很容易，它们最终会聚在一起，留出足够的空间给。。。等等，你是说潜水艇吗？唯一有这么多海参的地方就只有马里亚纳海沟的最底。。。”，你挂断了电话。

There are two herds of sea cucumbers sharing the same region; one always moves **east** (`>`), while the other always moves **south** (`v`). Each location can contain at most one sea cucumber; the remaining locations are **empty** (`.`). The submarine helpfully generates a map of the situation ([your puzzle input](day25.txt)). For example:

> 同一个地区的两群海参：一群向**东**（`>`）移动，另一群向**南**（`v`）移动。每个位置最多只能容纳一只海参，其余位置是**空的** (`.`)。潜水艇生成了一张有用的情况地图（[你的谜题输入](day25.txt）。例如：

```'
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
```

Every **step**, the sea cucumbers in the east-facing herd attempt to move forward one location, then the sea cucumbers in the south-facing herd attempt to move forward one location. When a herd moves forward, every sea cucumber in the herd first simultaneously considers whether there is a sea cucumber in the adjacent location it's facing (even another sea cucumber facing the same direction), and then every sea cucumber facing an empty location simultaneously moves into that location.

> 在每一**步**中，朝东的海参尝试前进一个位置，然后朝南的海参尝试前进一个位置。当一群海参向前移动时，群体中的所有海参会同时判断它所面对的前一个位置是否有海参（甚至是另一只朝向相同方向的海参），然后每一只面对空位置的海参会同时移动到这个位置。

So, in a situation like this:

> 所以，情况如下：

```'
...>>>>>...
```

After one step, only the rightmost sea cucumber would have moved:

> 一步之后，只有最右边的海参会移动：

```'
...>>>>.>..
```

After the next step, two sea cucumbers move:

> 下一步之后，两只海参动起来：

```'
...>>>.>.>.
```

During a single step, the east-facing herd moves first, then the south-facing herd moves. So, given this situation:

> 在一步中，朝东的群体先移动，然后朝南的群体再移动。因此，给定这样的情况：

```'
..........
.>v....v..
.......>..
..........
```

After a single step, of the sea cucumbers on the left, only the south-facing sea cucumber has moved (as it wasn't out of the way in time for the east-facing cucumber on the left to move), but both sea cucumbers on the right have moved (as the east-facing sea cucumber moved out of the way of the south-facing sea cucumber):

> 一步过后，左边的两只海参中只有朝南的海参移动了（因为它没有及时移走，它左边朝东的海参就无法移动），但右边的两只海参都移动了（因为朝东的海参移走了，朝南的海参可以移动）：

```'
..........
.>........
..v....v>.
..........
```

Due to **strong water currents** in the area, sea cucumbers that move off the right edge of the map appear on the left edge, and sea cucumbers that move off the bottom edge of the map appear on the top edge. Sea cucumbers always check whether their destination location is empty before moving, even if that destination is on the opposite side of the map:

> 由于这片地区有**强烈的水流**，离开地图右边缘的海参会出现在地图的左边缘，离开地图底部边缘的海参会出现在地图的顶部边缘。海参在移动之前总是检查它们的目的地位置是否是空的，即使该目的地在地图的另一侧：

```'
Initial state:
...>...
.......
......>
v.....>
......>
.......
..vvv..

After 1 step:
..vv>..
.......
>......
v.....>
>......
.......
....v..

After 2 steps:
....v>.
..vv...
.>.....
......>
v>.....
.......
.......

After 3 steps:
......>
..v.v..
..>v...
>......
..>....
v......
.......

After 4 steps:
>......
..v....
..>.v..
.>.v...
...>...
.......
v......
```

To find a safe place to land your submarine, the sea cucumbers need to stop moving. Again consider the first example:

> 为了找到一个安全的地方让你的潜水艇着陆，海参需要停止移动。再次考虑第一个例子：

```'
Initial state:
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>

After 1 step:
....>.>v.>
v.v>.>v.v.
>v>>..>v..
>>v>v>.>.v
.>v.v...v.
v>>.>vvv..
..v...>>..
vv...>>vv.
>.v.v..v.v

After 2 steps:
>.v.v>>..v
v.v.>>vv..
>v>.>.>.v.
>>v>v.>v>.
.>..v....v
.>v>>.v.v.
v....v>v>.
.vv..>>v..
v>.....vv.

After 3 steps:
v>v.v>.>v.
v...>>.v.v
>vv>.>v>..
>>v>v.>.v>
..>....v..
.>.>v>v..v
..v..v>vv>
v.v..>>v..
.v>....v..

After 4 steps:
v>..v.>>..
v.v.>.>.v.
>vv.>>.v>v
>>.>..v>.>
..v>v...v.
..>>.>vv..
>.v.vv>v.v
.....>>vv.
vvv>...v..

After 5 steps:
vv>...>v>.
v.v.v>.>v.
>.v.>.>.>v
>v>.>..v>>
..v>v.v...
..>.>>vvv.
.>...v>v..
..v.v>>v.v
v.v.>...v.

...

After 10 steps:
..>..>>vv.
v.....>>.v
..v.v>>>v>
v>.>v.>>>.
..v>v.vv.v
.v.>>>.v..
v.v..>v>..
..v...>v.>
.vv..v>vv.

...

After 20 steps:
v>.....>>.
>vv>.....v
.>v>v.vv>>
v>>>v.>v.>
....vv>v..
.v.>>>vvv.
..v..>>vv.
v.v...>>.v
..v.....v>

...

After 30 steps:
.vv.v..>>>
v>...v...>
>.v>.>vv.>
>v>.>.>v.>
.>..v.vv..
..v>..>>v.
....v>..>v
v.v...>vv>
v.v...>vvv

...

After 40 steps:
>>v>v..v..
..>>v..vv.
..>>>v.>.v
..>>>>vvv>
v.....>...
v.v...>v>>
>vv.....v>
.>v...v.>v
vvv.v..v.>

...

After 50 steps:
..>>v>vv.v
..v.>>vv..
v.>>v>>v..
..>>>>>vv.
vvv....>vv
..v....>>>
v>.......>
.vv>....v>
.>v.vv.v..

...

After 55 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv...>..>
>vv.....>.
.>v.vv.v..

After 56 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv....>.>
>vv......>
.>v.vv.v..

After 57 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v..

After 58 steps:
..>>v>vv..
..v.>>vv..
..>>v>>vv.
..>>>>>vv.
v......>vv
v>v....>>v
vvv.....>>
>vv......>
.>v.vv.v..
```

In this example, the sea cucumbers stop moving after **`58`** steps.

> 在这个例子中，海参在 **`58`** 步后停止了移动。

Find somewhere safe to land your submarine. **What is the first step on which no sea cucumbers move?**

> 找一个安全的地方降落你的潜水艇。**第一个没有海参移动的步是哪一步？**

Your puzzle answer was `384`.

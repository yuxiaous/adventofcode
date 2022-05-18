# [Day 11: Dumbo Octopus](https://adventofcode.com/2021/day/11)

You enter a large cavern full of rare bioluminescent [dumbo octopuses](https://www.youtube.com/watch?v=eih-VSaS2g0)! They seem to not like the Christmas lights on your submarine, so you turn them off for now.

> 你进入了一个大洞穴，里面充满了稀有的会生物发光的[小飞象章鱼](https://www.youtube.com/watch?v=eih-VSaS2g0)！他们似乎不喜欢你潜水艇上的圣诞彩灯，所以你立刻把它们关掉了。

There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains **energy** over time and **flashes** brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.

> 有 100 只章鱼整齐地排列在 10 x 10 的网格中。随着时间的推移，每只章鱼会慢慢积攒**能量**，并在能量充满时**发光**一小会儿。虽然你的灯关了，但如果你能预测闪光何时发生，也许可以在不打扰章鱼的情况下穿过洞穴。

Each octopus has an **energy level** - your submarine can remotely measure the energy level of each octopus ([your puzzle input](day11.txt)). For example:

> 每只章鱼都有一个**能量等级** -- 你的潜水艇可以远程测量每只章鱼的能量等级（[你的谜题输入](day11.txt)）。例如：

```'
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
```

The energy level of each octopus is a value between `0` and `9`. Here, the top-left octopus has an energy level of `5`, the bottom-right one has an energy level of `6`, and so on.

> 每条章鱼的能量等级是一个介于 `0` 和 `9` 之间的值。在这里，左上角的章鱼的能量等级为 `5`，右下角的章鱼的能量等级为 `6`，以此类推。

You can model the energy levels and flashes of light in **steps**. During a single step, the following occurs:

> 你可以为能量等级和发光**步骤**进行建模。在单个步骤中，会发生以下情况：

- First, the energy level of each octopus increases by `1`.
- Then, any octopus with an energy level greater than `9` **flashes**. This increases the energy level of all adjacent octopuses by `1`, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than `9`, it **also flashes**. This process continues as long as new octopuses keep having their energy level increased beyond `9`. (An octopus can only flash **at most once per step**.)
- Finally, any octopus that flashed during this step has its energy level set to `0`, as it used all of its energy to flash.

> - 首先，每条章鱼的能量等级增加 `1`。
> - 然后，任何能量等级大于 `9` 的章鱼都会发光。这会让所有相邻的章鱼的能量等级增加 `1`（包括斜角相邻的章鱼）。如果这导致一只章鱼的能量等级大于 `9`，那么它**也会发光**。只要新章鱼能够持续获得能量并且使得能量等级超过 `9`，这个过程就会一直持续下去。（一只章鱼每一步最多只能发光一次。）
> - 最后，任何在此步骤中发光的章鱼都将其能量等级恢复为 `0`，因为它使用了所有的能量来发光。

Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy. Consider the middle octopus with `1` energy in this situation:

> 相邻的闪光可能会导致一只章鱼在这一步直接发光，即使它在步骤开始时只有很少的能量。考虑在这种情况下能量为 `1` 的中间那只章鱼：

```'
Before any steps:
11111
19991
19191
19991
11111

After step 1:
34543
40004
50005
40004
34543

After step 2:
45654
51115
61116
51115
45654
```

An octopus is **highlighted** when it flashed during the given step.

> 当章鱼在给定步骤中发光时，它会被**高亮显示**（由于markdown限制，这里无法像原文一样高亮显示）。

Here is how the larger example above progresses:

> 这里是一个更大的例子的发展过程：

```'
Before any steps:
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

After step 1:
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637

After step 2:
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848

After step 3:
0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000

After step 4:
2263031977
0923031697
0032221150
0041111163
0076191174
0053411122
0042361120
5532241122
1532247211
1132230211

After step 5:
4484144000
2044144000
2253333493
1152333274
1187303285
1164633233
1153472231
6643352233
2643358322
2243341322

After step 6:
5595255111
3155255222
3364444605
2263444496
2298414396
2275744344
2264583342
7754463344
3754469433
3354452433

After step 7:
6707366222
4377366333
4475555827
3496655709
3500625609
3509955566
3486694453
8865585555
4865580644
4465574644

After step 8:
7818477333
5488477444
5697666949
4608766830
4734946730
4740097688
6900007564
0000009666
8000004755
6800007755

After step 9:
9060000644
7800000976
6900000080
5840000082
5858000093
6962400000
8021250009
2221130009
9111128097
7911119976

After step 10:
0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000
```

After step 10, there have been a total of `204` flashes. Fast forwarding, here is the same configuration every 10 steps:

> 在 10 步之后，总共有 `204` 次发光。快速推演，这里使用相同的配置模拟每 10 步的样子：

```'
After step 20:
3936556452
5686556806
4496555690
4448655580
4456865570
5680086577
7000009896
0000000344
6000000364
4600009543

After step 30:
0643334118
4253334611
3374333458
2225333337
2229333338
2276733333
2754574565
5544458511
9444447111
7944446119

After step 40:
6211111981
0421111119
0042111115
0003111115
0003111116
0065611111
0532351111
3322234597
2222222976
2222222762

After step 50:
9655556447
4865556805
4486555690
4458655580
4574865570
5700086566
6000009887
8000000533
6800000633
5680000538

After step 60:
2533334200
2743334640
2264333458
2225333337
2225333338
2287833333
3854573455
1854458611
1175447111
1115446111

After step 70:
8211111164
0421111166
0042111114
0004211115
0000211116
0065611111
0532351111
7322235117
5722223475
4572222754

After step 80:
1755555697
5965555609
4486555680
4458655580
4570865570
5700086566
7000008666
0000000990
0000000800
0000000000

After step 90:
7433333522
2643333522
2264333458
2226433337
2222433338
2287833333
2854573333
4854458333
3387779333
3333333333

After step 100:
0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766
```

After 100 steps, there have been a total of **`1656`** flashes.

> 在 100 步之后，总共有 **`1656`** 次发光。

Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. **How many total flashes are there after 100 steps?**

> 给定洞穴中小飞象章鱼的起始能量等级，模拟 100 步。**在 100 步之后总共发光了多少次？**

Your puzzle answer was `1749`.

## --- Part Two ---

It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be **synchronizing**!

> 似乎零星的闪光还不够亮，无法导航。但是，你可能有更好的选择：闪光似乎是可以同步的！

In the example above, the first time all octopuses flash simultaneously is step **`195`**:

> 在上面的例子中，所有章鱼第一次同时发光是在第 **`195`** 步时：

```'
After step 193:
5877777777
8877777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777
7777777777

After step 194:
6988888888
9988888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888
8888888888

After step 195:
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
```

If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. **What is the first step during which all octopuses flash?**

> 如果你能计算出章鱼同时发光的确切时刻，你应该能够导航并穿过洞穴。**第一次所有章鱼同时发光时是第几步？**

Your puzzle answer was `285`.

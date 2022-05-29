# [Day 22: Reactor Reboot](https://adventofcode.com/2021/day/22)

> 第22天：反应堆重启

Operating at these extreme ocean depths has overloaded the submarine's reactor; it needs to be rebooted.

> 在这种极端的海洋深度航行使潜水艇的反应堆超载了，它需要重新启动。

The reactor core is made up of a large 3-dimensional grid made up entirely of cubes, one cube per integer 3-dimensional coordinate (`x,y,z`). Each cube can be either **on** or **off**; at the start of the reboot process, they are all **off**. (Could it be an old model of a reactor you've seen [before](https://adventofcode.com/2020/day/17)?)

> 反应堆核心由一个大型的 3 维网格组成，每个网格都是一个正方体，每个正方体都有一个整数的 3 维坐标 (`x,y,z`)。每个正方体可以是**开启**的或**关闭**的，在重新启动过程开始时，它们都是**关闭**的。（这可能是你[之前](https://adventofcode.com/2020/day/17)见过的反应堆的旧模型吗？）

To reboot the reactor, you just need to set all of the cubes to either **on** or **off** by following a list of **reboot steps** ([your puzzle input](day22.txt)). Each step specifies a [cuboid](https://en.wikipedia.org/wiki/Cuboid) (the set of all cubes that have coordinates which fall within ranges for `x`, `y`, and `z`) and whether to turn all of the cubes in that cuboid **on** or **off**.

> 要重新启动反应堆，你只需要按照**重新启动步骤**（[你的谜题输入](day22.txt)）将所有的正方体设置为**开启**或**关闭**。每一步都指定一个[长方体](https://en.wikipedia.org/wiki/Cuboid)（坐标在 `x`、`y` 和 `z` 所指定的范围内的所有正方体的集合）并确定是否将长方体中的所有正方体**开启**或**关闭**。

For example, given these reboot steps:

> 例如，给定这些重启步骤：

```'
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
```

The first step (`on x=10..12,y=10..12,z=10..12`) turns **on** a 3x3x3 cuboid consisting of 27 cubes:

> 第一步（`on x=10..12,y=10..12,z=10..12`）**开启**了一个由 27 个正方体组成的 3x3x3 长方体：

- `10,10,10`
- `10,10,11`
- `10,10,12`
- `10,11,10`
- `10,11,11`
- `10,11,12`
- `10,12,10`
- `10,12,11`
- `10,12,12`
- `11,10,10`
- `11,10,11`
- `11,10,12`
- `11,11,10`
- `11,11,11`
- `11,11,12`
- `11,12,10`
- `11,12,11`
- `11,12,12`
- `12,10,10`
- `12,10,11`
- `12,10,12`
- `12,11,10`
- `12,11,11`
- `12,11,12`
- `12,12,10`
- `12,12,11`
- `12,12,12`

The second step (`on x=11..13,y=11..13,z=11..13`) turns **on** a 3x3x3 cuboid that overlaps with the first. As a result, only 19 additional cubes turn on; the rest are already on from the previous step:

> 第二步（`on x=11..13,y=11..13,z=11..13`）**开启**了一个与第一个长方体部分重叠的 3x3x3 长方体。结果，只有 19 个新的正方体被开启，其余的已经在上一步开启过了：

- `11,11,13`
- `11,12,13`
- `11,13,11`
- `11,13,12`
- `11,13,13`
- `12,11,13`
- `12,12,13`
- `12,13,11`
- `12,13,12`
- `12,13,13`
- `13,11,11`
- `13,11,12`
- `13,11,13`
- `13,12,11`
- `13,12,12`
- `13,12,13`
- `13,13,11`
- `13,13,12`
- `13,13,13`

The third step (`off x=9..11,y=9..11,z=9..11`) turns **off** a 3x3x3 cuboid that overlaps partially with some cubes that are on, ultimately turning off 8 cubes:

> 第三步（`off x=9..11,y=9..11,z=9..11`）**关闭**了一个 3x3x3 的长方体，它与一些已经开启的正方体部分重叠，最终关闭了 8 个正方体：

- `10,10,10`
- `10,10,11`
- `10,11,10`
- `10,11,11`
- `11,10,10`
- `11,10,11`
- `11,11,10`
- `11,11,11`

The final step (`on x=10..10,y=10..10,z=10..10`) turns **on** a single cube, `10,10,10`. After this last step, **`39`** cubes are **on**.

> 最后一步（`on x=10..10,y=10..10,z=10..10`）**开启**了一个单正方体：`10,10,10`。在这步之后，有 **`39`** 个正方体是**开启**的。

The initialization procedure only uses cubes that have `x`, `y`, and `z` positions of at least `-50` and at most `50`. For now, ignore cubes outside this region.

> 初始化过程仅使用 `x`、`y` 和 `z` 坐标从最小为 `-50` 到最大为 `50` 之间的正方体。现在，忽略该区域之外的正方体。

Here is a larger example:

> 这里是一个更大的例子：

```'
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
```

The last two steps are fully outside the initialization procedure area; all other steps are fully within it. After executing these steps in the initialization procedure region, **`590784`** cubes are **on**.

> 最后两步完全是在初始化过程区域之外的，而其他的所有步骤都在其中。在执行完成初始化过程区域中的这些步骤之后，有 **`590784`** 个正方体是**开启**的。

Execute the reboot steps. Afterward, considering only cubes in the region `x=-50..50,y=-50..50,z=-50..50`, **how many cubes are on?**

> 执行重启步骤。在此之后，只考虑 `x=-50..50,y=-50..50,z=-50..50` 区域中的立方体，**有多少个正方体是开启的？**

Your puzzle answer was `556501`.

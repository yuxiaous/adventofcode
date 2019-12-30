# [Day 6: Universal Orbit Map](https://adventofcode.com/2019/day/6)

> 第6天：环球轨道地图

You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits ([your puzzle input](day6.txt)).

> 你已登陆到了水星的环球轨道地图设施。由于太空导航经常涉及在轨道之间迁移，因此此处的轨道地图对于查找你和圣诞老人之间的有效路线是非常有用。你下载了一份本地轨道地图（[你的谜题输入](day6.txt)）。

Except for the universal Center of Mass (`COM`), every object in space is in orbit around exactly one other object. An [orbit](https://en.wikipedia.org/wiki/Orbit) looks roughly like this:

> 除了环球的质量中心（`COM`），太空中的每个物体都环绕另一个物体在轨道上运动。一条[轨道](https://en.wikipedia.org/wiki/Orbit)看上去大致如下所示：

```'
                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
```

In this diagram, the object `BBB` is in orbit around `AAA`. The path that `BBB` takes around `AAA` (drawn with lines) is only partly shown. In the map data, this orbital relationship is written `AAA)BBB`, which means "`BBB` is in orbit around `AAA`".

> 在这张图中，物体 `BBB` 在环绕 `AAA` 的轨道上。`BBB` 环绕 `AAA` 的路径（用线绘制）只显示了一部分。在地图数据中，把这种轨道关系记为 `AAA)BBB`，表示“`BBB` 在环绕 `AAA` 的轨道上”。

Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, the Universal Orbit Map facility uses **orbit count checksums** - the total number of **direct orbits** (like the one shown above) and **indirect orbits**.

> 在使用地图数据策划航线之前，你需要确保地图在下载过程中没有损坏。为了验证地图，环球轨道地图设施使用了**轨道计数校验和** —— **直接轨道**（类似上图）和**间接轨道**的总数。

Whenever `A` orbits `B` and `B` orbits `C`, then `A` **indirectly orbits** `C`. This chain can be any number of objects long: if `A` orbits `B`, `B` orbits `C`, and `C` orbits `D`, then `A` indirectly orbits `D`.

> 只要 `A` 环绕 `B`，`B` 环绕 `C`，则 `A` **间接环绕** `C`。这条链可以有任意长度：如果 `A` 环绕 `B`，`B` 环绕 `C` 并且 `C` 环绕 `D`，则 `A` 间接环绕 `D`。

For example, suppose you have the following map:

> 举个例子，假设你有以下地图：

```'
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
```

Visually, the above map of orbits looks like this:

> 在视觉上，上面的轨道地图看上去是下面这样的：

```'
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
```

In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.

> 在此视觉表示中，当两个物体通过一条线连接时，右侧的物体直接环绕左侧的物体。

Here, we can count the total number of orbits as follows:

- `D` directly orbits `C` and indirectly orbits `B` and `COM`, a total of `3` orbits.
- `L` directly orbits `K` and indirectly orbits `J`, `E`, `D`, `C`, `B`, and `COM`, a total of `7` orbits.
- `COM` orbits nothing.

> 在这里，我们可以计算出轨道总数，如下：
>
> - `D` 直接环绕 `C`，间接环绕 `B` 和 `COM`，总共有 `3` 条轨道。
> - `L` 直接绕着 `K`，间接环绕 `J`、`E`、`D`、`C`、`B` 和 `COM`，总共有 `7` 条轨道。
> - `COM` 没有环绕任何东西。

The total number of direct and indirect orbits in this example is **`42`**.

> 在此示例中，直接和间接的轨道总数为 **`42`**。

**What is the total number of direct and indirect orbits** in your map data?

> 在你的地图数据中，**直接和间接轨道的总数是多少**？

Your puzzle answer was `227612`.

## Part Two

Now, you just need to figure out how many **orbital transfers** you (`YOU`) need to take to get to Santa (`SAN`).

> 现在，你只需要弄清楚你（`YOU`）需要多少次**轨道迁移**才能到达圣诞老人（`SAN`）那里。

You start at the object `YOU` are orbiting; your destination is the object `SAN` is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

> 你的起始点在物体 `YOU` 处环绕，你的目的地在物体 `SAN` 处环绕。轨道迁移可以让你从一个物体所在地迁移到另一个物体（环绕其他物体或被其他物体环绕）所在地。

For example, suppose you have the following map:

> 举个例子，假设你有以下地图：

```'
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
```

Visually, the above map of orbits looks like this:

> 在视觉上，上面的轨道地图看上去是下面这样的：

```diff
                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
```

In this example, `YOU` are in orbit around `K`, and `SAN` is in orbit around `I`. To move from `K` to `I`, a minimum of `4` orbital transfers are required:

- `K` to `J`
- `J` to `E`
- `E` to `D`
- `D` to `I`

> 在此示例中，`YOU` 在 `K` 的轨道上，而 `SAN` 在 `I` 的轨道上。要从 `K` 移动到 `I`，至少需要进行 `4` 次轨道迁移：
>
> - `K` 到 `J`
> - `J` 到 `E`
> - `E` 到 `D`
> - `D` 到 `I`

Afterward, the map of orbits looks like this:

> 之后，轨道地图如下所示：

```'
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
```

**What is the minimum number of orbital transfers required** to move from the object `YOU` are orbiting to the object `SAN` is orbiting? (Between the objects they are orbiting - **not** between `YOU` and `SAN`.)

> 从物体 `YOU` 的轨道迁移到物体 `SAN` 的轨道 **所需的最少轨道迁移次数是多少**？（在它们所绕行的物体之间，**而不是** `YOU` 和 `SAN` 之间。）

Your puzzle answer was `454`.

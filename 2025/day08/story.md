# Day 8: Playground

> 第八天：游乐场

Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

> 掌握了传送器维护的新知识后，你自信地踏上了修好的传送器平台。

You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

> 你在一个陌生的传送器平台上重新实体化，发现自己身处一个巨大的地下空间，里面有一个超大的游乐场！

Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical [junction boxes](https://en.wikipedia.org/wiki/Junction_box).

> 在游乐场对面，一群精灵正在筹备一个雄心勃勃的圣诞节装饰项目。通过精心的吊装，他们悬挂了大量的小型电气[接线盒](https://en.wikipedia.org/wiki/Junction_box)。

Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

> 他们的计划是用长长的灯串将接线盒连接起来。大多数接线盒本身不供电；但是，当两个接线盒通过灯串连接时，电流就可以在这两个接线盒之间流通。

The Elves are trying to figure out **which junction boxes to connect** so that electricity can reach **every** junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

> 精灵们正在尝试弄清楚**应该连接哪些接线盒**，以便电流能够到达**每一个**接线盒。他们甚至列出了所有接线盒在三维空间中的位置（你的谜题输入）。

For example:

> 例如：

```
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
```

This list describes the position of 20 junction boxes, one per line. Each position is given as `X,Y,Z` coordinates. So, the first junction box in the list is at `X=162`, `Y=817`, `Z=812`.

> 这个列表描述了 20 个接线盒的位置，每行一个。每个位置以 `X,Y,Z` 坐标给出。因此，列表中的第一个接线盒位于 `X=162`，`Y=817`，`Z=812`。

To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are **as close together as possible** according to [straight-line distance](https://en.wikipedia.org/wiki/Euclidean_distance). In this example, the two junction boxes which are closest together are `162,817,812` and `425,690,689`.

> 为了节省灯串，精灵们希望根据[直线距离](https://en.wikipedia.org/wiki/Euclidean_distance)连接**尽可能靠近**的一对接线盒。在这个例子中，最靠近的两个接线盒是 `162,817,812` 和 `425,690,689`。

By connecting these two junction boxes together, because electricity can flow between them, they become part of the same **circuit**. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

> 将这两个接线盒连接在一起，由于电流可以在它们之间流动，它们就成了同一个**电路**的一部分。连接后，就形成了一个包含两个接线盒的电路，其余 18 个接线盒仍各自独立成电路。

Now, the two junction boxes which are closest together but aren't already directly connected are `162,817,812` and `431,825,988`. After connecting them, since `162,817,812` is already connected to another junction box, there is now a single circuit which contains **three** junction boxes and an additional 17 circuits which contain one junction box each.

> 现在，距离最近但尚未直接连接的两个接线盒是 `162,817,812` 和 `431,825,988`。连接它们后，由于 `162,817,812` 已经与另一个接线盒相连，现在就形成了一个包含**三个**接线盒的电路，以及另外 17 个各包含一个接线盒的电路。

The next two junction boxes to connect are `906,360,560` and `805,96,715`. After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

> 接下来要连接的两个接线盒是 `906,360,560` 和 `805,96,715`。连接它们后，有一个包含 3 个接线盒的电路，一个包含 2 个接线盒的电路，以及 15 个各包含一个接线盒的电路。

The next two junction boxes are `431,825,988` and `425,690,689`. Because these two junction boxes were **already in the same circuit**, nothing happens!

> 接下来的两个接线盒是 `431,825,988` 和 `425,690,689`。由于这两个接线盒**已经在同一个电路中**，所以什么也不会发生！

This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. They would like to know how big the circuits will be.

> 这个过程持续了一段时间，精灵们担心他们没有足够的延长线来连接所有这些电路。他们想知道电路会有多大。

After making the ten shortest connections, there are 11 circuits: one circuit which contains **5** junction boxes, one circuit which contains **4** junction boxes, two circuits which contain **2** junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces **`40`**.

> 在建立了十个最短的连接之后，共有 11 个电路：一个包含**5**个接线盒的电路，一个包含**4**个接线盒的电路，两个各包含**2**个接线盒的电路，以及七个各包含单个接线盒的电路。将三个最大电路的大小相乘（5、4 以及一个大小为 2 的电路）得到 **`40`**。

Your list contains many junction boxes; connect together the **1000** pairs of junction boxes which are closest together. Afterward, **what do you get if you multiply together the sizes of the three largest circuits?**

> 你的列表包含许多接线盒；将距离最近的**1000**对接线盒连接起来。之后，**如果将三个最大电路的大小相乘，你会得到什么？**

Your puzzle answer was `46398`.

## Part Two

The Elves were right; they **definitely** don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in **one large circuit**.

> 精灵们说得没错；他们**确实**没有足够的延长线。你需要继续将接线盒连接起来，直到它们全部组成**一个大电路**。

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at `216,146,977` and `117,168,530`. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (`216` and `117`) produces **`25272`**.

> 继续上面的例子，使所有接线盒形成一个单一电路的第一个连接是位于 `216,146,977` 和 `117,168,530` 的两个接线盒之间。精灵们需要知道这些接线盒离墙有多远，以便选择合适的延长线；将这两个接线盒的 X 坐标（`216` 和 `117`）相乘得到 **`25272`**。

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. **What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?**

> 继续将距离最近的未连接接线盒对连接起来，直到它们全部归于同一个电路。**将最后需要连接的两个接线盒的 X 坐标相乘，你会得到什么？**

Your puzzle answer was `8141888143`.

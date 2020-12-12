# Day 12: Rain Risk

> 第十二天：降雨风险

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take **evasive actions**!

> 你的渡轮正顺利地开往海岛，但没人想到一场暴风雨突如其来。渡轮需要进行回避行动！

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the [PA system](https://en.wikipedia.org/wiki/Public_address_system) to ask if anyone can help, you quickly volunteer.

> 不幸的是，渡轮的导航计算机似乎发生了故障，它并没有给出通往安全的航线，而是给出了极其兜圈子的指令。当机长使用 [PA 系统](https://en.wikipedia.org/wiki/Public_address_system)询问是否有人可以提供帮助时，你迅速成为了志愿。

The navigation instructions ([your puzzle input](day12.txt)) consists of a sequence of single-character **actions** paired with integer input **values**. After staring at them for a few minutes, you work out what they probably mean:

- Action **`N`** means to move **north** by the given value.
- Action **`S`** means to move **south** by the given value.
- Action **`E`** means to move **east** by the given value.
- Action **`W`** means to move **west** by the given value.
- Action **`L`** means to turn **left** the given number of degrees.
- Action **`R`** means to turn **right** the given number of degrees.
- Action **`F`** means to move **forward** by the given value in the direction the ship is currently facing.

> 导航指令（[你的谜题输入](day12.txt)）是一串由单字符作为动作与整数作为输入值组成的。在凝视几分钟后，你破解出了它们可能的含义：
>
> - 动作 **`N`** 表示向北移动给定距离。
> - 动作 **`S`** 表示向南移动给定距离。
> - 动作 **`E`** 表示向东移动给定距离。
> - 动作 **`W`** 表示向西移动给定距离。
> - 动作 **`L`** 表示向左转动给定角度。
> - 动作 **`R`** 表示向右转动给定角度。
> - 动作 **`F`** 表示沿着船当前所面对的方向向前移动给定距离。

The ship starts by facing **east**. Only the `L` and `R` actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is `N10`, the ship would move north 10 units, but would still move east if the following action were `F`.)

> 船开始时面向东方。只有 `L` 和 `R` 动作会改变船面向的方向。（也就是说，如果船面向东方，而下一条指令是 `N10`，则船将向北移动 10 个单位，但如果随后的动作为 `F`，则仍将向东移动。）

For example:

> 举个例子：

```'
F10
N3
F7
R90
F11
```

These instructions would be handled as follows:

- `F10` would move the ship 10 units east (because the ship starts by facing east) to **east 10, north 0**.
- `N3` would move the ship 3 units north to **east 10, north 3**.
- `F7` would move the ship another 7 units east (because the ship is still facing east) to **east 17, north 3**.
- `R90` would cause the ship to turn right by 90 degrees and face **south**; it remains at **east 17, north 3**.
- `F11` would move the ship 11 units south to **east 17, south 8**.

> 这些指令将按以下方式处理：
>
> - `F10` 将船向东移动 10 个单位（因为船开始时面向东方）到达 **东10，北0**。
> - `N3` 将船向北移动 3 个单位，到达 **东10，北3**。
> - `F7` 将船向东再移动 7 个单位（因为船仍旧面向东方），到达 **东17，北3**。
> - `R90` 将使船右转 90 度并面向 **南**，它仍就位于 **东17，北3**。
> - `F11` 会将船向南移动 11 个单位，到达 **东17，向南8**。

At the end of these instructions, the ship's [Manhattan distance](https://en.wikipedia.org/wiki/Manhattan_distance) (sum of the absolute values of its east/west position and its north/south position) from its starting position is `17 + 8` = **`25`**.

> 结束所有的指令，船从起点到终点的[曼哈顿距离](https://en.wikipedia.org/wiki/Manhattan_distance) （东西方向和北南方向的绝对值之和）为 `17 + 8` = **`25`**。

Figure out where the navigation instructions lead. **What is the Manhattan distance between that location and the ship's starting position?**

> 弄明白导航指令的终点在哪。船的终点与起点之间的曼哈顿距离是多少？

Your puzzle answer was `508`.

## --- Part Two ---

Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

> 在你将目的地告诉船长之前，你发现实际的动作含义原来都印在指令的背面。

Almost all of the actions indicate how to move a **waypoint** which is relative to the ship's position:

- Action **`N`** means to move the waypoint **north** by the given value.
- Action **`S`** means to move the waypoint **south** by the given value.
- Action **`E`** means to move the waypoint **east** by the given value.
- Action **`W`** means to move the waypoint **west** by the given value.
- Action **`L`** means to rotate the waypoint around the ship **left** (**counter-clockwise**) the given number of degrees.
- Action **`R`** means to rotate the waypoint around the ship **right** (**clockwise**) the given number of degrees.
- Action **`F`** means to move **forward** to the waypoint a number of times equal to the given value.

> 几乎所有动作都指示如何移动到一个相对于船舶位置的航标：
>
> - 动作 **`N`** 表示将航标向北移动给定距离。
> - 动作 **`S`** 表示将航标向南移动给定距离。
> - 动作 **`E`** 表示将航标向东移动给定距离。
> - 动作 **`W`** 表示将航标向西移动给定距离。
> - 动作 **`L`** 表示将航标绕船向左（逆时针）旋转给定角度。
> - 动作 **`R`** 表示将航标绕船向右（顺时针）旋转给定角度。
> - 动作 **`F`** 表示朝向航标前进给定次数。

The waypoint starts **10 units east and 1 unit north** relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

> 航标开始时相对于船的位置在 **向东 10 单位，向北 1 单位** 处。航标是相对于船的，也就是说，如果船移动，航标也会随之移动。

For example, using the same instructions as above:

- `F10` moves the ship to the waypoint 10 times (a total of **100 units east and 10 units north**), leaving the ship at **east 100, north 10**. The waypoint stays 10 units east and 1 unit north of the ship.
- `N3` moves the waypoint 3 units north to **10 units east and 4 units north of the ship**. The ship remains at **east 100, north 10**.
- `F7` moves the ship to the waypoint 7 times (a total of **70 units east and 28 units north**), leaving the ship at **east 170, north 38**. The waypoint stays 10 units east and 4 units north of the ship.
- `R90` rotates the waypoint around the ship clockwise 90 degrees, moving it to **4 units east and 10 units south of the ship**. The ship remains at **east 170, north 38**.
- `F11` moves the ship to the waypoint 11 times (a total of **44 units east and 110 units south**), leaving the ship at **east 214, south 72**. The waypoint stays 4 units east and 10 units south of the ship.

> 举个例子，使用与上面相同的指令：
>
> - `F10` 将船朝向航标移动 10 次（总计 **向东 100 单位，向北 10 单位**），船移动至 **东100，北10**。航标保持向东 10 单位，相北 1 单位。
> - `N3` 将航标向北移动 3 单位至 **向东 10 单位，向北 4 单位**。船仍旧位于 **东100，北10**。
> - `F7` 将船朝向航标移动 7 次（总计 **向东 70 单位，向北 28 单位**），将船移至**东170，北38个**。航标保持向东 10 单位，向北 4 单位。
> - `R90` 将航标绕船顺时针旋转 90 度，移至 **向东 4 单位，向南 10 单位**。船仍旧位于 **东170，北38**。
> - `F11` 将船朝向航标移动 11 次（总计 **向东 44 单位，向南 110 单位**），船移动至 **东214，南72**。 航标保持向东 4 单位，向南 10 单位。

After these operations, the ship's Manhattan distance from its starting position is `214 + 72` = **`286`**.

完成这些操作后，船从起点到终点的曼哈顿距离为 `214 + 72` = **`286`**。

Figure out where the navigation instructions actually lead. **What is the Manhattan distance between that location and the ship's starting position?**

> 弄明白导航实际指令的终点在哪。船的终点与起点之间的曼哈顿距离是多少？

Your puzzle answer was `30761`.

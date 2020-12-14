# Day 13: Shuttle Search

> 第十三天：班车搜索

Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship, you discover that no ships embark from that port to your vacation island. You'll need to get from the port to the nearest airport.

> 你的渡轮安全抵达了附近的一个港口，这里离你的目的地不远了。当你打电话准备预定另一艘船时，你发现这里没有航线前往你的度假小岛。你需要从这个港口去最近的机场。

Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! Each bus has an ID number that also indicates **how often the bus leaves for the airport**.

> 幸运的是，一个班车服务可将你从港口带到机场！每辆巴士都有一个 ID 号码，另外该 ID 号码还表示巴士出发去机场的频率。

Bus schedules are defined based on a **timestamp** that measures the **number of minutes** since some fixed reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the airport, then various other locations, and finally returns to the sea port to repeat its journey forever.

> 巴士时刻表是根据时间点定义的，该时间点用于表示从过去某个固定参考点以来的分钟数。从时间点 0 开始，所有巴士同时从海港出发。此后，每辆巴士先到达机场，再去其他不同的地方，最后返回海港，不断重复行程。

The time this loop takes a particular bus is also its ID number: the bus with ID `5` departs from the sea port at timestamps `0`, `5`, `10`, `15`, and so on. The bus with ID `11` departs at `0`, `11`, `22`, `33`, and so on. If you are there when the bus departs, you can ride that bus to the airport!

> 这个特定巴士的循环时间也是它的 ID 号码：ID 号码为 `5` 的巴士在 `0`、`5`、`10`、`15` 等时间点（依此类推）从海港出发。ID 号码为 `11` 的巴士从 `0`、`11`、`22`、`33` 等时间点（依此类推）出发。当巴士出发时如果你正好在那儿，你可以乘坐那辆巴士去机场！

Your notes ([your puzzle input](day13.txt)) consist of two lines. The first line is your estimate of the **earliest timestamp you could depart on a bus**. The second line lists the bus IDs that are in service according to the shuttle company; entries that show `x` must be out of service, so you decide to ignore them.

> 你的笔记（[您的谜题输入](day13.txt)）由两行组成。第一行是你预计的可以乘坐巴士出发的最早时间点。第二行列出了班车公司公布的使用中的巴士 ID，显示为 `x` 的条目想必已经停止了服务，因此你决定忽略它们。

To save time once you arrive, your goal is to figure out **the earliest bus you can take to the airport**. (There will be exactly one such bus.)

> 为了节省时间，当你到达后，你的目标是弄清楚你可以乘坐去机场的最早巴士。（将会只有一辆这样的巴士。）

For example, suppose you have the following notes:

> 举个例子，假设你有如下笔记：

```'
939
7,13,x,x,59,x,31,19
```

Here, the earliest timestamp you could depart is `939`, and the bus IDs in service are `7`, `13`, `59`, `31`, and `19`. Near timestamp `939`, these bus IDs depart at the times marked `D`:

> 在这个例子中，你可以出发的最早时间点是 `939`，且可以乘坐的巴士 ID 有 `7`、`13`、`59`、`31` 和 `19`。在时间点 `939` 附近，这些巴士 ID 的出发时间点上标记了 `D` ：

```'
time   bus 7   bus 13  bus 59  bus 31  bus 19
929      .       .       .       .       .
930      .       .       .       D       .
931      D       .       .       .       D
932      .       .       .       .       .
933      .       .       .       .       .
934      .       .       .       .       .
935      .       .       .       .       .
936      .       D       .       .       .
937      .       .       .       .       .
938      D       .       .       .       .
939      .       .       .       .       .
940      .       .       .       .       .
941      .       .       .       .       .
942      .       .       .       .       .
943      .       .       .       .       .
944      .       .       D       .       .
945      D       .       .       .       .
946      .       .       .       .       .
947      .       .       .       .       .
948      .       .       .       .       .
949      .       D       .       .       .
```

The earliest bus you could take is bus ID `59`. It doesn't depart until timestamp `944`, so you would need to wait `944 - 939 = 5` minutes before it departs. Multiplying the bus ID by the number of minutes you'd need to wait gives **`295`**.

> 你可以乘坐的最早一班巴士的 ID 为 `59`。它直到时间点 `944` 才出发，因此你需要等待 `944 - 939 = 5` 分钟。将巴士 ID 乘以你需要等待的分钟数得到 **`295`**。

**What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?**

> 你可以乘搭的最早一班去机场的巴士 ID 乘以你等待巴士的分钟数的乘积是多少？

Your puzzle answer was `1895`.

## --- Part Two ---

The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute. (The first line in your input is no longer relevant.)

> 班车公司正在举办一个竞赛：任何人如果能够找到满足条件的最早时间点就可以获得一枚金币的奖励，就是满足在第一个巴士 ID 离开后，后面列出的每个巴士 ID 在随后的每分钟依次离开的第一个时间点。（你的输入的第一行不再使用。）

For example, suppose you have the same list of bus IDs as above:

> 举个例子，假如你有与上面相同的巴士 ID 列表：

```'
7,13,x,x,59,x,31,19
```

An `x` in the schedule means there are no constraints on what bus IDs must depart at that time.

> 时刻表中的 `x` 表示在那个时间点没有规定必须出发的巴士 ID。

This means you are looking for the earliest timestamp (called `t`) such that:

- Bus ID `7` departs at timestamp `t`.
- Bus ID `13` departs one minute after timestamp `t`.
- There are no requirements or restrictions on departures at two or three minutes after timestamp `t`.
- Bus ID `59` departs four minutes after timestamp `t`.
- There are no requirements or restrictions on departures at five minutes after timestamp `t`.
- Bus ID `31` departs six minutes after timestamp `t`.
- Bus ID `19` departs seven minutes after timestamp `t`.

> 这表示你正在寻找的最早时间点（称为 `t`）满足：
>
> - 巴士 ID `7` 在时间点 `t` 出发。
> - 巴士 ID `13` 在时间点 `t` 之后的一分钟出发。
> - 没有巴士被要求或限制在时间点 `t` 之后的两分钟或三分钟出发 。
> - 巴士 ID `59` 在时间点 `t` 之后的四分钟出发。
> - 没有巴士被要求或限制在时间点 `t` 之后的五分钟出发。
> - 巴士 ID `31` 在时间点 `t` 之后的六分钟出发。
> - 巴士 ID `19` 在时间点 `t` 之后的七分钟出发。

The only bus departures that matter are the listed bus IDs at their specific offsets from `t`. Those bus IDs can depart at other times, and other bus IDs can depart at those times. For example, in the list above, because bus ID `19` must depart seven minutes after the timestamp at which bus ID `7` departs, bus ID `7` will always **also** be departing with bus ID `19` at seven minutes after timestamp `t`.

> 唯一需要关注的是列表中与时间点 `t` 有特殊间隔的巴士 ID。这些巴士 ID 可能与其他巴士 ID 在同一个时间点出发。例如，在上面的列表中，由于巴士 ID `19` 在必须在巴士 ID `7` 出发时间点之后的七分钟出发，因此巴士 ID `7` 也将与巴士 ID `19` 一起在时间点 `t` 之后的七分钟出发。

In this example, the earliest timestamp at which this occurs is **`1068781`**:

> 在这个例子中，发生这种情况的最早时间点 **`1068781`**：

```'
time     bus 7   bus 13  bus 59  bus 31  bus 19
1068773    .       .       .       .       .
1068774    D       .       .       .       .
1068775    .       .       .       .       .
1068776    .       .       .       .       .
1068777    .       .       .       .       .
1068778    .       .       .       .       .
1068779    .       .       .       .       .
1068780    .       .       .       .       .
1068781    D       .       .       .       .
1068782    .       D       .       .       .
1068783    .       .       .       .       .
1068784    .       .       .       .       .
1068785    .       .       D       .       .
1068786    .       .       .       .       .
1068787    .       .       .       D       .
1068788    D       .       .       .       D
1068789    .       .       .       .       .
1068790    .       .       .       .       .
1068791    .       .       .       .       .
1068792    .       .       .       .       .
1068793    .       .       .       .       .
1068794    .       .       .       .       .
1068795    D       D       .       .       .
1068796    .       .       .       .       .
1068797    .       .       .       .       .
```

In the above example, bus ID `7` departs at timestamp `1068788` (seven minutes after `t`). This is fine; the only requirement on that minute is that bus ID `19` departs then, and it does.

> 在上面的例子中，巴士 ID `7` 在时间点 `1068788`（`t` 之后的七分钟）出发。这没问题，对于那一分钟的唯一要求是巴士 ID `19` 也接着出发。

Here are some other examples:

- The earliest timestamp that matches the list `17,x,13,19` is **`3417`**.
- `67,7,59,61` first occurs at timestamp **`754018`**.
- `67,x,7,59,61` first occurs at timestamp **`779210`**.
- `67,7,x,59,61` first occurs at timestamp **`1261476`**.
- `1789,37,47,1889` first occurs at timestamp **`1202161486`**.

> 这里有一些其他例子：
>
> - 与列表 `17，x，13,19` 相匹配的最早时间点是 **`3417`**。
> - `67,7,59,61` 首先出现在时间点 **`754018`**。
> - `67，x，7,59,61` 首先出现在时间点 **`779210`**。
> - `67,7,x,59,61` 首先出现在时间点 **`1261476`** 。
> - `1789,37,47,1889` 首先出现在时间点 **`1202161486`**。

However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than `100000000000000`!

> 事实上，你的列表中有如此之多的巴士 ID，那么实际的最早时间点将会大于 `100000000000000`！

**What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?**

> 满足列表中所有的巴士 ID 按照它们在列表中的位置依次出发这个条件的最早时间点是什么？

Your puzzle answer was `840493039281088`.

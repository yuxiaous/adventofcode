# Day 23: LAN Party
> # 第二十三天：局域网派对

As The Historians wander around a secure area at Easter Bunny HQ, you come across posters for a [LAN party](https://en.wikipedia.org/wiki/LAN_party) scheduled for today! Maybe you can find it; you connect to a nearby [datalink port](https://adventofcode.com/2016/day/9) and download a map of the local network (your puzzle input).
> 当历史学家们在复活节兔子总部的安全区域四处游荡时，你发现了今天举办的[局域网派对](https://en.wikipedia.org/wiki/LAN_party)的海报！也许你能找到它；你连接到附近的[数据链路端口](https://adventofcode.com/2016/day/9)，下载了一份本地网络的地图（你的谜题输入）。

The network map provides a list of every **connection between two computers**. For example:
> 网络地图提供了每一对**计算机之间的连接**列表。例如：

```
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
```

Each line of text in the network map represents a single connection; the line `kh-tc` represents a connection between the computer named `kh` and the computer named `tc`. Connections aren't directional; `tc-kh` would mean exactly the same thing.
> 网络地图中的每一行文本代表一条连接；比如`kh-tc`表示名为`kh`的计算机和名为`tc`的计算机之间有一条连接。连接是无向的；`tc-kh`和`kh-tc`完全等价。

LAN parties typically involve multiplayer games, so maybe you can locate it by finding groups of connected computers. Start by looking for **sets of three computers** where each computer in the set is connected to the other two computers.
> 局域网派对通常涉及多人游戏，所以也许你可以通过寻找互相连接的计算机组来定位派对。首先，寻找**三台计算机组成的集合**，其中每台计算机都与另外两台相连。

In this example, there are `12` such sets of three inter-connected computers:
> 在本例中，有`12`组这样的三台互联计算机：

```
aq,cg,yn
aq,vc,wq
co,de,ka
co,de,ta
co,ka,ta
de,ka,ta
kh,qp,ub
qp,td,wh
tb,vc,wq
tc,td,wh
td,wh,yn
ub,vc,wq
```

If the Chief Historian is here, **and** he's at the LAN party, it would be best to know that right away. You're pretty sure his computer's name starts with `t`, so consider only sets of three computers where at least one computer's name starts with `t`. That narrows the list down to **`7`** sets of three inter-connected computers:
> 如果首席历史学家也在这里，**而且**他在局域网派对上，你最好能立刻知道。你很确定他的计算机名以`t`开头，所以只考虑至少有一台计算机名以`t`开头的三台互联计算机集合。这样列表缩小到**`7`**组：

```
co,de,ta
co,ka,ta
de,ka,ta
qp,td,wh
tb,vc,wq
tc,td,wh
td,wh,yn
```

Find all the sets of three inter-connected computers. **How many contain at least one computer with a name that starts with `t`?**
> 找出所有三台互联计算机的集合。**其中至少包含一台以`t`开头的计算机的集合有多少组？**

Your puzzle answer was `1200`.

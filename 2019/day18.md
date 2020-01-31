# Day 18: Many-Worlds Interpretation

> 第13天：多世界解释

As you approach Neptune, a planetary security system detects you and activates a giant [tractor beam](https://en.wikipedia.org/wiki/Tractor_beam) on [Triton](https://en.wikipedia.org/wiki/Triton_(moon))! You have no choice but to land.

> 当你接近海王星时，行星安全系统检测到你，并激活了[崔顿（海卫一）](https://en.wikipedia.org/wiki/Triton_(moon))上的一台巨大的[牵引光束](https://en.wikipedia.org/wiki/Tractor_beam)！你别无选择，只能着陆。

A scan of the local area reveals only one interesting feature: a massive underground vault. You generate a map of the tunnels ([your puzzle input](day18.txt)). The tunnels are too narrow to move diagonally.

> 对本地区的扫描显示出一个有趣的特征：一个庞大的地下金库。你生成了隧道的地图（[你的谜题输入](day18.txt)）。隧道很窄，无斜向移动。

Only one **entrance** (marked `@`) is present among the **open passages** (marked `.`) and **stone walls** (`#`), but you also detect an assortment of **keys** (shown as lowercase letters) and **doors** (shown as uppercase letters). Keys of a given letter open the door of the same letter: `a` opens `A`, `b` opens `B`, and so on. You aren't sure which key you need to disable the tractor beam, so you'll need to **collect all of them**.

> 在**通道**（标记为 `.`）和**石墙**（`#`）之中只有一个**入口**（标记为 `@`），但是你还检测到**钥匙**（显示为小写字母）和**门**（显示为大写字母）。所给定字母的钥匙可以打开同一字母的门：`a` 打开 `A`，`b` 打开 `B`，依此类推。你不确定哪把钥匙用来禁用牵引光束，所以你需要**收集所有的钥匙**。

For example, suppose you have the following map:

> 例如，假设你有以下地图：

```'
#########
#b.A.@.a#
#########
```

Starting from the entrance (`@`), you can only access a large door (`A`) and a key (`a`). Moving toward the door doesn't help you, but you can move `2` steps to collect the key, unlocking `A` in the process:

> 从入口（`@`）开始，你只能接触到一扇大门（`A`）和一把钥匙（`a`）。朝门过去没有任何用处，但是你可以移动 `2` 步来收集钥匙，这个过程中将解锁 `A`：

```'
#########
#b.....@#
#########
```

Then, you can move `6` steps to collect the only other key, `b`:

> 接下来，你可以移动 `6` 步骤来收集剩下的另一把钥匙 `b`：

```'
#########
#@......#
#########
```

So, collecting every key took a total of **`8`** steps.

> 因此，收集所有的钥匙总共用了 **`8`** 步。

Here is a larger example:

> 这是一个更大的示例：

```'
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
```

The only reasonable move is to take key `a` and unlock door `A`:

> 唯一合理的动作是获取钥匙 `a` 并解锁门 `A`：

```'
########################
#f.D.E.e.C.b.....@.B.c.#
######################.#
#d.....................#
########################
```

Then, do the same with key `b`:

> 然后，执行相同的操作获取钥匙 `b` ：

```'
########################
#f.D.E.e.C.@.........c.#
######################.#
#d.....................#
########################
```

...and the same with key `c`:

> ...以及钥匙 `c`：

```'
########################
#f.D.E.e.............@.#
######################.#
#d.....................#
########################
```

Now, you have a choice between keys `d` and `e`. While key `e` is closer, collecting it now would be slower in the long run than collecting key `d` first, so that's the best choice:

> 现在，你需要在钥匙 `d` 和 `e` 之间进行选择。尽管钥匙 `e` 更接近，但从长远来看，现在收集它要比首先收集钥匙 `d` 慢一些，所以最佳选择是：

```'
########################
#f...E.e...............#
######################.#
#@.....................#
########################
```

Finally, collect key `e` to unlock door `E`, then collect key `f`, taking a grand total of **`86`** steps.

> 最后，收集钥匙 `e` 解锁门 `E` ，然后收集钥匙 `f`，总共用了 **`86`** 步。

Here are a few more examples:

> 以下是更多的示例：

-

```'
    ########################
    #...............b.C.D.f#
    #.######################
    #.....@.a.B.c.d.A.e.F.g#
    ########################
```

Shortest path is `132` steps: `b`, `a`, `c`, `d`, `f`, `e`, `g`

> 最短的路径是 `132` 步：`b`，`a`，`c`，`d`，`f`，`e`，`g`

-

```'
    #################
    #i.G..c...e..H.p#
    ########.########
    #j.A..b...f..D.o#
    ########@########
    #k.E..a...g..B.n#
    ########.########
    #l.F..d...h..C.m#
    #################
```

Shortest paths are `136` steps;  
one is: `a`, `f`, `b`, `j`, `g`, `n`, `h`, `d`, `l`, `o`, `e`, `p`, `c`, `i`, `k`, `m`

> 最短的路径是 `136` 步，其一是：`a`，`f`，`b`，`j`，`g`，`n`，`h`，`d`，`l`，`o`，`e`，`p` ，`c`，`i`，`k`，`m`

-

```'
    ########################
    #@..............ac.GI.b#
    ###d#e#f################
    ###A#B#C################
    ###g#h#i################
    ########################
```

Shortest paths are `81` steps; one is: `a`, `c`, `f`, `i`, `d`, `g`, `b`, `e`, `h`

> 最短的路径是 `81` 步，其一是：`a`，`c`，`f`，`i`，`d`，`g`，`b`，`e`，`h`

**How many steps is the shortest path that collects all of the keys?**

> **收集所有钥匙的最短路径是多少步？**

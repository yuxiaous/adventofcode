# Day 18: Many-Worlds Interpretation

> 第13天：多世界解释

As you approach Neptune, a planetary security system detects you and activates a giant [tractor beam](https://en.wikipedia.org/wiki/Tractor_beam) on [Triton](https://en.wikipedia.org/wiki/Triton_(moon))! You have no choice but to land.

> 当你接近海王星时，行星安全系统检测到你，并激活了[崔顿（海卫一）](https://en.wikipedia.org/wiki/Triton_(moon))上的一台巨大的[牵引光束](https://en.wikipedia.org/wiki/Tractor_beam)！你别无选择，只能着陆。

A scan of the local area reveals only one interesting feature: a massive underground vault. You generate a map of the tunnels ([your puzzle input](day18.txt)). The tunnels are too narrow to move diagonally.

> 对本地区的扫描显示出一个有趣的特征：一个庞大的地下金库。你生成了隧道的地图（[你的谜题输入](day18.txt)）。隧道很窄，无斜向移动。

Only one **entrance** (marked `@`) is present among the **open passages** (marked `.`) and **stone walls** (`#`), but you also detect an assortment of **keys** (shown as lowercase letters) and **doors** (shown as uppercase letters). Keys of a given letter open the door of the same letter: `a` opens `A`, `b` opens `B`, and so on. You aren't sure which key you need to disable the tractor beam, so you'll need to **collect all of them**.

> 在**通道**（标记为 `.`）和**石墙**（`#`）之中只有一个**入口**（标记为 `@`），但是你还检测到**钥匙**（显示为小写字母）和**门**（显示为大写字母）。所给定字母的钥匙可以打开同一字母的门：`a` 打开 `A`，`b` 打开 `B`，依此类推。你不确定哪把钥匙用来禁用牵引光束，所以你需要**收集所有的钥匙**。

For example, suppose you have the following map:

> 举个例子，假设你有以下地图：

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

> 这是一个更大的例子：

```'
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
```

The only reasonable move is to take key `a` and unlock door `A`:

> 唯一可做的是获取钥匙 `a` 并解锁门 `A`：

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

Your puzzle answer was `3862`.

## Part Two

You arrive at the vault only to discover that there is not one vault, but **four** - each with its own entrance.

> 你到达金库后发现不只有一个金库，而是**四个** —— 每个金库都有自己的入口。

On your map, find the area in the middle that looks like this:

> 在你的地图上，找到中间的区域，如下所示：

```'
...
.@.
...
```

Update your map to instead use the correct data:

> 更新你的地图使用正确的数据：

```'
@#@
###
@#@
```

This change will split your map into four separate sections, each with its own entrance:

> 这个改变会将你的地图分隔为四个独立的部分，每个部分都有它自己的入口：

```'
#######       #######
#a.#Cd#       #a.#Cd#
##...##       ##@#@##
##.@.##  -->  #######
##...##       ##@#@##
#cB#Ab#       #cB#Ab#
#######       #######
```

Because some of the keys are for doors in other vaults, it would take much too long to collect all of the keys by yourself. Instead, you deploy four remote-controlled robots. Each starts at one of the entrances (`@`).

> 由于一些钥匙是用于其他金库中的门的，因此由你自己收集所有的钥匙将会花费非常长的时间。相反的，你部署了四个远程控制机器人。 每个机器人都从其中一个入口（`@`）开始。

Your goal is still to **collect all of the keys in the fewest steps**, but now, each robot has its own position and can move independently. You can only remotely control a single robot at a time. Collecting a key instantly unlocks any corresponding doors, regardless of the vault in which the key or door is found.

> 你的目标仍然是**用最少的步数收集所有钥匙**，但是现在，每个机器人都有自己的位置并且可以独立移动。你一次只能远程控制一个机器人。收集一把钥匙会立即解锁对应的门，无论找到钥匙或门在哪个金库。

For example, in the map above, the top-left robot first collects key `a`, unlocking door `A` in the bottom-right vault:

> 举个例子，在上面的地图中，左上方的机器人首先收集了钥匙 `a`，解锁了右下方金库中的门 `A`：

```'
#######
#@.#Cd#
##.#@##
#######
##@#@##
#cB#.b#
#######
```

Then, the bottom-right robot collects key `b`, unlocking door `B` in the bottom-left vault:

> 然后，右下方的机器人收集了钥匙 `b`，解锁了左下方金库的门 `B`：

```'
#######
#@.#Cd#
##.#@##
#######
##@#.##
#c.#.@#
#######
```

Then, the bottom-left robot collects key `c`:

> 然后，左下方的机器人收集了钥匙 `c`：

```'
#######
#@.#.d#
##.#@##
#######
##.#.##
#@.#.@#
#######
```

Finally, the top-right robot collects key `d`:

> 最后，右上方的机器人收集了钥匙 `d`：

```'
#######
#@.#.@#
##.#.##
#######
##.#.##
#@.#.@#
#######
```

In this example, it only took **`8`** steps to collect all of the keys.

> 在这个例子中，只花了 **`8`** 步就收集了所有的钥匙。

Sometimes, multiple robots might have keys available, or a robot might have to wait for multiple keys to be collected:

> 有时，多个机器人可能都拥有可用的钥匙，又或者一个机器人可能需要等待多个钥匙被收集：

```'
###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############
```

First, the top-right, bottom-left, and bottom-right robots take turns collecting keys `a`, `b`, and `c`, a total of `6 + 6 + 6 = 18` steps. Then, the top-left robot can access key `d`, spending another `6` steps; collecting all of the keys here takes a minimum of **`24`** steps.

> 首先，右上方、左下方和右下方的机器人轮流收集钥匙 `a`、`b` 和 `c`，总共 `6 + 6 + 6 = 18` 步。然后，左上方的机器人可以接触钥匙 `d`，花费另外的 `6` 步，收集所有的钥匙最少花费 **`24`** 步。

Here's a more complex example:

> 这是一个更复杂的例子：

```'
#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############
```

- Top-left robot collects key `a`.
- Bottom-left robot collects key `b`.
- Top-left robot collects key `c`.
- Bottom-left robot collects key `d`.
- Top-left robot collects key `e`.
- Bottom-left robot collects key `f`.
- Bottom-right robot collects key `g`.
- Top-right robot collects key `h`.
- Bottom-right robot collects key `i`.
- Top-right robot collects key `j`.
- Bottom-right robot collects key `k`.
- Top-right robot collects key `l`.

> - 左上方的机器人收集钥匙 `a`。
> - 左下方的机器人收集钥匙 `b`。
> - 左上方的机器人收集钥匙 `c`。
> - 左下方的机器人收集钥匙 `d`。
> - 左上方的机器人收集钥匙 `e`。
> - 左下方的机器人收集钥匙 `f`。
> - 右下方的机器人收集钥匙 `g`。
> - 右上方的机器人收集钥匙 `h`。
> - 右下方的机器人收集钥匙 `i`。
> - 右上方的机器人收集钥匙 `j`。
> - 右下方的机器人收集钥匙 `k`。
> - 右上方的机器人收集钥匙 `l`。

In the above example, the fewest steps to collect all of the keys is **`32`**.

> 在上面的例子中，收集所有钥匙所需的最少步数是 **`32`** 步。

Here's an example with more choices:

> 这是一个具有更多选择的例子：

```'
#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############
```

One solution with the fewest steps is:

- Top-left robot collects key `e`.
- Top-right robot collects key `h`.
- Bottom-right robot collects key `i`.
- Top-left robot collects key `a`.
- Top-left robot collects key `b`.
- Top-right robot collects key `c`.
- Top-left robot collects key `d`.
- Top-left robot collects key `f`.
- Top-left robot collects key `g`.
- Bottom-right robot collects key `k`.
- Bottom-right robot collects key `j`.
- Top-right robot collects key `l`.
- Bottom-left robot collects key `n`.
- Bottom-left robot collects key `m`.
- Bottom-left robot collects key `o`.

> 最少步数的一种解决方法是：
>
> - 左上方的机器人收集钥匙 `e`。
> - 右上方的机器人收集钥匙 `h`。
> - 右下方的机器人收集钥匙 `i`。
> - 左上方的机器人收集钥匙 `a`。
> - 左上方的机器人收集钥匙 `b`。
> - 右上方的机器人收集钥匙 `c`。
> - 左上方的机器人收集钥匙 `d`。
> - 左上方的机器人收集钥匙 `f`。
> - 左上方的机器人收集钥匙 `g`。
> - 右下方的机器人收集钥匙 `k`。
> - 右下方的机器人收集钥匙 `j`。
> - 右上方的机器人收集钥匙 `l`。
> - 左下方的机器人收集钥匙 `n`。
> - 左下方的机器人收集钥匙 `m`。
> - 左下方的机器人收集钥匙 `o`。

This example requires at least **`72`** steps to collect all keys.

> 这个例子需要至少 **`72`** 步来收集所有的钥匙。

After updating your map and using the remote-controlled robots, **what is the fewest steps necessary to collect all of the keys?**

> 在更新地图并使用远程控制机器人后，**收集所有钥匙所需的最少步数是多少？**

Your puzzle answer was `1626`.

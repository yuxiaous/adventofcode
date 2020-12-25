# Day 24: Lobby Layout

> 第二十四天：大堂布局

Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.

> 你做到了，你的木筏抵达了热带小岛，原来这只小螃蟹是一名优秀的导航员。接下来你准备前往度假酒店。

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the **new tile floor**.

> 当你进入大厅时，你发现了一个小问题：地面正在装修。在他们完成新地砖的安装之前，你无法到达接待前台。

The tiles are all **hexagonal**; they need to be arranged in a [hex grid](https://en.wikipedia.org/wiki/Hexagonal_tiling) with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.

> 地砖都是六边形的，它们需要拼接成一种非常特定的彩色图案，并排列在[六边形网格](https://en.wikipedia.org/wiki/Hexagonal_tiling)中。没心情浪费时间了，你决定提供帮助以便尽快弄清楚图案是什么样的。

The tiles are all **white** on one side and **black** on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.

> 所有的地砖都是一面白色，另一面黑色的。它们开始时都是白色朝上的。这个大厅足够大，可以容纳所有可能出现的图案。

A member of the renovation crew gives you a **list of the tiles that need to be flipped over** ([your puzzle input](day24.txt)). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a **reference tile** in the very center of the room. (Every line starts from the same reference tile.)

> 一名装修人员给你了一个需要翻转的地砖的列表（[你的谜题输入](day24.txt)）。从房间正中央的参考地砖开始，列表中的每一行都标识了一块需要通过一系列步骤进行翻转的单块地砖。（每一行都从同一块参考地砖开始。）

Because the tiles are hexagonal, every tile has **six neighbors**: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as `e`, `se`, `sw`, `w`, `nw`, and `ne`. A tile is identified by a series of these directions with **no delimiters**; for example, `esenee` identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

> 由于这些地砖是六边形的，因此每块地砖都有六个邻居：东，东南，西南，西，西北和东北。这些方向在你的列表中给出，分别是 `e`，`se`，`sw`，`w`，`nw`和`ne`。一块地砖由一串方向信息来标识，之间没有分隔符。例如，`esenee` 表示从参考地砖开始，先向东移动一块地砖，再向东南移动一块地砖，再向东北移动一块地砖，最后向东移动一块地砖，就是最终的地砖。

Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like `esew` flips a tile immediately adjacent to the reference tile, and a line like `nwwswee` flips the reference tile itself.

> 每当一块地砖被标识后，它就会从白色翻转为黑色，或从黑色翻转为白色。地砖可能会翻转多次。例如，类似 `esew` 这样的一行将翻转与参考地砖相邻的地砖，以及类似 `nwwswee` 这样的一行将翻转参考地砖本身。

Here is a larger example:

> 这里是一个更大的例子：

```'
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
```

In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of **`10`** tiles are **black**.

> 在上面的例子中，将 10 块地砖翻转一次（变为黑色），再将 5 块地砖翻转两次（先变为黑色，再变为白色）。当所有这些指令都被执行后，共有 **`10`** 块地砖变为黑色。

Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, **how many tiles are left with the black side up?**

> 浏览装修人员的列表，并确定哪些地砖需要翻转。当左右的指令都被执行后，剩下多少块黑色朝上的地砖？

Your puzzle answer was `282`.

## --- Part Two ---

The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

- Any **black** tile with **zero** or **more than 2** black tiles immediately adjacent to it is flipped to **white**.
- Any **white** tile with **exactly 2** black tiles immediately adjacent to it is flipped to **black**.

> 大厅的地砖是为了一场现场艺术展而制作的。地砖每天都会按照以下规则进行翻转：
>
> - 当相邻的地砖中没有黑色或者有两块以上黑色地砖时，黑色的地砖将翻转为白色。
> - 当相邻的地砖中恰好有两块黑色地砖时，白色的地砖将翻转为黑色。

Here, **tiles immediately adjacent** means the six tiles directly touching the tile in question.

> 在这里，相邻的地砖是指直接与该地砖接触的六块地砖。

The rules are applied **simultaneously** to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

> 规则同时适用于每块地砖，换句话说，首先确定哪些地砖需要翻转，然后将它们全部同时翻转。

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

> 在上面的例子中，经过几天后黑色朝上的地砖数量如下：

```'
Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
```

After executing this process a total of 100 times, there would be **`2208`** black tiles facing up.

> 当流程总共执行了 100 次以后，将会有 **`2208`** 块地砖黑色朝上。

**How many tiles will be black after 100 days?**

> 100 天后有多少块黑色朝上的地砖？

Your puzzle answer was `3445`.

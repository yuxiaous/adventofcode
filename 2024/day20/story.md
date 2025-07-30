# Day 20: Race Condition
> # 第二十天：竞态条件

The Historians are quite pixelated again. This time, a massive, black building looms over you - you're [right outside](https://adventofcode.com/2017/day/24) the CPU!
> 历史学家们又变得很像素化。这一次，一座巨大的黑色建筑矗立在你们头顶——你们[就在CPU外面](https://adventofcode.com/2017/day/24)！

While The Historians get to work, a nearby program sees that you're idle and challenges you to a **race**. Apparently, you've arrived just in time for the frequently-held **race condition** festival!
> 当历史学家们开始工作时，附近的一个程序发现你很闲，向你发起了**竞速**挑战。显然，你正好赶上了经常举办的**竞态条件**节！

The race takes place on a particularly long and twisting code path; programs compete to see who can finish in the **fewest picoseconds**. The winner even gets their very own [mutex](https://en.wikipedia.org/wiki/Lock_(computer_science))!
> 比赛在一条特别漫长且曲折的代码路径上进行；各程序比拼谁能用**最少皮秒**跑完。冠军甚至能获得属于自己的[互斥锁](https://en.wikipedia.org/wiki/Lock_(computer_science))！

They hand you a **map of the racetrack** (your puzzle input). For example:
> 他们给了你一张**赛道地图**（你的谜题输入）。例如：

```
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

The map consists of track (`.`) - including the **start** (`S`) and **end** (`E`) positions (both of which also count as track) - and **walls** (`#`).
> 地图由赛道（`.`，包括**起点**`S`和**终点**`E`，两者也算赛道）和**墙壁**（`#`）组成。

When a program runs through the racetrack, it starts at the start position. Then, it is allowed to move up, down, left, or right; each such move takes **1 picosecond**. The goal is to reach the end position as quickly as possible. In this example racetrack, the fastest time is `84` picoseconds.
> 程序在赛道上比赛时，从起点出发。它可以上下左右移动，每次移动耗时**1皮秒**。目标是尽快到达终点。本例中最快用时为 `84` 皮秒。

Because there is only a single path from the start to the end and the programs all go the same speed, the races used to be pretty boring. To make things more interesting, they introduced a new rule to the races: programs are allowed to **cheat**.
> 由于起点到终点只有一条路，大家速度又一样，比赛以前很无聊。为了增加趣味性，他们引入了新规则：允许程序**作弊**。

The rules for cheating are very strict. **Exactly once** during a race, a program may **disable collision** for up to **2 picoseconds**. This allows the program to **pass through walls** as if they were regular track. At the end of the cheat, the program must be back on normal track again; otherwise, it will receive a [segmentation fault](https://en.wikipedia.org/wiki/Segmentation_fault) and get disqualified.
> 作弊规则非常严格。比赛中**只能有一次**，程序可以**禁用碰撞**，最多持续**2皮秒**。这期间程序可以像走赛道一样**穿墙**。作弊结束时，程序必须回到普通赛道，否则会收到[段错误](https://en.wikipedia.org/wiki/Segmentation_fault)并被取消资格。

So, a program could complete the course in 72 picoseconds (saving **12 picoseconds**) by cheating for the two moves marked `1` and `2`:
> 例如，程序可以在标记为 `1` 和 `2` 的两步作弊，用时72皮秒（节省**12皮秒**）：

```
###############
#...#...12....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

Or, a program could complete the course in 64 picoseconds (saving **20 picoseconds**) by cheating for the two moves marked `1` and `2`:
> 或者，程序可以在标记为 `1` 和 `2` 的两步作弊，用时64皮秒（节省**20皮秒**）：

```
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...12..#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

This cheat saves **38 picoseconds**:
> 这种作弊节省了**38皮秒**：

```
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.####1##.###
#...###.2.#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

This cheat saves **64 picoseconds** and takes the program directly to the end:
> 这种作弊节省了**64皮秒**，直接到达终点：

```
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..21...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

Each cheat has a distinct **start position** (the position where the cheat is activated, just before the first move that is allowed to go through walls) and **end position**; cheats are uniquely identified by their start position and end position.
> 每次作弊都有唯一的**起始位置**（激活作弊的地方，即第一次可以穿墙前的位置）和**结束位置**；作弊由起止位置唯一标识。

In this example, the total number of cheats (grouped by the amount of time they save) are as follows:
> 在本例中，按节省时间分组的作弊总数如下：

- There are 14 cheats that save 2 picoseconds.
- There are 14 cheats that save 4 picoseconds.
- There are 2 cheats that save 6 picoseconds.
- There are 4 cheats that save 8 picoseconds.
- There are 2 cheats that save 10 picoseconds.
- There are 3 cheats that save 12 picoseconds.
- There is one cheat that saves 20 picoseconds.
- There is one cheat that saves 36 picoseconds.
- There is one cheat that saves 38 picoseconds.
- There is one cheat that saves 40 picoseconds.
- There is one cheat that saves 64 picoseconds.
> - 有14种作弊能节省2皮秒。
> - 有14种作弊能节省4皮秒。
> - 有2种作弊能节省6皮秒。
> - 有4种作弊能节省8皮秒。
> - 有2种作弊能节省10皮秒。
> - 有3种作弊能节省12皮秒。
> - 有1种作弊能节省20皮秒。
> - 有1种作弊能节省36皮秒。
> - 有1种作弊能节省38皮秒。
> - 有1种作弊能节省40皮秒。
> - 有1种作弊能节省64皮秒。

You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible, you'll need a list of the best cheats. **How many cheats would save you at least 100 picoseconds?**
> 你不确定赛道条件会怎样，为了给自己尽可能多的选择，你需要一份最佳作弊列表。**有多少种作弊能为你节省至少100皮秒？**

Your puzzle answer was `1417`.

## Part Two

The programs seem perplexed by your list of cheats. Apparently, the two-picosecond cheating rule was deprecated several milliseconds ago! The latest version of the cheating rule permits a single cheat that instead lasts at most **20 picoseconds**.
> 这些程序对你的作弊列表感到困惑。显然，2皮秒作弊规则在几毫秒前就已经废弃了！最新的作弊规则允许只进行一次作弊，但这次最多可以持续**20皮秒**。

Now, in addition to all the cheats that were possible in just two picoseconds, many more cheats are possible. This six-picosecond cheat saves **76 picoseconds**:
> 现在，除了原来2皮秒内能实现的作弊外，还有更多作弊可能。这种持续6皮秒的作弊能节省**76皮秒**：

```
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#1#####.#.#.###
#2#####.#.#...#
#3#####.#.###.#
#456.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

Because this cheat has the same start and end positions as the one above, it's the **same cheat**, even though the path taken during the cheat is different:
> 因为这个作弊和上面那个作弊的起止位置相同，所以它们算作**同一个作弊**，即使作弊期间走的路径不同：

```
###############
#...#...#.....#
#.#.#.#.#.###.#
#S12..#.#.#...#
###3###.#.#.###
###4###.#.#...#
###5###.#.###.#
###6.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
```

Cheats don't need to use all 20 picoseconds; cheats can last any amount of time up to and including 20 picoseconds (but can still only end when the program is on normal track). Any cheat time not used is lost; it can't be saved for another cheat later.
> 作弊不需要用满20皮秒；作弊可以持续任意时间，只要不超过20皮秒（但仍然只能在程序回到普通赛道时结束）。未用完的作弊时间会浪费，不能留到以后再用。

You'll still need a list of the best cheats, but now there are even more to choose between. Here are the quantities of cheats in this example that save **50 picoseconds or more**:
> 你仍然需要一份最佳作弊列表，但现在可选项更多了。以下是本例中能节省**50皮秒及以上**的作弊数量：

- There are 32 cheats that save 50 picoseconds.
- There are 31 cheats that save 52 picoseconds.
- There are 29 cheats that save 54 picoseconds.
- There are 39 cheats that save 56 picoseconds.
- There are 25 cheats that save 58 picoseconds.
- There are 23 cheats that save 60 picoseconds.
- There are 20 cheats that save 62 picoseconds.
- There are 19 cheats that save 64 picoseconds.
- There are 12 cheats that save 66 picoseconds.
- There are 14 cheats that save 68 picoseconds.
- There are 12 cheats that save 70 picoseconds.
- There are 22 cheats that save 72 picoseconds.
- There are 4 cheats that save 74 picoseconds.
- There are 3 cheats that save 76 picoseconds.
> - 有32种作弊能节省50皮秒。
> - 有31种作弊能节省52皮秒。
> - 有29种作弊能节省54皮秒。
> - 有39种作弊能节省56皮秒。
> - 有25种作弊能节省58皮秒。
> - 有23种作弊能节省60皮秒。
> - 有20种作弊能节省62皮秒。
> - 有19种作弊能节省64皮秒。
> - 有12种作弊能节省66皮秒。
> - 有14种作弊能节省68皮秒。
> - 有12种作弊能节省70皮秒。
> - 有22种作弊能节省72皮秒。
> - 有4种作弊能节省74皮秒。
> - 有3种作弊能节省76皮秒。

Find the best cheats using the updated cheating rules. **How many cheats would save you at least 100 picoseconds?**
> 按照更新后的作弊规则，找出最佳作弊方案。**有多少种作弊能为你节省至少100皮秒？**

Your puzzle answer was `1014683`.

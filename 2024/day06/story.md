# Day 6: Guard Gallivant
> # 第六天：守卫巡游

The Historians use their fancy [device](https://adventofcode.com/2024/day/4) again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year [1518](https://adventofcode.com/2018/day/5)! It turns out that having direct access to history is very convenient for a group of historians.
> 历史学家们再次使用他们那台神奇的[设备](https://adventofcode.com/2024/day/4)，这次把你们带到了北极原型服装制造实验室……时间是[1518年](https://adventofcode.com/2018/day/5)！事实证明，能够直接接触历史对一群历史学家来说非常方便。

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single **guard** is patrolling this part of the lab.
> 你们仍然要小心时间悖论，因此在历史学家们寻找首席的过程中，必须避免与1518年的人接触。不幸的是，这片实验室区域有一名**守卫**在巡逻。

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?
> 也许你可以提前推算出守卫的行动路线，这样历史学家们就能安全地搜寻了？

You start by making a map (your puzzle input) of the situation. For example:
> 你首先绘制了一张当前情况的地图（你的谜题输入）。例如：

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

The map shows the current position of the guard with `^` (to indicate the guard is currently facing **up** from the perspective of the map). Any **obstructions** - crates, desks, alchemical reactors, etc. - are shown as `#`.
> 地图上用 `^` 表示守卫当前位置（表示守卫当前朝**上**）。所有**障碍物**——箱子、桌子、炼金反应堆等——都用 `#` 表示。

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
> 1518年的实验室守卫遵循非常严格的巡逻协议，反复执行以下步骤：

- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.
> - 如果正前方有障碍物，则右转90度。
> - 否则，向前迈一步。

Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):
> 按照上述协议，守卫会向上移动几步，直到遇到障碍物（本例中是一堆失败的服装原型）：

```
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:
> 由于守卫前方有障碍物，她会先右转，然后继续沿新方向直行：

```
....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Reaching another obstacle (a spool of several **very** long polymers), she turns right again and continues downward:
> 遇到另一个障碍物（一卷**非常**长的聚合物）后，她再次右转并继续向下：

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
```

This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):
> 这个过程会持续一段时间，但最终守卫会离开地图区域（在经过一罐万能溶剂后）：

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
```

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. **Including the guard's starting position**, the positions visited by the guard before leaving the area are marked with an `X`:
> 通过预测守卫的路线，你可以确定实验室中哪些具体位置会被巡逻经过。**包括守卫的起始位置**，守卫在离开区域前经过的位置都用 `X` 标记：

```
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
```

In this example, the guard will visit **`41`** distinct positions on your map.
> 在这个例子中，守卫会在你的地图上经过 **`41`** 个不同的位置。

Predict the path of the guard. **How many distinct positions will the guard visit before leaving the mapped area?**
> 预测守卫的路径。**在离开地图区域前，守卫会经过多少个不同的位置？**

Your puzzle answer was `5305`.

## Part Two

While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and [record](https://adventofcode.com/2018/day/4) the nightly status of the lab's guard post on the walls of the closet.
> 当历史学家们开始绕开守卫的巡逻路线工作时，你借用了他们的神奇设备，走出实验室。从一个安全的储藏室里，你穿越回过去几个月，并在储藏室的墙上记录了实验室守卫岗哨每晚的状态。

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.
> 当你回到历史学家们身边时，对他们来说仿佛只过了几秒钟，他们解释说守卫的巡逻区域实在太大，他们无法在不被发现的情况下安全地搜查实验室。

Fortunately, they are **pretty sure** that adding a single new obstruction **won't** cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get **stuck in a loop**, making the rest of the lab safe to search.
> 幸运的是，他们**很确定**添加一个新的障碍物**不会**引发时间悖论。他们希望把新的障碍物放在某个位置，让守卫**陷入循环**，这样实验室的其他区域就可以安全搜查了。

To have the lowest chance of creating a time paradox, The Historians would like to know **all** of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.
> 为了最大程度降低时间悖论的风险，历史学家们想知道**所有**可以放置障碍物的位置。新的障碍物不能放在守卫的起始位置——因为守卫现在就在那儿，会发现的。

In the above example, there are only **`6`** different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use `O` to mark the new obstruction, `|` to show a position where the guard moves up/down, `-` to show a position where the guard moves left/right, and `+` to show a position where the guard moves both up/down and left/right.
> 在上面的例子中，只有 **`6`** 个不同的位置可以让守卫因新障碍物而陷入循环。这六种情况的图中，`O` 表示新障碍物，`|` 表示守卫上下移动的位置，`-` 表示左右移动的位置，`+` 表示既有上下又有左右移动的位置。

Option one, put a printing press next to the guard's starting position:
> 选项一，把一台印刷机放在守卫起始位置旁边：

```
....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
```

Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:
> 选项二，把一堆失败的服装原型放在地图区域的右下角：

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
```

Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:
> 选项三，把一箱烟囱挤压原型面料放在右下角的站立桌旁：

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
```

Option four, put an alchemical retroencabulator near the bottom left corner:
> 选项四，把一个炼金术逆变器放在左下角附近：

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
```

Option five, put the alchemical retroencabulator a bit to the right instead:
> 选项五，把炼金术逆变器稍微向右移动：

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
```

Option six, put a tank of sovereign glue right next to the tank of universal solvent:
> 选项六，把一罐万能胶放在万能溶剂旁边：

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
```

It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are **`6`** different positions you could choose.
> 你用什么作为障碍物其实无关紧要，只要你和历史学家们能在守卫没注意到的情况下把它放好就行。重要的是要有足够多的选择，这样你就能找到一个最小化时间悖论的方案，在这个例子中，你有 **`6`** 个不同的位置可以选择。

You need to get the guard stuck in a loop by adding a single new obstruction. **How many different positions could you choose for this obstruction?**
> 你需要通过添加一个新的障碍物让守卫陷入循环。**你有多少个不同的位置可以选择放置这个障碍物？**

Your puzzle answer was `2143`.

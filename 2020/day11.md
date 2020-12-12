# Day 11: Seating System

> 第十一天：就座系统

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

> 你的飞机着陆了，预留给你了充足的时间。你旅程的最后一站是乘坐直达热带小岛的渡轮，在那里你终于可以开始你的假期了。当你到达登上轮渡的等候区时，你发现来得太早了，这里都还空空如也！

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout ([your puzzle input](day11.txt)).

> 通过对人们在等候区选择（或放弃）座位的过程进行建模，你确信你可以预测出最佳的座位。你快速绘制了一幅座位布局图（[你的谜题输入](day11.txt)）。

The seat layout fits neatly on a grid. Each position is either floor (`.`), an empty seat (`L`), or an occupied seat (`#`). For example, the initial seat layout might look like this:

> 座位布局整齐地排列在网格上。每个位置都可能是地板（`.`）、一个空座位（`L`）或一个占用座位（`#`）。例如，初始座位布局可能看上去像下图所示：

```'
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
```

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the **number of occupied seats** adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

- If a seat is **empty** (`L`) and there are **no** occupied seats adjacent to it, the seat becomes **occupied**.
- If a seat is **occupied** (`#`) and **four or more** seats adjacent to it are also occupied, the seat becomes **empty**.
- Otherwise, the seat's state does not change.

> 现在，你只需要为即将到来的人建模。幸运的是，人是完全可以预测的，并且始终遵循一套简单的规则。所有决定均基于与该座位相邻的已占用座位的数量（即座位的上、下、左、右和对角线这八个位置）。以下规则同时适用于每个座位：
>
> - 如果一个座位是空的（`L`），并且旁边没有被占用的座位，则该座位即将被占用。
> - 如果一个座位被占用了（`#`），并且有四个或以上的相邻座位也是被占用的，则该座位将变为空。
> - 其他情况下，座位的状态不变。

Floor (`.`) never changes; seats don't move, and nobody sits on the floor.

> 地板（`.`）不会改变，座位不会移动，并且没人会坐在地板上。

After one round of these rules, every seat in the example layout becomes occupied:

> 经过一轮这些规则，例子中的所有座位都会被占用：

```'
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
```

After a second round, the seats with four or more occupied adjacent seats become empty again:

> 经过第二轮，周围有四个或以上被占用的座位再次变空：

```'
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
```

This process continues for three more rounds:

> 这个过程将持续进行三轮甚至更多：

```'
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
```

```'
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
```

```'
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
```

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count **`37`** occupied seats.

> 在这时，发生了一件有趣的事情：混乱变得稳定，这些规则的进一步应用导致座位的状态不再发生改变！一旦人们停止四处走动，你统计出有 **`37`** 个被占用座位。

Simulate your seating area by applying the seating rules repeatedly until no seats change state. **How many seats end up occupied?**

> 通过重复应用座位规则来模拟你的座位区域，直到没有座位的状态发生改变为止。最终有多少个被占用的座位？

Your puzzle answer was `2152`.

## --- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about **the first seat they can see** in each of those eight directions!

> 当人们开始过来，你意识到自己错了。人们不仅在乎相邻的座位，他们也在乎八个方向上可以看到的第一个座位！

Now, instead of considering just the eight immediately adjacent seats, consider the **first seat** in each of those eight directions. For example, the empty seat below would see **eight** occupied seats:

> 现在，除了需要考虑紧邻的八个座位，也要考虑八个方向中每个方向可以看到的第一座位。例如，下面的空座位将看到八个被占用的座位：

```'
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
```

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

> 下面最左边的空座位只能看到一个空座位，而看不到其他的被占用的座位：

```'
.............
.L.L.#.#.#.#.
.............
```

The empty seat below would see **no** occupied seats:

> 下面的空座位看不到被占用的座位：

```'
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
```

Also, people seem to be more tolerant than you expected: it now takes **five or more** visible occupied seats for an occupied seat to become empty (rather than **four or more** from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

> 此外，人们似乎比你预期的要宽容：现在需要看见五个或更多被占用的座位才能使一个被占用的座位变空（而不是以前规则的四个或更多）。其他规则仍然适用：看到没有人占空的空座位，没有规则匹配的座位不会改变，地板也不会改变。

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

> 给定与上面相同的初始布局，这些新规则将导致座位区的变化如下：

```'
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
```

```'
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
```

```'
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
```

```'
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
```

```'
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
```

```'
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
```

```'
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
```

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count **`26`** occupied seats.

> 同样，在这时，人们停止四处移动，座位区域达到平衡。一旦这种情况发生，你统计出有 **`26`** 个被占用座位。

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, **how many seats end up occupied?**

> 有了新的方法，并且改变了由被占用到变空的座位规则，一旦达到平衡，最终有多少个座位被占用？

Your puzzle answer was `1937`.

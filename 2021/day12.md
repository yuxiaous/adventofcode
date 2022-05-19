# [Day 12: Passage Pathing](https://adventofcode.com/2021/day/12)]

> 第12天：通道路径

With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just **a** path - the only way to know if you've found the best path is to find **all** of them.

> 由于你的潜水艇的地下子系统处于次优状态，你要尽快离开这个洞穴的唯一方法就是自己找到一条路径。不只是**一条**路径 -- 了解你是否找到最佳路径的唯一方法是找到**全部**路径。

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves ([your puzzle input](day12.txt)). For example:

> 幸运的是，传感器大部分仍在工作，所以你为剩余的洞穴构建了一幅粗略的地图（[你的谜题输入](day12.txt)）。例如：

```'
start-A
start-b
A-c
A-b
b-d
A-end
b-end
```

This is a list of how all of the caves are connected. You start in the cave named `start`, and your destination is the cave named `end`. An entry like `b-d` means that cave `b` is connected to cave `d` - that is, you can move between them.

> 这是所有洞穴如何连接的列表。你从名为 `start` 的洞穴开始，你的目的地是名为 `end` 的洞穴。像 `b-d` 这样的条目意味着洞穴 `b` 与洞穴 `d` 相连 -- 也就是说，你可以在它们之间移动。

So, the above cave system looks roughly like this:

> 所以，上面的洞穴系统看上去大致是这样的：

```'
    start
    /   \
c--A-----b--d
    \   /
     end
```

Your goal is to find the number of distinct **paths** that start at `start`, end at `end`, and don't visit small caves more than once. There are two types of caves: **big** caves (written in uppercase, like `A`) and **small** caves (written in lowercase, like `b`). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should **visit small caves at most once**, and can **visit big caves any number of times**.

> 你的目标是找出从 `start` 开始、到 `end` 结束的不同**路径**的数量，并且不要多次访问小洞穴。洞穴有两种类型：**大**洞穴（用大写字母表示，如 `A`）和**小**洞穴（用小写字母表示，如 `b`）。多次访问任何一个小洞穴都是浪费时间，而大洞穴足够大，是值得多次访问的。因此，你找到的所有路径都应该遵守这个规则：**小洞穴最多访问一次，大洞穴可以访问任意次数**。

Given these rules, there are **`10`** paths through this example cave system:

> 鉴于这些规则，有 **`10`** 条路径通过这个例子的洞穴系统：

```'
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
```

(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

> （上面列表中的每一行对应一条单独的路径，这条路径所访问的洞穴按照访问顺序排列，并用逗号分隔。）

Note that in this cave system, cave `d` is never visited by any path: to do so, cave `b` would need to be visited twice (once on the way to cave `d` and a second time when returning from cave `d`), and since cave `b` is small, this is not allowed.

> 请注意，在这个洞穴系统中，洞穴 `d` 没有被任何路径访问：如果这么做了，洞穴 `b` 就会被访问两次（一次在前往洞穴 `d` 的途中，第二次从洞穴 `d` 返回时），并且由于洞穴 `b` 很小，所以这是不允许的。

Here is a slightly larger example:

> 这是一个稍微大一点的例子：

```'
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
```

The `19` paths through it are as follows:

> 通过它的 `19` 条路径如下：

```'
start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
```

Finally, this even larger example has `226` paths through it:

> 最后，这个更大的例子有 `226` 条路径通过它：

```'
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
```

**How many paths through this cave system are there that visit small caves at most once?**

> **小洞穴最多访问一次的情况下，通过这个洞穴系统有多少条路径？**

Your puzzle answer was `5874`.

## --- Part Two ---

After reviewing the available paths, you realize you might have time to visit a single small cave **twice**. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named `start` and `end` can only be visited **exactly once each**: once you leave the `start` cave, you may not return to it, and once you reach the `end` cave, the path must end immediately.

> 查看可用路径后，你意识到你也许有时间可以访问其中一个小洞穴**两次**。具体来说，大洞穴可以访问任意次数，其中一个小洞穴最多访问两次，其余小洞穴最多访问一次。但是，名为 `start` 和 `end` 的洞穴只能访问**一次**：一旦离开 `start` 洞穴，你就不能再返回了；一旦到达 `end` 洞穴，路径就立即结束了。

Now, the `36` possible paths through the first example above are:

> 现在，上面第一个例子中，有 `36` 条可能的路径通过它：

```'
start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end
```

The slightly larger example above now has `103` paths through it, and the even larger example now has `3509` paths through it.

> 上面稍大的例子现在有 `103` 条路径通过它，更大的例子现在有 `3509` 条路径通过它。

Given these new rules, **how many paths through this cave system are there?**

> 鉴于这些新规则，**通过这个洞穴系统有多少条路径？**

Your puzzle answer was `153592`.

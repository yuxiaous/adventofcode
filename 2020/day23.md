# --- Day 23: Crab Cups ---

> 第二十三天：螃蟹杯子

The small crab challenges **you** to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.

> 小螃蟹向你发起了游戏挑战！螃蟹将打乱一些杯子，而你必须预测它们的最终排列。

The cups will be arranged in a circle and labeled **clockwise** ([your puzzle input](day23.txt)). For example, if your labeling were `32415`, there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would be labeled `3`, `2`, `4`, `1`, `5`, and then back to `3` again.

> 杯子将排列成一个圆圈，并按照顺时针进行标记（[你的谜题输入](day23.txt)）。例如，如果你的标签为 `32415`，则有五个杯子围成一个圆圈，从第一个杯子沿顺时针方向绕圆圈，杯子分别标记为 `3`，`2`，`4`，`1`，`5`，然后又回到 `3`。

Before the crab starts, it will designate the first cup in your list as the **current cup**. The crab is then going to do **100 moves**.

> 在螃蟹准备开始之前，列表中的第一个杯子被指定为当前杯子。螃蟹接下来将移动 100 次。

Each **move**, the crab does the following actions:

- The crab picks up the **three cups** that are immediately **clockwise** of the **current cup**. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
- The crab selects a **destination cup**: the cup with a **label** equal to the **current cup's** label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it **wraps around** to the highest value on any cup's label instead.
- The crab places the cups it just picked up so that they are **immediately clockwise** of the destination cup. They keep the same order as when they were picked up.
- The crab selects a new **current cup**: the cup which is immediately clockwise of the current cup.

> 每次移动，螃蟹都会执行以下操作：
>
> - 螃蟹会沿着顺时针方向从当前杯子之后选中三个杯子。将它们从圆圈中拿走，可以根据需要调整杯子的间距以保持圆形。
> - 螃蟹会选择一个目标杯子：目标杯子的标签等于当前杯子的标签减一。如果选中的杯子正好是刚才拿走的杯子之一，那么螃蟹会一直减下去，直到找到一个刚才没有被拿走的杯子。如果在这个过程中出现了标签值小于所有标签的最小值的情况，那么它会环绕到所有标签的最大值。
> - 螃蟹将刚拿走的杯子放到目标杯子顺时针方向之后，并保持拿起时相同的顺序。
> - 螃蟹会选择一个新的当前杯子：当前杯子顺时针方向之后的杯子。

For example, suppose your cup labeling were `389125467`. If the crab were to do merely 10 moves, the following changes would occur:

> 举个例子，假设你的杯子标签为 `389125467`。如果螃蟹只移动 10 次，将发生如下变化：

```'
-- move 1 --
cups: (3) 8  9  1  2  5  4  6  7 
pick up: 8, 9, 1
destination: 2

-- move 2 --
cups:  3 (2) 8  9  1  5  4  6  7 
pick up: 8, 9, 1
destination: 7

-- move 3 --
cups:  3  2 (5) 4  6  7  8  9  1 
pick up: 4, 6, 7
destination: 3

-- move 4 --
cups:  7  2  5 (8) 9  1  3  4  6 
pick up: 9, 1, 3
destination: 7

-- move 5 --
cups:  3  2  5  8 (4) 6  7  9  1 
pick up: 6, 7, 9
destination: 3

-- move 6 --
cups:  9  2  5  8  4 (1) 3  6  7 
pick up: 3, 6, 7
destination: 9

-- move 7 --
cups:  7  2  5  8  4  1 (9) 3  6 
pick up: 3, 6, 7
destination: 8

-- move 8 --
cups:  8  3  6  7  4  1  9 (2) 5 
pick up: 5, 8, 3
destination: 1

-- move 9 --
cups:  7  4  1  5  8  3  9  2 (6)
pick up: 7, 4, 1
destination: 5

-- move 10 --
cups: (5) 7  4  1  8  3  9  2  6 
pick up: 7, 4, 1
destination: 3

-- final --
cups:  5 (8) 3  7  4  1  9  2  6 
```

In the above example, the cups' values are the labels as they appear moving clockwise around the circle; the **current cup** is marked with `( )`.

> 在上面的例子中，杯子的值就是围绕圆圈顺时针移动的标签，当前杯子标记为 `( )`。

After the crab is done, what order will the cups be in? Starting **after the cup labeled `1`**, collect the other cups' labels clockwise into a single string with no extra characters; each number except `1` should appear exactly once. In the above example, after 10 moves, the cups clockwise from `1` are labeled `9`, `2`, `6`, `5`, and so on, producing **`92658374`**. If the crab were to complete all 100 moves, the order after cup `1` would be **`67384529`**.

> 当螃蟹结束后，杯子的顺序是什么？从标有 `1` 的杯子之后开始，顺时针收集其他杯子的标签组成一串没有多余字符的字符串；排除掉 `1`，每个数字出现一次。在上面的例子中，在移动了 10 次之后，从 `1` 开始顺时针方向的杯子分别标记为 `9`，`2`，`6`，`5`，依此类推，得到 **`92658374`**。如果螃蟹完成全部的 100 次移动，则杯子 `1` 之后的顺序为 **`67384529`**。

Using your labeling, simulate 100 moves. **What are the labels on the cups after cup `1`?**

> 使用你的标签，模拟 100 次移动。杯子 `1` 之后的标签是什么？

Your puzzle answer was `43769582`.

## --- Part Two ---

Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), you are quite surprised when the crab starts arranging **many** cups in a circle on your raft - **one million** (`1000000`) in total.

> 你惊讶的发现螃蟹在你的木筏上开始将许许多多的杯子排列成一圆圈，足足有一百万个之多（`1000000`），你唯一能想到的就是翻译出错了（因为你不擅长螃蟹语言）

Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. (For example, if your labeling were `54321`, the cups would be numbered `5`, `4`, `3`, `2`, `1`, and then start counting up from `6` until one million is reached.) In this way, every number from one through one million is used exactly once.

> 你前几个杯子的标签仍然是正确的。但在之后，剩下的杯子的编号将从你的列表中最大编号的后面开始逐一递增，直到达到一百万。（例如，如果你的标签为 `54321`，则杯子将被编号为 `5`，`4`，`3`，`2`，`1`，然后从 `6` 开始逐一递增，直到一百万。）这种情况下，从一到一百万中的每个数字都只用一次。

After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; the crab is going to do **ten million** (`10000000`) moves!

> 当你发现出错的地方原来是翻译螃蟹数字有误后，你意识到小螃蟹不打算只做 100 次移动，而是打算做一千万（`10000000`）次移动！

The crab is going to hide your **stars** - one each - under the **two cups that will end up immediately clockwise of cup `1`**. You can have them if you predict what the labels on those cups will be when the crab is finished.

> 螃蟹打算把你的星星藏在两个杯子下面（各藏一个），放在杯子 `1` 的顺时针方向之后。如果你能预测螃蟹完成后那些杯子上的标签是什么，你就可以获得它们。

In the above example (`389125467`), this would be `934001` and then `159792`; multiplying these together produces **`149245887792`**.

> 在上面的例子（`389125467`）中，标签为 `934001` 和 `159792`，相乘得到 **`149245887792`**。

Determine which two cups will end up immediately clockwise of cup `1`. **What do you get if you multiply their labels together?**

> 确定杯子 `1` 的顺时针方向之后是哪两个杯子。如果将它们的标签相乘会得到什么？

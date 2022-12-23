# Day 11: Monkey in the Middle

> 第11天：中间的猴子 

As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then, one of the items from your pack goes flying overhead. Monkeys are playing [Keep Away](https://en.wikipedia.org/wiki/Keep_away) with your missing things!

> 你终于可以开始向上游出发了，你注意到你的背包比你记忆中的要轻得多。就在这时，背包里的一件物品从你头顶飞过。猴子正在用你丢失的东西玩[“你来抢啊”](https://en.wikipedia.org/wiki/Keep_away)游戏！

To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on **how worried you are about each item**.

> 为了取回你的东西，你需要能够预测猴子会把你的东西扔到哪里。经过仔细观察，你发现猴子会根据**你对每件物品的担忧程度**来运作。

You take some notes ([your puzzle input](day11.txt)) on the items each monkey currently has, how worried you are about those items, and how the monkey makes decisions based on your worry level. For example:

> 你做了一些笔记（[你的谜题输入](day11.txt)），内容包括每只猴子当前拥有的物品、你对这些物品的担忧程度以及猴子根据你的担忧程度做出决定。例如：

```
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
```

Each monkey has several attributes:

- `Starting items` lists your **worry level** for each item the monkey is currently holding in the order they will be inspected.
- `Operation` shows how your worry level changes as that monkey inspects an item. (An operation like `new = old * 5` means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
- `Test` shows how the monkey uses your worry level to decide where to throw an item next.
  - `If true` shows what happens with an item if the `Test` was true.
  - `If false` shows what happens with an item if the `Test` was false.

> 每只猴子都有一些属性：
>
> - `Starting items` 列出了你对这只猴子当前持有的每件物品的**担忧程度**，顺序是它们被检查的顺序。
> - `Operation` 显示当猴子检查物品时你的担忧程度如何变化。（例如 `new = old * 5` 这样的操作表示 你在猴子检查物品后的担忧程度是检查前的五倍。）
> - `Test` 显示猴子如何利用你的担忧程度来判断将物品扔到哪里。
>    - `If true` 显示如果 `Test` 为真，物品会发生什么。
>    - `If false` 显示如果 `Test` 为假，物品会发生什么。

After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be **divided by three** and rounded down to the nearest integer.

> 在每只猴子检查一件物品之后，测试你的担忧程度之前，你松了口气，因为这只猴子的检查没有损坏物品，所以使你的担忧程度**除以三**并向下取整。

The monkeys take turns inspecting and throwing items. On a single monkey's **turn**, it inspects and throws all of the items it is holding one at a time and in the order listed. Monkey `0` goes first, then monkey `1`, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a **round**.

> 猴子们会轮流检查和投掷物品。在一只猴子的**回合**中，它会按照列出的顺序依次检查并扔掉它持有的物品。猴子“0”先开始，然后是猴子“1”，依此类推，直到每只猴子都轮到一次。每只猴子都轮到一次的过程称为一**轮**。

When a monkey throws an item to another monkey, the item goes on the **end** of the recipient monkey's list. A monkey that starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.

> 当一只猴子将一件物品扔给另一只猴子时，该物品会放入接收猴子的列表**末尾**。如果一只猴子在一轮开始时没有物品，当轮到它时它依旧可以检查并扔掉这个过程中它接收到的物品。如果一只猴子在回合开始时没有任何物品，则回合结束。

In the above example, the first round proceeds as follows:

> 在上面的例子中，第一轮的过程如下：

```
Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.
Monkey 1:
  Monkey inspects an item with a worry level of 54.
    Worry level increases by 6 to 60.
    Monkey gets bored with item. Worry level is divided by 3 to 20.
    Current worry level is not divisible by 19.
    Item with worry level 20 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 65.
    Worry level increases by 6 to 71.
    Monkey gets bored with item. Worry level is divided by 3 to 23.
    Current worry level is not divisible by 19.
    Item with worry level 23 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 75.
    Worry level increases by 6 to 81.
    Monkey gets bored with item. Worry level is divided by 3 to 27.
    Current worry level is not divisible by 19.
    Item with worry level 27 is thrown to monkey 0.
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 6 to 80.
    Monkey gets bored with item. Worry level is divided by 3 to 26.
    Current worry level is not divisible by 19.
    Item with worry level 26 is thrown to monkey 0.
Monkey 2:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by itself to 6241.
    Monkey gets bored with item. Worry level is divided by 3 to 2080.
    Current worry level is divisible by 13.
    Item with worry level 2080 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 60.
    Worry level is multiplied by itself to 3600.
    Monkey gets bored with item. Worry level is divided by 3 to 1200.
    Current worry level is not divisible by 13.
    Item with worry level 1200 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 97.
    Worry level is multiplied by itself to 9409.
    Monkey gets bored with item. Worry level is divided by 3 to 3136.
    Current worry level is not divisible by 13.
    Item with worry level 3136 is thrown to monkey 3.
Monkey 3:
  Monkey inspects an item with a worry level of 74.
    Worry level increases by 3 to 77.
    Monkey gets bored with item. Worry level is divided by 3 to 25.
    Current worry level is not divisible by 17.
    Item with worry level 25 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 500.
    Worry level increases by 3 to 503.
    Monkey gets bored with item. Worry level is divided by 3 to 167.
    Current worry level is not divisible by 17.
    Item with worry level 167 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 620.
    Worry level increases by 3 to 623.
    Monkey gets bored with item. Worry level is divided by 3 to 207.
    Current worry level is not divisible by 17.
    Item with worry level 207 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 1200.
    Worry level increases by 3 to 1203.
    Monkey gets bored with item. Worry level is divided by 3 to 401.
    Current worry level is not divisible by 17.
    Item with worry level 401 is thrown to monkey 1.
  Monkey inspects an item with a worry level of 3136.
    Worry level increases by 3 to 3139.
    Monkey gets bored with item. Worry level is divided by 3 to 1046.
    Current worry level is not divisible by 17.
    Item with worry level 1046 is thrown to monkey 1.
```

After round 1, the monkeys are holding items with these worry levels:

> 第一轮过后，猴子们持有的物品和担忧程度如下：

```
Monkey 0: 20, 23, 27, 26
Monkey 1: 2080, 25, 167, 207, 401, 1046
Monkey 2: 
Monkey 3: 
```

Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.

> 猴子 2 和 3 在这一轮结束后没有持有任何物品，他们都在一轮中检查了物品，并在一轮结束前将它们全部扔掉了。

This process continues for a few more rounds:

> 这个过程持续了几轮：

```
After round 2, the monkeys are holding items with these worry levels:
Monkey 0: 695, 10, 71, 135, 350
Monkey 1: 43, 49, 58, 55, 362
Monkey 2: 
Monkey 3: 

After round 3, the monkeys are holding items with these worry levels:
Monkey 0: 16, 18, 21, 20, 122
Monkey 1: 1468, 22, 150, 286, 739
Monkey 2: 
Monkey 3: 

After round 4, the monkeys are holding items with these worry levels:
Monkey 0: 491, 9, 52, 97, 248, 34
Monkey 1: 39, 45, 43, 258
Monkey 2: 
Monkey 3: 

After round 5, the monkeys are holding items with these worry levels:
Monkey 0: 15, 17, 16, 88, 1037
Monkey 1: 20, 110, 205, 524, 72
Monkey 2: 
Monkey 3: 

After round 6, the monkeys are holding items with these worry levels:
Monkey 0: 8, 70, 176, 26, 34
Monkey 1: 481, 32, 36, 186, 2190
Monkey 2: 
Monkey 3: 

After round 7, the monkeys are holding items with these worry levels:
Monkey 0: 162, 12, 14, 64, 732, 17
Monkey 1: 148, 372, 55, 72
Monkey 2: 
Monkey 3: 

After round 8, the monkeys are holding items with these worry levels:
Monkey 0: 51, 126, 20, 26, 136
Monkey 1: 343, 26, 30, 1546, 36
Monkey 2: 
Monkey 3: 

After round 9, the monkeys are holding items with these worry levels:
Monkey 0: 116, 10, 12, 517, 14
Monkey 1: 108, 267, 43, 55, 288
Monkey 2: 
Monkey 3: 

After round 10, the monkeys are holding items with these worry levels:
Monkey 0: 91, 16, 20, 98
Monkey 1: 481, 245, 22, 26, 1092, 30
Monkey 2: 
Monkey 3: 

...

After round 15, the monkeys are holding items with these worry levels:
Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
Monkey 1: 110, 36
Monkey 2: 
Monkey 3: 

...

After round 20, the monkeys are holding items with these worry levels:
Monkey 0: 10, 12, 14, 26, 34
Monkey 1: 245, 93, 53, 199, 115
Monkey 2: 
Monkey 3: 
```

Chasing all of the monkeys at once is impossible; you're going to have to focus on the **two most active** monkeys if you want any hope of getting your stuff back. Count the **total number of times each monkey inspects items** over 20 rounds:

> 一次追赶所有的猴子是不可能的。如果你想找回你的东西，你将不得不只专注**两只最活跃**的猴子。计算 20 轮中**每只猴子检查物品的总次数**：

```
Monkey 0 inspected items 101 times.
Monkey 1 inspected items 95 times.
Monkey 2 inspected items 7 times.
Monkey 3 inspected items 105 times.
```

In this example, the two most active monkeys inspected items 101 and 105 times. The level of **monkey business** in this situation can be found by multiplying these together: **`10605`**.

> 在这个例子中，两只最活跃的猴子分别检查了物品 101 和 105 次。在这种情况下，**猴子生意**的水平可以通过将它们相乘得到：**`10605`**。

Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. **What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?**

> 通过计算猴子们在 20 轮中检查了多少物品来确定要追逐哪些猴子。**经过 20 轮投掷物品的猿猴闹剧，猴子生意的水平是多少？**

Your puzzle answer was `54054`.

## Part Two

You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item **no longer causes your worry level to be divided by three**.

> 你担心你可能永远也无法取回物品了。你是如此担心，事实上，猴子的检查没有损坏物品这件事已经无法使你感到宽慰，**这使你的担忧程度不再除以三**。

Unfortunately, that relief was all that was keeping your worry levels from reaching **ridiculous levels**. You'll need to **find another way to keep your worry levels manageable**.

> 不幸的是，正是因为这种宽慰才使你的担忧程度没有达到**荒谬的程度**。你需要**寻找另一种方法来控制你的担忧程度**。

At this rate, you might be putting up with these monkeys for a **very long time** - possibly **`10000` rounds**!

> 按照这个速度，你可能会忍受这些猴子**很长时间**，也许是 **`10000` 轮**！

With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

> 有了这些新规则，你仍然能够在 10000 轮之后算出猴子生意。使用上面的相同例子：

```
== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.
```

After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of **monkey business** in this situation is now **`2713310158`**.

> 10000 轮之后，最活跃的两只猴子分别检查了 52166 次和 52013 次物品。将它们相乘，这种情况下的**猴子生意**的水平是 **`2713310158`**。

Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, **what is the level of monkey business after 10000 rounds?**

> 现在，每个物品检查后担忧程度不再除以三了。你需要寻找另一种方法来控制你的担忧程度。再次从谜题输入的初始状态开始，**10000 轮后猴子生意的水平是多少？**

Your puzzle answer was `14314925001`.

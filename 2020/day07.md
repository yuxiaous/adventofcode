# Day 7: Handy Haversacks

> 第七天：便利袋

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to **issues in luggage processing**.

> 你准时降落在了中转机场并准备接下来的飞行。实际上，你甚至有时间可以吃点东西。由于行李处理问题，目前所有航班都被推迟了。

Due to recent aviation regulations, many rules ([your puzzle input](day07.txt)) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

> 基于最新的航空条令，关于行李及其内容的许多规定（[你的谜题输入](day07.txt)）正在执行。包必须使用颜色进行编码，并且必须包含特定数量的其他颜色进行编码的包。显然，负责这些规定的人没有人考虑过需要多长时间来执行！

For example, consider the following rules:

> 举个例子，考虑以下规则：

```'
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
```

These rules specify the required contents for 9 bag types. In this example, every `faded blue` bag is empty, every `vibrant plum` bag contains 11 bags (5 `faded blue` and 6 `dotted black`), and so on.

> 这些规则指定了 9 种类型的必要内容。在这个例子中，`faded blue` 颜色的包是空的，`vibrant plum` 颜色的包含有 11 个包（5 个 `faded blue` 和 6 个 `dotted black`），依此类推。

You have a **`shiny gold`** bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one `shiny gold` bag?)

> 你有一个 `shiny gold` 颜色的包。如果你想将它装在其他包中，有多少种不同的颜色的最外层包是有效的？（换句话说：最终多少种颜色可以容纳至少一个 `shiny gold` 颜色的包？）

In the above rules, the following options would be available to you:

- A `bright white` bag, which can hold your `shiny gold` bag directly.
- A `muted yellow` bag, which can hold your `shiny gold` bag directly, plus some other bags.
- A `dark orange` bag, which can hold `bright white` and `muted yellow` bags, either of which could then hold your `shiny gold` bag.
- A `light red` bag, which can hold `bright white` and `muted yellow` bags, either of which could then hold your `shiny gold` bag.

> 根据上面的规则，你可以使用以下几种方式：
>
> - 一个 `bright white` 包，可以直接容纳你的 `shiny gold` 包。
> - 一个 `muted yellow` 包，可以直接容纳你的 `shiny gold` 包，以及一些其他包。
> - 一个 `dark orange` 包，可以容纳 `bright white` 包和 `muted yellow` 包，然后其中一个可以容纳你的 `shiny gold` 包。
> - 一个 `light red` 包，可以容纳 `bright white` 包和 `muted yellow` 包，然后其中一个可以容纳你的 `shiny gold` 包。

So, in this example, the number of bag colors that can eventually contain at least one `shiny gold` bag is **`4`**.

> 因此，在这个例子中，最终可以包含至少一个 `shiny gold` 颜色的包的数量为 `4`。

**How many bag colors can eventually contain at least one shiny gold bag?** (The list of rules is quite long; make sure you get all of it.)

> 最终有多少种颜色的包可以容纳至少一个 `shiny gold` 颜色的包？（规则列表很长，请确保你获得了所有的内容。）

Your puzzle answer was `211`.

## --- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

> 这些天你乘飞机变得非常昂贵，不是因为机票价格，而是因为你需要为如此荒谬的包的数量买单！

Consider again your `shiny gold` bag and the rules from the above example:

- `faded blue` bags contain `0` other bags.
- `dotted black` bags contain `0` other bags.
- `vibrant plum` bags contain `11` other bags: 5 `faded blue` bags and 6 `dotted black` bags.
- `dark olive` bags contain `7` other bags: 3 `faded blue` bags and 4 `dotted black` bags.

> 再次研究一下你的 `shiny gold` 包和上面例子中的规则：
>
> - `faded blue` 包含有 `0` 个其他包。
> - `dotted black` 包含有 `0` 个其他包。
> - `vibrant plum` 包含有 `11` 个其他包：5 个 `faded blue` 包和 6 个 `dotted black` 包。
> - `dark olive` 包含有 `7` 个其他包：3 个 `faded blue` 包和 4 个 `dotted black` 包。

So, a single `shiny gold` bag must contain 1 `dark olive` bag (and the 7 bags within it) plus 2 `vibrant plum` bags (and the 11 bags within **each** of those): `1 + 1*7 + 2 + 2*11` = **`32`** bags!

> 因此，一个 `shiny gold` 包可以放下 1 个 `dark olive` 包（及其中的 7 个包）和 2 个 `vibrant plum` 包（及其每个中的 11 个包）：`1 + 1*7 + 2 + 2*11` = **`32`** 个包！

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

> 当然，实际的规则比这个例子不知道高到哪里去了，即使嵌套数量在拓扑上变得不切实际，也要确保统计到所有的包！

Here's another example:

> 这是另一个例子：

```'
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
```

In this example, a single `shiny gold` bag must contain **`126`** other bags.

> 在这个例子中，一个 `shiny gold` 包可以放下 **`126`** 个其他包。

**How many individual bags are required inside your single `shiny gold` bag?**

> 一个 `shiny gold` 包可以放多少个单独的包？

Your puzzle answer was `12414`.

# Day 3: Rucksack Reorganization

> 第3天：登山包重组

One Elf has the important job of loading all of the [rucksacks](https://en.wikipedia.org/wiki/Rucksack) with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

> 一个精灵有一项重要工作，是为所有[登山包](https://en.wikipedia.org/wiki/Rucksack)装上丛林旅行所需的补给品。不幸的是，那个精灵并没有完全按照包装说明进行操作，因此现在需要重新排列一些物品。

Each rucksack has two large **compartments**. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

> 每个登山包都有两个大的**隔间**。每种给定类型的所有物品应该放入两个隔间中的一个。负责打包的精灵错误地理解了这个规则，认为每个登山包只放入一种物品类型。

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, `a` and `A` refer to different types of items).

> 精灵们已经列出了当前每个登山包中的所有物品（[你的谜题输入](day03.txt)），但他们需要你帮助查找错误。每种物品的类型都由单个小写或大写字母标识（即 `a` 和 `A` 指的是不同的物品类型）。

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

> 每个登山包中的物品列表都以一行字符串的形式给出。每个登山包的两个隔间中总是有相同数量的物品，所以前半段字符串代表第一个隔间中的物品，而后半段字符串代表第二个隔间中的物品。

For example, suppose you have the following list of contents from six rucksacks:

> 举个例子，假设你有以下六个登山包的内容列表：

```'
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

- The first rucksack contains the items `vJrwpWtwJgWrhcsFMMfFFhFp`, which means its first compartment contains the items `vJrwpWtwJgWr`, while the second compartment contains the items `hcsFMMfFFhFp`. The only item type that appears in both compartments is lowercase **`p`**.
- The second rucksack's compartments contain `jqHRNqRjqzjGDLGL` and `rsFMfFZSrLrFZsSL`. The only item type that appears in both compartments is uppercase **`L`**.
- The third rucksack's compartments contain `PmmdzqPrV` and `vPwwTWBwg`; the only common item type is uppercase **`P`**.
- The fourth rucksack's compartments only share item type **`v`**.
- The fifth rucksack's compartments only share item type **`t`**.
- The sixth rucksack's compartments only share item type **`s`**.

> - 第一个登山包装有物品 `vJrwpWtwJgWrhcsFMMfFFhFp`，这意味着它的第一个隔间包含物品`vJrwpWtwJgWr`，而第二个隔间包含物品 `hcsFMMfFFhFp`。唯一的两个隔间都有的物品类型是小写的 **`p`**。
> - 第二个登山包的隔间包含 `jqHRNqRjqzjGDLGL` 和 `rsFMfFZSrLrFZsSL`。唯一的两个隔间都有的物品类型是大写的 **`L`**。
> - 第三个登山包的隔间包含 `PmmdzqPrV` 和 `vPwwTWBwg`。唯一的相同物品类型是大写的 **`P`**。
> - 第四个登山包隔间的唯一相同物品类型 **`v`**。
> - 第五个登山包隔间的唯一相同物品类型 **`t`**。
> - 第六个登山包隔间的唯一相同物品类型 **`s`**。

To help prioritize item rearrangement, every item type can be converted to a **priority**:

- Lowercase item types `a` through `z` have priorities 1 through 26.
- Uppercase item types `A` through `Z` have priorities 27 through 52.

> 为了帮助确定物品重新排列的优先级，每种物品的类型都可以转换为一个**优先级**：
>
> - 小写的物品类型 `a` 到 `z` 优先级为 1 到 26。
> - 大写的物品类型 `A` 到 `Z` 优先级为 27 到 52。

In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (`p`), 38 (`L`), 42 (`P`), 22 (`v`), 20 (`t`), and 19 (`s`); the sum of these is **`157`**.

> 在上面的例子中，同时出现在每个登山包两个隔间中的物品类型的优先级分别是 16 (`p`), 38 (`L`), 42 (`P`), 22 (`v`), 20 ( `t`) 和 19 (`s`)。它们的总和是 **`157`**。

Find the item type that appears in both compartments of each rucksack. **What is the sum of the priorities of those item types?**

> 找到同时出现在每个登山包两个隔间中的物品类型。**这些物品类型的优先级总和是多少？**

# [Day 14: Extended Polymerization](https://adventofcode.com/2021/day/14)

> 第14天：扩展聚合

The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has [polymerization](https://en.wikipedia.org/wiki/Polymerization) equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

> 这个深度令人难以置信的压力开始给你的潜水艇带来拉伤。潜水艇有[聚合](https://en.wikipedia.org/wiki/Polymerization)设备，可以生产合适的材料来加固潜水艇，并且附近的活火山洞穴应该有足够数量的必要原料。

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a **polymer template** and a list of **pair insertion** rules ([your puzzle input](day14.txt)). You just need to work out what polymer would result after repeating the pair insertion process a few times.

> 潜水艇手册里包含了如何获得最佳聚合物分子式的说明。具体来说，它提供了一个**聚合物模板**和一个**对插入**规则列表（[你的谜题输入](day14.txt)）。你需要分析出在多次重复插入对的过程后产生了什么聚合物。

For example:

> 举个例子：

```'
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
```

The first line is the **polymer template** - this is the starting point of the process.

> 第一行是**聚合物模板** -- 这是过程的起点。

The following section defines the **pair insertion** rules. A rule like `AB -> C` means that when elements `A` and `B` are immediately adjacent, element `C` should be inserted between them. These insertions all happen simultaneously.

> 之后的部分定义了**对插入**规则。例如 `AB -> C` 这样的规则表示，当元素 `A` 和 `B` 紧邻时，可以在它们之间插入元素 `C`。所有这些插入过程都是同时发生的。

So, starting with the polymer template `NNCB`, the first step simultaneously considers all three pairs:

> 因此，从聚合物模板 `NNCB` 开始，第一步需要同时考虑三个对：

- The first pair (`NN`) matches the rule `NN -> C`, so element **`C`** is inserted between the first `N` and the second `N.`
- The second pair (`NC`) matches the rule `NC -> B`, so element **`B`** is inserted between the `N` and the `C`.
- The third pair (`CB`) matches the rule `CB -> H`, so element **`H`** is inserted between the `C` and the `B`.

> - 第一个对（`NN`）与规则 `NN -> C` 匹配，因此元素 **`C`** 被插入到第一个 `N` 和第二个 `N` 之间。
> - 第二个对（`NC`）与规则 `NC -> B` 匹配，所以元素 **`B`** 被插入到 `N` 和 `C` 之间。
> - 第三个对（`CB`）与规则 `CB -> H` 匹配，所以元素 **`H`** 被插入到 `C` 和 `B` 之间。

Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

> 请注意，这些对重叠：第一个对的第二个元素是下一个对的第一个元素。此外，由于需要同时考虑所有的对，因此在下一个步骤之前，新插入的元素不会被视为一个对中的一部分。

After the first step of this process, the polymer becomes `N`**`C`**`N`**`B`**`C`**`H`**`B`.

> 在这个过程的第一步之后，聚合物变成了 `N`**`C`**`N`**`B`**`C`**`H`**`B`。

Here are the results of a few steps using the above rules:

> 以下是使用上述规则的几个步骤后的结果：

```'
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
```

This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, `B` occurs 1749 times, `C` occurs 298 times, `H` occurs 161 times, and `N` occurs 865 times; taking the quantity of the most common element (`B`, 1749) and subtracting the quantity of the least common element (`H`, 161) produces `1749 - 161 =` **`1588`**.

> 这种聚合物生长迅速。在 5 个步骤后，它的长度变为了 97；在 10 个步骤后，它的长度变为了 3073。在 10 个步骤后，`B` 出现了 1749 次，`C` 出现了 298 次，`H` 出现了 161 次，`N` 出现了 865 次。取最多元素的数量（`B`，1749）减去最少元素的数量（`H`，161），得到 `1749 - 161 =` **`1588`**。

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. **What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?**

> 对聚合物模板进行 10 步对插入，并在结果中找出最多和最少的元素。**如果你取最多元素的数量减去最少元素的数量，你会得到什么？**

Your puzzle answer was `2657`.

## --- Part Two ---

The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of **40 steps** should do it.

> 产出的聚合物的强度不足以加固潜水艇。你需要进行更多次对插入过程，应该进行总共 **40 步**。

In the above example, the most common element is `B` (occurring `2192039569602` times) and the least common element is `H` (occurring `3849876073` times); subtracting these produces **`2188189693529`**.

> 在上面的例子中，最多的元素是 `B`（出现了 `2192039569602` 次），最少的元素是 `H`（出现了 `3849876073` 次），相减得到 **`2188189693529`**。

Apply **40** steps of pair insertion to the polymer template and find the most and least common elements in the result. **What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?**

> 将 **40** 对插入步骤应用于聚合物模板，并在结果中找到最常见和最不常见的元素。 **如果你取最常见元素的数量并减去最不常见元素的数量，你会得到什么？**

Your puzzle answer was `2911561572630`.

# Day 5: Print Queue
> # 第五天：打印队列

Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.
> 在谷神星的搜寻让大家满意后，这群学者建议接着去扫描17号地下室的文具堆。

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a [very familiar printer](https://adventofcode.com/2017/day/1) beckons you over.
> 圣诞节临近，北极的打印部门比以往任何时候都要忙碌。历史学家们继续在这个具有历史意义的设施中搜寻时，一位操作着非常熟悉的打印机的精灵招呼你过去。

The Elf must recognize you, because they waste no time explaining that the new **sleigh launch safety manual** updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.
> 这位精灵一定认出了你，因为他毫不犹豫地解释说新的**雪橇发射安全手册**更新无法正确打印。如果不能及时更新安全手册，后果将非常严重，于是你主动提出帮忙。

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a **very specific order**. The notation `X|Y` means that if both page number `X` and page number `Y` are to be produced as part of an update, page number `X` **must** be printed at some point before page number `Y`.
> 安全协议明确规定，安全手册的新页面必须以**非常特定的顺序**打印。记号 `X|Y` 表示，如果一次更新中既有页码 `X` 又有页码 `Y`，则 `X` **必须**在 `Y` 之前的某个位置被打印。

The Elf has for you both the **page ordering rules** and the **pages to produce in each update** (your puzzle input), but can't figure out whether each update has the pages in the right order.
> 精灵给了你**页面排序规则**和**每次更新要打印的页面**（你的谜题输入），但他无法判断每次更新的页面顺序是否正确。

For example:
> 例如：

```
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```

The first section specifies the **page ordering rules**, one per line. The first rule, `47|53`, means that if an update includes both page number 47 and page number 53, then page number 47 **must** be printed at some point before page number 53. (47 doesn't necessarily need to be **immediately** before 53; other pages are allowed to be between them.)
> 第一部分指定了**页面排序规则**，每行一条。第一条规则 `47|53` 表示，如果一次更新中既有47页又有53页，则47页**必须**在53页之前的某个位置被打印。（47页不必**紧挨着**53页，其他页可以夹在中间。）

The second section specifies the page numbers of each **update**. Because most safety manuals are different, the pages needed in the updates are different too. The first update, `75,47,61,53,29`, means that the update consists of page numbers 75, 47, 61, 53, and 29.
> 第二部分指定了每次**更新**的页码。由于大多数安全手册都不同，每次更新所需的页面也不同。第一个更新 `75,47,61,53,29` 表示这次更新包含页面 75、47、61、53 和 29。

To get the printers going as soon as possible, start by identifying **which updates are already in the right order**.
> 为了尽快让打印机开始工作，首先要确定**哪些更新已经是正确顺序**。

In the above example, the first update (`75,47,61,53,29`) is in the right order:
> 在上面的例子中，第一个更新（`75,47,61,53,29`）顺序是正确的：

- `75` is correctly first because there are rules that put each other page after it: `75|47`, `75|61`, `75|53`, and `75|29`.
- `47` is correctly second because 75 must be before it (`75|47`) and every other page must be after it according to `47|61`, `47|53`, and `47|29`.
- `61` is correctly in the middle because 75 and 47 are before it (`75|61` and `47|61`) and 53 and 29 are after it (`61|53` and `61|29`).
- `53` is correctly fourth because it is before page number 29 (`53|29`).
- `29` is the only page left and so is correctly last.
> - `75` 正确地排在第一位，因为有规则要求其他每一页都在它之后：`75|47`、`75|61`、`75|53` 和 `75|29`。
> - `47` 正确地排在第二位，因为75必须在它前面（`75|47`），而且根据 `47|61`、`47|53` 和 `47|29`，其他每一页都必须在它后面。
> - `61` 正确地排在中间，因为75和47在它前面（`75|61` 和 `47|61`），53和29在它后面（`61|53` 和 `61|29`）。
> - `53` 正确地排在第四位，因为它在29前面（`53|29`）。
> - `29` 是剩下的唯一一页，因此正确地排在最后。

Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.
> 因为第一个更新没有包含某些页码，涉及这些缺失页码的排序规则会被忽略。

The second and third updates are also in the correct order according to the rules. Like the first update, they also do not include every page number, and so only some of the ordering rules apply - within each update, the ordering rules that involve missing page numbers are not used.
> 第二个和第三个更新根据规则也顺序正确。和第一个更新一样，它们也没有包含所有页码，因此只应用部分排序规则——每个更新中，涉及缺失页码的排序规则不会被使用。

The fourth update, `75,97,47,61,53`, is **not** in the correct order: it would print 75 before 97, which violates the rule `97|75`.
> 第四个更新 `75,97,47,61,53` 顺序**不正确**：它会在97之前打印75，违反了 `97|75` 规则。

The fifth update, `61,13,29`, is also **not** in the correct order, since it breaks the rule `29|13`.
> 第五个更新 `61,13,29` 也**不正确**，因为它违反了 `29|13` 规则。

The last update, `97,13,75,29,47`, is **not** in the correct order due to breaking several rules.
> 最后一个更新 `97,13,75,29,47` 由于违反了多条规则，也**不正确**。

For some reason, the Elves also need to know the **middle page number** of each update being printed. Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:
> 出于某种原因，精灵们还需要知道每个正在打印的更新的**中间页码**。由于你目前只打印顺序正确的更新，你需要找出每个顺序正确的更新的中间页码。在上面的例子中，顺序正确的更新如下：

```
75,47,61,53,29
97,61,53,29,13
75,29,13
```

These have middle page numbers of `61`, `53`, and `29` respectively. Adding these page numbers together gives **`143`**.
> 它们的中间页码分别是 `61`、`53` 和 `29`。将这些页码相加得到 **`143`**。

Of course, you'll need to be careful: the actual list of **page ordering rules** is bigger and more complicated than the above example.
> 当然，你需要小心：实际的**页面排序规则**列表比上面的例子要大得多，也复杂得多。

Determine which updates are already in the correct order. **What do you get if you add up the middle page number from those correctly-ordered updates?**
> 判断哪些更新已经是正确顺序。**将这些顺序正确的更新的中间页码相加，你会得到多少？**

Your puzzle answer was `6034`.

## Part Two

While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.
> 当精灵们开始打印顺序正确的更新时，你有点时间来修正剩下的那些。

For each of the **incorrectly-ordered updates**, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:
> 对于每个**顺序不正确的更新**，请使用页面排序规则将页码排列到正确顺序。以上例为例，下面是三条顺序不正确的更新及其正确顺序：

- `75,97,47,61,53` becomes `97,75,47,61,53`.
- `61,13,29` becomes `61,29,13`.
- `97,13,75,29,47` becomes `97,75,47,29,13`.
> - `75,97,47,61,53` 变为 `97,75,47,61,53`。
> - `61,13,29` 变为 `61,29,13`。
> - `97,13,75,29,47` 变为 `97,75,47,29,13`。

After taking **only the incorrectly-ordered updates** and ordering them correctly, their middle page numbers are `47`, `29`, and `47`. Adding these together produces **`123`**.
> 只对**顺序不正确的更新**进行正确排序后，它们的中间页码分别是 `47`、`29` 和 `47`。将这些数相加得到 **`123`**。

Find the updates which are not in the correct order. **What do you get if you add up the middle page numbers after correctly ordering just those updates?**
> 找出那些顺序不正确的更新。**仅将这些更新正确排序后，它们的中间页码相加，你会得到多少？**

Your puzzle answer was `6305`.

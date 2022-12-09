# Day 5: Supply Stacks

> 第5天：补给品堆垛

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked **crates**, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

> 最后的补给品从船上卸下后，探险队就可以出发了。补给品存放在带有标记的**板条箱**的堆垛中，但由于所需的补给品被压下许多其他板条箱之下，因此需要重新排列这些板条箱。

The ship has a **giant cargo crane** capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

> 这艘船有一个**巨型货物起重机**，能够在堆垛之间移动板条箱。为确保没有板条箱被压碎或翻倒，起重机操作员将按照一系列精心计划过的步骤重新排列它们。重新排列板条箱后，所需的板条箱将位于每个堆垛的顶部。

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her **which** crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

> 精灵们不想在这个微妙的过程中打断起重机操作员，但他们忘了问她**哪个**板条箱最终会放在哪里，他们打算准备尽快卸载它们以便可以上船。

They do, however, have a drawing of the starting stacks of crates **and** the rearrangement procedure ([your puzzle input](day05.txt)). For example:

> 其实，他们确实有板条箱的初始堆垛图纸**以及**重新排列的步骤（[你的谜题图输入](day05.txt)）。例如：

```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```

In this example, there are three stacks of crates. Stack 1 contains two crates: crate `Z` is on the bottom, and crate `N` is on top. Stack 2 contains three crates; from bottom to top, they are crates `M`, `C`, and `D`. Finally, stack 3 contains a single crate, `P`.

> 在这个例子中，有三堆板条箱。堆垛 1 包含两个板条箱：板条箱 `Z` 在底部，板条箱 `N` 在顶部。堆垛 2 包含三个板条箱，从底部到顶部，它们分别是 `M`、`C` 和 `D`。最后，堆垛 3 包含一个板条箱，`P`。

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

> 然后，给出重新排列的步骤。在这个过程的每一步中，一定数量的板条箱从一个堆垛移到另一个堆垛。在上面的重新排列步骤的第一步中，有 1 个板条箱从堆垛 2 移至堆垛 1，结果如下：

```
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
```

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved **one at a time**, so the first crate to be moved (`D`) ends up below the second and third crates:

> 在第二步中，三个板条箱从堆垛 1 移至堆垛 3。由于**一次只能移动一个**板条箱，因此第一个板条箱 (`D`) 最终位于第二个和第三个板条箱下方：

```
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
```

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved **one at a time**, crate `C` ends up below crate `M`:

> 然后，两个板条箱从堆垛 2 移至堆垛 1。同样，因为**一次只能移动一个**板条箱，板条箱 `C` 最终位于板条箱 `M` 下方：

```
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
```

Finally, one crate is moved from stack 1 to stack 2:

> 最后，将一个板条箱从堆垛 1 移至堆垛 2：

```
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
```

The Elves just need to know **which crate will end up on top of each stack**; in this example, the top crates are `C` in stack 1, `M` in stack 2, and `Z` in stack 3, so you should combine these together and give the Elves the message **`CMZ`**.

> 精灵们需要知道**哪个板条箱最终会出现在每个堆垛的顶部**。在这个例子中，最上面的板条箱分别是堆垛 1 的 `C`，堆垛 2 的 `M`，堆垛 3 的 `Z`，所以你应该将它们组合在一起并给精灵们消息 **`CMZ`**。

**After the rearrangement procedure completes, what crate ends up on top of each stack?**

> **重新排列步骤完成后，哪些板条箱会位于每个堆垛的顶部？**

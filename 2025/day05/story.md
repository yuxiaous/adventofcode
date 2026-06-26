# Day 5: Cafeteria

> 第五天：自助餐厅

As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

> 当叉车冲破墙壁时，精灵们高兴地发现另一边原来真的有一家自助餐厅。

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

> 你听到厨房里传来一阵骚动。"照这样下去，我们就没时间在餐厅里挂花环了！"你决心已定，前去查看。

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

> "要是我们没有在圣诞节前切换到新的库存管理系统就好了！"另一个精灵喊道。你问发生了什么事。

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are **fresh** and which are **spoiled**. When you ask how it works, they give you a copy of their database (your puzzle input).

> 厨房里的精灵们解释了情况：由于他们复杂的新库存管理系统，他们无法判断哪些食材是**新鲜的**，哪些是**变质的**。当你问这个系统如何运作时，他们给了你一份数据库的副本（你的谜题输入）。

The database operates on **ingredient IDs**. It consists of a list of **fresh ingredient ID ranges**, a blank line, and a list of **available ingredient IDs**. For example:

> 数据库基于**食材ID**运作。它包含一个**新鲜食材ID范围**列表、一个空行以及一个**可用食材ID**列表。例如：

```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

The fresh ID ranges are **inclusive**: the range `3-5` means that ingredient IDs `3`, `4`, and `5` are all **fresh**. The ranges can also **overlap**; an ingredient ID is fresh if it is in **any** range.

> 新鲜ID范围是**包含端点的**：范围 `3-5` 意味着食材ID `3`、`4` 和 `5` 都是**新鲜的**。范围也可以**重叠**；一个食材ID如果在**任意**范围内就是新鲜的。

The Elves are trying to determine which of the **available ingredient IDs** are **fresh**. In this example, this is done as follows:

> 精灵们正在尝试确定哪些**可用食材ID**是**新鲜的**。在这个例子中，判断过程如下：

- Ingredient ID `1` is spoiled because it does not fall into any range.
- Ingredient ID `5` is **fresh** because it falls into range `3-5`.
- Ingredient ID `8` is spoiled.
- Ingredient ID `11` is **fresh** because it falls into range `10-14`.
- Ingredient ID `17` is **fresh** because it falls into range `16-20` as well as range `12-18`.
- Ingredient ID `32` is spoiled.

> - 食材ID `1` 是变质的，因为它不在任何范围内。
> - 食材ID `5` 是**新鲜的**，因为它落在范围 `3-5` 内。
> - 食材ID `8` 是变质的。
> - 食材ID `11` 是**新鲜的**，因为它落在范围 `10-14` 内。
> - 食材ID `17` 是**新鲜的**，因为它既落在范围 `16-20` 内，也落在范围 `12-18` 内。
> - 食材ID `32` 是变质的。

So, in this example, **`3`** of the available ingredient IDs are fresh.

> 因此，在这个例子中，有 **`3`** 个可用食材ID是新鲜的。

Process the database file from the new inventory management system. **How many of the available ingredient IDs are fresh?**

> 处理新库存管理系统中的数据库文件。**有多少个可用食材ID是新鲜的？**

Your puzzle answer was `720`.

# Day 1: Calorie Counting

> 第1天：卡路里计算

Santa's reindeer typically eat regular reindeer food, but they need a lot of [magical energy](https://adventofcode.com/2018/day/25) to deliver presents on Christmas. For that, their favorite snack is a special type of **star** fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

> 圣诞老人的驯鹿通常吃普通的驯鹿食物，但它们需要大量的[魔法能量](https://adventofcode.com/2018/day/25)才能在圣诞节送礼物。为此，他们最喜欢的点心是一种只生长在丛林深处的特殊星状水果。精灵们带着你去长着这种水果生长的小丛林进行他们的年度探险。

To supply enough magical energy, the expedition needs to retrieve a minimum of **fifty stars** by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

> 为了提供足够的魔法能量，探险队需要在 12 月 25 日之前取回至少**五十颗星**。尽管精灵向你保证树林里有大量水果，但你还是决定把沿途看到的任何水果都摘下来，以防万一。

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

> 通过解决谜题收集星星。降临节日历中的每一天都会提供两个谜题。当你完成第一个谜题时，第二个谜题才会解锁。每个谜题授予**一颗星**。祝你好运！

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of **Calories** each Elf is carrying ([your puzzle input](day01.txt)).

> 丛林杂草丛生，很难驾车或从空中进入，所以精灵们的探险传统上是徒步进行的。当你的小船靠近陆地时，精灵们开始盘点他们的物资。一个重要的考虑因素是食物，尤其是每个精灵携带的**卡路里**数量（[你的谜题输入](day01.txt)）。

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

> 精灵们轮流记下随身携带的各种正餐、点心、口粮等所含的卡路里数，一行一项。每个精灵用一个空行将他们自己的清单与前一个精灵的清单分开。

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

> 例如，假设精灵们写下了他们物品的卡路里并得到以下列表：

```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```

This list represents the Calories of the food carried by five Elves:

- The first Elf is carrying food with `1000`, `2000`, and `3000` Calories, a total of **`6000`** Calories.
- The second Elf is carrying one food item with **`4000`** Calories.
- The third Elf is carrying food with `5000` and `6000` Calories, a total of **`11000`** Calories.
- The fourth Elf is carrying food with `7000`, `8000`, and `9000` Calories, a total of **`24000`** Calories.
- The fifth Elf is carrying one food item with **`10000`** Calories.

> 这个列表代表了五个精灵所携带的食物的卡路里：
> 
> - 第一个精灵携带的食物有 `1000`、`2000` 和 `3000` 卡路里，总共 **`6000`** 卡路里。
> - 第二个精灵携带了一份 **`4000`** 卡路里的食物。
> - 第三个精灵携带的食物有 `5000` 和 `6000` 卡路里，总共 **`11000`** 卡路里。
> - 第四个精灵携带的食物有 `7000`、`8000` 和 `9000` 卡路里，总共 **`24000`** 卡路里。
> - 第五个精灵携带了一份 **`10000`** 卡路里的食物。

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the **most** Calories. In the example above, this is **`24000`** (carried by the fourth Elf).

> 万一精灵们饿了，需要额外的零食，他们需要知道向哪个精灵请求：他们想知道携带**最多**卡路里的精灵携带了多少卡路里。在上面的例子中，是 **`24000`**（由第四个精灵携带）。

Find the Elf carrying the most Calories. **How many total Calories is that Elf carrying?**

> 找到携带最多卡路里的精灵。**这个精灵携带了多少卡路里？**

Your puzzle answer was `72017`.

## Part Two

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually **run out of snacks**.

> 当你计算出精灵问题的答案时，他们已经意识到携带最多卡路里食物的精灵最终可能会**被吃空零食**。

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the **top three** Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

> 为了避免这种不可接受的情况，精灵们转而想知道携带卡路里最多的**前三名**精灵所携带的总卡路里。这样一来，即使其中一个精灵的零食吃完了，他们还有两个备用。

In the example above, the top three Elves are the fourth Elf (with `24000` Calories), then the third Elf (with `11000` Calories), then the fifth Elf (with `10000` Calories). The sum of the Calories carried by these three elves is **`45000`**.

> 在上面的例子中，排名前三的精灵分别是第四个精灵（`24000` 卡路里），第三个精灵（`11000` 卡路里），和第五个精灵（`10000`卡路里）。这三个精灵携带的卡路里总和是 **`45000`**。

Find the top three Elves carrying the most Calories. **How many Calories are those Elves carrying in total?**

> 找到携带卡路里最多的前三名精灵。**这些精灵总共携带了多少卡路里？**

Your puzzle answer was `212520`.

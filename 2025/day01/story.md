# Day 1: Secret Entrance

> 第一天：秘密入口

The Elves have good news and bad news.

> 精灵们带来了一个好消息和一个坏消息。

The good news is that they've discovered [project management](https://en.wikipedia.org/wiki/Project_management)! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.

> 好消息是他们发现了[项目管理](https://en.wikipedia.org/wiki/Project_management)！这给了他们所需的工具来避免以往的圣诞紧急情况。例如，他们现在知道北极的装饰需要尽快完成，以便其他关键任务能按时开始。

The bad news is that they've realized they have a **different** emergency: according to their resource planning, none of them have any time left to decorate the North Pole!

> 坏消息是他们意识到自己遇到了一个**不同的**紧急情况：根据他们的资源规划，没人还有时间装饰北极！

To save Christmas, the Elves need **you** to **finish decorating the North Pole by December 12th**.

> 为了拯救圣诞节，精灵们需要**你**在**12月12日前完成北极的装饰**。

Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

> 通过解谜来收集星星。每天会发布两个谜题；完成第一个后第二个才会解锁。每个谜题奖励**一颗星**。祝你好运！

You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the **password** seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

> 你到达北极基地的秘密入口，准备开始装饰。不幸的是，**密码**似乎被改了，你进不去。墙上贴着一份文件，贴心地解释道：

"Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

> "由于新的安全协议，密码被锁在下面的保险柜里。请查看附件文件以获取新密码组合。"

The safe has a dial with only an arrow on it; around the dial are the numbers `0` through `99` in order. As you turn the dial, it makes a small **click** noise as it reaches each number.

> 保险柜上有一个转盘，上面只有一根指针；转盘周围按顺序排列着数字 `0` 到 `99`。转动转盘时，每到达一个数字就会发出微小的**咔嗒**声。

The attached document (your puzzle input) contains a sequence of **rotations**, one per line, which tell you how to open the safe. A rotation starts with an `L` or `R` which indicates whether the rotation should be to the **left** (toward lower numbers) or to the **right** (toward higher numbers). Then, the rotation has a **distance** value which indicates how many clicks the dial should be rotated in that direction.

> 附件文件（你的谜题输入）包含一系列**旋转**指令，每行一条，告诉你如何打开保险柜。每条旋转以 `L` 或 `R` 开头，表示旋转方向是向**左**（朝向较小的数字）还是向**右**（朝向较大的数字）。然后，旋转指令有一个**距离**值，表示转盘应向该方向旋转多少格。

So, if the dial were pointing at `11`, a rotation of `R8` would cause the dial to point at `19`. After that, a rotation of `L19` would cause it to point at `0`.

> 因此，如果转盘指向 `11`，旋转 `R8` 将使转盘指向 `19`。之后，旋转 `L19` 将使其指向 `0`。

Because the dial is a circle, turning the dial **left from `0`** one click makes it point at `99`. Similarly, turning the dial **right from `99`** one click makes it point at `0`.

> 由于转盘是一个圆圈，从 `0` 向**左**转一格会使转盘指向 `99`。同样，从 `99` 向**右**转一格会使转盘指向 `0`。

So, if the dial were pointing at `5`, a rotation of `L10` would cause it to point at `95`. After that, a rotation of `R5` could cause it to point at `0`.

> 因此，如果转盘指向 `5`，旋转 `L10` 将使其指向 `95`。之后，旋转 `R5` 将使其指向 `0`。

The dial starts by pointing at `50`.

> 转盘初始指向 `50`。

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is **the number of times the dial is left pointing at `0` after any rotation in the sequence**.

> 你可以遵循这些指令，但你最近参加的官方北极秘密入口安全培训研讨会告诉你，这个保险柜实际上是个幌子。真正的密码是**序列中任意一次旋转结束后转盘指向 `0` 的次数**。

For example, suppose the attached document contained the following rotations:

> 例如，假设附件文件中包含以下旋转指令：

```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

Following these rotations would cause the dial to move as follows:

> 按照这些旋转指令，转盘的移动情况如下：

- The dial starts by pointing at `50`.
- The dial is rotated `L68` to point at `82`.
- The dial is rotated `L30` to point at `52`.
- The dial is rotated `R48` to point at **`0`**.
- The dial is rotated `L5` to point at `95`.
- The dial is rotated `R60` to point at `55`.
- The dial is rotated `L55` to point at **`0`**.
- The dial is rotated `L1` to point at `99`.
- The dial is rotated `L99` to point at **`0`**.
- The dial is rotated `R14` to point at `14`.
- The dial is rotated `L82` to point at `32`.

> - 转盘初始指向 `50`。
> - 旋转 `L68`，转盘指向 `82`。
> - 旋转 `L30`，转盘指向 `52`。
> - 旋转 `R48`，转盘指向 **`0`**。
> - 旋转 `L5`，转盘指向 `95`。
> - 旋转 `R60`，转盘指向 `55`。
> - 旋转 `L55`，转盘指向 **`0`**。
> - 旋转 `L1`，转盘指向 `99`。
> - 旋转 `L99`，转盘指向 **`0`**。
> - 旋转 `R14`，转盘指向 `14`。
> - 旋转 `L82`，转盘指向 `32`。

Because the dial points at `0` a total of three times during this process, the password in this example is **`3`**.

> 在此过程中，转盘总共三次指向 `0`，因此此示例中的密码是 **`3`**。

Analyze the rotations in your attached document. **What's the actual password to open the door?**

> 分析附件文件中的旋转指令。**打开门的实际密码是多少？**

Your puzzle answer was `1084`.

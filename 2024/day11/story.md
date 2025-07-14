# Day 11: Plutonian Pebbles
> # 第十一天：冥王星鹅卵石

The ancient civilization on [Pluto](https://adventofcode.com/2019/day/20) was known for its ability to manipulate spacetime, and while The Historians explore their infinite corridors, you've noticed a strange set of physics-defying stones.
> 冥王星上的古代文明以其操控时空的能力而闻名。当历史学家们探索那些无尽的走廊时，你注意到了一组违反物理规律的奇异石头。

At first glance, they seem like normal stones: they're arranged in a perfectly **straight line**, and each stone has a **number** engraved on it.
> 乍一看，它们像普通石头：被排成一条**直线**，每块石头上都刻着一个**数字**。

The strange part is that every time you blink, the stones **change**.
> 奇怪的是，每当你眨眼时，这些石头都会**发生变化**。

Sometimes, the number engraved on a stone changes. Other times, a stone might **split in two**, causing all the other stones to shift over a bit to make room in their perfectly straight line.
> 有时，石头上的数字会改变。有时，一块石头会**分裂成两块**，导致其他石头稍微移动以在直线上腾出空间。

As you observe them for a while, you find that the stones have a consistent behavior. Every time you blink, the stones each **simultaneously** change according to the **first applicable rule** in this list:
> 你观察了一会儿，发现这些石头有一套固定的行为。每次你眨眼时，每块石头会**同时**按照下列**第一条适用规则**发生变化：

- If the stone is engraved with the number `0`, it is replaced by a stone engraved with the number `1`.
- If the stone is engraved with a number that has an **even** number of digits, it is replaced by **two stones**. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: `1000` would become stones `10` and `0`.)
- If none of the other rules apply, the stone is replaced by a new stone; the old stone's number **multiplied by 2024** is engraved on the new stone.
> - 如果石头上刻着数字 `0`，它会被刻着 `1` 的石头替换。
> - 如果石头上的数字位数是**偶数**，它会被**两块石头**替换。左半部分的数字刻在新的左侧石头上，右半部分的数字刻在新的右侧石头上。（新数字不会保留多余的前导零：`1000` 会变成 `10` 和 `0`。）
> - 如果没有其他规则适用，则用一块新石头替换原石头，新石头上刻着原数字乘以2024。

No matter how the stones change, their **order is preserved**, and they stay on their perfectly straight line.
> 无论石头如何变化，它们的**顺序都保持不变**，始终排成一条直线。

How will the stones evolve if you keep blinking at them? You take a note of the number engraved on each stone in the line (your puzzle input).
> 如果你不断眨眼，这些石头会如何演变？你记录下了当前每块石头上的数字（你的谜题输入）。

If you have an arrangement of five stones engraved with the numbers `0 1 10 99 999` and you blink once, the stones transform as follows:
> 如果你有五块石头，数字分别为 `0 1 10 99 999`，眨眼一次后，石头会这样变化：

- The first stone, `0`, becomes a stone marked `1`.
- The second stone, `1`, is multiplied by 2024 to become `2024`.
- The third stone, `10`, is split into a stone marked `1` followed by a stone marked `0`.
- The fourth stone, `99`, is split into two stones marked `9`.
- The fifth stone, `999`, is replaced by a stone marked `2021976`.
> - 第一块 `0` 变成刻着 `1` 的石头。
> - 第二块 `1` 乘以2024变成 `2024`。
> - 第三块 `10` 分裂成一块刻着 `1` 和一块刻着 `0` 的石头。
> - 第四块 `99` 分裂成两块刻着 `9` 的石头。
> - 第五块 `999` 替换为刻着 `2021976` 的石头。

So, after blinking once, your five stones would become an arrangement of seven stones engraved with the numbers `1 2024 1 0 9 9 2021976`.
> 所以，眨眼一次后，你的五块石头会变成七块，数字分别为 `1 2024 1 0 9 9 2021976`。

Here is a longer example:
> 下面是一个更长的例子：

```
Initial arrangement:
125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
```

In this example, after blinking six times, you would have `22` stones. After blinking 25 times, you would have **`55312`** stones!
> 在这个例子中，眨眼六次后你会有 `22` 块石头。眨眼25次后，你会有 **`55312`** 块石头！

Consider the arrangement of stones in front of you. **How many stones will you have after blinking 25 times?**
> 看看你面前的石头排列。**眨眼25次后你会有多少块石头？**

Your puzzle answer was `218079`.

## Part Two
> ## 第二部分

The Historians sure are taking a long time. To be fair, the infinite corridors **are** very large.
> 历史学家们确实花了很长时间。说实话，那些无尽的走廊**确实**非常大。

**How many stones would you have after blinking a total of 75 times?**
> **如果你总共眨眼75次，你会有多少块石头？**

Your puzzle answer was `259755538429618`.

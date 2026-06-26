# Day 3: Lobby

> 第三天：大厅

You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all **offline**.

> 你走下短短的楼梯，进入大得惊人的大厅，快速通过了安检。然而，当你到达主电梯时，发现每部电梯上方都亮着红灯：它们全部**离线**了。

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

> "抱歉，"一位精灵一边摆弄着附近的控制面板，一边道歉。"好像是某种电涌把它们烧坏了。我会尽快让它们恢复在线的。"

You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

> 你解释了你需要继续深入地下。"好吧，你至少可以坐自动扶梯下到印刷部门，不过没有电梯的话你也没法走太远。也就是说，如果自动扶梯没有也离线的话你是可以下去的。"

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

> "不过，别担心！它没烧坏，只是需要电力。也许你可以在我修电梯的时候把电源先运转起来。"

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their [joltage](https://adventofcode.com/2020/day/10) rating, a value from `1` to `9`. You make a note of their joltage ratings (your puzzle input). For example:

> 附近有一些电池，正是为这种紧急情况给自动扶梯供电准备的。每个电池都标注了它的[电压](https://adventofcode.com/2020/day/10)等级，取值为 `1` 到 `9`。你记下了它们的电压等级（你的谜题输入）。例如：

```
987654321111111
811111111111119
234234234234278
818181911112111
```

The batteries are arranged into **banks**; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on **exactly two** batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like `12345` and you turn on batteries `2` and `4`, the bank would produce `24` jolts. (You cannot rearrange batteries.)

> 电池被组织成**电池组**；输入中的每一行数字对应一组电池。在每一组中，你需要打开**恰好两个**电池；该电池组产生的电压等于你打开的电池上数字所组成的数值。例如，如果你有一组 `12345`，打开了电池 `2` 和 `4`，那么这组将产生 `24` 的电压。（你不能重新排列电池。）

You'll need to find the largest possible joltage each bank can produce. In the above example:

> 你需要找到每组电池能产生的最大电压。在上面的例子中：

- In `987654321111111`, you can make the largest joltage possible, **`98`**, by turning on the first two batteries.
- In `811111111111119`, you can make the largest joltage possible by turning on the batteries labeled `8` and `9`, producing **`89`** jolts.
- In `234234234234278`, you can make **`78`** by turning on the last two batteries (marked `7` and `8`).
- In `818181911112111`, the largest joltage you can produce is **`92`**.

> - 在 `987654321111111` 中，你可以通过打开前两个电池来产生最大电压 **`98`**。
> - 在 `811111111111119` 中，你可以通过打开标有 `8` 和 `9` 的电池，产生 **`89`** 电压。
> - 在 `234234234234278` 中，你可以通过打开最后两个电池（标有 `7` 和 `8`），产生 **`78`**。
> - 在 `818181911112111` 中，你能产生的最大电压是 **`92`**。

The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is `98` + `89` + `78` + `92` = **`357`**.

> 总输出电压是每组最大电压之和，因此在这个例子中，总输出电压为 `98` + `89` + `78` + `92` = **`357`**。

There are many batteries in front of you. Find the maximum joltage possible from each bank; **what is the total output joltage?**

> 你面前有很多电池。找出每组可能的最大电压；**总输出电压是多少？**

Your puzzle answer was `17403`.

## Part Two

The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the [static friction](https://en.wikipedia.org/wiki/Static_friction) of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

> 自动扶梯纹丝不动。精灵解释说，可能需要更高的电压来克服系统的[静摩擦力](https://en.wikipedia.org/wiki/Static_friction)，于是她按下了那个大大的红色"电压极限安全超载"按钮。她反复确认"是的，我确定"的次数多到你数不清，而你在等待时顺便把大厅装饰了一番。

Now, you need to make the largest joltage by turning on **exactly twelve** batteries within each bank.

> 现在，你需要通过在每组中打开**恰好十二个**电池来产生最大的电压。

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be **`12`** digits in each bank's joltage output instead of two.

> 电池组的输出电压仍然是所打开电池的数字组成的数值；唯一的区别是，现在每组电压输出将有 **`12`** 位数字，而不是两位。

Consider again the example from before:

> 再次考虑之前的例子：

```
987654321111111
811111111111119
234234234234278
818181911112111
```

Now, the joltages are much larger:

> 现在，电压要大得多：

- In `987654321111111`, the largest joltage can be found by turning on everything except some `1`s at the end to produce **`987654321111`**.
- In the digit sequence `811111111111119`, the largest joltage can be found by turning on everything except some `1`s, producing **`811111111119`**.
- In `234234234234278`, the largest joltage can be found by turning on everything except a `2` battery, a `3` battery, and another `2` battery near the start to produce **`434234234278`**.
- In `818181911112111`, the joltage **`888911112111`** is produced by turning on everything except some `1`s near the front.

> - 在 `987654321111111` 中，可以通过打开除末尾部分 `1` 之外的所有电池来产生最大电压 **`987654321111`**。
> - 在数字序列 `811111111111119` 中，可以通过打开除部分 `1` 之外的所有电池来产生最大电压 **`811111111119`**。
> - 在 `234234234234278` 中，可以通过打开除一个 `2`、一个 `3` 和开头附近另一个 `2` 之外的所有电池来产生最大电压 **`434234234278`**。
> - 在 `818181911112111` 中，通过打开除开头附近部分 `1` 之外的所有电池，产生电压 **`888911112111`**。

The total output joltage is now much larger: `987654321111` + `811111111119` + `434234234278` + `888911112111` = **`3121910778619`**.

> 现在的总输出电压要大得多：`987654321111` + `811111111119` + `434234234278` + `888911112111` = **`3121910778619`**。

**What is the new total output joltage?**

> **新的总输出电压是多少？**

Your puzzle answer was `173416889848394`.

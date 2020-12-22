# Day 21: Allergen Assessment

> 第二十一天：过敏原评估

You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.

> 你的火车抵达了最后一站，这里是最接近度假岛屿而又不会弄湿鞋子的地方了。这里甚至都没有船，但现在没有任何东西可以阻止你的步伐了：你建造了一个木筏。你只需要为你的旅程准备几天的食物就可以了。

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you **do** understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.

> 你不会说当地语言，因此看不懂食品上的成分清单。但是过敏原却是以你看得懂的语言列出的。你应该能够使用这些信息来确定哪种成分包含哪种过敏原，并确定在旅途中可以安全携带哪些食物。

You start by compiling a list of foods ([your puzzle input](day21.txt)), one food per line. Each line includes that food's **ingredients list** followed by some or all of the allergens the food contains.

> 你开始编制一份食物清单（[你的谜题输入](day21.txt)），每行一种食物。每行都包含食物的成分清单，然后是包含的部分或全部过敏原。

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. **Allergens aren't always marked**; when they're listed (as in `(contains nuts, shellfish)` after an ingredients list), the ingredient that contains each listed allergen will be **somewhere in the corresponding ingredients list**. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

> 每种过敏原最多存在于一种成分中，每种成分最多包含一种过敏原，过敏原并不总是被标出的，当它们被列出时（如成分表后的 `（包含坚果，贝类）`），列出过敏原的成分将在成分表中的某个对应的位置。但是，即使未列出过敏原，仍可能存在包含过敏原的成分：也许他们忘记给标记它，或者以你不知道的语言标记它。

For example, consider the following list of foods:

> 举个例子，假设有以下食物列表：

```'
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
```

The first food in the list has four ingredients (written in a language you don't understand): `mxmxvkd`, `kfcds`, `sqjhc`, and `nhms`. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: `dairy` and `fish`.

> 列表中的第一种食物有四种成分（使用你不懂的语言书写）：`mxmxvkd`，`kfcds`，`sqjhc` 和 `nhms`。虽然食物中可能含有其他过敏原，但食物中肯定含有的一些过敏原列在后面：`乳制品`和`鱼`。

The first step is to determine which ingredients **can't possibly** contain any of the allergens in any food in your list. In the above example, none of the ingredients `kfcds`, `nhms`, `sbzzf`, or `trh` can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces **`5`**: they all appear once each except `sbzzf`, which appears twice.

> 第一步是确定你的列表中的食物哪些成分不可能包含过敏原。在上面的例子中，成分 `kfcds`， `nhms`，`sbzzf` 或 `trh` 均不能包含过敏原。计算这些成分中的任何一种出现在其他成分列表中的次数得到 **`5`**：除 `sbzzf`（出现两次）外，它们全部都只出现了一次。

Determine which ingredients cannot possibly contain any of the allergens in your list. **How many times do any of those ingredients appear?**

> 确定列表中哪些成分不可能包含任何过敏原。这些成分出现了多少次？

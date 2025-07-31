# Day 22: Monkey Market
> # 第二十二天：猴子市场

As you're all teleported deep into the jungle, a [monkey](https://adventofcode.com/2022/day/11) steals The Historians' device! You'll need to get it back while The Historians are looking for the Chief.
> 你们被传送到丛林深处时，一只[猴子](https://adventofcode.com/2022/day/11)偷走了历史学家的设备！在历史学家们寻找首席的同时，你得把它夺回来。

The monkey that stole the device seems willing to trade it, but only in exchange for an absurd number of bananas. Your only option is to buy bananas on the Monkey Exchange Market.
> 偷设备的猴子似乎愿意交易，但只肯用天文数字的香蕉交换。你唯一的办法是在猴子交易市场上买香蕉。

You aren't sure how the Monkey Exchange Market works, but one of The Historians senses trouble and comes over to help. Apparently, they've been studying these monkeys for a while and have deciphered their secrets.
> 你不太清楚猴子交易市场的规则，但一位历史学家察觉到麻烦，过来帮忙。原来他研究这些猴子很久，已经破解了它们的秘密。

Today, the Market is full of monkeys buying **good hiding spots**. Fortunately, because of the time you recently spent in this jungle, you know lots of good hiding spots you can sell! If you sell enough hiding spots, you should be able to get enough bananas to buy the device back.
> 今天，市场上满是猴子在买**好藏身处**。幸运的是，你最近在这片丛林待过，知道很多好藏身处可以卖！只要卖得够多，你就能换回设备所需的香蕉。

On the Market, the buyers seem to use random prices, but their prices are actually only [pseudorandom](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)! If you know the secret of how they pick their prices, you can wait for the perfect time to sell.
> 市场上的买家看似用随机价格，但其实只是[伪随机](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)！如果你知道他们定价的秘密，就能等到最佳时机出售。

The part about secrets is literal, the Historian explains. Each buyer produces a pseudorandom sequence of secret numbers where each secret is derived from the previous.
> 历史学家解释说，“秘密”是真的。每个买家会生成一串伪随机的秘密数字，每个秘密都由上一个推导而来。

In particular, each buyer's **secret** number evolves into the next secret number in the sequence via the following process:
> 具体来说，每个买家的**秘密**数字通过如下过程演化为下一个秘密数字：

- Calculate the result of **multiplying the secret number by `64`**. Then, **mix** this result into the secret number. Finally, **prune** the secret number.
- Calculate the result of **dividing the secret number by `32`**. Round the result down to the nearest integer. Then, **mix** this result into the secret number. Finally, **prune** the secret number.
- Calculate the result of **multiplying the secret number by `2048`**. Then, **mix** this result into the secret number. Finally, **prune** the secret number.
> - 先用秘密数字乘以`64`，然后**混合**这个结果到秘密数字，再**修剪**秘密数字。
> - 用秘密数字除以`32`，向下取整，然后**混合**这个结果到秘密数字，再**修剪**秘密数字。
> - 用秘密数字乘以`2048`，然后**混合**这个结果到秘密数字，再**修剪**秘密数字。

Each step of the above process involves **mixing** and **pruning**:
> 上述每一步都涉及**混合**和**修剪**：

- To **mix** a value into the secret number, calculate the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is `42` and you were to **mix** `15` into the secret number, the secret number would become `37`.)
- To **prune** the secret number, calculate the value of the secret number [modulo](https://en.wikipedia.org/wiki/Modulo) `16777216`. Then, the secret number becomes the result of that operation. (If the secret number is `100000000` and you were to **prune** the secret number, the secret number would become `16113920`.)
> - **混合**：将给定值与秘密数字做[位异或](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)，结果作为新的秘密数字。（如秘密数字为`42`，混合`15`后变为`37`。）
> - **修剪**：将秘密数字对`16777216`取模，结果作为新的秘密数字。（如秘密数字为`100000000`，修剪后变为`16113920`。）

After this process completes, the buyer is left with the next secret number in the sequence. The buyer can repeat this process as many times as necessary to produce more secret numbers.
> 完成上述过程后，买家得到序列中的下一个秘密数字。买家可以反复执行此过程，生成更多秘密数字。

So, if a buyer had a secret number of `123`, that buyer's next ten secret numbers would be:
> 例如，某买家的秘密数字为`123`，其后十个秘密数字为：

```
15887950
16495136
527345
704524
1553684
12683156
11100544
12249484
7753432
5908254
```

Each buyer uses their own secret number when choosing their price, so it's important to be able to predict the sequence of secret numbers for each buyer. Fortunately, the Historian's research has uncovered the **initial secret number of each buyer** (your puzzle input). For example:
> 每个买家用自己的秘密数字定价，所以预测每个买家的秘密数字序列很重要。幸运的是，历史学家的研究已经找到了每个买家的**初始秘密数字**（你的谜题输入）。例如：

```
1
10
100
2024
```

This list describes the **initial secret number** of four different secret-hiding-spot-buyers on the Monkey Exchange Market. If you can simulate secret numbers from each buyer, you'll be able to predict all of their future prices.
> 这份列表描述了猴子交易市场上四个不同藏身处买家的**初始秘密数字**。如果你能模拟每个买家的秘密数字，就能预测他们所有未来的价格。

In a single day, buyers each have time to generate `2000` **new** secret numbers. In this example, for each buyer, their initial secret number and the 2000th new secret number they would generate are:
> 每天，每个买家有时间生成`2000`个**新**秘密数字。本例中，每个买家的初始秘密数字和第2000个新秘密数字如下：

```
1: 8685429
10: 4700978
100: 15273692
2024: 8667524
```

Adding up the 2000th new secret number for each buyer produces **`37327623`**.
> 把每个买家的第2000个新秘密数字加起来，得到 **`37327623`**。

For each buyer, simulate the creation of 2000 new secret numbers. **What is the sum of the 2000th secret number generated by each buyer?**
> 对每个买家，模拟生成2000个新秘密数字。**每个买家第2000个秘密数字之和是多少？**

Your puzzle answer was `14691757043`.

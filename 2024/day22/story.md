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

## Part Two

Of course, the secret numbers aren't the prices each buyer is offering! That would be ridiculous. Instead, the **prices** the buyer offers are just the **ones digit** of each of their secret numbers.
> 当然，秘密数字并不是买家真正出的价格！那太荒谬了。实际上，买家给出的**价格**只是他们每个秘密数字的**个位数**。

So, if a buyer starts with a secret number of `123`, that buyer's first ten **prices** would be:
> 所以，如果某买家的初始秘密数字是 `123`，那么该买家的前十个**价格**将是：

```
3 (from 123)
0 (from 15887950)
6 (from 16495136)
5 (etc.)
4
4
6
4
4
2
```

This price is the number of **bananas** that buyer is offering in exchange for your information about a new hiding spot. However, you still don't speak [monkey](https://adventofcode.com/2022/day/21), so you can't negotiate with the buyers directly. The Historian speaks a little, but not enough to negotiate; instead, he can ask another monkey to negotiate on your behalf.
> 这个价格就是买家愿意用来交换你新藏身处信息的香蕉数量。不过，你还是不会说猴语，所以无法直接和买家讨价还价。历史学家会一点点猴语，但还不够谈判；他只能让另一只猴子代你谈判。

Unfortunately, the monkey only knows how to decide when to sell by looking at the **changes** in price. Specifically, the monkey will only look for a specific sequence of **four consecutive changes** in price, then immediately sell when it sees that sequence.
> 不幸的是，这只猴子只会根据价格的**变化**来决定什么时候卖出。具体来说，猴子只会寻找某个特定的连续**四次价格变化**的序列，一旦看到这个序列就会立刻卖出。

So, if a buyer starts with a secret number of `123`, that buyer's first ten secret numbers, prices, and the associated changes would be:
> 比如，如果某个买家的初始秘密数字是 `123`，那么该买家的前十个秘密数字、价格和对应的变化如下：

```
     123: 3 
15887950: 0 (-3)
16495136: 6 (6)
  527345: 5 (-1)
  704524: 4 (-1)
 1553684: 4 (0)
12683156: 6 (2)
11100544: 4 (-2)
12249484: 4 (0)
 7753432: 2 (-2)
```

Note that the first price has no associated change because there was no previous price to compare it with.
> 注意，第一个价格没有对应的变化，因为没有前一个价格可供比较。

In this short example, within just these first few prices, the highest price will be `6`, so it would be nice to give the monkey instructions that would make it sell at that time. The first `6` occurs after only two changes, so there's no way to instruct the monkey to sell then, but the second `6` occurs after the changes `-1,-1,0,2`. So, if you gave the monkey that sequence of changes, it would wait until the first time it sees that sequence and then immediately sell your hiding spot information at the current price, winning you `6` bananas.
> 在这个简短的例子中，仅在前几个价格中，最高价格是`6`，如果能让猴子在那时卖出就好了。第一个`6`只经历了两次变化，因此无法让猴子在那时卖出，但第二个`6`出现在变化序列`-1,-1,0,2`之后。所以，如果你给猴子这个变化序列，它会等到第一次出现该序列时立刻卖出你的藏身处信息，获得`6`根香蕉。

Each buyer only wants to buy one hiding spot, so after the hiding spot is sold, the monkey will move on to the next buyer. If the monkey **never** hears that sequence of price changes from a buyer, the monkey will never sell, and will instead just move on to the next buyer.
> 每个买家只想买一个藏身处，所以一旦卖出后，猴子就会转向下一个买家。如果猴子**从未**在某个买家那里听到该变化序列，它就不会卖出，而是直接转向下一个买家。

Worse, you can only give the monkey **a single sequence** of four price changes to look for. You can't change the sequence between buyers.
> 更糟糕的是，你只能给猴子**一组**四个价格变化的序列让它去寻找，不能针对不同买家更换序列。

You're going to need as many bananas as possible, so you'll need to **determine which sequence** of four price changes will cause the monkey to get you the **most bananas overall**. Each buyer is going to generate `2000` secret numbers after their initial secret number, so, for each buyer, you'll have **`2000` price changes** in which your sequence can occur.
> 你需要尽可能多的香蕉，所以你要**确定哪组四连变动序列**能让猴子帮你获得**最多香蕉总数**。每个买家会在初始秘密数字后生成`2000`个新秘密数字，因此每个买家会有**2000**次价格变化，供你的序列出现。

Suppose the initial secret number of each buyer is:
> 假设每个买家的初始秘密数字如下：

```
1
2
3
2024
```

There are many sequences of four price changes you could tell the monkey, but for these four buyers, the sequence that will get you the most bananas is `-2,1,-1,3`. Using that sequence, the monkey will make the following sales:
> 你可以告诉猴子很多种四连变动序列，但对于这四个买家，能获得最多香蕉的序列是 `-2,1,-1,3`。用这个序列，猴子会在以下时刻卖出：

- For the buyer with an initial secret number of `1`, changes `-2,1,-1,3` first occur when the price is **`7`**.
- For the buyer with initial secret `2`, changes `-2,1,-1,3` first occur when the price is **`7`**.
- For the buyer with initial secret `3`, the change sequence `-2,1,-1,3` **does not occur** in the first 2000 changes.
- For the buyer starting with `2024`, changes `-2,1,-1,3` first occur when the price is **`9`**.
> - 初始秘密数字为`1`的买家，第一次出现`-2,1,-1,3`时价格为**7**。
> - 初始秘密数字为`2`的买家，第一次出现`-2,1,-1,3`时价格为**7**。
> - 初始秘密数字为`3`的买家，前2000次变化中没有出现该序列。
> - 初始秘密数字为`2024`的买家，第一次出现`-2,1,-1,3`时价格为**9**。

So, by asking the monkey to sell the first time each buyer's prices go down `2`, then up `1`, then down `1`, then up `3`, you would get **`23`** (`7 + 7 + 9`) bananas!
> 所以，如果你让猴子在每个买家的价格依次出现“降2、升1、降1、升3”时卖出，你能获得**23**（`7 + 7 + 9`）根香蕉！

Figure out the best sequence to tell the monkey so that by looking for that same sequence of changes in every buyer's future prices, you get the most bananas in total. **What is the most bananas you can get?**
> 找出最优的四连变动序列，让猴子在每个买家未来价格中都寻找同样的序列，这样你能获得最多香蕉。**你最多能获得多少根香蕉？**

Your puzzle answer was `1831`.

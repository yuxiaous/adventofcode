# Day 2: Password Philosophy

> 第二天：密码哲学

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via [toboggan](https://en.wikipedia.org/wiki/Toboggan).

> 你的航班将在几天后从海岸机场出发，从这里到海岸最简单的方法是通过雪橇。

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

> 北极雪橇租赁店的店主今天过得很糟糕。“我们的计算机出了点问题，我们无法登录！” 于是你询问是否可以看一看。

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

> 他们的密码数据库似乎有些损坏：一些雪橇公司官方策略中不被允许的密码被选中并生效了。

To try to debug the problem, they have created a list ([your puzzle input](day02.txt)) of **passwords** (according to the corrupted database) and **the corporate policy when that password was set**.

> 为了尝试调试这个问题，他们创建了一个密码列表（[你谜题输入](day02.txt)）（根据损坏的数据库）以及设置该密码时的公司策略。

For example, suppose you have the following list:

> 举个例子，假设你有如下列表：

```'
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, `1-3 a` means that the password must contain `a` at least `1` time and at most `3` times.

> 每行先给出密码策略，然后给出密码。密码策略指示为了使密码生效，一个给定字母所必须出现的最低次数和最高次数。例如，`1-3 a` 表示密码必须包含 `a` 最少 1 次且最多 3 次。

In the above example, **`2`** passwords are valid. The middle password, `cdefg`, is not; it contains no instances of `b`, but needs at least `1`. The first and third passwords are valid: they contain one `a` or nine `c`, both within the limits of their respective policies.

> 在上面的例子中，其中 **`2`** 个密码是有效的。中间密码 `cdefg` 无效，因为它不包含 `b`，该字母至少需要 `1` 个。第一个和第三个密码是有效的：它们包含一个 `a` 或九个 `c`，两者都满足各自的策略限制。

**How many passwords are valid** according to their policies?

> 根据他们的策略，有多少个密码是有效的？

Your puzzle answer was `434`.

## --- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

> 看来你已经正确地验证了密码，但它们似乎并不是雪橇公司官方认证系统所期望的。

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

> 店主突然意识到，他刚才偶然间提到的密码策略规则是他在街道另一头的小雪橇出租店里的旧工作所使用的！雪橇公司官方策略实际上有一些不同。

Each policy actually describes two **positions in the password**, where `1` means the first character, `2` means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) **Exactly one of these positions** must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

> 每个策略实际上描述了密码中的两个位置，其中 `1` 表示第一个字符，`2` 表示第二个字符，依此类推。（注意，雪橇公司策略中没有“索引为零”的概念！）这些位置的其中一个必须包含给定的字母。其他字母的出现与策略执行目的无关。

Given the same example list from above:

- `1-3 a: abcde` is **valid**: position `1` contains `a` and position `3` does not.
- `1-3 b: cdefg` is **invalid**: neither position `1` nor position `3` contains `b`.
- `2-9 c: ccccccccc` is **invalid**: both position `2` and position `9` contain `c`.

> 给出与上面同样的例子：
>
> - `1-3 a: abcde` 是有效的：位置 `1` 包含 `a` 并且位置 `3` 不包含。
> - `1-3 b: cdefg` 是无效的：位置 `1` 和位置 `3` 都不包含 `b`。
> - `2-9 c: ccccccccc` 是无效的：位置 `2` 和位置 `9` 都包含 `c`。

**How many passwords are valid** according to the new interpretation of the policies?

> 根据新策略的解释，有多少个密码是有效的？

Your puzzle answer was `509`.

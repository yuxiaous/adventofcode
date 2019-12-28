# Day 4: Secure Container

> 第4天：安全容器

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

> 你到达金星燃料仓库后才发现它受到密码的保护。精灵们把密码写在了便签上，但是有人把它丢掉了。

However, they do remember a few key facts about the password:

- It is a six-digit number.
- The value is within the range given in [your puzzle input](day4.txt).
- Two adjacent digits are the same (like `22` in `122345`).
- Going from left to right, the digits **never decrease**; they only ever increase or stay the same (like `111123` or `135679`).

> 但是，他们还对密码有点印象：
>
> - 它是一个六位数的数字。
> - 它的值在[你的谜题输入](day4.txt)所给定的范围内。
> - 它包含相同的相邻数字（例如 `122345` 中的 `22`）。
> - 它的数字从左到右**从不减少**：增加或保持不变（例如 `111123` 或 `135679`）。

Other than the range rule, the following are true:

- `111111` meets these criteria (double `11`, never decreases).
- `223450` does not meet these criteria (decreasing pair of digits `50`).
- `123789` does not meet these criteria (no double).

> 排除掉上面第二条关于给定范围的规则，以下密码也符合规则：
>
> - `111111` 符合这些条件（一对 `11`，没有减少）。
> - `223450` 不符合这些条件（减少的两个数字 `50`）。
> - `123789` 不符合这些条件（没有相同数字）。

**How many different passwords** within the range given in [your puzzle input](day4.txt) meet these criteria?

> 在[你的谜题输入](day4.txt)给出的范围内，**有多少种不同的密码**满足这些规则？

Your puzzle answer was `466`.

## Part Two

An Elf just remembered one more important detail: the two adjacent matching digits **are not part of a larger group of matching digits**.

> 一个精灵突然想起了一个更重要的细节：两个符合规则的相邻数字**不是更大的符合规则数字的一部分**。（[译者注]意思是其中的两位相同数字有且只有两位。）

Given this additional criterion, but still ignoring the range rule, the following are now true:

- `112233` meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
- `123444` no longer meets the criteria (the repeated `44` is part of a larger group of `444`).
- `111122` meets the criteria (even though `1` is repeated more than twice, it still contains a double `22`).

> 给定了这个新增的规则（仍然忽略关于给定范围的规则），现在以下密码符合规则：
>
> - `112233` 满足这些条件，因为数字从不减少并且所有重复的数字正好是两位数。
> - `123444` 不再符合条件（重复的 `44` 是较大的 `444` 中的一部分）。
> - `111122` 符合条件（即使 `1` 重复超过两次，但仍包含一对 `22`）。

**How many different passwords** within the range given in [your puzzle input](day4.txt) meet all of the criteria?

> 在[你的谜题输入](day4.txt)给出的范围内，**有多少种不同的密码**满足所有的规则？

Your puzzle answer was `292`.

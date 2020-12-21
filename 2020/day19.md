# Day 19: Monster Messages

> 第十九天：怪兽信息

You land in an airport surrounded by dense forest. As you walk to your high-speed train, the Elves at the Mythical Information Bureau contact you again. They think their satellite has collected an image of a **sea monster**! Unfortunately, the connection to the satellite is having problems, and many of the messages sent back from the satellite have been corrupted.

> 你降落在一个被茂密森林包围的机场中。当你步行前往高速列车时，神话信息局的精灵们再次联系了你。他们认为他们的卫星收集到了一张海怪的图像！不幸的是，与卫星的连接出现问题，从卫星发送回的很多消息都已损坏。

They sent you a list of **the rules valid messages should obey** and a list of **received messages** they've collected so far ([your puzzle input](day19.txt)).

> 他们向你发送了一份有效消息应遵循的规则列表，以及一份迄今为止收集到的消息的列表（[你的谜题输入](day19.txt)）。

The **rules for valid messages** (the top part of your puzzle input) are numbered and build upon each other. For example:

> 有效消息的规则（谜题输入的上半部分）已编号并相互依赖。例如：

```'
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
```

Some rules, like `3: "b"`, simply match a single character (in this case, `b`).

> 有些规则，例如 `3: "b"`，简单匹配了一个单字符（在这个例子中为 `b`）。

The remaining rules list the sub-rules that must be followed; for example, the rule `0: 1 2` means that to match rule `0`, the text being checked must match rule `1`, and the text after the part that matched rule `1` must then match rule `2`.

> 其余规则列出了必须遵循的子规则。例如，规则 `0: 1 2` 表示匹配规则 `0`，检查的文本必须匹配规则 `1`，匹配规则 `1` 的部分之后的文本必须匹配规则 `2`。

Some of the rules have multiple lists of sub-rules separated by a pipe (`|`). This means that **at least one** list of sub-rules must match. (The ones that match might be different each time the rule is encountered.) For example, the rule `2: 1 3 | 3 1` means that to match rule `2`, the text being checked must match rule `1` followed by rule `3` **or** it must match rule `3` followed by rule `1`.

> 一些规则有多个子规则列表，这些子规则列表由管道（`|`）分隔。这表示必须匹配其中至少一个子规则列表。（每次遇到该规则时，匹配的规则可能会有所不同。）例如，规则 `2：1 3 | 3 1` 表示匹配规则 `2`，文本的检查必须先匹配规则 `1` 然后是规则 `3`，或者先匹配规则 `3` 然后是规则 `1`。

Fortunately, there are no loops in the rules, so the list of possible matches will be finite. Since rule `1` matches `a` and rule `3` matches `b`, rule `2` matches either `ab` or `ba`. Therefore, rule `0` matches `aab` or `aba`.

> 幸运的是，因为规则中没有循环，所以列表中的可能匹配项是有限的。由于规则 `1` 匹配 `a`，规则 `3` 匹配 `b`，因此规则 `2` 匹配 `ab` 或 `ba`，规则 `0` 匹配 `aab` 或 `aba`。

Here's a more interesting example:

> 这里是一些更有趣的例子：

```'
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
```

Here, because rule `4` matches `a` and rule `5` matches `b`, rule `2` matches two letters that are the same (`aa` or `bb`), and rule `3` matches two letters that are different (`ab` or `ba`).

> 这里，因为规则 `4` 匹配 `a`，规则 `5` 匹配 `b`，规则 `2` 匹配两个相同的字母（即 `aa` 或 `bb`），规则 `3` 匹配两个不同的字母（即 `ab` 或 `ba`）。

Since rule `1` matches rules `2` and `3` once each in either order, it must match two pairs of letters, one pair with matching letters and one pair with different letters. This leaves eight possibilities: `aaab`, `aaba`, `bbab`, `bbba`, `abaa`, `abbb`, `baaa`, or `babb`.

> 由于规则 `1` 在每个分隔中各匹配一次规则 `2` 和 `3` ，因此必须匹配两对字母，一对相同字母，一对不同字母。这产生八种可能：`aaab`，`aaba`，`bbab`，`bbba`，`abaa`，`abbb`，`baaa` 或 `babb`。

Rule `0`, therefore, matches `a` (rule `4`), then any of the eight options from rule `1`, then `b` (rule `5`): `aaaabb`, `aaabab`, `abbabb`, `abbbab`, `aabaab`, `aabbbb`, `abaaab`, or `ababbb`.

> 因此，规则 `0` 匹配 `a`（规则 `4`），然后匹配规则 `1` 中八个选项的任意一个，然后匹配 `b`（规则 `5`）：`aaaabb`，`aaabab`，`abbabb`，`abbbab`，`aabaab`，`aabbbb`，`abaaab` 或 `ababbb`。

The **received messages** (the bottom part of your puzzle input) need to be checked against the rules so you can determine which are valid and which are corrupted. Including the rules and the messages together, this might look like:

> 需要根据规则检查收到的消息（谜题输入的下半部分），以便你可以确定哪些是有效的和哪些是损坏的。将规则和消息合在一起，看起来像这样：

```'
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
```

Your goal is to determine **the number of messages that completely match rule `0`**. In the above example, `ababbb` and `abbbab` match, but `bababa`, `aaabbb`, and `aaaabbb` do not, producing the answer **`2`**. The whole message must match all of rule `0`; there can't be extra unmatched characters in the message. (For example, `aaaabbb` might appear to match rule `0` above, but it has an extra unmatched `b` on the end.)

> 你的目标是确定完全匹配规则 `0` 的消息数量。在上面的例子中，`ababbb` 和 `abbbab` 是匹配的，但是 `bababa`，`aaabbb` 和 `aaaabbb` 是不匹配的，所以答案是 **`2`**。消息必须与规则 `0` 完整匹配，消息中不能出现多余的不匹配字符。（例如，`aaaabbb` 可能看起来与上面的规则 `0` 挺匹配的，但最后有多出了一个不匹配的字母 `b`。）

**How many messages completely match rule `0`?**

> 有多少消息完全符合规则 `0`？

Your puzzle answer was `134`.

## --- Part Two ---

As you look over the list of messages, you realize your matching rules aren't quite right. To fix them, completely replace rules `8: 42` and `11: 42 31` with the following:

> 当你查阅消息列表后，你意识到你的匹配规则不太准确。要解决这些问题，需要完全替换规则 `8: 42` 和 `11: 42 31` 为以下内容：

```'
8: 42 | 42 8
11: 42 31 | 42 11 31
```

This small change has a big impact: now, the rules **do** contain loops, and the list of messages they could hypothetically match is infinite. You'll need to determine how these changes affect which messages are valid.

> 这个小变化产生了很大的影响：现在，规则包含循环了，并且假设可以匹配的消息列表是无限的。你需要确定这些变化如何影响有效的消息。

Fortunately, many of the rules are unaffected by this change; it might help to start by looking at which rules always match the same set of values and how **those** rules (especially rules `42` and `31`) are used by the new versions of rules `8` and `11`.

> 幸运的是，大部分规则不受这个变化的影响。这或许对你有所帮助：首先查看哪些规则始终匹配相同的值的集合，以及它们（尤其是规则 `42` 和 `31`）如何被新版本的规则 `8` 和 `11` 所使用的。

(Remember, **you only need to handle the rules you have**; building a solution that could handle any hypothetical combination of rules would be [significantly more difficult](https://en.wikipedia.org/wiki/Formal_grammar).)

> （记住，你只需要处理你所拥有的规则，构建出包含所有假设规则组合的解决方案[显然太难了](https://en.wikipedia.org/wiki/Formal_grammar)。）

For example:

```'
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
```

Without updating rules `8` and `11`, these rules only match three messages: `bbabbbbaabaabba`, `ababaaaaaabaaab`, and `ababaaaaabbbaba`.

> 在不更新规则 `8` 和 `11` 的情况下，这些规则只匹配三条消息：`bbabbbbaabaabba`，`ababaaaaaabaaab` 和 `ababaaaaabbbaba`。

However, after updating rules `8` and `11`, a total of **`12`** messages match:

但是在更新规则 `8` 和 `11` 之后，总共可以匹配 **`12`** 条消息：

- `bbabbbbaabaabba`
- `babbbbaabbbbbabbbbbbaabaaabaaa`
- `aaabbbbbbaaaabaababaabababbabaaabbababababaaa`
- `bbbbbbbaaaabbbbaaabbabaaa`
- `bbbababbbbaaaaaaaabbababaaababaabab`
- `ababaaaaaabaaab`
- `ababaaaaabbbaba`
- `baabbaaaabbaaaababbaababb`
- `abbbbabbbbaaaababbbbbbaaaababb`
- `aaaaabbaabaaaaababaa`
- `aaaabbaabbaaaaaaabbbabbbaaabbaabaaa`
- `aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba`

**After updating rules `8` and `11`, how many messages completely match rule `0`?**

在更新规则 `8` 和 `11` 后，有多少消息完全符合规则 `0`？

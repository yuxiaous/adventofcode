# Day 4: Passport Processing

> 第四天：处理护照

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

> 当你到达机场后才意识到你带着的证件是北极证书而不是护照。尽管这些文件都极为相仿，但北极证书不是由一个国家发行的，因此它实际上并不是一份可以用于在世界上大部分地区旅行的有效文件。

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

> 不过，看来你并不是唯一一个遇到问题的人。自动护照扫描仪前排了很长的队伍，这种耽搁很可能会打乱你的旅行行程。

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

> 由于存在一些网络安全漏洞，你意识到你可能可以同时解决这两个问题。

The automatic passport scanners are slow because they're having trouble **detecting which passports have all required fields**. The expected fields are as follows:

> 自动护照扫描仪很慢，因为它们在检测哪些护照具有所有必填字段时遇到问题。预期字段如下：

- `byr` (Birth Year)
- `iyr` (Issue Year)
- `eyr` (Expiration Year)
- `hgt` (Height)
- `hcl` (Hair Color)
- `ecl` (Eye Color)
- `pid` (Passport ID)
- `cid` (Country ID)

Passport data is validated in batch files ([your puzzle input](day04.txt)). Each passport is represented as a sequence of `key:value` pairs separated by spaces or newlines. Passports are separated by blank lines.

> 护照数据在批处理文件（[你的谜题输入](day04.txt)）中进行验证。每本护照都表示为一系列用空格或换行符分隔的键值对。护照之间用空行分隔。

Here is an example batch file containing four passports:

> 这是一个例子，批处理文件包含四本护照数据：

```'
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
```

The first passport is **valid** - all eight fields are present. The second passport is **invalid** - it is missing `hgt` (the Height field).

> 第一本护照是有效的（所有的八个字段都存在）。第二本护照是无效的（缺少 `hgt` 身高字段）。

The third passport is interesting; the **only missing field** is `cid`, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing `cid` fields. Treat this "passport" as **valid**.

> 第三本护照很有趣，唯一缺少的字段是 `cid`，因此它看起来很像是来自北极证书的数据，而不是护照！当然，如果你让系统暂时忽略缺少的 `cid` 字段，没有人会注意到这点。此时“护照”将视为有效。

The fourth passport is missing two fields, `cid` and `byr`. Missing `cid` is fine, but missing any other field is not, so this passport is **invalid**.

> 第四本护照缺少了两个字段，即 `cid` 和 `byr`。 缺少 `cid` 是可以的，但是缺少任何其他字段是不行的，因此这本护照是无效的。

According to the above rules, your improved system would report **`2`** valid passports.

> 根据上述规则，经你改造后的系统将报告 `2` 本有效护照。

Count the number of **valid** passports - those that have all required fields. Treat `cid` as optional. **In your batch file, how many passports are valid?**

> 统计有效护照（具有所有必填字段的护照）的数量。将 `cid` 视为可选项。在你的批处理文件中，有多少本护照有效？

Your puzzle answer was `242`.

## --- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

> 现在，这列队伍的移动速度快了很多，但是你偷听到机场安保人员在谈论带有无效数据的护照是如何通过的。最好尽快添加一些数据验证！

You can continue to ignore the `cid` field, but each other field has strict rules about what values are valid for automatic validation:

> 你可以继续忽略 `cid` 字段，但是其他字段都具有严格的规则——关于什么值对自动验证是有效的：

- `byr` (Birth Year) - four digits; at least `1920` and at most `2002`.
- `iyr` (Issue Year) - four digits; at least `2010` and at most `2020`.
- `eyr` (Expiration Year) - four digits; at least `2020` and at most `2030`.
- `hgt` (Height) - a number followed by either `cm` or `in`:
  - If `cm`, the number must be at least `150` and at most `193`.
  - If `in`, the number must be at least `59` and at most `76`.
- `hcl` (Hair Color) - a `#` followed by exactly six characters `0`-`9` or `a`-`f`.
- `ecl` (Eye Color) - exactly one of: `amb` `blu` `brn` `gry` `grn` `hzl` `oth`.
- `pid` (Passport ID) - a nine-digit number, including leading zeroes.
- `cid` (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both **present** and **valid** according to the above rules. Here are some example values:

> 你的工作是根据上述规则统计所有必填字段都存在且有效的护照。以下是一些值的例子：

```'
byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
```

Here are some invalid passports:

> 以下是一些无效的护照：

```'
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
```

Here are some valid passports:

> 以下是一些有效的护照：

```'
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
```

Count the number of **valid** passports - those that have all required fields and valid values. Continue to treat `cid` as optional. **In your batch file, how many passports are valid?**

> 统计有效护照（具有所有必填字段且值有效的护照）的数量。将 `cid` 视为可选项。在你的批处理文件中，有多少本护照有效？

Your puzzle answer was `186`.

# [Day 16: Packet Decoder](https://adventofcode.com/2021/day/16)

> 第16天：包解码器

As you leave the cave and reach open waters, you receive a transmission from the Elves back on the ship.

> 当你离开洞穴并到达开阔水域时，你收到来自船上的精灵发来的传输内容。

The transmission was sent using the Buoyancy Interchange Transmission System (BITS), a method of packing numeric expressions into a binary sequence. Your submarine's computer has saved the transmission in [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) ([your puzzle input](day16.txt)).

> 传输是使用浮动交换传输系统 (BITS) 进行的，这是一种将数值表达式打包成二进制序列的方法。你的潜水艇计算机已经将传输的内容保存为了[十六进制](https://en.wikipedia.org/wiki/Hexadecimal)（[你的谜题输入](day16.txt)）。

The first step of decoding the message is to convert the hexadecimal representation into binary. Each character of hexadecimal corresponds to four bits of binary data:

> 解码消息的第一步是将十六进制转换为二进制。每一个十六进制字符对应四位二进制数据：

```'
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111
```

The BITS transmission contains a single **packet** at its outermost layer which itself contains many other packets. The hexadecimal representation of this packet might encode a few extra `0` bits at the end; these are not part of the transmission and should be ignored.

> BITS 传输在其最外层只包含单个**数据包**，该数据包内包含许多其他数据包。这个数据包的十六进制数据可能会为了对齐，在末尾编码一些额外的 `0` 位，这些不是传输内容的一部分，应该被忽略。

Every packet begins with a standard header: the first three bits encode the packet **version**, and the next three bits encode the packet **type ID**. These two values are numbers; all numbers encoded in any packet are represented as binary with the most significant bit first. For example, a version encoded as the binary sequence `100` represents the number `4`.

> 每个数据包都开始于一个标准头：前三位编码了数据包的**版本**，接下来的三位编码了数据包的**类型 ID**。这两个值是数字，所有数据包中编码的数字都是以二进制的格式表示的，有效位在前。例如，使用二进制序列 `100` 进行编码的版本号，实际表示为数字 `4`。

Packets with type ID `4` represent a **literal value**. Literal value packets encode a single binary number. To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits, and then it is broken into groups of four bits. Each group is prefixed by a `1` bit except the last group, which is prefixed by a `0` bit. These groups of five bits immediately follow the packet header. For example, the hexadecimal string `D2FE28` becomes:

> 类型 ID 为 `4` 的数据包表示一个**字面值**。字面值数据包编码了一个二进制的数字。如何实现呢？在二进制的数字前填充零，直到长度达到四的倍数，然后将其按照每四位一组进行分组。除了最后一组添加一位前缀 `0`，其余每组添加一位前缀 `1`。这些五位一组的数据紧跟在数据包头后面。例如，十六进制字串 `D2FE28` 变为二进制：

```'
110100101111111000101000
VVVTTTAAAAABBBBBCCCCC
```

Below each bit is a label indicating its purpose:

> 每个位下面都有一个标签，用来表明位的用途：

- The three bits labeled `V` (`110`) are the packet version, `6`.
- The three bits labeled `T` (`100`) are the packet type ID, `4`, which means the packet is a literal value.
- The five bits labeled `A` (`10111`) start with a `1` (not the last group, keep reading) and contain the first four bits of the number, `0111`.
- The five bits labeled `B` (`11110`) start with a `1` (not the last group, keep reading) and contain four more bits of the number, `1110`.
- The five bits labeled `C` (`00101`) start with a `0` (last group, end of packet) and contain the last four bits of the number, `0101`.
- The three unlabeled `0` bits at the end are extra due to the hexadecimal representation and should be ignored.

> - 标记为 `V` 的三位（`110`）是数据包的版本：`6`。
> - 标记为 `T` 的三位（`100`）是数据包类型 ID：`4`，表示这个数据包是一个字面值。
> - 标记为 `A` 的五位（`10111`）以 `1` 开头（不是最后一组，继续读取）并且包含数字的前四位：`0111`。
> - 标记为 `B` 的五位（`11110`）以 `1` 开头（不是最后一组，继续读取）并且包含另外四位数字：`1110`。
> - 标记为 `C` 的五位（`00101`）以 `0` 开头（最后一组，数据包的结尾）并且包含数字的最后四位：`0101`。
> - 由于需要十六进制对齐，末尾未标记的三个 `0` 位是附加的，应该被忽略。

So, this packet represents a literal value with binary representation `011111100101`, which is `2021` in decimal.

> 因此，这个数据包表示一个二进制的字面值 `011111100101`，即十进制的 `2021`。

Every other type of packet (any packet with a type ID other than `4`) represent an **operator** that performs some calculation on one or more sub-packets contained within. Right now, the specific operations aren't important; focus on parsing the hierarchy of sub-packets.

> 每一种其他类型的数据包（其他类型 ID 不是 `4` 的数据包）都代表一种**操作符**，它对包含在其中的一个或多个子数据包执行一些计算。现在，具体的操作并不重要，重点在于解析子数据包的层次结构。

An operator packet contains one or more packets. To indicate which subsequent binary data represents its sub-packets, an operator packet can use one of two modes indicated by the bit immediately after the packet header; this is called the **length type ID**:

> 一个操作符数据包包含一个或多个数据包。操作符数据包有两种模式，使用紧接在数据包头之后的位来判断，称为**长度类型 ID**，指明哪些后续的二进制数据是子数据包：

- If the length type ID is `0`, then the next **15** bits are a number that represents the **total length in bits** of the sub-packets contained by this packet.
- If the length type ID is `1`, then the next **11** bits are a number that represents the **number of sub-packets immediately contained** by this packet.

> - 如果长度类型 ID 为 `0`，那么接下来的 **15** 位是一个数字，表示当前数据包包含的子数据包的**总长度**（以位为单位）。
> - 如果长度类型 ID 为 `1`，那么接下来的 **11** 位是一个数字，表示当前数据包包含的**子数据包数量**。

Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.

> 最后，在长度类型 ID 位和 15 位或 11 位的字段之后，子数据包紧跟其后。

For example, here is an operator packet (hexadecimal string `38006F45291200`) with length type ID `0` that contains two sub-packets:

> 例如，这是一个操作符数据包（十六进制字串 `38006F45291200`），长度类型 ID 为 `0`，包含两个子数据包：

```'
00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
```

- The three bits labeled `V` (`001`) are the packet version, `1`.
- The three bits labeled `T` (`110`) are the packet type ID, `6`, which means the packet is an operator.
- The bit labeled `I` (`0`) is the length type ID, which indicates that the length is a 15-bit number representing the number of bits in the sub-packets.
- The 15 bits labeled `L` (`000000000011011`) contain the length of the sub-packets in bits, `27`.
- The 11 bits labeled `A` contain the first sub-packet, a literal value representing the number `10`.
- The 16 bits labeled `B` contain the second sub-packet, a literal value representing the number `20`.

> - 标记为 `V` 的三位（`001`）是数据包的版本：`1`。
> - 标记为 `T` 的三位（`110`）是数据包的类型 ID：`6`，表示这个数据包是一个运算符。
> - 标记为 `I` 的位（`0`）是长度类型 ID，表示这个数字的长度为 15 位，这个数字的值表示子数据包中的位的数量。
> - 标记为 `L` 的 15 位（`000000000011011`）包含子数据包的长度（以位为单位）：`27`。
> - 标记为 `A` 的 11 位包含第一个子数据包，一个表示数字 `10` 的字面值。
> - 标记为 `B` 的 16 位包含第二个子数据包，一个表示数字 `20` 的字面值。

After reading 11 and 16 bits of sub-packet data, the total length indicated in `L` (27) is reached, and so parsing of this packet stops.

> 读取 11 位以及 16 位子包数据后，达到 `L` 中表示的总长度（27），所以停止该数据包的解析。

As another example, here is an operator packet (hexadecimal string `EE00D40C823060`) with length type ID `1` that contains three sub-packets:

> 这是另一个例子，这里是一个操作符数据包（十六进制字串`EE00D40C823060`），长度类型 ID 为 `1`，包含三个子数据包：

```'
11101110000000001101010000001100100000100011000001100000
VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC
```

- The three bits labeled `V` (`111`) are the packet version, `7`.
- The three bits labeled `T` (`011`) are the packet type ID, `3`, which means the packet is an operator.
- The bit labeled `I` (`1`) is the length type ID, which indicates that the length is a 11-bit number representing the number of sub-packets.
- The 11 bits labeled `L` (`00000000011`) contain the number of sub-packets, `3`.
- The 11 bits labeled `A` contain the first sub-packet, a literal value representing the number `1`.
- The 11 bits labeled `B` contain the second sub-packet, a literal value representing the number `2`.
- The 11 bits labeled `C` contain the third sub-packet, a literal value representing the number `3`.

> - 标记为 `V` 的三位（`111`）是数据包的版本：`7`。
> - 标记为 `T` 的三位（`011`）是数据包的类型 ID：`3`，表示这个数据包是一个运算符。
> - 标记为 `I` 的位（`1`）是长度类型 ID，表示这个数字的长度为 11 位，这个数字的值表示子数据包的数量。
> - 标记为 `L` 的 11 位（`00000000011`）包含子数据包的数量：`3`。
> - 标记为 `A` 的 11 位包含第一个子数据包，一个表示数字 `1` 的字面值。
> - 标记为 `B` 的 11 位包含第二个子数据包，一个表示数字 `2` 的字面值。
> - 标记为 `C` 的 11 位包含第三个子数据包，一个表示数字 `3` 的字面值。

After reading 3 complete sub-packets, the number of sub-packets indicated in `L` (3) is reached, and so parsing of this packet stops.

> 读取完 3 个完整的子数据包后，达到 `L` 中表示的子数据包个数（3），所以停止该数据包的解析。

For now, parse the hierarchy of the packets throughout the transmission and **add up all of the version numbers**.

> 现在，在传输过程中解析数据包的层次结构并**将所有版本号相加**。

Here are a few more examples of hexadecimal-encoded transmissions:

> 以下是更多十六进制编码传输的例子：

- `8A004A801A8002F478` represents an operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6); this packet has a version sum of **`16`**.
- `620080001611562C8802118E34` represents an operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values. This packet has a version sum of **`12`**.
- `C0015000016115A2E0802F182340` has the same structure as the previous example, but the outermost packet uses a different length type ID. This packet has a version sum of **`23`**.
- `A0016C880162017C3686B18A3D4780` is an operator packet that contains an operator packet that contains an operator packet that contains five literal values; it has a version sum of **`31`**.

> - `8A004A801A8002F478` 表示一个操作符数据包（版本 4），其中包含一个操作符数据包（版本 1），其中包含一个操作符数据包（版本 5），其中包含一个字面值（版本 6）。这个数据包的版本总和为 **`16`**。
> - `620080001611562C8802118E34` 表示一个操作符数据包（版本 3），其中包含两个子数据包的，每个子数据包都是一个操作符数据包，分别包含两个字面值。这个数据包的版本总和为 **`12`**。
> - `C0015000016115A2E0802F182340` 与前面两个例子的结构相同，但最外层的数据包使用了不同的长度类型 ID。这个数据包的版本总和为 **`23`**。
> - `A0016C880162017C3686B18A3D4780` 是一个操作符数据包，其中包含一个操作符数据包，其中包含一个操作符数据包，其中包含五个字面值。它的版本总和为 **`31`**。

Decode the structure of your hexadecimal-encoded BITS transmission; **what do you get if you add up the version numbers in all packets?**

> 解码十六进制编码的 BITS 传输结构，**如果将所有数据包中的版本号相加，会得到什么？**

Your puzzle answer was `999`.

## --- Part Two ---

Now that you have the structure of your transmission decoded, you can calculate the value of the expression it represents.

> 现在你已经解码了传输的结构，你可以计算出它的表达式的值了。

Literal values (type ID `4`) represent a single number as described above. The remaining type IDs are more interesting:

> 字面值（类型 ID 为 `4`）表示单个数字，上面以及描述过了。其余的类型 ID 更加有趣：

- Packets with type ID `0` are **sum** packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
- Packets with type ID `1` are **product** packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
- Packets with type ID `2` are **minimum** packets - their value is the minimum of the values of their sub-packets.
- Packets with type ID `3` are **maximum** packets - their value is the maximum of the values of their sub-packets.
- Packets with type ID `5` are **greater than** packets - their value is **1** if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is **0**. These packets always have exactly two sub-packets.
- Packets with type ID `6` are **less than** packets - their value is **1** if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is **0**. These packets always have exactly two sub-packets.
- Packets with type ID `7` are **equal to** packets - their value is **1** if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is **0**. These packets always have exactly two sub-packets.

- 类型 ID 为 `0` 的数据包是**和**数据包 -- 它的值是其子数据包的值的总和。如果只有一个子数据包，它的值就是子数据包的值。
- 类型 ID 为 `1` 的数据包是**积**数据包 -- 它的值是其子数据包的值的乘积。如果只有一个子数据包，它的值就是子数据包的值。
- 类型 ID 为 `2` 的数据包是**最小值**数据包 -- 它的值是其所有子数据包的值的最小值。
- 类型 ID 为 `3` 的数据包是**最大值**数据包 -- 它的值是其所有子数据包的值的最大值。
- 类型 ID 为 `5` 的数据包是**大于**数据包 -- 如果第一个子数据包的值大于第二个子数据包的值，则它的值为 **1**，否则为 **0**。这些数据包都只有两个子数据包。
- 类型 ID 为 `6` 的数据包是**小于**数据包 -- 如果第一个子数据包的值小于第二个子数据包的值，则它的值为 **1**，否则为 **0**。这些数据包都只有两个子数据包。
- 类型 ID 为 `7` 的数据包是**等于**数据包 -- 如果第一个子数据包的值等于第二个子数据包的值，则它的值为 **1**，否则为 **0**。这些数据包都只有两个子数据包。

Using these rules, you can now work out the value of the outermost packet in your BITS transmission.

> 使用这些规则，现在你可以计算出 BITS 传输中最外层数据包的值了。

For example:

> 举个例子：

- `C200B40A82` finds the sum of `1` and `2`, resulting in the value **`3`**.
- `04005AC33890` finds the product of `6` and `9`, resulting in the value **`54`**.
- `880086C3E88112` finds the minimum of `7`, `8`, and `9`, resulting in the value **`7`**.
- `CE00C43D881120` finds the maximum of `7`, `8`, and `9`, resulting in the value **`9`**.
- `D8005AC2A8F0` produces `1`, because `5` is less than `15`.
- `F600BC2D8F` produces `0`, because `5` is not greater than `15`.
- `9C005AC2F8F0` produces `0`, because `5` is not equal to `15`.
- `9C0141080250320F1802104A08` produces `1`, because `1` + `3` = `2` * `2`.

> - `C200B40A82` 求 `1` 和 `2` 的和，得到的值为 **`3`**。
> - `04005AC33890` 求 `6` 和 `9` 的积，得到的值为 **`54`**。
> - `880086C3E88112` 求 `7`、`8` 和 `9` 的最小值，得到的值为 **`7`**。
> - `CE00C43D881120` 求 `7`、`8` 和 `9` 的最大值，得到的值为 **`9`**。
> - `D8005AC2A8F0` 得到 `1`，因为 `5` 小于 `15`。
> - `F600BC2D8F` 得到 `0`，因为 `5` 不大于 `15`。
> - `9C005AC2F8F0` 得到 `0`，因为 `5` 不等于 `15`。
> - `9C0141080250320F1802104A08` 得到 `1`，因为 `1` + `3` = `2` * `2`。

**What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?**

> **分析由十六进制编码的 BITS 传输表示的表达式，会得到什么？**

Your puzzle answer was `3408662834145`.

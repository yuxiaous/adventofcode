# Day 24: Crossed Wires
> # 第二十四天：交叉电线

You and The Historians arrive at the edge of a [large grove](https://adventofcode.com/2022/day/23) somewhere in the jungle. After the last incident, the Elves installed a small device that monitors the fruit. While The Historians search the grove, one of them asks if you can take a look at the monitoring device; apparently, it's been malfunctioning recently.
> 你和历史学家们来到丛林中某处的一片[大果园](https://adventofcode.com/2022/day/23)边缘。上次事件后，精灵们安装了一个小装置来监控水果。当历史学家们在果园里搜寻时，其中一人问你能否帮忙看看监控装置；显然它最近一直出故障。

The device seems to be trying to produce a number through some boolean logic gates. Each gate has two inputs and one output. The gates all operate on values that are either **true** (`1`) or **false** (`0`).
> 这个装置似乎试图通过一些布尔逻辑门来产生一个数字。每个逻辑门有两个输入和一个输出。所有逻辑门的输入值都是**真**（`1`）或**假**（`0`）。

- `AND` gates output `1` if **both** inputs are `1`; if either input is `0`, these gates output `0`.
- `OR` gates output `1` if **one or both** inputs is `1`; if both inputs are `0`, these gates output `0`.
- `XOR` gates output `1` if the inputs are **different**; if the inputs are the same, these gates output `0`.
> - `AND`门：只有**两个输入都是`1`**时输出`1`；只要有一个输入为`0`，输出就是`0`。
> - `OR`门：**任一或两个输入为`1`**时输出`1`；两个输入都是`0`时输出`0`。
> - `XOR`门：**两个输入不同**时输出`1`；输入相同时输出`0`。

Gates wait until both inputs are received before producing output; wires can carry `0`, `1` or no value at all. There are no loops; once a gate has determined its output, the output will not change until the whole system is reset. Each wire is connected to at most one gate output, but can be connected to many gate inputs.
> 逻辑门会等到两个输入都到达后才产生输出；电线可以传递`0`、`1`或没有值。系统中没有回路；一旦某个门确定了输出，输出就不会再变，直到整个系统重置。每根电线最多只连接到一个门的输出，但可以连接到多个门的输入。

Rather than risk getting shocked while tinkering with the live system, you write down all of the gate connections and initial wire values (your puzzle input) so you can consider them in relative safety. For example:
> 为了避免在操作带电系统时被电到，你把所有门的连接和初始电线值都记了下来（你的谜题输入），这样可以更安全地分析。例如：

```
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
```

Because gates wait for input, some wires need to start with a value (as inputs to the entire system). The first section specifies these values. For example, `x00: 1` means that the wire named `x00` starts with the value `1` (as if a gate is already outputting that value onto that wire).
> 因为逻辑门要等输入，所以有些电线需要有初始值（作为整个系统的输入）。第一部分指定了这些值。例如，`x00: 1`表示名为`x00`的电线初始值为`1`（就好像有个门已经把这个值输出到这根电线上）。

The second section lists all of the gates and the wires connected to them. For example, `x00 AND y00 -> z00` describes an instance of an `AND` gate which has wires `x00` and `y00` connected to its inputs and which will write its output to wire `z00`.
> 第二部分列出了所有逻辑门及其连接的电线。例如，`x00 AND y00 -> z00`描述了一个`AND`门，它的输入是`x00`和`y00`，输出写到`z00`。

In this example, simulating these gates eventually causes `0` to appear on wire `z00`, `0` to appear on wire `z01`, and `1` to appear on wire `z02`.
> 在这个例子中，模拟这些门最终会让电线`z00`呈现`0`，电线`z01`呈现`0`，电线`z02`呈现`1`。

Ultimately, the system is trying to produce a **number** by combining the bits on all wires starting with `z`. `z00` is the least significant bit, then `z01`, then `z02`, and so on.
> 最终，系统试图通过组合所有以`z`开头的电线上的比特来产生一个**数字**。`z00`是最低位，然后是`z01`，再是`z02`，以此类推。

In this example, the three output bits form the binary number `100` which is equal to the decimal number **`4`**.
> 在本例中，这三个输出比特组成二进制数`100`，等于十进制的**`4`**。

Here's a larger example:
> 下面是一个更大的例子：

```
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
```

After waiting for values on all wires starting with `z`, the wires in this system have the following values:
> 等待所有以`z`开头的电线有值后，这个系统中各电线的值如下：

```
bfw: 1
bqk: 1
djm: 1
ffh: 0
fgs: 1
frj: 1
fst: 1
gnj: 1
hwm: 1
kjc: 0
kpj: 1
kwq: 0
mjb: 1
nrd: 1
ntg: 0
pbm: 1
psh: 1
qhw: 1
rvg: 0
tgd: 0
tnw: 1
vdt: 1
wpb: 0
z00: 0
z01: 0
z02: 0
z03: 1
z04: 0
z05: 1
z06: 1
z07: 1
z08: 1
z09: 1
z10: 1
z11: 0
z12: 0
```

Combining the bits from all wires starting with `z` produces the binary number `0011111101000`. Converting this number to decimal produces **`2024`**.
> 把所有以`z`开头的电线上的比特组合起来，得到二进制数`0011111101000`。将其转换为十进制得到**`2024`**。

Simulate the system of gates and wires. **What decimal number does it output on the wires starting with `z`?**
> 模拟这个门和电线系统。**以`z`开头的电线输出的十进制数字是多少？**

Your puzzle answer was `63168299811048`.

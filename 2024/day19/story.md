# Day 19: Linen Layout
> # 第十九天：浴巾拼接

Today, The Historians take you up to the [hot springs](https://adventofcode.com/2023/day/12) on Gear Island! Very [suspiciously](https://www.youtube.com/watch?v=ekL881PJMjI), absolutely nothing goes wrong as they begin their careful search of the vast field of helixes.
> 今天，历史学家们带你去了齿轮岛的[温泉](https://adventofcode.com/2023/day/12)！非常[可疑地](https://www.youtube.com/watch?v=ekL881PJMjI)，他们开始仔细搜寻大片螺旋田时，居然什么意外都没发生。

Could this **finally** be your chance to visit the [onsen](https://en.wikipedia.org/wiki/Onsen) next door? Only one way to find out.
> 这**终于**是你去隔壁[温泉](https://en.wikipedia.org/wiki/Onsen)的机会吗？只有试试才知道。

After a brief conversation with the reception staff at the onsen front desk, you discover that you don't have the right kind of money to pay the admission fee. However, before you can leave, the staff get your attention. Apparently, they've heard about how you helped at the hot springs, and they're willing to make a deal: if you can simply help them **arrange their towels**, they'll let you in for **free**!
> 在温泉前台和接待员简短交谈后，你发现自己没有合适的钱支付门票。不过，还没等你离开，工作人员就叫住了你。显然，他们听说了你在温泉的英勇事迹，愿意和你做个交易：只要你能帮他们**整理浴巾**，就可以**免费**入场！

Every towel at this onsen is marked with a **pattern of colored stripes**. There are only a few patterns, but for any particular pattern, the staff can get you as many towels with that pattern as you need. Each stripe can be **white** (`w`), **blue** (`u`), **black** (`b`), **red** (`r`), or **green** (`g`). So, a towel with the pattern `ggr` would have a green stripe, a green stripe, and then a red stripe, in that order. (You can't reverse a pattern by flipping a towel upside-down, as that would cause the onsen logo to face the wrong way.)
> 这里的每条浴巾都有一组**彩色条纹图案**。图案种类不多，但每种图案的浴巾你都可以要多少有多少。条纹可以是**白色**（`w`）、**蓝色**（`u`）、**黑色**（`b`）、**红色**（`r`）、**绿色**（`g`）。比如 `ggr` 图案的浴巾就是绿、绿、红三条纹，顺序不能反转（否则温泉的标志就会倒过来）。

The Official Onsen Branding Expert has produced a list of **designs** - each a long sequence of stripe colors - that they would like to be able to display. You can use any towels you want, but all of the towels' stripes must exactly match the desired design. So, to display the design `rgrgr`, you could use two `rg` towels and then an `r` towel, an `rgr` towel and then a `gr` towel, or even a single massive `rgrgr` towel (assuming such towel patterns were actually available).
> 官方温泉品牌专家列出了一份**设计清单**——每个设计是一串条纹颜色。他们希望能展示这些设计。你可以用任意浴巾，但所有浴巾的条纹必须和目标设计完全吻合。比如要展示 `rgrgr`，你可以用两条 `rg` 浴巾再加一条 `r`，也可以用一条 `rgr` 再加一条 `gr`，甚至用一条超长的 `rgrgr` 浴巾（如果有这种图案的话）。

To start, collect together all of the available towel patterns and the list of desired designs (your puzzle input). For example:
> 首先，收集所有可用的浴巾图案和目标设计列表（你的谜题输入）。例如：

```
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
```

The first line indicates the available towel patterns; in this example, the onsen has unlimited towels with a single red stripe (`r`), unlimited towels with a white stripe and then a red stripe (`wr`), and so on.
> 第一行是可用的浴巾图案；本例中，温泉有无限条单红条纹（`r`）、无限条白红条纹（`wr`）等浴巾。

After the blank line, the remaining lines each describe a design the onsen would like to be able to display. In this example, the first design (`brwrr`) indicates that the onsen would like to be able to display a black stripe, a red stripe, a white stripe, and then two red stripes, in that order.
> 空行后，每行是温泉希望展示的一个设计。本例中，第一个设计 `brwrr` 表示希望依次展示黑、红、白、红、红条纹。

Not all designs will be possible with the available towels. In the above example, the designs are possible or impossible as follows:
> 并不是所有设计都能用现有浴巾拼出来。上例中，各设计的可行性如下：

- `brwrr` can be made with a `br` towel, then a `wr` towel, and then finally an `r` towel.
- `bggr` can be made with a `b` towel, two `g` towels, and then an `r` towel.
- `gbbr` can be made with a `gb` towel and then a `br` towel.
- `rrbgbr` can be made with `r`, `rb`, `g`, and `br`.
- `ubwu` is **impossible**.
- `bwurrg` can be made with `bwu`, `r`, `r`, and `g`.
- `brgr` can be made with `br`, `g`, and `r`.
- `bbrgwb` is **impossible**.
> - `brwrr` 可以用 `br`、`wr`、`r` 浴巾拼出。
> - `bggr` 可以用 `b`、两个 `g`、一个 `r` 浴巾拼出。
> - `gbbr` 可以用 `gb`、`br` 浴巾拼出。
> - `rrbgbr` 可以用 `r`、`rb`、`g`、`br` 浴巾拼出。
> - `ubwu` **无法拼出**。
> - `bwurrg` 可以用 `bwu`、`r`、`r`、`g` 浴巾拼出。
> - `brgr` 可以用 `br`、`g`、`r` 浴巾拼出。
> - `bbrgwb` **无法拼出**。

In this example, **`6`** of the eight designs are possible with the available towel patterns.
> 在本例中，8个设计中有 **6** 个可以用现有浴巾图案拼出。

To get into the onsen as soon as possible, consult your list of towel patterns and desired designs carefully. **How many designs are possible?**
> 为了尽快进温泉，请仔细核对你的浴巾图案和目标设计列表。**有多少个设计是可行的？**

Your puzzle answer was `336`.

## Part Two
> ## 第二部分

The staff don't really like some of the towel arrangements you came up with. To avoid an endless cycle of towel rearrangement, maybe you should just give them every possible option.
> 工作人员其实并不喜欢你拼出来的某些浴巾组合。为了避免无休止地调整浴巾，也许你应该把所有可能的方案都列出来。

Here are all of the different ways the above example's designs can be made:
> 下面是上面例子中每个设计的所有拼接方式：

`brwrr` can be made in two different ways: `b`, `r`, `wr`, `r` **or** `br`, `wr`, `r`.
> `brwrr` 有两种拼法：`b`、`r`、`wr`、`r` **或** `br`、`wr`、`r`。

`bggr` can only be made with `b`, `g`, `g`, and `r`.
> `bggr` 只能用 `b`、`g`、`g`、`r` 拼出。

`gbbr` can be made 4 different ways:
> `gbbr` 有4种拼法：

- `g`, `b`, `b`, `r`
- `g`, `b`, `br`
- `gb`, `b`, `r`
- `gb`, `br`

`rrbgbr` can be made 6 different ways:
> `rrbgbr` 有6种拼法：

- `r`, `r`, `b`, `g`, `b`, `r`
- `r`, `r`, `b`, `g`, `br`
- `r`, `r`, `b`, `gb`, `r`
- `r`, `rb`, `g`, `b`, `r`
- `r`, `rb`, `g`, `br`
- `r`, `rb`, `gb`, `r`

`bwurrg` can only be made with `bwu`, `r`, `r`, and `g`.
> `bwurrg` 只能用 `bwu`、`r`、`r`、`g` 拼出。

`brgr` can be made in two different ways: `b`, `r`, `g`, `r` **or** `br`, `g`, `r`.
> `brgr` 有两种拼法：`b`、`r`、`g`、`r` **或** `br`、`g`、`r`。

`ubwu` and `bbrgwb` are still impossible.
> `ubwu` 和 `bbrgwb` 依然无法拼出。

Adding up all of the ways the towels in this example could be arranged into the desired designs yields **`16`** (`2 + 1 + 4 + 6 + 1 + 2`).
> 把本例中所有设计的拼接方式加起来，总共有 **16** 种（`2 + 1 + 4 + 6 + 1 + 2`）。

They'll let you into the onsen as soon as you have the list. **What do you get if you add up the number of different ways you could make each design?**
> 只要你把所有方案列出来，他们就让你进温泉。**把每个设计的所有拼接方式数量加起来，结果是多少？**

Your puzzle answer was `758890600222015`.

# [Day 2: Dive!](https://adventofcode.com/2021/day/2)

> 第2天：潜水！

Now, you need to figure out how to pilot this thing.

> 现在，你需要弄清楚如何驾驶这个东西。

It seems like the submarine can take a series of commands like `forward 1`, `down 2`, or `up 3`:

> 看起来潜水艇可以执行一系列命令，例如`forward 1`、`down 2`或`up 3`：

- `forward X` increases the horizontal position by `X` units.
- `down X` **increases** the depth by `X` units.
- `up X` **decreases** the depth by `X` units.

> - `forward X` 增加 `X` 单位的水平位置。
> - `down X` **增加** `X` 单位的深度。
> - `up X` **减少** `X` 单位的深度。

Note that since you're on a submarine, `down` and `up` affect your **depth**, and so they have the opposite result of what you might expect.

> 请注意，由于你在潜水艇上，`down` 和 `up` 会影响你的**深度**，所以它们会得到与你预期相反的结果。

The submarine seems to already have a planned course ([your puzzle input](day02.txt)). You should probably figure out where it's going. For example:

> 潜水艇似乎已经设置了计划的路线（[你的谜题输入](day02.txt)）。你或许应该弄清楚它要去哪里。例如：

```diff
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

Your horizontal position and depth both start at `0`. The steps above would then modify them as follows:

> 你的水平位置和深度都从 `0` 开始。然后上面的步骤将改变它们，如下：

- `forward 5` adds `5` to your horizontal position, a total of `5`.
- `down 5` adds `5` to your depth, resulting in a value of `5`.
- `forward 8` adds `8` to your horizontal position, a total of `13`.
- `up 3` decreases your depth by `3`, resulting in a value of `2`.
- `down 8` adds `8` to your depth, resulting in a value of `10`.
- `forward 2` adds `2` to your horizontal position, a total of `15`.

> - `forward 5` 将你的水平位置增加 `5`，累计为 `5`。
> - `down 5` 将你的深度增加 `5`，结果值为 `5`。
> - `forward 8` 将你的水平位置增加 `8`，累计为 `13`。
> - `up 3` 将你的深度减少 `3`，结果值为 `2`。
> - `down 8` 将你的深度增加 `8`，结果值为 `10`。
> - `forward 2` 将你的水平位置增加 `2`，累计为 `15`。

After following these instructions, you would have a horizontal position of `15` and a depth of `10`. (Multiplying these together produces **`150`**.)

> 按照这些指令操作后，你将得到水平位置为 `15` 和深度为 `10`。（将这些值相乘得到 **`150`**。）

Calculate the horizontal position and depth you would have after following the planned course. **What do you get if you multiply your final horizontal position by your final depth?**

> 在执行计划路线后，计算水平位置和深度。**如果将最终的水平位置乘以最终的深度，会得到什么？**

Your puzzle answer was `2215080`.

## --- Part Two ---

Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

> 基于你的计算，计划中的路线似乎没有任何意义。你找到潜水艇手册，发现这个过程实际上稍微复杂一些。

In addition to horizontal position and depth, you'll also need to track a third value, **aim**, which also starts at `0`. The commands also mean something entirely different than you first thought:

> 除了水平位置和深度之外，你还需要跟踪第三个值**目标值**，它也从 `0` 开始。这些命令的含义也与你最初想象的完全不同：

- `down X` **increases** your aim by `X` units.
- `up X` **decreases** your aim by `X` units.
- `forward X` does two things:
  - It increases your horizontal position by `X` units.
  - It increases your depth by your aim **multiplied by** `X`.

> - `down X` 将你的目标值**增加** `X` 个单位。
> - `up X` 将你的目标值**减少** `X` 个单位。
> - `forward X` 做两件事：
>   - 它将你的水平位置增加 `X` 个单位。
>   - 它将你的深度增加目标值**乘以** `X`。

Again note that since you're on a submarine, `down` and `up` do the opposite of what you might expect: "down" means aiming in the positive direction.

> 再次注意，由于你在潜水艇上，`down` 和 `up` 的作用与你预期的相反："down"意味着目标值增加。

Now, the above example does something different:

> 现在，上面的例子做了一些不同的事情：

- `forward 5` adds `5` to your horizontal position, a total of `5`. Because your aim is `0`, your depth does not change.
- `down 5` adds `5` to your aim, resulting in a value of `5`.
- `forward 8` adds `8` to your horizontal position, a total of `13`. Because your aim is `5`, your depth increases by `8*5=40`.
- `up 3` decreases your aim by `3`, resulting in a value of `2`.
- `down 8` adds `8` to your aim, resulting in a value of `10`.
- `forward 2` adds `2` to your horizontal position, a total of `15`. Because your aim is `10`, your depth increases by `2*10=20` to a total of `60`.

> - `forward 5` 将你的水平位置增加 `5`，累计为 `5`。因为你的目标值是 `0`，所以你的深度没有变化。
> - `down 5` 将你的目标值增加 `5`，结果值为 `5`。
> - `forward 8` 将你的水平位置增加 `8`，累计为 `13`。因为你的目标值是 `5`，所以你的深度增加了 `8*5=40`。
> - `up 3` 将你的目标值减少 `3`，结果值为 `2`。
> - `down 8` 将你的目标增加 `8`，结果值为 `10`。
> - `forward 2` 将你的水平位置增加 `2`，累计为 `15`。因为你的目标值是 `10`，所以你的深度增加 `2*10=20`，总共达到了 `60`。

After following these new instructions, you would have a horizontal position of `15` and a depth of `60`. (Multiplying these produces **`900`**.)

> 按照这些新指令操作后，你的水平位置为 `15` 和深度为 `60`。（将这些值相乘得到 **`900`**。）

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. **What do you get if you multiply your final horizontal position by your final depth?**

> 使用这个新指令，在执行计划路线后，计算水平位置和深度。 **如果将最终的水平位置乘以最终的深度，会得到什么？**

Your puzzle answer was `1864715580`.

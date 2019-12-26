# [Day 1: The Tyranny of the Rocket Equation](https://adventofcode.com/2019/day/1)

> 第1天：火箭方程式的暴政

Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from **fifty stars**.

> 当圣诞老人向其他星球运送礼物的时候在太阳系的边缘搁浅了！为了准确地计算出他在太空中的位置，安全地调整其跃迁引擎 ，并及时返回地球以拯救圣诞节，他需要你带给他**五十颗星**。

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

> 通过解决谜题来收集星星。Advent日历期间每天会有两道谜题激活；只有当你完成第一道谜题后，第二道谜题才会解锁。每个谜题授予**一颗星**。祝你好运！

The Elves quickly load you into a spacecraft and prepare to launch.

> 精灵们迅速的将你装进宇宙飞船并准备发射。

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

> 在第一次是否出发的投票中，每个精灵都是投了出发，直到他们看到燃料表。他们还没有确定所需的燃料量。

Fuel required to launch a given **module** is based on its **mass**. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

> 发射一个给定的**模块**所需的燃料取决于它的**质量**。具体地说，要算出一个模块所需的燃料，得先获取它的质量，除以三，向下取整，最后减去 2。

For example:

- For a mass of `12`, divide by 3 and round down to get `4`, then subtract 2 to get `2`.
- For a mass of `14`, dividing by 3 and rounding down still yields `4`, so the fuel required is also `2`.
- For a mass of `1969`, the fuel required is `654`.
- For a mass of `100756`, the fuel required is `33583`.

> 举个例子：
>
> - 质量为 `12`，除以 3 并向下取整得到 `4`，然后减去 2 得到 `2`。
> - 质量为 `14`，除以 3 并向下取整仍会得到 `4`，因此所需的燃料也是 `2`。
> - 质量为 `1969`，所需的燃料是 `654`。
> - 质量为 `100756`，所需的燃料是 `33583`。

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module ([your puzzle input](day1.txt)), then add together all the fuel values.

> 燃料表需要知道总的燃油需求量。要算出它，需要分别计算出每个模块的质量（[你的谜题输入](day1.txt)）所需的燃料量，然后将所有这些燃料值相加。

**What is the sum of the fuel requirements** for all of the modules on your spacecraft?

> 你的宇宙飞船上的所有模块**所需的燃料总和是多少**？

Your puzzle answer was `3412207`.

## Part Two

During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

> 在第二次是否出发的投票中，负责火箭方程式二次确认的精灵停止了发射程序。显然，你忘记为刚刚添加的燃料添加燃料。

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel **also** requires fuel, and **that** fuel requires fuel, and so on. Any mass that would require **negative fuel** should instead be treated as if it requires **zero fuel**; the remaining mass, if any, is instead handled by **wishing really hard**, which has no mass and is outside the scope of this calculation.

> 燃料本身也像模块一样需要燃料 —— 得先获取它的质量，除以三，向下取整，最后减去 2。事实上，那些燃料**还**需要燃料，**那些**新增加的燃料还需要燃料，依此类推。如果某个质量需要的燃料计算为**负**则应被视为**零**；剩余的质量（如果有的话）将视为**可有可无**，认为没有质量并且不在此计算范围之内。

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

> 因此，对于每个模块的质量，计算其燃料并将其添加到总计中。然后，将刚刚计算出的燃料的质量作为输入，并重复该过程，直到燃料需求为零或负。例如：

- A module of mass `14` requires `2` fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is `0`, which would call for a negative fuel), so the total fuel required is still just `2`.
- At first, a module of mass `1969` requires `654` fuel. Then, this fuel requires `216` more fuel (`654 / 3 - 2`). `216` then requires `70` more fuel, which requires `21` fuel, which requires `5` fuel, which requires no further fuel. So, the total fuel required for a module of mass `1969` is `654 + 216 + 70 + 21 + 5 = 966`.
- The fuel required by a module of mass `100756` and its fuel is: `33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346`.

> - 质量为 `14` 的模块需要 `2` 份燃料。 这些燃料不需要更多的燃料（2 除以 3 并且向下取整为 `0`，继续算下去燃料为负），因此总的燃料需求量仍然只有为 `2` 份。
> - 最开始，质量为 `1969` 的模块需要 `654` 份燃料。然后，这些燃料又需要 `216` 份燃料（`654/3-2`）。`216` 又需要 `70` 份燃料，接下来需要 `21` 份燃料，接下来需要 `5` 份燃料，再接下来就不需要更多的燃料了。因此，质量为 `1969` 的模块所需的燃料总量为 `654 + 216 + 70 + 21 + 5 = 966`。
> - 质量为 `100756` 的模块所需的燃料为：`33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346`。

**What is the sum of the fuel requirements** for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

> 同时考虑增加的燃料的质量，你的宇宙飞船上的所有模块**所需的燃料总和是多少**？（分别计算每个模块的燃料需求，然后将它们加起来。）

Your puzzle answer was `5115436`.

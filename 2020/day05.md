# Day 5: Binary Boarding

> 第五天：二进制登机

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

> 你登机时发现了一个新问题：你丢失了登机牌！你不确定哪个座位是你的，而且所有空乘人员都正忙于突然增多的人潮。

You write a quick program to use your phone's camera to scan all of the nearby boarding passes ([your puzzle input](day05.txt)); perhaps you can find your seat through process of elimination.

> 你编写了一个快速程序，使用你的手机相机扫描附近的所有登机牌（[你的谜题输入](day05.txt)），也许你可以通过排除法找到你的位置。

Instead of [zones or groups](https://www.youtube.com/watch?v=oAHbLRjF0vo), this airline uses **binary space partitioning** to seat people. A seat might be specified like `FBFBBFFRLR`, where `F` means "front", `B` means "back", `L` means "left", and `R` means "right".

> 该航空公司使用“二进制空间分割法”来代替“区或组”的方式进行乘客就坐安排。可以像 `FBFBBFFRLR` 这样指定一个座位，其中 `F` 表示“前”，`B` 表示“后”，`L` 表示“左”，`R` 表示“右”。

The first 7 characters will either be `F` or `B`; these specify exactly one of the **128 rows** on the plane (numbered `0` through `127`). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the **front** (`0` through `63`) or the **back** (`64` through `127`). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

> 前七个字符为 `F` 或 `B`，它们准确指定了飞机上的 128 排（编号为 `0` 到 `127`）之一。每个字母告诉你指定座位在一个区域的哪一半。从全部的排数开始，第一个字母表示座位位于前排（`0` 到 `63`）还是后排（`64` 到 `127`）。下一个字母表示座位位于所选区域的哪一半，依此类推，直到你只剩下一排。

For example, consider just the first seven characters of `FBFBBFFRLR`:

- Start by considering the whole range, rows `0` through `127`.
- `F` means to take the **lower half**, keeping rows `0` through `63`.
- `B` means to take the **upper half**, keeping rows `32` through `63`.
- `F` means to take the **lower half**, keeping rows `32` through `47`.
- `B` means to take the **upper half**, keeping rows `40` through `47`.
- `B` keeps rows `44` through `47`.
- `F` keeps rows `44` through `45`.
- The final `F` keeps the lower of the two, **row `44`**.

> 举个例子，仅考虑 `FBFBBFFRLR` 的前七个字符：
>
> - 首先考虑整个范围，从第 `0` 排至第 `127` 排。
> - `F` 表示取前半部分，保留第 `0` 排至第 `63` 排。
> - `B` 表示取后半部分，保留第 `32` 排至第 `63` 排。
> - `F` 表示取前半部分，保留第 `32` 排至第 `47` 排。
> - `B` 表示取后半部分，保留第 `40` 排至第 `47` 排。
> - `B` 保留第 `44` 排至第 `47` 排。
> - `F` 保留第 `44` 排至第 `45` 排。
> - 最后的 `F` 保留两个中的前半部分，即第 `44` 排。

The last three characters will be either `L` or `R`; these specify exactly one of the **8 columns** of seats on the plane (numbered `0` through `7`). The same process as above proceeds again, this time with only three steps. `L` means to keep the **lower half**, while `R` means to keep the **upper half**.

> 后三个字符为 `L` 或 `R`，它们准确指定了飞机上的 8 列座位（编号为 `0` 至 `7`）之一。再次执行与上述相同的过程，这次仅需三个步骤。`L` 表示保留左半部分，而 `R` 表示保留右半部分。

For example, consider just the last 3 characters of `FBFBBFFRLR`:

- Start by considering the whole range, columns `0` through `7`.
- `R` means to take the **upper half**, keeping columns `4` through `7`.
- `L` means to take the **lower half**, keeping columns `4` through `5`.
- The final `R` keeps the upper of the two, **column `5`**.

> 举个例子，仅考虑 `FBFBBFFRLR` 的后三个字符：
>
> - 首先考虑整个范围，从第 `0` 列至第 `7` 列。
> - `R` 表示取右半部分，保留第 `4` 列至第 `7` 列。
> - `L` 表示取左半部分，保留第 `4` 列至第 `5` 列。
> - 最后的 `R` 保留两个中的右半部分，即第 `5` 列。

So, decoding `FBFBBFFRLR` reveals that it is the seat at **row `44`, column `5`**.

> 因此，解码 `FBFBBFFRLR` 后会发现它是第 `44` 排，第 `5` 列的座位。

Every seat also has a unique **seat ID**: multiply the row by 8, then add the column. In this example, the seat has ID `44 * 8 + 5 = 357`.

> 每个座位还拥有唯一的座位 ID：将行号乘以 8，然后加上列号。在这个例子中，座位的 ID 为 `44 * 8 + 5 = 357`。

Here are some other boarding passes:

- `BFFFBBFRRR`: row `70`, column `7`, seat ID `567`.
- `FFFBBBFRRR`: row `14`, column `7`, seat ID `119`.
- `BBFFBBFRLL`: row `102`, column `4`, seat ID `820`.

> 以下是一些其他登机牌信息：
>
> - `BFFFBBFRRR`: 第 `70` 排, 第 `7` 列, 座位 ID 是 `567`。
> - `FFFBBBFRRR`: 第 `14` 排, 第 `7` 列, 座位 ID 是 `119`。
> - `BBFFBBFRLL`: 第 `102` 排, 第 `4` 列, 座位 ID 是 `820`。

As a sanity check, look through your list of boarding passes. **What is the highest seat ID on a boarding pass?**

> 做一个完整性检查，浏览你的登机牌列表。登机牌中最高的座位 ID 是多少？

Your puzzle answer was `915`.

## --- Part Two ---

**Ding!** The "fasten seat belt" signs have turned on. Time to find your seat.

> 叮！“系紧安全带”标志打开了。是时候找到你的座位了。

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

> 这是一次满员的飞行，因此你的座位应该是列表中唯一缺少的登机牌。但是，有一个问题：这架飞机上最前面和最后面的一些座位是不存在的，因此它们也不会出现在你的列表中。

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

> 因为你的座位不是在最前面或最后面，所以你的座位号 +1 和 -1 的座位号将会出现在你的列表中。

**What is the ID of your seat?**

> 你的座位号是多少？

Your puzzle answer was `699`.

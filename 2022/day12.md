# Day 12: Hill Climbing Algorithm

> 第12天：爬山算法

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

> 你尝试使用你的手持设备联系精灵们，但你所在的河边地势太低了，无法获得良好的信号。

You ask the device for a heightmap of the surrounding area ([your puzzle input](day12.txt)). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where `a` is the lowest elevation, `b` is the next-lowest, and so on up to the highest elevation, `z`.

> 你用设备生成了一份周围区域的高度图（[你的谜题输入](day12.txt)）。高度图显示了分割成网格的局部区域俯视图，网格中每个正方形的海拔由一个小写字母表示，其中 `a` 表示最低海拔，`b` 表示次低海拔，依此类推直到最高海拔 `z`。

Also included on the heightmap are marks for your current position (`S`) and the location that should get the best signal (`E`). Your current position (`S`) has elevation `a`, and the location that should get the best signal (`E`) has elevation `z`.

> 高度图上还包括你当前位置的标记 (`S`) 以及可以获得最佳信号的位置 (`E`)。你当前的位置 (`S`) 的海拔高度为 `a`，应该获得最佳信号的位置 (`E`) 的海拔高度为 `z`。

You'd like to reach `E`, but to save energy, you should do it in **as few steps as possible**. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be **at most one higher** than the elevation of your current square; that is, if your current elevation is `m`, you could step to elevation `n`, but not to elevation `o`. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

> 你想要到达 `E` 点，但为了节省能量，你应该**用尽可能少的步数**完成。在每一步中，你只能向上、向下、向左或向右移动一个方格。为了不拿出你的登山装备，下一个方块的高度比你当前方块的高度**最多高一格**。也就是说，如果你当前的海拔高度是 `m`，你可以走到海拔高度为 `n` 的方格，但不能走到海拔高度为 `o` 的方格。（这也意味着目标方块的高度可以比当前方块的高度低很多。）

For example:

> 举个例子：

```
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
```

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the `e` at the bottom. From there, you can spiral around to the goal:

> 这里，你从左上角开始。你的目的地在中间附近。你可以从向下或向右移动开始，但最终你需要到达底部的 `e`。从那里，你可以螺旋形接近目标：

```
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
```

In the above diagram, the symbols indicate whether the path exits each square moving up (`^`), down (`v`), left (`<`), or right (`>`). The location that should get the best signal is still `E`, and `.` marks unvisited squares.

> 在上图中，符号表示向上（`^`）、向下（`v`）、向左（`<`）或向右（`>`）移出每个方块的路径方向。可以获得最好信号的位置仍然是 `E`，`.` 表示未访问的方块。

This path reaches the goal in **`31`** steps, the fewest possible.

> 这条路径用 **`31`** 步到达了目的地，是最短的路径。

**What is the fewest steps required to move from your current position to the location that should get the best signal?**

> **从你当前位置移动到获得最佳信号的位置所需的最少步数是多少？**

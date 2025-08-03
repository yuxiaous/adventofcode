# Day 25: Code Chronicle
> # 第二十五天：代码编年史

Out of ideas and time, The Historians agree that they should go back to check the **Chief Historian's office** one last time, just in case he went back there without you noticing.
> 想不出别的办法，也没时间了，历史学家们决定最后再去**首席历史学家的办公室**看看，以防他悄悄回去了你没注意到。

When you get there, you are surprised to discover that the door to his office is **locked**! You can hear someone inside, but knocking yields no response. The locks on this floor are all fancy, expensive, virtual versions of [five-pin tumbler locks](https://en.wikipedia.org/wiki/Pin_tumbler_lock), so you contact North Pole security to see if they can help open the door.
> 到了那里，你惊讶地发现办公室的门**锁上了**！你能听到里面有人，但敲门没有回应。这层的锁全都是花哨又昂贵的虚拟[五珠弹子锁](https://en.wikipedia.org/wiki/Pin_tumbler_lock)，于是你联系了北极安保，看看他们能不能帮你开门。

Unfortunately, they've lost track of which locks are installed and which keys go with them, so the best they can do is send over **schematics of every lock and every key** for the floor you're on (your puzzle input).
> 不幸的是，他们已经搞不清装了哪些锁、哪些钥匙配哪些锁了，所以他们只能把你所在楼层**所有锁和所有钥匙的结构图**都发给你（你的谜题输入）。

The schematics are in a cryptic file format, but they do contain manufacturer information, so you look up their support number.
> 这些结构图用一种神秘的文件格式保存，不过里面有制造商信息，于是你查到了他们的客服电话。

"Our Virtual Five-Pin Tumbler product? That's our most expensive model! **Way** more secure than--" You explain that you need to open a door and don't have a lot of time.
> “我们的虚拟五珠弹子锁？那可是我们最贵的型号！**比——**”你打断了对方，解释你需要开门，而且时间紧迫。

"Well, you can't know whether a key opens a lock without actually trying the key in the lock (due to quantum hidden variables), but you **can** rule out some of the key/lock combinations."
> “嗯，你不能在不实际试钥匙的情况下确定钥匙能不能开锁（因为有量子隐变量），但你**可以**排除一些钥匙和锁的组合。”

"The virtual system is complicated, but part of it really is a crude simulation of a five-pin tumbler lock, mostly for marketing reasons. If you look at the schematics, you can figure out whether a key could possibly fit in a lock."
> “虚拟系统很复杂，但有一部分确实是对五珠弹子锁的粗糙模拟，主要是为了营销。如果你看结构图，其实可以判断一把钥匙是否可能插进一把锁。”

He transmits you some example schematics:
> 他给你发来了一些示例结构图：

```
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
```

"The locks are schematics that have the top row filled (`#`) and the bottom row empty (`.`); the keys have the top row empty and the bottom row filled. If you look closely, you'll see that each schematic is actually a set of columns of various heights, either extending downward from the top (for locks) or upward from the bottom (for keys)."
> “锁的结构图顶部一行全是`#`，底部一行全是`.`；钥匙的结构图顶部一行全是`.`，底部一行全是`#`。仔细看你会发现，每个结构图其实就是若干列，每列有不同的高度，要么从上往下（锁），要么从下往上（钥匙）。”

"For locks, those are the pins themselves; you can convert the pins in schematics to a list of heights, one per column. For keys, the columns make up the shape of the key where it aligns with pins; those can also be converted to a list of heights."
> “对于锁，这些就是弹子本身；你可以把结构图里的弹子转成每列一个高度的列表。对于钥匙，这些列组成了钥匙的形状，对应弹子的地方；同样可以转成高度列表。”

"So, you could say the first lock has pin heights `0,5,3,4,3`:"
> “所以，你可以说第一个锁的弹子高度是`0,5,3,4,3`：”

```
#####
.####
.####
.####
.#.#.
.#...
.....
```

"Or, that the first key has heights `5,0,2,1,3`:"
> “或者说，第一个钥匙的高度是`5,0,2,1,3`：”

```
.....
#....
#....
#...#
#.#.#
#.###
#####
```

"These seem like they should fit together; in the first four columns, the pins and key don't overlap. However, this key **cannot** be for this lock: in the rightmost column, the lock's pin overlaps with the key, which you know because in that column the sum of the lock height and key height is more than the available space."
> “这看起来好像能配合；前四列弹子和钥匙都不重叠。但实际上这把钥匙**不能**开这把锁：在最右一列，锁的弹子和钥匙重叠了，因为那一列弹子高度加钥匙高度超过了可用空间。”

"So anyway, you can narrow down the keys you'd need to try by just testing each key with each lock, which means you would have to check... wait, you have **how** many locks? But the only installation **that** size is at the North--" You disconnect the call.
> “总之，你可以通过把每把钥匙和每把锁都试一遍来缩小需要尝试的钥匙数量，也就是说你得检查……等等，你说你有**多少**把锁？但只有北极才有**那么**大的装置——”你挂断了电话。

In this example, converting both locks to pin heights produces:
> 在这个例子中，把两把锁都转成弹子高度得到：

```
0,5,3,4,3
1,2,0,5,3
```

Converting all three keys to heights produces:
> 把三把钥匙都转成高度得到：

```
5,0,2,1,3
4,3,4,0,2
3,0,2,0,1
```

Then, you can try every key with every lock:
> 然后，你可以把每把钥匙和每把锁都试一遍：

- Lock `0,5,3,4,3` and key `5,0,2,1,3`: **overlap** in the last column.
- Lock `0,5,3,4,3` and key `4,3,4,0,2`: **overlap** in the second column.
- Lock `0,5,3,4,3` and key `3,0,2,0,1`: all columns **fit**!
- Lock `1,2,0,5,3` and key `5,0,2,1,3`: **overlap** in the first column.
- Lock `1,2,0,5,3` and key `4,3,4,0,2`: all columns **fit**!
- Lock `1,2,0,5,3` and key `3,0,2,0,1`: all columns **fit**!
> - 锁`0,5,3,4,3`和钥匙`5,0,2,1,3`：最后一列**重叠**。
> - 锁`0,5,3,4,3`和钥匙`4,3,4,0,2`：第二列**重叠**。
> - 锁`0,5,3,4,3`和钥匙`3,0,2,0,1`：所有列都**匹配**！
> - 锁`1,2,0,5,3`和钥匙`5,0,2,1,3`：第一列**重叠**。
> - 锁`1,2,0,5,3`和钥匙`4,3,4,0,2`：所有列都**匹配**！
> - 锁`1,2,0,5,3`和钥匙`3,0,2,0,1`：所有列都**匹配**！

So, in this example, the number of unique lock/key pairs that fit together without overlapping in any column is **`3`**.
> 所以，在这个例子中，能完全匹配、不重叠的锁/钥匙组合有**`3`**对。

Analyze your lock and key schematics. **How many unique lock/key pairs fit together without overlapping in any column?**
> 分析你的锁和钥匙结构图。**有多少对锁和钥匙在所有列都不重叠，可以完全匹配？**

Your puzzle answer was `3619`.

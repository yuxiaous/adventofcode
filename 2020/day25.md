# Day 25: Combo Breaker

> 第二十五天：组合断路器

You finally reach the check-in desk. Unfortunately, their registration systems are currently offline, and they cannot check you in. Noticing the look on your face, they quickly add that tech support is already on the way! They even created all the room keys this morning; you can take yours now and give them your room deposit once the registration system comes back online.

> 你终于到达了接待前台。不幸的是，他们的注册系统当前处于离线状态，无法为你登记。他们注意到你的表情，迅速补充道，技术支持马上就来！他们在今天早上已经制作了所有房间的钥匙，一旦注册系统重新上线，你就可以立刻拿走你的房间钥匙并支付房费。

The room key is a small [RFID](https://en.wikipedia.org/wiki/Radio-frequency_identification) card. Your room is on the 25th floor and the elevators are also temporarily out of service, so it takes what little energy you have left to even climb the stairs and navigate the halls. You finally reach the door to your room, swipe your card, and - **beep** - the light turns red.

> 房间钥匙是一张很小的 [RFID](https://en.wikipedia.org/wiki/Radio-frequency_identification) 卡。你的房间位于 25 楼，电梯不巧暂时停止了服务，因此你耗尽了仅剩的一点体力用来爬楼梯和寻找房间。你终于到达了你的房间门前，刷卡，一阵哔哔声，指示灯变成了红色。

Examining the card more closely, you discover a phone number for tech support.

> 你仔细检查门卡，发现上面有一个技术支持的电话号码。

"Hello! How can we help you today?" You explain the situation.

> “您好！我们能为您提供什么帮助吗？” 你向他们说明了情况。

"Well, it sounds like the card isn't sending the right command to unlock the door. If you go back to the check-in desk, surely someone there can reset it for you." Still catching your breath, you describe the status of the elevator and the exact number of stairs you just had to climb.

> “好的，听起来像是门卡没有发送正确的命令来解锁门。请您返回接待前台，会有人为你重置它。” 你仍在喘气，向对方描述了电梯的情况以及你刚才爬过的楼梯。

"I see! Well, your only other option would be to reverse-engineer the cryptographic handshake the card does with the door and then inject your own commands into the data stream, but that's definitely impossible." You thank them for their time.

> “我明白了！好的，您唯一的选项是对门卡与房门之间的加密握手过程进行逆向工程，然后将自己的命令注入进数据流，但这无疑是不可能的。”你感谢了他们。

Unfortunately for the door, you know a thing or two about cryptographic handshakes.

> 不幸的是，对于房门的加密握手过程，你所知甚少。

The handshake used by the card and the door involves an operation that **transforms** a **subject number**. To transform a subject number, start with the value `1`. Then, a number of times called the **loop size**, perform the following steps:

- Set the value to itself multiplied by the **subject number**.
- Set the value to the remainder after dividing the value by **`20201227`**.

> 门卡和房门使用的握手过程涉及一个转换房间号的操作。要转换房间号，需要一个值从 `1` 开始，然后执行一定次数（称为循环次数）的以下步骤：
>
> - 将值乘以房间号。
> - 将值除以 **`20201227`** 之后得到的余数。

The card always uses a specific, secret **loop size** when it transforms a subject number. The door always uses a different, secret loop size.

> 门卡在转换房间号时始终使用一个特定的保密循环次数。房门则始终使用另一个不同的保密循环次数。

The cryptographic handshake works like this:

- The **card** transforms the subject number of **`7`** according to the **card's** secret loop size. The result is called the **card's public key**.
- The **door** transforms the subject number of **`7`** according to the **door's** secret loop size. The result is called the **door's public key**.
- The card and door use the wireless RFID signal to transmit the two public keys ([your puzzle input](day25.txt)) to the other device. Now, the card has the **door's** public key, and the **door** has the **card's** public key. Because you can eavesdrop on the signal, you have both public keys, but neither device's loop size.
- The **card** transforms the subject number of **the door's public key** according to the **card's** loop size. The result is the **encryption key**.
- The **door** transforms the subject number of **the card's public key** according to the **door's** loop size. The result is the same **encryption key** as the **card** calculated.

> 加密握手的工作方式如下：
>
> - 门卡根据卡的保密循环次数转换房间号 **`7`**，其结果称为卡的公钥。
> - 房门根据门的保密循环次数转换房间号 **`7`**，其结果称为门的公钥。
> - 卡和门之间使用无线 RFID 信号将两个公钥（[你的谜题输入](day25.txt)）传输给对方。现在，卡拥有了门的公钥，门拥有了卡的公钥。因为你可以监听到信号，所以你也拥有两个公钥，但是你没有设备的循环次数。
> - 门卡根据卡的循环次数转换门的公钥，其结果是密钥。
> - 房门根据门的循环次数转换卡的公钥。其结果是与卡计算出的相同的密钥。

If you can use the two public keys to determine each device's loop size, you will have enough information to calculate the secret **encryption key** that the card and door use to communicate; this would let you send the `unlock` command directly to the door!

> 如果你可以使用两个公钥来确定每个设备的循环次数，那么你就有足够的信息来计算门卡和房门之间用于通信的保密密钥。这将使你可以直接向房门发送 `unlock` 命令！

For example, suppose you know that the card's public key is `5764801`. With a little trial and error, you can work out that the card's loop size must be **`8`**, because transforming the initial subject number of `7` with a loop size of `8` produces `5764801`.

> 举个例子，假设你知道门卡的公钥为 `5764801`。经过反复试验，你就能得出该门卡的循环次数为 **`8`**，因为通过 `8` 次循环转换初始的房间号 `7` 将得到 `5764801`。

Then, suppose you know that the door's public key is `17807724`. By the same process, you can determine that the door's loop size is **`11`**, because transforming the initial subject number of `7` with a loop size of `11` produces `17807724`.

> 然后，假设你知道门的公钥是 `17807724`。通过相同的过程，你可以确定房门的循环次数为 **`11`**，因为通过 `11` 次循环转换初始的房间号 `7` 将得到 `17807724`。

At this point, you can use either device's loop size with the other device's public key to calculate the **encryption key**. Transforming the subject number of `17807724` (the door's public key) with a loop size of `8` (the card's loop size) produces the encryption key, **`14897079`**. (Transforming the subject number of `5764801` (the card's public key) with a loop size of `11` (the door's loop size) produces the same encryption key: **`14897079`**.)

> 此时，你可以使用其中一个设备的循环次数和另一设备的公钥来计算密钥。通过 `8` 次循环（卡的循环次数）来转换房间号 `17807724`（门的公钥）将得到密钥：**`14897079`**。（通过 `11` 次循环（门的循环次数）来转换房间号 `5764801`（卡的公钥）将得到相同的密钥：**`14897079`**。）

**What encryption key is the handshake trying to establish?**

> 握手过程尝试建立的密钥什么？

Your puzzle answer was `3015200`.

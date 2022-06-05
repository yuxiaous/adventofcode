#!/usr/bin/env python3
'''
# 分析

通过 puzzle input 发现：
- 由14组相似的指令组成
- 每组指令中有3处是有差异的，其余的指令均相同

下面是一组指令，差异的部分用a、b和c表示。

inp w
mul x 0
add x z
mod x 26
div z (a)
add x (b)
eql x w
eql x 0    x = (z % 26) + b    !=    w
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (c)
mul y x
add z y    z = (z / a) * (25 * x + 1) + (w + c) * x

阅读指令后发现：
- w 作为输入变量使用
- x、y 作为中间计算的临时变量使用
- z 作为结果变量使用，会传递给下一组代码

每组指令由上一组得到的结果z与当前组的输入w共同得到新一组的结果z，逻辑如下：
if (z % 26) + b == w:
    return (z / a)
else:
    return (z / a) * 26 + w + c

观察图 day24.png 发现：
- 有6组中的 div z (a) 指令的a参数是1，即除以1，结果z值不变
- 有6组中的 div z (a) 指令的a参数是26，即除以26，使结果z值减小

再结合上面的代码，当指令中出现 div z 26 时，如果满足 (z % 26) + b == w 的条件，其结果z就会减小，将上一组的结果z的增大变化抵消掉。相当于一个Undo。

# 思路：

- 按顺序选取一组指令和它后面的一组指令连续运行，即运行2组指令
- 通过循环给出两组指令的输入w1和w2，范围是1~9
- 找出运行完成2组指令后z为0的w1和w2值（可能存在多个肯能），根据要求，选出合适的输入值
- 将这2个输入值按照指令的组索引，存入model对于的索引位置里
- 根据上面的分析，这2组指令产生互相抵消结果的作用，所以可以同时将它们从运行代码中移出
- 依次使用如上方法找出所有配对的指令组

'''

input = open('day24.txt').read().strip()
input = input.split('\n')


class ArithmeticLogicUnit:
    def __init__(self):
        self.variables = {}
        self.variables['w'] = 0
        self.variables['x'] = 0
        self.variables['y'] = 0
        self.variables['z'] = 0
        self.inputs = []

    def inp(self, a):
        value = self.inputs[0]
        self.inputs.pop(0)
        if type(value) == int:
            self.variables[a] = value
        else:
            self.variables[a] = int(value)

    def add(self, a, b):
        if type(b) == int:
            self.variables[a] = self.variables[a] + b
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = self.variables[a] + int(b)
        else:
            self.variables[a] = self.variables[a] + self.variables[b]

    def mul(self, a, b):
        if type(b) == int:
            self.variables[a] = self.variables[a] * b
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = self.variables[a] * int(b)
        else:
            self.variables[a] = self.variables[a] * self.variables[b]

    def div(self, a, b):
        if type(b) == int:
            self.variables[a] = int(self.variables[a] / b)
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = int(self.variables[a] / int(b))
        else:
            self.variables[a] = int(self.variables[a] / self.variables[b])

    def mod(self, a, b):
        if type(b) == int:
            self.variables[a] = self.variables[a] % b
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = self.variables[a] % int(b)
        else:
            self.variables[a] = self.variables[a] % self.variables[b]

    def eql(self, a, b):
        if type(b) == int:
            self.variables[a] = 1 if self.variables[a] == b else 0
        elif b.lstrip('-').replace('.', '', 1).isdigit():
            self.variables[a] = 1 if self.variables[a] == int(b) else 0
        else:
            self.variables[a] = 1 if self.variables[a] == self.variables[b] else 0

    def execute(self, instruction: str):
        cmd = instruction.split()
        op = cmd[0]
        if op == 'inp':
            self.inp(cmd[1])
        elif op == 'add':
            self.add(cmd[1], cmd[2])
        elif op == 'mul':
            self.mul(cmd[1], cmd[2])
        elif op == 'div':
            self.div(cmd[1], cmd[2])
        elif op == 'mod':
            self.mod(cmd[1], cmd[2])
        elif op == 'eql':
            self.eql(cmd[1], cmd[2])


class Program:
    def __init__(self, input):
        self.instructions = [x for x in input]

    def run(self, alu: ArithmeticLogicUnit):
        for instruction in self.instructions:
            alu.execute(instruction)


def part1(input: str):
    length = int(len(input) / 14)

    programs: list[Program] = []
    for i in range(14):
        start = i * length
        end = start + length
        program = Program(input[start:end])
        programs.append(program)

    programs_list = programs.copy()
    programs_map: map[Program:int] = {}

    def find_largest():
        for i in range(len(programs_list)-1):
            program1 = programs_list[i]
            program2 = programs_list[i+1]

            for w1 in reversed(range(1, 10)):
                for w2 in reversed(range(1, 10)):
                    alu = ArithmeticLogicUnit()
                    alu.inputs.append(w1)
                    alu.inputs.append(w2)
                    program1.run(alu)
                    program2.run(alu)

                    if alu.variables['x'] == 0:
                        programs_map[program1] = w1
                        programs_map[program2] = w2
                        programs_list.remove(program1)
                        programs_list.remove(program2)
                        return

    while len(programs_list) > 0:
        find_largest()
    model = [programs_map[p] for p in programs]
    return ''.join([str(x) for x in model])


def part2(input):
    length = int(len(input) / 14)

    programs: list[Program] = []
    for i in range(14):
        start = i * length
        end = start + length
        program = Program(input[start:end])
        programs.append(program)

    programs_list = programs.copy()
    programs_map: map[Program:int] = {}

    def find_smallest():
        for i in range(len(programs_list)-1):
            program1 = programs_list[i]
            program2 = programs_list[i+1]

            for w1 in range(1, 10):
                for w2 in range(1, 10):
                    alu = ArithmeticLogicUnit()
                    alu.inputs.append(w1)
                    alu.inputs.append(w2)
                    program1.run(alu)
                    program2.run(alu)

                    if alu.variables['x'] == 0:
                        programs_map[program1] = w1
                        programs_map[program2] = w2
                        programs_list.remove(program1)
                        programs_list.remove(program2)
                        return

    while len(programs_list) > 0:
        find_smallest()
    model = [programs_map[p] for p in programs]
    return ''.join([str(x) for x in model])


if __name__ == '__main__':
    print('--- Day 24: Arithmetic Logic Unit ---')
    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')

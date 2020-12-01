from IntcodeComputer import IntcodeComputer

class SpringScript:
    def __init__(self):
        self.computer = IntcodeComputer()
        self.computer.load('day21.txt')

    def execute(self, script):
        index = 0
        ret = -1

        def on_input():
            nonlocal index
            char = script[index]
            index += 1
            return ord(char)

        def on_output(queue):
            nonlocal ret
            code = queue.get()
            if code < 128:
                print(chr(code), end='')
            else:
                ret = code

        self.computer.setInputCallback(on_input)
        self.computer.setOutputCallback(on_output)
        self.computer.run().join()
        return ret


part1 = '''NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
'''

part2 = '''NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
RUN
'''

script = SpringScript()
ret = script.execute(part2)
print(ret)

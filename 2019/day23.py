from IntcodeComputer import IntcodeComputer
from queue import Queue
import threading

mutex = threading.Lock()

class packet:
    def __init__(self, address, x, y):
        self.address = address
        self.x = x
        self.y = y

class Switch:
    def __init__(self):
        self.computers = {}
        self.nat_last = None


    def on_input(self, computer):
        ret = -1
        mutex.acquire()
        info = self.computers[computer.address]
        mutex.release()
        if not info['packet'] and len(info['rx'].queue) > 0:
            info['packet'] = info['rx'].get()
            # print(info['address'], 'R', info['packet'])
        if info['packet']:
            mutex.acquire()
            ret = info['packet'].pop(0)
            mutex.release()

            if len(info['packet']) == 0:
                mutex.acquire()
                info['packet'] = None
                mutex.release()
        return ret

    def on_output(self, queue, computer):
        global mutex
        if len(queue.queue) >= 3:
            addr = queue.get()
            x = queue.get()
            y = queue.get()
            # print(info['address'], 'T', [addr, x, y])
            mutex.acquire()
            info = self.computers[computer.address]
            info['tx'].put([addr, x, y])
            mutex.release()

    def add_computer(self, computer, address):
        info = {}
        info['computer'] = computer
        info['address'] = address
        info['tx'] = Queue()
        info['rx'] = Queue()
        info['packet'] = [address]

        self.computers[address] = info

        computer.address = address
        computer.setInputCallback(self.on_input)
        computer.setOutputCallback(self.on_output)
        
    def schedule(self):
        global mutex
        while True:
            idle = True
            for addr in self.computers:
                info = self.computers[addr]
                mutex.acquire()
                tx = info['tx']
                mutex.release()
                while len(tx.queue) > 0:
                    idle = False
                    packet = tx.get()
                    print("schedule", addr, packet)
                    addr = packet.pop(0)
                    if addr == 255:
                        self.nat(packet)
                    elif addr < 50:
                        mutex.acquire()
                        self.computers[addr]['rx'].put(packet)
                        mutex.release()
                    else:
                        print("addr", addr)
            if idle:
                packet = self.nat_last
                if packet:
                    mutex.acquire()
                    self.computers[0]['rx'].put(packet)
                    mutex.release()
            

    def nat(self, packet):
        print("NAT", packet)
        self.nat_last = packet

    def run(self):
        for addr in self.computers:
            computer = self.computers[addr]['computer']
            computer.run(True)
        self.schedule()
        

switch = Switch()

for i in range(50):
    computer = IntcodeComputer()
    computer.load('day23.txt')
    switch.add_computer(computer, i)

switch.run()
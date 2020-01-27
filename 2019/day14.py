import re

test1 = '157 ORE => 5 NZVS\n165 ORE => 6 DCFZ\n44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL\n12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ\n179 ORE => 7 PSHF\n177 ORE => 5 HKGWZ\n7 DCFZ, 7 PSHF => 2 XJWVT\n165 ORE => 2 GPVTF\n3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'
test2 = '2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG\n17 NVRVD, 3 JNWZP => 8 VPVL\n53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL\n22 VJHF, 37 MNCFX => 5 FWMGM\n139 ORE => 4 NVRVD\n144 ORE => 7 JNWZP\n5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC\n5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV\n145 ORE => 6 MNCFX\n1 NVRVD => 8 CXFTF\n1 VJHF, 6 MNCFX => 4 RFSQX\n176 ORE => 6 VJHF'
test3 = '171 ORE => 8 CNZTR\n7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL\n114 ORE => 4 BHXH\n14 VRPVC => 6 BMBT\n6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL\n6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT\n15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW\n13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW\n5 BMBT => 4 WPTQ\n189 ORE => 9 KTJDG\n1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP\n12 VRPVC, 27 CNZTR => 2 XDBXC\n15 KTJDG, 12 BHXH => 5 XCVML\n3 BHXH, 2 VRPVC => 7 MZWV\n121 ORE => 7 VRPVC\n7 XCVML => 6 RJRHP\n5 BHXH, 4 VRPVC => 5 LTCX'

class Day14:
    def __init__(self, reactions):
        self.reactions = {}
        for reaction in reactions.split('\n'):
            name, materials = self.list_materials(reaction)
            self.reactions[name] = materials

    def list_materials(self, reaction):
        sides = reaction.split(' => ')
        input_chemicals = sides[0].split(', ')
        output_chemical = sides[1]
        materials = {}
        # input chemicals
        for chemical in input_chemicals:
            num, name = self.amount_chemical(chemical)
            materials[name] = num
        # output chemical
        num, name = self.amount_chemical(output_chemical)
        materials[name] = num

        return name, materials

    def amount_chemical(self, chemical):
        reg = r'(\d+)\s(\w+)'
        m = re.match(reg, chemical)
        num = int(m.group(1))
        name = m.group(2)
        return num, name

    def produce(self, chemicals):
        costs = {}

        def add_to_costs(name, num):
            if name in costs:
                costs[name] += num
            else:
                costs[name] = num

        for name in chemicals:
            num = chemicals[name]

            if name not in self.reactions or num < 0:
                add_to_costs(name, num)
                continue
            
            materials = self.reactions[name]
            multiple = int(num / materials[name])
            remainder = int(num % materials[name])

            if remainder > 0:
                multiple += 1
                remainder -= materials[name]
                add_to_costs(name, remainder)

            if multiple > 0:
                for material in materials:
                    if material != name:
                        add_to_costs(material, materials[material] * multiple)
        
        # Production end
        if costs == chemicals:
            return chemicals
        # Production continues
        return self.produce(costs)

    def part1(self):
        costs = self.produce({'FUEL': 1})
        # print(costs)
        return costs['ORE']

    def part2(self):
        ORE = 1000000000000
        limit = (1, ORE)

        while True:
            mid_fuel = int((limit[0] + limit[1]) / 2)
            if mid_fuel == limit[0]:
                return mid_fuel

            mid_costs = self.produce({'FUEL': mid_fuel})
            mid_ore = mid_costs['ORE']
            if mid_ore > ORE:
                limit = (limit[0], mid_fuel)
            elif mid_ore < ORE:
                limit = (mid_fuel, limit[1])
            else:
                return mid_fuel

def main():
    reactions = open('day14.txt').read().strip()
    day14 = Day14(reactions)
    print(f'Part 1: {day14.part1()}')
    print(f'Part 2: {day14.part2()}')

if __name__ == "__main__":
    main()

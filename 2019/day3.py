#!/usr/bin/env python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def make_segment(start, goes):
    direction = goes[:1]
    steps = int(goes[1:])

    if direction == 'R':
        return Segment(Point(start.x + 1, start.y), Point(start.x + steps, start.y))
    elif direction == 'L':
        return Segment(Point(start.x - 1, start.y), Point(start.x - steps, start.y))
    elif direction == 'U':
        return Segment(Point(start.x, start.y + 1), Point(start.x, start.y + steps))
    elif direction == 'D':
        return Segment(Point(start.x, start.y - 1), Point(start.x, start.y - steps))

def is_vertical(segment):
    return segment.start.x == segment.end.x

def is_horizontal(segment):
    return segment.start.y == segment.end.y

def is_cross(segment1, segment2):
    if (segment1.start.x - segment2.start.x) * (segment1.end.x - segment2.end.x) > 0:
        return False
    if (segment1.start.y - segment2.start.y) * (segment1.end.y - segment2.end.y) > 0:
        return False
    return True

def get_intersection(segment1, segment2):
    if is_cross(segment1, segment2):
        if is_vertical(segment1):
            return Point(segment1.start.x, segment2.end.y)
        else:
            return Point(segment2.start.x, segment1.end.y)

def get_distance(origin, point):
    return abs(point.x - origin.x) + abs(point.y - origin.y)

def is_on_segment(segment, point):
    if is_horizontal(segment):
        if (segment.start.x - point.x) * (segment.end.x - point.x) > 0:
            return False
        return segment.end.y == point.y
    else:
        if (segment.start.y - point.y) * (segment.end.y - point.y) > 0:
            return False
        return segment.start.x == point.x

def get_steps(path, point):
    steps = 0
    for segment in path:
        if is_on_segment(segment, point):
            if is_horizontal(segment):
                steps += abs(point.x - segment.start.x) + 1
            else:
                steps += abs(point.y - segment.start.y) + 1
            break
        else:
            if is_horizontal(segment):
                steps += abs(segment.end.x - segment.start.x) + 1
            else:
                steps += abs(segment.end.y - segment.start.y) + 1
    return steps

# test1 = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
# test2 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83']
# test3 = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

def main():
    with open('day3.txt') as f:
        wires = f.read().strip().split('\n')
        central = Point(0, 0)

        paths = []
        for wire in wires:
            start = central
            segments = []
            for goes in wire.split(','):
                segment = make_segment(start, goes)
                start = segment.end
                segments.append(segment)
            paths.append(segments)
        
        intersections = []
        for segment1 in paths[0]:
            for segment2 in paths[1]:
                point = get_intersection(segment1, segment2)
                if point:
                    # print(point)
                    intersections.append(point)

        # Part 1
        closest = min(intersections, key=lambda p: get_distance(central, p))
        print('Part 1:', get_distance(central, closest))

        # Part2
        totals = []
        for intersection in intersections:
            steps1 = get_steps(paths[0], intersection)
            steps2 = get_steps(paths[1], intersection)
            totals.append(steps1 + steps2)

        fewest = min(totals)
        print('Part 2:', fewest)

if __name__ == "__main__":
    main()

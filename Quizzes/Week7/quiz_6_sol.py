# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by Eric Martin for COMP9021


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, pt_1, pt_2):
        if pt_1.x == pt_2.x and pt_1.y == pt_2.y:
            print('Cannot create line')
            return
        self.pt_1 = pt_1
        self.pt_2 = pt_2
        if pt_2.x == pt_1.x:
            self.slope = float('inf')
            self.intersect = pt_1.x
        elif pt_2.y == pt_1.y:
            self.slope = 0
            self.intersect = pt_1.y
        else:
            self.slope = (pt_2.y - pt_1.y) / (pt_2.x - pt_1.x)
            self.intersect = pt_1.y - pt_1.x * self.slope

    def __eq__(self, other):
        return self.slope == other.slope and self.intersect == other.intersect


class Parallelogram:
    def __init__(self, line_1, line_2, line_3, line_4):
        slopes = {line_1.slope, line_2.slope, line_3.slope, line_4.slope}
        if len(slopes) != 2:
            print('Cannot create parallelogram')
            return
        self.sides = defaultdict(set)
        lines = line_1, line_2, line_3, line_4
        if len(lines) != 4:
            print('Cannot create parallelogram')
            return
        for line in lines:
            self.sides[line.slope].add(line.intersect)
        for slope in slopes:
            if len(self.sides[slope]) != 2:
                print('Cannot create parallelogram')
                return
            self.sides[slope] = sorted(self.sides[slope])

    def divides_into_two_parallelograms(self, line):
        if line.slope not in self.sides:
            return False
        return self.sides[line.slope][0] < line.intersect < self.sides[line.slope][1]
        
    

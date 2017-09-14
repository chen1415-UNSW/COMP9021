# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by *** for COMP9021


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Line:
    def __init__(self,pt_1,pt_2):
        self.pt_1 = Point(pt_1.x,pt_1.y)
        self.pt_2 = Point(pt_2.x,pt_2.y)
        if pt_1.x == pt_2.x and pt_1.y == pt_2.y:
            print('Cannot create line')
        elif pt_1.y == pt_2.y:
            self.k = 0
            self.b = pt_1.y
        elif pt_1.x == pt_2.x:
            self.k = None
            self.b = pt_1.x
        else:
            self.k = (pt_2.y-pt_1.y) / (pt_2.x-pt_1.x)
            self.b = pt_1.y - (self.k * pt_1.x)
class Parallelogram:
    def __init__(self,line_1,line_2,line_3,line_4):
        self.l1 = (line_1.k, line_1.b)
        self.l2 = (line_2.k, line_2.b)
        self.l3 = (line_3.k, line_3.b)
        self.l4 = (line_4.k, line_4.b)

        if (self.l1[0] == self.l2[0] and self.l1[1] != self.l2[1] and self.l3[0] == self.l4[0] and self.l3[1] != self.l4[1]):
            if(self.l1[1] > self.l2[1]):
                self.para_edge_1 = (self.l1[0], self.l1[1], self.l2[1])
            else:
                self.para_edge_1 = (self.l1[0], self.l2[1], self.l1[1])
            if(self.l3[1] > self.l4[1]):
                self.para_edge_2 = (self.l3[0], self.l3[1], self.l4[1])
            else:
                self.para_edge_2 = (self.l3[0], self.l4[1], self.l3[1])

        elif (self.l1[0] == self.l3[0] and self.l1[1] != self.l3[1] and self.l2[0] == self.l4[0] and self.l2[1] != self.l4[1]):
            if(self.l1[1] > self.l3[1]):
                self.para_edge_1 = (self.l1[0], self.l1[1], self.l3[1])
            else:
                self.para_edge_1 = (self.l1[0], self.l3[1], self.l1[1])
            if(self.l2[1] > self.l4[1]):
                self.para_edge_2 = (self.l2[0], self.l2[1], self.l4[1])
            else:
                self.para_edge_2 = (self.l2[0], self.l4[1], self.l2[1])

        elif (self.l1[0] == self.l4[0] and self.l1[1] != self.l4[1] and self.l2[0] == self.l3[0] and self.l2[1] != self.l3[1]):
            if(self.l1[1] > self.l4[1]):
                self.para_edge_1 = (self.l1[0], self.l1[1], self.l4[1])
            else:
                self.para_edge_1 = (self.l1[0], self.l4[1], self.l1[1])
            if(self.l2[1] > self.l3[1]):
                self.para_edge_2 = (self.l2[0], self.l2[1], self.l3[1])
            else:
                self.para_edge_2 = (self.l2[0], self.l3[1], self.l2[1])

        else:
            print('Cannot create parallelogram')

    def divides_into_two_parallelograms(self, line):
        if line.k == self.para_edge_1[0] and self.para_edge_1[2] < line.b < self.para_edge_1[1]:
            return True
        elif line.k == self.para_edge_2[0] and self.para_edge_2[2] < line.b < self.para_edge_2[1]:
            return True
        return False
        
    

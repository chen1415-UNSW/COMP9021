# Code for insertion into a priority queue
# implemented as a binary tree
#
# All rights reserved


from binary_tree import *
from math import log
from math import log2


class PriorityQueue(BinaryTree):
    def __init__(self, value = None):
        self.value = value
        self.left_num = 0
        self.right_num = 0
        if self.value is not None:
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        else:
            self.left_node = None
            self.right_node = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        elif self.left_num == 0 and self.right_num == 0:
            # insert into left node
            if value <= self.value:
                value,self.value = self.value,value
            self.left_node = PriorityQueue(value)
            self.left_num += 1
        elif self.left_num == 1 and self.right_num == 0:
            # insert into right
            if value <= self.value:
                value,self.value = self.value,value
            self.right_node = PriorityQueue(value)
            self.right_num += 1
        else:
            if value <= self.value:
                value,self.value = self.value,value
                
            left = (log2(self.left_num+1)*10)%10
            right = (log2(self.right_num+1)*10)%10

            if left > 0:
                # should insert into left node
                self.left_node.insert(value)
                self.left_num += 1
            elif right > 0:
                # should insert into right node
                self.right_node.insert(value)
                self.right_num += 1
            elif left == 0 and right == 0:
                if self.left_num > self.right_num:
                    # insert into right
                    self.right_node.insert(value)
                    self.right_num += 1
                else:
                    # start a new level of subnodes from left
                    self.left_node.insert(value)
                    self.left_num += 1
                

            
                
                    
            
        
        
        

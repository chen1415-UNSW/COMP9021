# Written by Eric Martin for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        length = len(self)
        if length < 2:
            return
        first_node = self.head
        current_node = self.head
        print ('first_node 123 ',current_node.value)
        print ('current_node 321',current_node.value)        
        for _ in range(length // 2 - 1):
            current_node = current_node.next_node
            print('12312313',current_node.value)
        self.head = current_node.next_node
        current_node = self.head
        for i in range(length // 2 - 1):
            next_node = first_node
            for _ in range(length // 2 - 2 - i):
                next_node = next_node.next_node
            next_next_node = current_node.next_node
            current_node.next_node = next_node.next_node
            next_node.next_node.next_node = next_next_node
            current_node = next_next_node
        last_node = current_node.next_node
        current_node.next_node = first_node
        first_node.next_node = last_node
    

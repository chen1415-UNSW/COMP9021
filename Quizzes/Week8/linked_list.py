# A Linked List abstract data type
#
# Written by Eric Martin for COMP9021


from copy import deepcopy


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None


class LinkedList:
    def memory(self):
        node=self.head
        while node:
            print(node)
            node=node.next_node
            
    def __init__(self, L = None, key = lambda x: x):
        '''Creates an empty list or a list built from a subscriptable object,
        the key of each value being by default the value itself.

        >>> LinkedList().print()
        >>> LinkedList([]).print()
        >>> LinkedList((0,)).print()
        0
        >>> LinkedList(range(4)).print()
        0, 1, 2, 3
        '''
        self.key = key
        if L is None:
            self.head = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node = node.next_node

    def print(self, separator = ', '):
        '''
        >>> LinkedList(range(4)).print(':')
        0:1:2:3
        >>> LinkedList(range(4)).print('--')
        0--1--2--3
        '''
        if not self.head:
            return
        node = self.head
        print(node.value, end = '')
        node = node.next_node
        while node:
            print(separator, node.value, sep = '', end = '')
            node = node.next_node
        print()

    def duplicate(self):
        '''
        >>> L = LinkedList(L = [[[1]], [[2]]])
        >>> L1 = L.duplicate()
        >>> L1.head.value[0][0] = 0
        >>> L1.print()
        [[0]], [[2]]
        >>> L.print()
        [[1]], [[2]]
        '''
        if not self.head:
            return None
        node = self.head
        node_copy = Node(deepcopy(node.value))
        LL = LinkedList(key = self.key)
        LL.head = node_copy
        node = node.next_node
        while node:
            node_copy.next_node = Node(deepcopy(node.value))
            node_copy = node_copy.next_node
            node = node.next_node
        return LL

    def __len__(self):
        '''
        >>> len(LinkedList())
        0
        >>> len(LinkedList([0]))
        1
        >>> len(LinkedList((0, 1)))
        2
        '''
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next_node
        return length

    def apply_function(self, function):
        '''
        >>> L = LinkedList(range(3))
        >>> L.apply_function(lambda x: 2 * x)
        >>> L.print()
        0, 2, 4
        '''
        node = self.head
        while node:
            node.value = function(node.value)
            node = node.next_node

    def is_sorted(self):
        '''
        >>> LinkedList().is_sorted()
        True
        >>> LinkedList([0]).is_sorted()
        True
        >>> LinkedList([0, 0]).is_sorted()
        True
        >>> LinkedList([0, 1]).is_sorted()
        True
        >>> LinkedList([1, 0]).is_sorted()
        False
        >>> LinkedList([0, 1, 2, 3]).is_sorted()
        True
        >>> LinkedList([0, 2, 1, 3]).is_sorted()
        False
        >>> LinkedList([0, 1, 2, 3], lambda x: -x).is_sorted()
        False
        >>> LinkedList([3, 2, 1, 0], lambda x: -x).is_sorted()
        True
        '''
        node = self.head
        while node and node.next_node:
            if self.key(node.value) > self.key(node.next_node.value):
                return False
            node = node.next_node
        return True

    def extend(self, LL):
        '''
        >>> L = LinkedList()
        >>> L.extend(LinkedList(range(2)))
        >>> L.print()
        0, 1
        >>> L = LinkedList(range(2))
        >>> L.extend(LinkedList())
        >>> L.print()
        0, 1
        >>> L = LinkedList(range(2))
        >>> L.extend(LinkedList(range(2, 4)))
        >>> L.print()
        0, 1, 2, 3
        '''
        if not self.head:
            self.head = LL.head
            return
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = LL.head

    def reverse(self):
        '''
        >>> L = LinkedList()
        >>> L.reverse()
        >>> L.print()
        >>> L = LinkedList([0])
        >>> L.reverse()
        >>> L.print()
        0
        >>> L = LinkedList([0, 1])
        >>> L.reverse()
        >>> L.print()
        1, 0
        >>> L = LinkedList(range(4))
        >>> L.reverse()
        >>> L.print()
        3, 2, 1, 0
        '''
        if not self.head or not self.head.next_node:
            return
        node = self.head
        while node.next_node.next_node:
            node = node.next_node
        last_node = node.next_node
        node.next_node = None
        self.reverse()
        last_node.next_node = self.head
        self.head = last_node

    def index_of_value(self, value):
        '''
        >>> L = LinkedList()
        >>> L.index_of_value(0)
        -1
        >>> L = LinkedList(range(10, 15))
        >>> L.index_of_value(10)
        0
        >>> L.index_of_value(14)
        4
        >>> L.index_of_value(12)
        2
        >>> L.index_of_value(16)
        -1
        '''
        index = 0
        node = self.head
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next_node
        return -1

    def value_at(self, index):
        '''
        >>> L = LinkedList()
        >>> L.value_at(0)
        >>> L = LinkedList(range(10, 15))
        >>> L = LinkedList(range(10, 15))
        >>> L.value_at(0)
        10
        >>> L.value_at(4)
        14
        >>> L.value_at(2)
        12
        >>> L.value_at(6)
        '''
        if index < 0:
            return None
        node = self.head
        while node and index:
            node = node.next_node
            index -= 1
        if node and index == 0:
            return node.value
        return None

    def prepend(self, LL):
        '''
        >>> L = LinkedList()
        >>> L.prepend(LinkedList(range(2)))
        >>> L.print()
        0, 1
        >>> L = LinkedList(range(2))
        >>> L.prepend(LinkedList())
        >>> L.print()
        0, 1
        >>> L = LinkedList(range(2))
        >>> L.prepend(LinkedList(range(2, 4)))
        >>> L.print()
        2, 3, 0, 1
        '''
        if not LL.head:
            return
        node = LL.head
        while node.next_node:
            node = node.next_node
        node.next_node = self.head
        self.head = LL.head
            
    def append(self, value):
        '''
        >>> L = LinkedList()
        >>> L.append(0)
        >>> L.print()
        0
        >>> L = LinkedList([0])
        >>> L.append(1)
        >>> L.print()
        0, 1
        >>> L = LinkedList(range(2))
        >>> L.append(2)
        >>> L.print()
        0, 1, 2
        '''
        if not self.head:
            self.head = Node(value)
            return
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = Node(value)

    def insert_value_at(self, value, index):
        '''
        >>> L = LinkedList()
        >>> L.insert_value_at(0, 3)
        >>> L.print()
        0
        >>> L = LinkedList([1])
        >>> L.insert_value_at(0, -1)
        >>> L.print()
        0, 1
        >>> L = LinkedList([1])
        >>> L.insert_value_at(0, 0)
        >>> L.print()
        0, 1
        >>> L = LinkedList([0])
        >>> L.insert_value_at(1, 1)
        >>> L.print()
        0, 1
        >>> L = LinkedList([0])
        >>> L.insert_value_at(1, 2)
        >>> L.print()
        0, 1
        >>> L = LinkedList([0, 2])
        >>> L.insert_value_at(1, 1)
        >>> L.print()
        0, 1, 2
        '''
        new_node = Node(value)
        if index <= 0:
            new_node.next_node = self.head
            self.head = new_node
            return
        if not self.head:
            self.head = new_node
        node = self.head
        while node.next_node and index > 1:
            node = node.next_node
            index -= 1
        next_node = node.next_node
        node.next_node= new_node
        new_node.next_node = next_node

    def insert_value_before(self, value_1, value_2):
        '''
        >>> L = LinkedList([1, 2])
        >>> L.insert_value_before(0, 1)
        True
        >>> L.print()
        0, 1, 2
        >>> L = LinkedList([0, 2])
        >>> L.insert_value_before(1, 2)
        True
        >>> L.print()
        0, 1, 2
        >>> L = LinkedList([0, 1])
        >>> L.insert_value_before(2, 3)
        False
        >>> L.print()
        0, 1
        '''
        if not self.head:
            return False
        if self.head.value == value_2:
            self.insert_value_at(value_1, 0)
            return True
        node = self.head
        while node.next_node and node.next_node.value != value_2:
            node = node.next_node
        if not node.next_node:
            return False
        new_node = Node(value_1)
        new_node.next_node = node.next_node
        node.next_node = new_node
        return True

    def insert_value_after(self, value_1, value_2):
        '''
        >>> L = LinkedList([0, 1])
        >>> L.insert_value_after(2, 1)
        True
        >>> L.print()
        0, 1, 2
        >>> L = LinkedList([0, 2])
        >>> L.insert_value_after(1, 0)
        True
        >>> L.print()
        0, 1, 2
        >>> L = LinkedList([0, 1])
        >>> L.insert_value_after(3, 2)
        False
        >>> L.print()
        0, 1
        '''
        if not self.head:
            return False
        node = self.head
        while node and node.value != value_2:
            node = node.next_node
        if not node:
            return False
        new_node = Node(value_1)
        new_node.next_node = node.next_node
        node.next_node = new_node
        return True

    def insert_sorted_value(self, value):
        '''
        >>> L = LinkedList()
        >>> L.insert_sorted_value(1)
        >>> L.print()
        1
        >>> L.insert_sorted_value(0)
        >>> L.print()
        0, 1
        >>> L.insert_sorted_value(2)
        >>> L.print()
        0, 1, 2
        >>> L.insert_sorted_value(1)
        >>> L.print()
        0, 1, 1, 2
        '''
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value <= self.key(self.head.value):
            new_node.next_node = self.head
            self.head = new_node
            return
        node = self.head
        while node.next_node and value > self.key(node.next_node.value):
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
            

    def delete_value(self, value):
        '''
        >>> L = LinkedList([0, 1, 1, 2])
        >>> L.delete_value(3)
        False
        >>> L.delete_value(1)
        True
        >>> L.print()
        0, 1, 2
        >>> L.delete_value(0)
        True
        >>> L.print()
        1, 2
        >>> L.delete_value(2)
        True
        >>> L.print()
        1
        >>> L.delete_value(1)
        True
        >>> L.print()
        >>> L.delete_value(0)
        False
        '''
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next_node
            return True
        node = self.head
        while node.next_node and node.next_node.value != value:
            node = node.next_node
        if node.next_node:
            node.next_node = node.next_node.next_node
            return True
        return False
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()    
    


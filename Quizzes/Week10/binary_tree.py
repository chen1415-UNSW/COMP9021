# A Binary Tree abstract data type
#
# Written by Eric Martin for COMP9021


class BinaryTree:
    def __init__(self, value = None):
        self.value = value
        if self.value is not None:
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
        else:
            self.left_node = None
            self.right_node = None

    def height(self):
        '''An empty tree is of height 0.
        The height of a nonempty tree is the length of its longest branch minus 1.
        So both an empty tree and a tree consisting of its root are of height 0.
        
        >>> t = BinaryTree()
        >>> t.height()
        0
        >>> t = BinaryTree(1)
        >>> t.height()
        0
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.height()
        3
        '''
        if self.value is None:
            return 0
        return max(self.left_node._height(), self.right_node._height())

    def _height(self):
        if self.value is None:
            return 0
        return max(self.left_node._height(), self.right_node._height()) + 1

    def size(self):
        '''Returns the number of nodes.
        
        >>> t = BinaryTree()
        >>> t.size()
        0
        >>> t = BinaryTree(1)
        >>> t.size()
        1
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.size()
        7
        '''
        if self.value is None:
            return 0
        return 1 + self.left_node.size() + self.right_node.size()

    def occurs_in_tree(self, value):
        '''
        >>> t = BinaryTree()
        >>> t.occurs_in_tree(0)
        False
        >>> t = BinaryTree(1)
        >>> t.occurs_in_tree(0)
        False
        >>> t.occurs_in_tree(1)
        True
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.occurs_in_tree(0)
        False
        >>> t.occurs_in_tree(1), t.occurs_in_tree(2), t.occurs_in_tree(3)
        (True, True, True)
        >>> t.occurs_in_tree(4), t.occurs_in_tree(5), t.occurs_in_tree(6)
        (True, True, True)
        '''
        if self.value is None:
            return False
        if self.value == value:
            return True
        return self.left_node.occurs_in_tree(value) or self.right_node.occurs_in_tree(value)

    def occurs_in_bst(self, value):
        '''
        >>> t = BinaryTree()
        >>> t.occurs_in_bst(0)
        False
        >>> t = BinaryTree(1)
        >>> t.occurs_in_bst(0)
        False
        >>> t.occurs_in_bst(1)
        True
        >>> t = BinaryTree(4); t_L = BinaryTree(2); t_LL = BinaryTree(1); t_LR = BinaryTree(3)
        >>> t_R = BinaryTree(5); t_RR = BinaryTree(7); t_RRL = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL; t_L.right_node = t_LR
        >>> t.right_node = t_R; t_R.right_node = t_RR; t_RR.left_node = t_RRL
        >>> t.occurs_in_bst(0)
        False
        >>> t.occurs_in_bst(1), t.occurs_in_bst(2), t.occurs_in_bst(3)
        (True, True, True)
        >>> t.occurs_in_bst(4), t.occurs_in_bst(5), t.occurs_in_bst(6), t.occurs_in_bst(7)
        (True, True, True, True)
        '''
        if self.value is None:
            return False
        if self.value == value:
            return True
        if value < self.value:
            return self.left_node.occurs_in_bst(value)
        return self.right_node.occurs_in_bst(value)

    def is_bst(self):
        '''
        >>> t = BinaryTree()
        >>> t.is_bst()
        True
        >>> t = BinaryTree(1)
        >>> t.is_bst()
        True
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.is_bst()
        False
        >>> t = BinaryTree(4); t_L = BinaryTree(2); t_LL = BinaryTree(1); t_LR = BinaryTree(3)
        >>> t_R = BinaryTree(5); t_RR = BinaryTree(7); t_RRL = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL; t_L.right_node = t_LR
        >>> t.right_node = t_R; t_R.right_node = t_RR; t_RR.left_node = t_RRL
        >>> t.is_bst()
        True
        '''
        if self.value is None:
            return True
        node = self.left_node
        if node.value is not None:
            while node.right_node.value is not None:
                node = node.right_node
            if self.value <= node.value:
                return False
        node = self.right_node
        if node.value:
            while node.left_node.value is not None:
                node = node.left_node
        if node.value is not None and self.value >= node.value:
            return False
        return self.left_node.is_bst() and self.right_node.is_bst()

    def insert_in_bst(self, value):
        '''
        >>> t = BinaryTree()
        >>> t.insert_in_bst(4)
        True
        >>> t.print_binary_tree()
        4
        >>> t.insert_in_bst(2)
        True
        >>> t.print_binary_tree()
              2
        4
        <BLANKLINE>
        >>> t.insert_in_bst(1)
        True
        >>> t.print_binary_tree()
                    1
              2
        <BLANKLINE>
        4
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> t.insert_in_bst(5)
        True
        >>> t.print_binary_tree()
                    1
              2
        <BLANKLINE>
        4
        <BLANKLINE>
              5
        <BLANKLINE>
        >>> t.insert_in_bst(3)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              5
        <BLANKLINE>
        >>> t.insert_in_bst(6)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              5
                    6
        >>> t.insert_in_bst(7)
        True
        >>> t.print_binary_tree()
        <BLANKLINE>
                    1
        <BLANKLINE>
              2
        <BLANKLINE>
                    3
        <BLANKLINE>
        4
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
              5
        <BLANKLINE>
                    6
                          7
        >>> t.insert_in_bst(1), t.insert_in_bst(2), t.insert_in_bst(3)
        (False, False, False)
        >>> t.insert_in_bst(4), t.insert_in_bst(5), t.insert_in_bst(6), t.insert_in_bst(7)
        (False, False, False, False)
        '''
        if self.value is None:
            self.value = value
            self.left_node = BinaryTree()
            self.right_node = BinaryTree()
            return True
        if self.value == value:
            return False
        if value < self.value:
            return self.left_node.insert_in_bst(value)
        return self.right_node.insert_in_bst(value)


    def delete_in_bst(self, value):
        '''
        >>> t = BinaryTree(4); t_L = BinaryTree(2); t_LL = BinaryTree(1); t_LR = BinaryTree(3)
        >>> t_R = BinaryTree(5); t_RR = BinaryTree(6); t_RRR = BinaryTree(7)
        >>> t.left_node = t_L; t_L.left_node = t_LL; t_L.right_node = t_LR
        >>> t.right_node = t_R; t_R.right_node = t_RR; t_RR.right_node = t_RRR
        >>> t.print_binary_tree()
        <BLANKLINE>
                    1
        <BLANKLINE>
              2
        <BLANKLINE>
                    3
        <BLANKLINE>
        4
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
              5
        <BLANKLINE>
                    6
                          7
        >>> t.delete_in_bst(0.5), t.delete_in_bst(1.5), t.delete_in_bst(2.5), t.delete_in_bst(3.5)
        (False, False, False, False)
        >>> t.delete_in_bst(4.5), t.delete_in_bst(5.5), t.delete_in_bst(6.5), t.delete_in_bst(7.5)
        (False, False, False, False)
        >>> t.delete_in_bst(5)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              6
                    7
        >>> t.delete_in_bst(7)
        True
        >>> t.print_binary_tree()
                    1
              2
                    3
        4
        <BLANKLINE>
              6
        <BLANKLINE>
        >>> t.delete_in_bst(2)
        True
        >>> t.print_binary_tree()
        <BLANKLINE>
              1
                    3
        4
        <BLANKLINE>
              6
        <BLANKLINE>
        >>> t.delete_in_bst(4)
        True
        >>> t.print_binary_tree()
              1
        3
              6
        >>> t.delete_in_bst(1)
        True
        >>> t.print_binary_tree()
        <BLANKLINE>
        3
              6
        >>> t.delete_in_bst(6)
        True
        >>> t.print_binary_tree()
        3
        >>> t.delete_in_bst(3)
        True
        >>> t.print_binary_tree()
        '''
        return self._delete_in_bst(value, self, '')

    def _delete_in_bst(self, value, parent, link):
        if self.value is None:
            return False
        if value < self.value:
            return self.left_node._delete_in_bst(value, self, 'L')
        if value > self.value:
            return self.right_node._delete_in_bst(value, self, 'R')
        if self.left_node.value is None:
            new_tree = self.right_node
        elif self.right_node.value is None:
            new_tree = self.left_node
        elif self.left_node.right_node.value is None:
            new_tree = self.left_node
            new_tree.right_node = self.right_node
        else:
            # Looking for the node containing the largest value
            # smaller than the value to delete.
            # That node will be node_2 and its parent node_1
            node_1 = self.left_node
            node_2 = node_1.right_node
            while node_2.right_node.value is not None:
                node_1 = node_2
                node_2 = node_2.right_node
            # The value stored in node_2 is meant to replace
            # the value to delete.
            # The replacement will only happen in case the value
            # being deleted is stored in the root; otherwise,
            # node_2 will be connected to the parent
            # of the node storing the value to delete.
            new_tree = node_2
            # Values larger than the value to delete
            # are larger than the replacing value.
            new_tree.right_node = self.right_node
            # Values between the value to delete
            # and the value stored in the parent P
            # of the node N storing that value 
            # are larger than the replacing value
            # and can be linked to P since N is going away.
            node_1.right_node = node_2.left_node
            # The replacing value is larger than
            # all other values stored on the left
            # of the node N containing the value to delete,
            # and can be linked to the node containing that value
            # since N is going.
            new_tree.left_node = self.left_node      
        if link == '':
            self.value = new_tree.value
            self.left_node = new_tree.left_node
            self.right_node = new_tree.right_node
        elif link == 'L':
            parent.left_node = new_tree
        else:
            parent.right_node = new_tree
        return True
    
    def print_binary_tree(self):
        '''
        >>> t = BinaryTree()
        >>> t.print_binary_tree()
        >>> t = BinaryTree(1)
        >>> t.print_binary_tree()
        1
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.print_binary_tree()
        <BLANKLINE>
                    1
        <BLANKLINE>
              2
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        3
        <BLANKLINE>
                    4
                          6
              5
        <BLANKLINE>
                    6
        <BLANKLINE>
        '''
        if self.value is None:
            return
        self._print_binary_tree(0, self.height())

    def _print_binary_tree(self, n, height):
        if n > height:
            return
        if self.value is None:
            print('\n' * (2 ** (height - n + 1) - 1), end = '')
        else:
            self.left_node._print_binary_tree(n + 1, height)
            print('      ' * n, self.value, sep = '')
            self.right_node._print_binary_tree(n + 1, height)
            
    def pre_order_traversal(self):
        '''
        >>> t = BinaryTree()
        >>> t.pre_order_traversal()
        []
        >>> t = BinaryTree(1)
        >>> t.pre_order_traversal()
        [1]
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.pre_order_traversal()
        [3, 2, 1, 5, 4, 6, 6]
        '''
        if self.value is None:
            return []
        values = [self.value]
        values.extend(self.left_node.pre_order_traversal())
        values.extend(self.right_node.pre_order_traversal())
        return values

    def in_order_traversal(self):
        '''
        >>> t = BinaryTree()
        >>> t.in_order_traversal()
        []
        >>> t = BinaryTree(1)
        >>> t.in_order_traversal()
        [1]
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.in_order_traversal()
        [1, 2, 3, 4, 6, 5, 6]
        '''
        if self.value is None:
            return []
        values = self.left_node.in_order_traversal()
        values.append(self.value)
        values.extend(self.right_node.in_order_traversal())
        return values

    def post_order_traversal(self):
        '''
        >>> t = BinaryTree()
        >>> t.post_order_traversal()
        []
        >>> t = BinaryTree(1)
        >>> t.post_order_traversal()
        [1]
        >>> t = BinaryTree(3); t_L = BinaryTree(2); t_LL = BinaryTree(1)
        >>> t_R = BinaryTree(5); t_RL = BinaryTree(4); t_RLR = BinaryTree(6); t_RR = BinaryTree(6)
        >>> t.left_node = t_L; t_L.left_node = t_LL
        >>> t.right_node = t_R; t_R.left_node = t_RL; t_RL.right_node = t_RLR ; t_R.right_node = t_RR
        >>> t.post_order_traversal()
        [1, 2, 6, 4, 6, 5, 3]
        '''
        if self.value is None:
            return []
        values = self.left_node.post_order_traversal()
        values.extend(self.right_node.post_order_traversal())
        values.append(self.value)
        return values

           
if __name__ == '__main__':
    import doctest
    doctest.testmod()    

    

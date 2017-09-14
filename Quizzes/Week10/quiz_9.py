# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree import *
from collections import defaultdict

def print_tree_growing_down(tree):

    level_total = tree.height()
    width_total = 2**(level_total+1) - 1
    matrix = defaultdict(list)
    
    # full fill the dict
    for i in range(level_total+1):

        matrix[i] = [' ' for j in range(width_total)]
    
    # start with root node
    first_cor = (width_total+1)//2 - 1 
    matrix[0][first_cor] = tree.value
    
    def print_tree_level(tree, last_level, direct, last_cor):
        nonlocal matrix
        nonlocal level_total 
        this_level = last_level + 1
        width = 2**(level_total-this_level+1)//2
        
        if direct == 'left':
            this_cor = last_cor - width
        if direct == 'right':
            this_cor = last_cor + width
        if tree.value is not None:    
            matrix[this_level][this_cor] = tree.value
            
        if tree.left_node:
            print_tree_level(tree.left_node, this_level, 'left', this_cor)
        if tree.right_node:
            print_tree_level(tree.right_node, this_level, 'right', this_cor)


    if tree.left_node:
        print_tree_level(tree.left_node, 0, 'left', first_cor)
    if tree.right_node:
        print_tree_level(tree.right_node, 0, 'right', first_cor)
                
    for i in range(level_total,-1,-1):
        for j in matrix[i]:
            print(j, end='')
        print()

    return True

# Possibly write additional function(s)
        

provided_input = input('Enter two integers, with the second one between 0 and 10: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
##    print('Insert: ',datum, 'Height: ',tree.height())
print_tree_growing_down(tree)
           

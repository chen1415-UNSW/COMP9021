# Implemements the insertion into a priority queue
# with smallest elements being of highest priority
# as a binary tree.
#
# Written by Eric Martin for COMP9021


import sys
from random import randint, seed
from priority_queue import *


provided_input = input('Enter two integers, the second one nonnegative and at most equal to 10: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except:
    print('Incorrect input, giving up.')
    sys.exit()
seed(seed_arg)
pq = PriorityQueue()
for i in range(nb_of_nodes - 1):
    pq.insert(randint(0, nb_of_nodes))
    pq.print_binary_tree()
    print()
pq.insert(randint(0, nb_of_nodes))
pq.print_binary_tree()



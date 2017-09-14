import sys
from random import seed, sample
from linked_list import *
from extended_linked_list_sol import ExtendedLinkedList

def collect_references(L, length):
    node = L.head
    references = set()
    for i in range(length):
        references.add(id(node))
        node = node.next_node
    return references
        

provided_input = input('Enter 2 positive integers: ')
try:
    provided_input = [int(arg) for arg in provided_input.split()]
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()
    
if len(provided_input) != 2:
    print('Incorrect input (not 2 arguments), giving up.')
    sys.exit()
for_seed, length = provided_input
if length < 0 or length > 100:
    print('Incorrect input (2nd integer not positive, giving up.')
    sys.exit()
seed(for_seed)

L = sample(list(range(length * 10)), length)

LL = ExtendedLinkedList(L)
LL.print()
print('----------------------------------------')
LL.rearrange()

    


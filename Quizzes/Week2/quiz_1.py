
import sys
from random import seed, randint


max_value = 19

try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('The generated list is:')
print('  ', L)
#start writing here

do_L = L
L = []
L.append(do_L.pop(0))

#print('L is: ', L)

for i in range(len(do_L)):
    j = len(do_L)
    if(j!=0):
        k = 0
        while (k < j and do_L[k] <= L[i]):
            k = k + 1
        if (k == j):
            L.append(do_L.pop(0))
        else:
            L.append(do_L.pop(k))
    else:
        break

#transformation done
print('The transformed list is:')
print('  ', L)

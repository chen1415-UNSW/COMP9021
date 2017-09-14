# Randomly fills an array of size 10x10 with 0s and 1s, and
# outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


def explore_board():
    knight_count = 0
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]:
                knight_count += 1
                bolt_crazy_horse(i, j)
    return knight_count


def bolt_crazy_horse(i, j):
    if not grid[i][j]:
        return
    grid[i][j] = 0
    if i - 2 >= 0:
        if j:
            bolt_crazy_horse(i - 2, j - 1)
        if j + 1 < dim:
            bolt_crazy_horse(i - 2, j + 1)
    if i + 2 < dim:
        if j:
            bolt_crazy_horse(i + 2, j - 1)
        if j + 1 < dim:
            bolt_crazy_horse(i + 2, j + 1)
    if j - 2 >= 0:
        if i:
            bolt_crazy_horse(i - 1, j - 2)
        if i + 1 < dim:
            bolt_crazy_horse(i + 1, j - 2)
    if j + 2 < dim:
        if i:
            bolt_crazy_horse(i - 1, j + 2)
        if i + 1 < dim:
            bolt_crazy_horse(i + 1, j + 2)


try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers: ').split()]
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[None] * dim for _ in range(dim)]
if n > 0:
    for i in range(dim):
        for j in range(dim):
            grid[i][j] = randrange(n) > 0
else:
    for i in range(dim):
        for j in range(dim):
            grid[i][j] = randrange(-n) == 0
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
else:
    print('At least {} chess'.format(nb_of_knights), end = ' ')
    print('knight has', end = ' ') if nb_of_knights == 1 else print('knights have', end = ' ')
    print('explored this board.')


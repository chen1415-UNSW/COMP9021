# Randomly fills an array of size 10x10 with 0s and 1s, and
# outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10

def display():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(grid[i][j], end = '')
        print()
    print()


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


def explore_board():
    nb_of_knights=0
    for i in range(dim):
        for j in range(dim):
           if(grid[i][j]==True):
               all_points_can_be_reached_by_one_knight(i,j,grid)
               nb_of_knights=nb_of_knights+1
           if(check(grid)==True):
               return nb_of_knights
           

def all_points_can_be_reached_by_one_knight (i,j,grid):
    L1=[]
    L1.append((i,j))

    for k in L1:
        if(k[0]-1>=0 and k[0]-1<=dim-1 and k[1]-2>=0 and k[1]-2<=dim-1 and grid[k[0]-1][k[1]-2]==True and (k[0]-1,k[1]-2) not in L1):
            L1.append((k[0]-1,k[1]-2))

        if(k[0]-2>=0 and k[0]-2<=dim-1 and k[1]-1>=0 and k[1]-1<=dim-1 and grid[k[0]-2][k[1]-1]==True and (k[0]-2,k[1]-1) not in L1):
            L1.append((k[0]-2,k[1]-1))

        if(k[0]+2>=0 and k[0]+2<=dim-1 and k[1]-1>=0 and k[1]-1<=dim-1 and grid[k[0]+2][k[1]-1]==True and (k[0]+2,k[1]-1) not in L1):
            L1.append((k[0]+2,k[1]-1))

        if(k[0]+1>=0 and k[0]+1<=dim-1 and k[1]-2>=0 and k[1]-2<=dim-1 and grid[k[0]+1][k[1]-2]==True and (k[0]+1,k[1]-2) not in L1):
            L1.append((k[0]+1,k[1]-2))

        if(k[0]-2>=0 and k[0]-2<=dim-1 and k[1]+1>=0 and k[1]+1<=dim-1 and grid[k[0]-2][k[1]+1]==True and (k[0]-2,k[1]+1) not in L1):
            L1.append((k[0]-2,k[1]+1))

        if(k[0]-1>=0 and k[0]-1<=dim-1 and k[1]+2>=0 and k[1]+2<=dim-1 and grid[k[0]-1][k[1]+2]==True and (k[0]-1,k[1]+2) not in L1):
            L1.append((k[0]-1,k[1]+2))

        if(k[0]+1>=0 and k[0]+1<=dim-1 and k[1]+2>=0 and k[1]+2<=dim-1 and grid[k[0]+1][k[1]+2]==True and (k[0]+1,k[1]+2) not in L1):
            L1.append((k[0]+1,k[1]+2))

        if(k[0]+2>=0 and k[0]+2<=dim-1 and k[1]+1>=0 and k[1]+1<=dim-1 and grid[k[0]+2][k[1]+1]==True and (k[0]+2,k[1]+1) not in L1):
            L1.append((k[0]+2,k[1]+1))

    
    for m in L1:
        grid[m[0]][m[1]]='visted'
    L1=sorted(L1)
    #print(L1)
    #print(grid)
    return grid

def check(grid):
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]==True:
                return False
    return True


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


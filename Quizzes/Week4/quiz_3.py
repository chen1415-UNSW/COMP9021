# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the number of blocks
# in the largest block construction, determined by rows of 1s that can be stacked
# on top of each other. 
#
# Written by *** and Eric Martin for COMP9021


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


def size_of_largest_construction():
    # #do_L=[[0]]*100]
    # for j in range(10):
    #     for i in range(10):
    #         #print(grid[i][j])
    #         if(grid[i][j]==0):
    #             break
    #         if(grid[i][j]!=0):
    #             grid[i][j]=1
    #             while (grid[i][j+1]!=0):
    #                 grid[i][j+1]=grid[i][j]+1
    #                 if(i>10 or j>10):
    #                     continue
    #     print(grid)

    # #print(do_L)
    L=[]
    for i in range(9,-1,-1):
        sum_c=0
        for j in range(10):
            if(grid[i][j]!=0):
                k=i
                while(grid[k][j]!=0 and k>=0):
                    sum_c=sum_c+1
                    k=k-1
                    if(grid[k][j]==0):
                        L.append(sum_c)
            if (grid[i][j]==0 or j>=9):
                L.append(sum_c)
                sum_c=0
            
    #print(L)
    return(max(L))

            #     m=i
            #     n=j
            #     print('m is: ',m)
            #     print('n is: ',n)
            #     while(grid[m][j]!=0):
            #         block=block+1
            #         m=m-1
            #         if(grid[i][n+1]==0):
            #             break
                    
                #n=n+1
                #while(grid[i][n]!=0):
                    #block=block+1
                    #n=n+1
                        #print('2',block)
                #print('3',block)
# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    pass
    # Replace pass above with your code

            
try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest block construction has {} blocks.'.format(size_of_largest_construction()))  

import sys
import math
import statistics
import copy

file_name = input('Which data file do you want to use? ')
try:
    file_object = open(file_name)
    L1=[]
    L2=[]
    Read=file_object.readlines()
    if (Read==[]):
        raise ValueError
        sys.exit()
    for line in Read:
        data = line.split()
        #print('Read is:',Read)
        #print('data is:',data)
        for i in range(len(data)):
            if i % 2 == 0:
                L1.append(int(data[i]))
                #print('L1 is: ',L1)
            else:
                L2.append(int(data[i]))
                #print('L2 is: ',L2)
except IOError:
    print('Incorrect input, giving up!')
    sys.exit()
except ValueError:
    print('Incorrect input, giving up!')
    sys.exit()
file_object.close()

#print('L1 is: ',L1)
#print('L2 is: ',L2)

max_mean_value = statistics.mean(L2)
#print('max_mean_value is: {:.2f}'.format(max_mean_value))
min_value= min(L2)
#print('max_mean_value is: {:.2f}'.format(min_value))


outcome=[]
for i in range(int(min_value),int(max_mean_value)):
    M=L2[:]
    for j in range(len(M)-1):
        if(M[j]<i):
            M[j+1] = M[j+1] - (i-M[j]) - (L1[j+1]-L1[j])
            # if the island smaller than i, ship form i+1
        if(M[j]>i):
            # if the island bigger than i, decide whether ship to the next island
            if( M[j]-i > (L1[j+1]-L1[j])):
                M[j+1]=M[j+1] + (M[j]-i) - ((L1[j+1]-L1[j]))
                # if the lose is less, ship
            if( M[j]-i <= (L1[j+1]-L1[j])):
                # if the lose is bigger, no ship
                pass
        if(M[j]==i):
            # if the lose equal to the deliver, no ship
            pass
    if(M[-1]>=i):
        outcome.append(i)
        # (i can be reached) add i into the result
    if(M[-1]<i):
        #-- i will bigger than the number finally
        # (i can not be reached)
        # break and print the last in outcome
        break

print('The maximum quantity of fish that each town can have is: {}.'.format(outcome[-1]))




        




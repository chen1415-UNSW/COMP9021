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

max_mean_value = int(statistics.mean(L2))
#print('max_mean_value is: {:.2f}'.format(max_mean_value))
min_value= int(min(L2))
#print('max_mean_value is: {:.2f}'.format(min_value))
ave = int((max_mean_value+min_value)/2)

def check(ave):
    outcome=[]
    M=L2[:]
    for j in range(len(M)-1):
        if(M[j]<ave):
            M[j+1] = M[j+1] - (ave-M[j]) - (L1[j+1]-L1[j])
            # if the island smaller than i, ship form i+1
        if(M[j]>ave):
            # if the island bigger than i, decide whether ship to the next island
            if( M[j]-ave > (L1[j+1]-L1[j])):
                M[j+1]=M[j+1] + (M[j]-ave) - ((L1[j+1]-L1[j]))
                # if the lose is less, ship
            if( M[j]-ave <= (L1[j+1]-L1[j])):
                # if the lose is bigger, no ship
                pass
        if(M[j]==ave):
            # if the lose equal to the deliver, no ship
            pass
    if(M[-1]>ave):
        # ave can be reached 
        # find a bigger one
        # wang shang zhao
        return 1
    if(M[-1]<ave):
        # ave cannot be reached
        # find a small one
        # wang xia zhao
        return 2
    if(M[-1]==ave):
        #print(ave)
        #print(result)
        return 0
        # right number

temp=0
while check(ave)!=0:
    if(check(ave)==2):
        max_mean_value=ave
        ave=(max_mean_value+min_value)/2
        if(abs(temp-ave)<0.01):
            #print('t ',temp)
            #print('ave ',ave)
            break
    if(check(ave)==1):
        min_value=ave
        ave=(max_mean_value+min_value)/2
    temp=ave


print('The maximum quantity of fish that each town can have is: {}.'.format(int(temp)))




        




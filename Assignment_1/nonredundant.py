import sys
import re
import time


file_name = input('Which data file do you want to use? ')
x,y,z=file_name.split()
print(x,y,z)
try:
    file = open(file_name)
    L1=[]
    L2=[]
    while True:
        Read=file.readline()
        if (Read==''):
            break
        Temp=re.split(r'[\n R , ()]',Read)
        #print(Temp)
        Temp_unit=[int(Temp[2]),int(Temp[3])]
        L2.append(Temp_unit)
        L1.append(int(Temp[2]))
        L1.append(int(Temp[3]))
    if(L2==[]):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up!')
    sys.exit()
except IOError:
    print('Incorrect input, giving up!')
    sys.exit()
file.close()

L1=list(set(L1))
#print('L1 is: ',L1)
#print('L2 is: ',L2)

t1=time.time()
temp=[]
for i in L2:
    for j in L2:
        if(i[1]==j[0] and [i[0],j[1]] not in temp):
            temp.append([i[0],j[1]])
#print('temp 1',temp)

len_L=[]
for k in range(len(L2)):
    #if (len(temp) in len_L):
        #break
    for i in temp:
        for j in L2:
            if(i==j):
                L2.remove(j)
            if(i!=j and i[1]==j[0]):
                if([i[0],j[1]] not in temp):
                    temp.append([i[0],j[1]])
                    #print('temp: ',temp)
                    #n=temp[-1]
                    #print(n)
                    
#print('temp 2',temp)
#print('length', len_L)
t2=time.time()
#print('time:', t2-t1)
print('The nonredundant facts are: ')
for i in L2:
    if(i not in temp):
        print('R({},{})'.format(i[0],i[1]))







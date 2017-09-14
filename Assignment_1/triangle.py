import sys
import re
import copy

file_name = input('Which data file do you want to use? ')
try:
    file = open(file_name)
    do_L=[]
    L=[]
    Read=file.readlines()
    #print(Read)
    if (Read==[]):
        raise ValueError
        sys.exit()
    for line in Read:
        data = line.split()
        do_L.append(data)
    for i in do_L:
        temp=[]
        for j in i:
            temp.append(int(j))
            #print(temp)
        L.append(temp)
except IOError:
    print('Incorrect input!')
    sys.exit()
except ValueError:
    print('Incorrect input, giving up!')
    sys.exit()
file.close()

record=[]
#print('len ',len(L))  --5
for i in range(len(L)-1,-1,-1):
    i_re=len(L)-i-1
    #print('i is: ',i)
    line=[]
    for j in range(0,len(L[i])):
        #print(i) #-- 4 3 2 1
        #print(L[i][j])
        global m
        m=i+1
        global n
        n=j+1
        if(i+1==len(L)):
            line.append([L[i][j],1,[L[i][j]]])
            #line.append(1)
            #line.append(L[i][j])
            #print('line 1 is : ', line)
        if( i+1<len(L) and record[i_re-1][j][0]==record[i_re-1][j+1][0]):
            sum_v=L[i][j]+record[i_re-1][j][0]
            line.append([sum_v,record[i_re-1][j][1]+record[i_re-1][j+1][1],copy.deepcopy(record[i_re-1][j][2])])
            line[j][2].append(L[i][j])
            #record_i_j.append(record_m_j[0]+1)
            #record_i_j.append(L[i][j])
            #record_i_j.extend(record_m_j[2:-1])
            #print('line 2 is: ',line)
        if( i+1<len(L) and record[i_re-1][j][0]<record[i_re-1][j+1][0]):
            sum_v=L[i][j]+record[i_re-1][j+1][0]
            line.append([sum_v,record[i_re-1][j+1][1],copy.deepcopy(record[i_re-1][j+1][2])])
            line[j][2].append(L[i][j])
            #record_i_j.append(sum_v)
            #record_i_j.append(record_m_n[0]+1)
            #record_i_j.append(L[i][j])
            #record_i_j.extend(record_m_n[2:-1])
            #print('line 3 is: ',line)
        if( i+1<len(L) and record[i_re-1][j][0]>record[i_re-1][j+1][0]):
            sum_v=L[i][j]+record[i_re-1][j][0]
            line.append([sum_v,record[i_re-1][j][1],copy.deepcopy(record[i_re-1][j][2])])
            line[j][2].append(L[i][j])
    record.append(copy.deepcopy(line))
    #print('line is: ',line)
    #print(record)

final=record[-1][-1][-1]
#print(final)
seq=[]
for i in range(len(final)-1,-1,-1):
    seq.append(final[i])

print('The largest sum is: ',record[-1][-1][0])
print('The number of paths yielding this sum is: ',record[-1][-1][1])
print('The leftmost path yielding this sum is: ',seq)
            

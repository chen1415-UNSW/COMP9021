import sys

file_name = input('Which data file do you want to use? ')
try:
    file_object = open(file_name)
    land=[]
    land=file_object.read().split()
except IOError:
    print('Incorrect input, giving up!')
    sys.exit()
if(land==[]):
    print('Incorrect input, giving up!')
    sys.exit()
file_object.close()

n = input('How many decilitres of water do you want to pour down? ')
try:
    val = int(n)
    if val<0:
        raise ValueError
except ValueError:
    print('please enter the right number!!')
    sys.exit()

L=[]
for i in land:
    if(isinstance(i,str)==True):
        L.append(int(i))
L_sort=[]
L_sort= sorted(L)
L_count=list(set(L))

height=[0]*(max(L_count)+1)
for i in L_sort:
    height[i]+=1
#print('L:',L)
#print('L_sort:',L_sort)
#print('L_count:',L_count)
#print('height:',height)


do_L=height[:]
#print('do_L:',do_L)
del do_L[-1]
#print('do_L:',do_L)
sum1=0
volume=0
volume_list=[0]*len(L_count)

def find_the_first_null_zero(arr):
    for i in arr:
        if i!=0:
            return(i)
loop=-1
for i in do_L:
    sum1=i+sum1
    volume=volume+sum1
    volume_list.append(volume)
    check=do_L.index(i)
    loop=loop+1
    #print('i is:',i)
    #print('loop is: ',loop)
    #print('check is: ',check)
    #print('volume:',volume)
    #print('volume_list:',volume_list)
    if(int(n)<volume and volume==height[1]):
        water=int(n)/volume+L_count[0]
        print('The water rises to {:.2f} centimetres.'.format(water))
        break
    if(int(n)==volume and height[loop+1]!=0 and i!=0):
        water=loop+find_the_first_null_zero(L_count)
        #print(i)
        #print(L_count[check])
        print('The water rises to {:.2f} centimetres.'.format(water))
        break
    if(int(n)==volume and height[loop+1]==0 and i!=0):
        water=int(n)-volume+loop+1
        print('The water rises to {:.2f} centimetres.'.format(water))
        break
    if(int(n)==volume and height[loop]==0):
        water=int(n)-volume+loop+1
        print('The water rises to {:.2f} centimetres.'.format(water))
        break
    if(int(n)==volume and i==0):
        #0 position not right use loop
        #print('volume:',volume)
        water=int(n)/(sum(height[:loop]))+find_the_first_null_zero(L_count)
        print('The water rises to {:.2f} centimetres.'.format(water))
        break
    if(int(n)<volume and volume!=height[1]):
        #print('sumheight:',sum(height[:(loop+1)]))
        water=(int(n)-volume_list[-2])/(sum(height[:loop+1])) + loop
        print('The water rises to {:.2f} centimetres.'.format(water))
        break
    
if(int(n)>volume_list[-1]):
    water=(int(n)-volume_list[-1])/(sum(height)) + L_count[-1]
    print('The water rises to {:.2f} centimetres.'.format(water))


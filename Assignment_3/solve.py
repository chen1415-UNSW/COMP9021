#written by hao chen 
#z5102446


import sys
import copy
import os
import re
import itertools
import collections

# begin with read the document
file_name = input('Which text file do you want to use for the puzzle? ')

try:
    with open(file_name,'r',encoding='utf_8') as file_object:
        content = file_object.read()
        # if content have no information, raise error
        if content == '':
            raise ValueError
        #replace '\n' to space
        content = content.replace('\n',' ')       
except IOError:
    print('Incorrect file.')
    sys.exit()
except ValueError:
    print('Incorrect input.')
    sys.exit()


# part 1: find all names
# we remove all punctuation mark, and find names behind Sir and Sirs
# then set so we get the correct one


text = copy.deepcopy(content)
# split the content with ?/!/. so we can see all sentences
content = re.split(r'[?!.]', content)
L_name = []
for line in content:
    # replace all punctuation marks, so we can see just words
    line = line.replace(',','')
    line = line.replace(':','')
    line = line.replace('"','')
    line = line.split()
    for i in range(len(line)):
        # the name is always behind Sir or Sirs, so we find them all
        # when it comes to Sirs, we keep looking until 'and'+1 word
        if line[i] == 'Sir':
            L_name.append(line[i+1])
        if line[i] == 'Sirs':
            x = i
            while True:
                x = x + 1
                if line[x] != 'and':
                    L_name.append(line[x])
                if line[x] == 'and':
                    L_name.append(line[x+1])
                    break

# we remove repeated names and sorted it by the string lower sequence
L_name = list(set(L_name))
L_name = sorted(L_name, key=str.lower)

#print names
print('The Sirs are: ',end='')
for i in L_name:
    print(i, end = ' ')
print()
# the part one of A3 ends


# part 2: 1. find how many people speak, list who they are and what they said 
#         2. list all possibile situation
#         3. create the object for all people, True for knight and False for Knave
#         4. go through the first situation to the last situation and record the mathed situation
#         5. about macth: the speaker has a status (T/F) and his/her claim has a status(T/F)
#                         if his/her status is same with his claim (T-T or F-F) then it mathed


# create the dictionary to store the speaker and his/her claim
info = collections.defaultdict(list)

# make sure no sentence ends with "
text = text.replace('."','".')
text = text.replace('!"','"!')
text = text.replace('?"','"?')
text = re.split(r'[?!.]', text)

for line in text:
    # remove all marks and replace " with d_q
    line = line.replace(',','')
    line = line.replace(':','')
    line = line.replace('"',' d_q ')
    line = line.split()
    # when find the first 'd_q' record its position and keep finding
    # until meet the next 'd_q' then record all information between two 'd_q'  --the claims
    # outside the 'd_q' find the Sir and record it in the dictionary --the speaker
    # remove all 'd_q' finally so i will not go beyound the index
    text_n = ''
    statement = []
    for i in range(len(line)-2):
        if line[i] == 'd_q':
            n_1 = i
            x = i
            while True:
                x = x + 1
                if line[x] != 'd_q':
                    text_n = text_n + ' '+ line[x]
                if line[x] == 'd_q' or x == len(line)-1 :
                    n_2 = x
                    statement.append(text_n)
                    for line_s in statement:
                        line_s = line_s.split()
                    for y in range(len(line)):
                        if y < n_1 or y > n_2:
                            if line[y] == 'Sir':
                                info[line[y+1]].append(line_s)
                    del line[n_1]
                    del line[n_2-1]
                    break
                    


# list all possible situation (from 0 knight to all knight)
assumption = {}

for i in range(0,len(L_name)+1):
    assumption[i] = []
    do_L = []
    # use the itertools to make the combinations
    iter = itertools.combinations(L_name,i)
    do_L.append(list(iter))
    for x in do_L:
        for y in x:
            assumption[i].append(y)


# create the True/False class
# value = 1 means state is True -- Knight
# value = 0 means state is False -- Knave
# set the default value = Flase

L_init = copy.deepcopy(L_name)

class status:
    def __init__(self,name,value = 0):
        self.name = name
        self.value = value
        self.state = False
        if value == 1:
            self.state = True
        if value == 0:
            self.state = False

# create the object
for i in range(len(L_init)):
    L_init[i] = status(L_name[i])

# build a dictionary to store all possible situations
# from 0 0 0 0 -> 1 1 1 1
# key is how many Knight in all people from 0 to all is Knight

L_all_situation = {}
#list all possible situation
siutuation = copy.deepcopy(assumption)
for key in siutuation:
    L_all_situation[key] = []
    for i in siutuation[key]:
        L_record = []
        for x in i:
            L_record.append(x)
        L_s = copy.deepcopy(L_init)
        for k in L_s:
            if k.name in L_record:
                k.state = True
        L_all_situation[key].append(L_s)


# count person number as nb_of_person
nb_of_person = len(L_name)



# create the list to see all combinations
# for example:    [(A,False),(B,False),(C,False),(D,False)]
# all the way to  [(A,True),(B,True),(C,True),(D,True)]   -- assume 4 people together

L_object = []

for i in L_name:
    l_object = status(i)
    L_object.append(l_object)

L_state = []
for key in L_all_situation:
    for i in L_all_situation[key]:
        temp = []
        for j in range(nb_of_person):
            temp.append((i[j].name,i[j].state))
        L_state.append(temp)



# based on the claimes, we can find all people who are mentioned
# if 'us' appear then L_n shoud be same as L_name
# else we replace the 'I' into names by the dictionary
def find_all_names(key,arr,L_name):
    L_n = []
    if 'us' in arr:
        return L_name
    if 'I' in arr:
        L_n.append(key)
    for i in range(len(arr)):
        if arr[i] == 'Sir':
            L_n.append(arr[i+1])
    return L_n

# then we judge whether the claim is Ture
# split into 8 type of sentences, and the each refers to Knight or Knave
# L_n is the list store the people who are mentioned by one speaker

def judge_claim(key, L_s, words, L_n):

    # Type 1, at least.
    # if one of the L_n is True/False then this claim is True
    if 'least' in words and 'Knight' in words:
        for i in L_s:
            for j in L_n:
                if i[0] == j and i[1] == True:
                    return True                   
    if 'least' in words and 'Knave' in words:
        for i in L_s:
            for j in L_n:
                if i[0] == j and i[1] == False:
                    return True

    # Type 2, at most.
    # if only one of the L_n is True/False then this claim is True
    # if no people in L_n is True/False then this claim is alse True
    if 'most' in words and 'Knight' in words:
        temp = []
        for i in L_s:
            for j in L_n:
                if i[0] == j and i[1] == True:
                    temp.append(j)
        if len(temp) <= 1:
            return True
    if 'most' in words and 'Knave' in words:
        temp = []
        for i in L_s:
            for j in L_n:
                if i[0] == j and i[1] == False:
                    temp.append(j)
        if len(temp) <= 1:
            return True
        
    # Type 3, exactly/Exactly.
    # if just one of the L_n is True/False then this claim is True      
    if 'exactly' in words or 'Exactly' in words:
        if 'Knight' in words:
            temp = []
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == True:
                        temp.append(j)
            if len(temp) == 1:
                return True
    if 'exactly' in words or 'Exactly' in words:
        if 'Knave' in words:
            temp = []
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == False:
                        temp.append(j)
            if len(temp) == 1:
                return True

    # Type 4, all/All.
    # if all people of the L_n is True/False then this claim is True 
    if 'All' in words or 'all' in words:
        if 'Knights' in words:
            temp = []
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == True:
                        temp.append(j)
            if len(temp) == nb_of_person:
                return True
    if 'All' in words or 'all' in words:
        if 'Knaves' in words:
            temp = []
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == False:
                        temp.append(j)
            if len(temp) == nb_of_person:
                return True

    # Type 5, I am.
    # in this situation L_n will only contion one name
    # if this name is True/False the this claim is True
    if words[0] == 'I' and words[1] == 'am':
        if 'Knight' in words:
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == True:
                        return True
    if words[0] == 'I' and words[1] == 'am':
        if 'Knave' in words:
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == False:
                        return True

    # Type 6, Sir XXX is a.
    # in this situation L_n will only contion one name
    # if this name is True/False the this claim is True
    if words[0] == 'Sir' and words[2] == 'is':
        if 'Knight' in words:
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == True:
                        return True
    if words[0] == 'Sir' and words[2] == 'is':
        if 'Knave' in words:
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == False:
                        return True

    # Type 7, Sir XXX or Sir XXX is a .
    # if just one person in L_n is True/False then this claim is True
    if 'or' in words and 'Knight' in words:
        temp = []
        for i in L_s:
            for j in L_n:
                if i[0] == j and i[1] == True:
                    temp.append(j)
        if len(temp) >= 1:
            return True
    if 'or' in words and 'Knave' in words:
        temp = []
        for i in L_s:
            for j in L_n:
                if i[0] == j and i[1] == False:
                    temp.append(j)
        if len(temp) >= 1:
            return True

    # Type 8, Sir XXX and Sir XXX are 
    # if all people in L_n is True/False then this claim is True
    if 'All' not in words and 'all' not in words and words[-2] == 'are':
        if 'Knights' in words:
            temp = []
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == True:
                        temp.append(j)
            if len(temp) == len(L_n):
                return True
    if 'All' not in words and 'all' not in words and words[-2] == 'are':
        if 'Knaves' in words:
            temp = []
            for i in L_s:
                for j in L_n:
                    if i[0] == j and i[1] == False:
                        temp.append(j)
            if len(temp) == len(L_n):
                return True
            
    # else this claim is False
    return False

# caculate the number of all claims, which is all a situation need to pass if this situation is satisfied
length_of_claims = 0
for key in info.keys():
    length_of_claims = length_of_claims + len(info[key])
        

 
L_result = []
L_n = []
# go through the first situation to the last situaion (from no kinghts to all knights)
for i in L_state:
    L_s = i
    temp_Result = []
    for key in info:
        for value in info[key]:
            words = value
            # find all mentioned name in one claim
            L_n = find_all_names(key,words,L_name)
            for j in L_s:
                # if one person is True and his/her claim is True, add this situion to the temp lsit
                if j[0] == key and judge_claim(key, L_s, words, L_n) == True and j[1] == True:
                    temp_Result.append(L_s)
                # if one person is True and his/her claim is False, add this situion to the temp lsit
                if j[0] == key and judge_claim(key, L_s, words, L_n) == False and j[1] == False:
                    temp_Result.append(L_s)
    # if one situation could be pass by every statement by every speaker  
    # then this situation could be one possible result
    # -- judge by how many times this situation passed
    if len(temp_Result)==length_of_claims:
        L_result.append(L_s)




#print the final result
if len(L_result) == 0:
    print('There is no solution.')
elif len(L_result)==1:
    print('There is a unique solution:')
    for i in L_result:
        for j in i:
            if j[1] == True:
                print('Sir {} is a Knight.'.format(j[0]))
            if j[1] == False:
                print('Sir {} is a Knave.'.format(j[0]))
else:
    print('There are {} solutions.'.format(len(L_result)))            


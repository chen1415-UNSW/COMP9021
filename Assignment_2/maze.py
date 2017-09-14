#written by hao chen 
#z5102446

import sys
import copy
import os

'''
command line input
'''

if __name__ == '__main__':
    commandline = sys.argv
    expect_commands = [['--file'],['-print','--file']]
    if not commandline[1:-1] in expect_commands:
        print('I expect -- file followed by filename and possibly -print as command line arguments.')
        sys.exit()
    else:
        if len(commandline) == 3:
            choice_of_print = False
        elif len(commandline) == 4:
            choice_of_print = True
        file_name = commandline[-1]



'''
read the documents
'''

#file_name = input('Which data file do you want to use? ')
#file_name = 'maze2.txt'
try:
    file_object = open(file_name)
    maze=[]
    temp=[]
    temp2=[]
    Read=file_object.readlines()
    if (Read==[]):
        raise ValueError
        sys.exit()
    for line in Read:
        data = line.split()
        temp.append(data)
    for i in temp:
        if i!=[]:
            temp2.append(i)
    for i in temp2:
        row = []
        if len(i)==1: # distinguish data
            for x in i:
                for y in x:
                    row.append(int(y))
        else:
            for k in i:
                row.append(int(k))
        maze.append(row)
        
# maze larger than 2*2
    if len(maze) < 2 or len(maze[0]) < 2:
        raise ValueError

# maze euqal length in every line
    for i in range(len(maze)-1):
        if len(maze[i]) != len(maze[i+1]):
            raise ValueError
        
# value constriant on the right line and the bottom line        
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if i == len(maze) - 1:
                if maze[i][j] == 2 or maze[i][j] == 3:
                    raise ValueError
            if j == len(maze[0]) - 1:
                if maze[i][j] == 1 or maze[i][j] == 3:
                    raise ValueError
                
# length and width constraint                
    if len(maze) > 31 or len(maze[0]) > 41:
            raise ValueError

except IOError:
    print('Incorrect input.')
    sys.exit()
except ValueError:
    print('Incorrect input.')
    sys.exit()
file_object.close()



'''
build the maze class
'''
class maze_details:
    def __init__(self,gate_value,walls_value, inner_points, areas, cul_de_sacs, paths):
        self.gate_value = gate_value
        self.walls_value = walls_value
        self.inner_points = inner_points
        self.areas = areas
        self.cul_de_sacs = cul_de_sacs
        self.paths = paths
maze_info = maze_details(0,0,0,0,0,0)




'''
find the gates
'''
class block:
    def __init__(self,value,right_value,down_value):
        self.value = value
        self.right_value = right_value
        self.down_value = down_value
        self.dir = [True,True,True,True]
        if self.value == 1:
            self.dir[0] = False
        elif self.value == 2:
            self.dir[2] = False
        elif self.value == 3:
            self.dir[0] = False
            self.dir[2] = False
        if self.right_value == 2 or self.right_value == 3:
            self.dir[3] = False
        if self.down_value == 1 or self.down_value == 3:
            self.dir[1] = False
        self.vis = False


points=copy.deepcopy(maze)


# create the object L_points
L_points=[]

for i in range(0,len(maze)-1):
    row = []
    for j in range(0,len(maze[0])-1):
        row.append(None)
    L_points.append(row)

length = len(maze) #= 6
width = len(maze[0]) #= 8

for i in range(len(L_points)):
    for j in range(len(L_points[0])):
        L_points[i][j] = block(maze[i][j],maze[i][j+1],maze[i+1][j])

def find_true(arr,n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == True and i!=n :
            count = count + 1
    return count

# find the gates under different situations
L_gates=[]
for i in range(len(L_points)):
    for j in range(len(L_points[0])):
        if length == 2 and width == 2:
            if i == 0 and j == 0:
                n = find_true(L_points[i][j].dir,None)
                for x in range(0,n):
                    L_gates.append((i,j))

        # just one line
        elif length == 2:
            if j == 0:
                n = find_true(L_points[i][j].dir, 3)
                for x in range(0,n):
                    L_gates.append((i,j))
                    
            if j > 0 and j < width-2:
                if L_points[i][j].dir[0]  == True or L_points[i][j].dir[1] == True:
                    L_gates.append((i,j))
                    if L_points[i][j].dir[0]  == True and L_points[i][j].dir[1] == True:
                        L_gates.append((i,j))
                        
            if j == width-2:
                n = find_true(L_points[i][j].dir, 2)
                for x in range(0,n):
                    L_gates.append((i,j))
        # just one column
        elif width == 2:
            if i == 0 :
                 n = find_true(L_points[i][j].dir, 1)
                 for x in range(0,n):
                     L_gates.append((i,j))
                     
            if i > 0 and i < length - 2:
                if L_points[i][j].dir[2] == True or L_points[i][j].dir[3] == True:
                    L_gates.append((i,j))
                    if L_points[i][j].dir[2] == True and L_points[i][j].dir[3] == True:
                        L_gates.append((i,j))
                        
            if i == length-2:
                n = find_true(L_points[i][j].dir, 0)
                for x in range(0,n):
                    L_gates.append((i,j))                        

       # normal situation
        else:
            if i == 0 and j == 0:
                if(L_points[i][j].dir[0] == True or L_points[i][j].dir[2] == True):
                    L_gates.append((i,j))
                    if(L_points[i][j].dir[0] == True and L_points[i][j].dir[2] == True):
                        L_gates.append((i,j))
                
            elif i == 0 and j < width-2:
                if(L_points[i][j].dir[0] == True):
                    L_gates.append((i,j))

            elif i == 0 and j == width-2:
                if(L_points[i][j].dir[0] == True or L_points[i][j].dir[3] == True):
                    L_gates.append((i,j))
                    if(L_points[i][j].dir[0] == True and L_points[i][j].dir[3] == True):
                        L_gates.append((i,j))
                
                
            elif i == length-2 and j == 0 :
                if(L_points[i][j].dir[1] == True or L_points[i][j].dir[2] == True):
                    L_gates.append((i,j))
                    if(L_points[i][j].dir[1] == True and L_points[i][j].dir[2] == True):
                        L_gates.append((i,j))
                        
            elif i == length-2 and j < width-2:
                if(L_points[i][j].dir[1] == True):
                    L_gates.append((i,j))
                    
            elif i == length-2 and j == width-2:
                if(L_points[i][j].dir[1] == True or L_points[i][j].dir[3] == True):
                    L_gates.append((i,j))
                    if(L_points[i][j].dir[1] == True and L_points[i][j].dir[3] == True):
                        L_gates.append((i,j))

            elif i < length-2 and j==0:
                if(L_points[i][j].dir[2] == True):
                    L_gates.append((i,j))
                    
            elif i < length-2 and j==width-2:
                if(L_points[i][j].dir[3] == True):
                    L_gates.append((i,j))
            
       
maze_info.gate_value = (len(L_gates))


'''
find the wall
'''
class wall_node:
    def __init__(self,up_value,down_value,left_value,right_value):
        self.dir = [0,0,0,0]
        self.up_value = up_value
        self.down_value = down_value
        self.left_value = left_value
        self.right_value = right_value
        if self.up_value == 1:
            self.dir[0] = 1
        if self.down_value == 1:
            self.dir[1] = 1
        if self.left_value == 1:
            self.dir[2] = 1
        if self.right_value == 1:
            self.dir[3] = 1
        self.vis = False
        self.draw_v_row = False
        self.draw_v_col = False


L_wall=[]

#create the walls objecte
for i in range(0,len(maze)):
    row = []
    for j in range(0,len(maze[0])):
        row.append(None)
    L_wall.append(row)

            
walls=copy.deepcopy(L_wall)
for i in range(0,len(walls)):
    for j in range(0,len(walls[0])):
        walls[i][j] = wall_node(0,0,0,0)


#row
length = len(maze) #= 2
width = len(maze[0]) #= 10
for i in range(0,len(maze)):
    for j in range(0,len(maze[0])):
        if maze[i][j] == 1:
            walls[i][j].dir[3] = 1
            walls[i][j+1].dir[2] = 1
        if maze[i][j] == 3:
            walls[i][j].dir[3] = 1
            walls[i][j+1].dir[2] = 1

#column
for i in range(0,len(maze)):
    for j in range(0,len(maze[0])):
        if maze[i][j] == 2:
            walls[i][j].dir[1] = 1
            walls[i+1][j].dir[0] = 1
        if maze[i][j] == 3:
            walls[i][j].dir[1] = 1
            walls[i+1][j].dir[0] = 1


# find the connected walls
def visit_wall(me,i,j):
    if 0 <= i <= length and 0 <= j <= width:
        if me.vis == False:
            me.vis = True
            if me.dir[0] == 1:
                visit_wall(walls[i-1][j],i-1,j)
                
            if me.dir[1] == 1:
                visit_wall(walls[i+1][j],i+1,j)
                
            if me.dir[2] == 1:
                visit_wall(walls[i][j-1],i,j-1)
                
            if me.dir[3] == 1:
                visit_wall(walls[i][j+1],i,j+1)

    
# caculate number of walls 
L_w=[]
nb_walls=0
for i in range(0,len(maze)):
    for j in range(0,len(maze[0])):
        if walls[i][j].vis == False and walls[i][j].dir != [0,0,0,0]:
            visit_wall(walls[i][j],i,j)
            nb_walls = nb_walls + 1
            
maze_info.walls_value = (nb_walls)


'''
find the innerpoints
'''

innerpoints = copy.deepcopy(maze)

class innerpoints:
    def __init__(self,value,right_value,down_value):
        self.value = value
        self.right_value = right_value
        self.down_value = down_value
        self.dir = [True,True,True,True]
        if self.value == 1:
            self.dir[0] = False
        elif self.value == 2:
            self.dir[2] = False
        elif self.value == 3:
            self.dir[0] = False
            self.dir[2] = False
        if self.right_value == 2 or self.right_value == 3:
            self.dir[3] = False
        if self.down_value == 1 or self.down_value == 3:
            self.dir[1] = False
        self.vis = False

L_inner=[]
for i in range(0,len(maze)-1):
    row = []
    for j in range(0,len(maze[0])-1):
        row.append(None)
    L_inner.append(row)
       
#create the innerpoints object
for i in range(len(L_inner)):
    for j in range(len(L_inner[0])):
        L_inner[i][j] = innerpoints(0,0,0)
        
for i in range(len(L_inner)):
    for j in range(len(L_inner[0])):
        L_inner[i][j] = innerpoints(maze[i][j],maze[i][j+1],maze[i+1][j])


# work recursively to visit points
def visit_innerpoints (i,j):
    if 0 <= i < length-1 and 0 <= j < width-1:
        if L_inner[i][j].vis == False:
            L_inner[i][j].vis = True
            if L_inner[i][j].dir[0] == True:
                visit_innerpoints(i-1,j)
                
            if L_inner[i][j].dir[1] == True:
                visit_innerpoints(i+1,j)
                
            if L_inner[i][j].dir[2] == True:
                visit_innerpoints(i,j-1)
                
            if L_inner[i][j].dir[3] == True:
                visit_innerpoints(i,j+1)


# caculate the accessible areas
nb_inner_points = 0
nb_areas = 0
for i in range(0,len(maze)):
    for j in range(0,len(maze[0])):
        if (i,j) in L_gates and L_inner[i][j].vis == False:
            visit_innerpoints(i,j)
            nb_areas = nb_areas + 1


#caculate the unvisited points
L_in = []
for i in range(len(L_inner)):
    for j in range(len(L_inner[0])):
        if L_inner[i][j].vis == False:
            nb_inner_points = nb_inner_points + 1
            L_in.append((i,j))


maze_info.inner_points = (nb_inner_points)
'''
find the accessible area
'''

maze_info.areas = (nb_areas)


'''
find sets of accessible cul-de-sacs that ara all connected
'''

class ways:
    def __init__(self,value,right_value,down_value):
        self.value = value
        self.right_value = right_value
        self.down_value = down_value
        self.dir = [True,True,True,True]
        if self.value == 1:
            self.dir[0] = False
        elif self.value == 2:
            self.dir[2] = False
        elif self.value == 3:
            self.dir[0] = False
            self.dir[2] = False
        if self.right_value == 2 or self.right_value == 3:
            self.dir[3] = False
        if self.down_value == 1 or self.down_value == 3:
            self.dir[1] = False
        self.vis = False
        self.row_vis = False
        self.col_vis = False


#create the way object
L_ways=[]
for i in range(0,len(maze)-1):
    row = []
    for j in range(0,len(maze[0])-1):
        row.append(None)
    L_ways.append(row)
       

for i in range(len(L_ways)):
    for j in range(len(L_ways[0])):
        L_ways[i][j] = ways(maze[i][j],maze[i][j+1],maze[i+1][j])



# create the value for each point, so the red X can be found
class node_cul:
    def __init__(self,value):
        self.value = value
        self.vis = False


#create the node_cul object
L_cul = copy.deepcopy(L_ways)
L_c = []
for i in range(0,len(L_cul)):
    for j in range(0,len(L_cul[0])):
        if (i,j) not in L_in:
            count = 0
            for y in L_ways[i][j].dir:
                if y == True:
                    count = count + 1
            L_cul[i][j] = node_cul(count)
            L_c.append((i,j))
        else:
            L_cul[i][j] = node_cul(0)


def check_value(L_cul):
    for i in range(0,len(L_cul)):
        for j in range(0,len(L_cul[0])):
            if L_cul[i][j].value == 1:
                return False
    return True


# find all points with value 1 and change it, until no 1 value exist
while check_value(L_cul) == False:
    for i in range(0,len(L_cul)):
        for j in range(0,len(L_cul[0])):
            if L_cul[i][j].value == 1:
                L_cul[i][j].value = -1

                if L_ways[i][j].dir[0] == True and (i-1,j) in L_c:
                    L_cul[i-1][j].value = L_cul[i-1][j].value - 1
                    
                    
                if L_ways[i][j].dir[1] == True and (i+1,j) in L_c:
                    L_cul[i+1][j].value = L_cul[i+1][j].value - 1
                    
                    
                if L_ways[i][j].dir[2] == True and (i,j-1) in L_c:
                    L_cul[i][j-1].value = L_cul[i][j-1].value - 1
                   
                    
                if L_ways[i][j].dir[3] == True and (i,j+1) in L_c:
                    L_cul[i][j+1].value = L_cul[i][j+1].value - 1
                    

#record all red X
L_cul_de = []            
def find_culs(i,j,L_cul_de):
    if 0 <= i < length-1 and 0 <= j < width-1 and L_cul[i][j].value <= -1:
        if L_cul[i][j].vis == False:
            L_cul[i][j].vis = True
            
            if L_ways[i][j].dir[0] == True:
                find_culs(i-1,j,L_cul_de)
                
            if L_ways[i][j].dir[1] == True:
                find_culs(i+1,j,L_cul_de)
                
            if L_ways[i][j].dir[2] == True:
                find_culs(i,j-1,L_cul_de)
                
            if L_ways[i][j].dir[3] == True:
                find_culs(i,j+1,L_cul_de)

            L_cul_de.append((i,j))



#caculate the cul-de-sals
nb_cul = 0
for i in range(0,len(L_cul)):
    for j in range(0,len(L_cul[0])):
        if L_cul[i][j].value < 0 and L_cul[i][j].vis == False:
            find_culs(i,j,L_cul_de)
            nb_cul = nb_cul + 1
            

      
maze_info.cul_de_sacs = (nb_cul)

'''
find the entry-exit path
'''

# record all points can be uniquely reached by the gates
L_reach = [] 
def find_path(i,j,L_reach):
    if 0 <= i < length-1 and 0 <= j < width-1 and L_cul[i][j].value == 2 and (i,j) not in L_cul_de:
        if L_cul[i][j].vis == False:
            L_cul[i][j].vis = True
            
            if L_ways[i][j].dir[0] == True:
                find_path(i-1,j,L_reach)
                
            if L_ways[i][j].dir[1] == True:
                find_path(i+1,j,L_reach)
                
            if L_ways[i][j].dir[2] == True:
                find_path(i,j-1,L_reach)
                
            if L_ways[i][j].dir[3] == True:
                find_path(i,j+1,L_reach)

            L_reach.append((i,j))



def check_diff(arr1,arr2):
    temp = []
    for i in arr1:
        if i in arr2:
            temp.append(i)
    if len(temp) == 1:
        return True
    else:
        return False
    
route = {}
# go start with the gate, try to see where can be reached
nb_path = 0
for i in range(0,len(L_ways)):
    for j in range(0,len(L_ways[0])):
        if (i,j) in L_gates and L_ways[i][j].vis == False:
            L_reach_gates = []
            find_path(i,j,L_reach_gates)
            L_gates.remove((i,j))
            if check_diff(L_reach_gates,L_gates) == True:
                nb_path = nb_path + 1
                route[(i,j)] = list(reversed(L_reach_gates))
            

maze_info.paths = (nb_path)            


'''
print the expected values 
'''
if choice_of_print == False:

    if maze_info.gate_value == 0:
        print('The maze has no gate.')
    elif maze_info.gate_value == 1:
        print('The maze has a single gate.')
    else:
        print('The maze has {} gates.'.format(maze_info.gate_value))



    if maze_info.walls_value == 0:
        print('The maze has no wall.')
    elif maze_info.walls_value == 1:
        print('The maze has a single wall that are all connected.')
    else:
        print('The maze has {} sets of walls that are all connected.'.format(maze_info.walls_value))



    if maze_info.inner_points == 0:
        print('The maze has no inaccessible inner point.')
    elif maze_info.inner_points == 1:
        print('The maze has a unique inaccessible inner point.')
    else:
        print('The maze has {} inaccessible inner points.'.format(maze_info.inner_points))


    if maze_info.areas == 0:
        print('The maze has no accessible area.')
    if maze_info.areas == 1:
        print('The maze has a unique accessible area.')
    else:
        print('The maze has {} accessible areas.'.format(maze_info.areas))


    if maze_info.cul_de_sacs == 0:
        print('The maze has no accessible cul-de-sac.')
    elif maze_info.cul_de_sacs == 1:
        print('The maze has accessible cul-de-sacs that are all connected.')
    else:
        print('The maze has {} sets of accessible cul-de-sacs that are all connected.'.format(maze_info.cul_de_sacs))


    if maze_info.paths == 0:
        print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
    elif maze_info.paths == 1:
        print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
    else:
        print('The maze has {} entry-exit paths with no intersections not to cul-de-sacs.'.format(maze_info.paths))



'''
draw the maze by latex
'''
if choice_of_print == True:



    file_name=file_name.split('.')[0]+'.tex'
    file=open(file_name,'w')
    file.write('\\documentclass[10pt]{article}\n')
    file.write('\\usepackage{tikz}\n')
    file.write('\\usetikzlibrary{shapes.misc}\n')
    file.write('\\usepackage[margin=0cm]{geometry}\n')
    file.write('\\pagestyle{empty}\n')
    file.write('\\tikzstyle{every node}=[cross out, draw, red]\n')
    file.write('\n')
    file.write('\\begin{document}\n')
    file.write('\n')
    file.write('\\vspace*{\\fill}\n')
    file.write('\\begin{center}\n')
    file.write('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n')

    file.write('% Walls\n')
   
    row = len(walls)
    col = len(walls[0])

    for i in range(row):
        for j in range(col):
            if walls[i][j].dir[3] == True and walls[i][j].draw_v_row == False:
                walls[i][j].draw_v_row = True
                n=j
                while True:
                    n= n + 1
                    walls[i][n].draw_v_row = True
                    if walls[i][n].dir[3] == False:
                        break
                file.write('    \\draw ('+str(j)+','+str(i)+')')
                file.write(' -- ('+str(n)+','+str(i)+');\n')


    for j in range(col):
        for i in range(row):
            if walls[i][j].dir[1] == True and walls[i][j].draw_v_col == False:
                walls[i][j].draw_v_col = True
                n=i
                while True:
                    n= n + 1
                    walls[n][j].draw_v_col = True
                    if walls[n][j].dir[1] == False:
                        break
                file.write('    \\draw ('+str(j)+','+str(i)+')')
                file.write(' -- ('+str(j)+','+str(n)+');\n')


    file.write('% Pillars\n')
    for i in range(row):
        for j in range(col):
            if walls[i][j].dir == [False,False,False,False]:
                file.write('    \\fill[green] ('+str(j)+','+str(i)+')')
                file.write(' circle(0.2);\n')


    file.write('% Inner points in accessible cul-de-sacs\n')
    for i in range(row):
        for j in range(col):
            if (i,j) in L_cul_de:
                file.write('    \\node at ('+str(j+0.5)+','+str(i+0.5)+')')
                file.write(' {};\n')

    file.write('% Entry-exit paths without intersections\n')

    # find all points need to be draw in yellow line

    L_route = []
    for x in route:
        for i in route[x]:
            L_route.append(i)
            
    L_route = sorted(L_route)


    '''
    ban red X ways in this points
    '''
    L_cul_de = sorted(L_cul_de)

    for i in L_route:
            
        if L_ways[i[0]][i[1]].dir[0] == True:
            if (i[0]-1,i[1]) in L_cul_de:
                L_ways[i[0]][i[1]].dir[0] = False
                
        if L_ways[i[0]][i[1]].dir[1] == True:
            if (i[0]+1,i[1]) in L_cul_de:
                 L_ways[i[0]][i[1]].dir[1] = False
                
        if L_ways[i[0]][i[1]].dir[2] == True:
            if (i[0],i[1]-1) in L_cul_de:
                L_ways[i[0]][i[1]].dir[2] = False
                
        if L_ways[i[0]][i[1]].dir[3] == True:
            if (i[0],i[1]+1) in L_cul_de:
                L_ways[i[0]][i[1]].dir[3] = False



   #distinguish the points in row and col

    L_route_row = []
    L_route_col = []
    for i in L_route:
        if L_ways[i[0]][i[1]].dir[2] == True or L_ways[i[0]][i[1]].dir[3] == True:
            L_route_row.append(i)
    for i in L_route:
        if L_ways[i[0]][i[1]].dir[0] == True or L_ways[i[0]][i[1]].dir[1] == True:
            L_route_col.append(i)


    # distinguish the row and the col by how many times that we have to draw
    L_drow_row = []
    L_drow_col = []



    L_route_col_new = []
    for i in L_route_col:
        L_route_col_new.append((i[1],i[0]))

    L_route_col_new = sorted(L_route_col_new)



    L_route_col = []
    for i in L_route_col_new:
        L_route_col.append((i[1],i[0]))
        

    do_L = []
    for i in L_route_row:
        if not i in do_L:
            do_L.append(i)
        if L_ways[i[0]][i[1]].dir[3] == True:
            if not (i[0],i[1]+1) in L_route_row:
                L_drow_row.append(do_L)
                do_L=[]
            else:
                do_L.append((i[0],i[1]+1))
        else:
            L_drow_row.append(do_L)
            do_L=[]

    do_L2 = []
    for i in L_route_col:
        if not i in do_L2:
            do_L2.append(i)
        if L_ways[i[0]][i[1]].dir[1] == True:
            if not (i[0]+1,i[1]) in L_route_col:
                L_drow_col.append(do_L2)
                do_L2=[]
            else:
                do_L2.append((i[0]+1,i[1]))
        else:
            L_drow_col.append(do_L2)
            do_L2=[]



    #drow the yellow line in row 
    for i in L_drow_row:

        if L_ways[i[0][0]][i[0][1]].dir[2] == True:
            file.write('    \\draw[dashed, yellow] ('+str(i[0][1]-0.5)+','+str(i[0][0]+0.5)+')')
        else:
            file.write('    \\draw[dashed, yellow] ('+str(i[0][1]+0.5)+','+str(i[0][0]+0.5)+')')
        if L_ways[i[-1][0]][i[-1][1]].dir[3] == True:
            file.write(' -- ('+str(i[-1][1]+1.5)+','+str(i[-1][0]+0.5)+');\n')
        else:
            file.write(' -- ('+str(i[-1][1]+0.5)+','+str(i[-1][0]+0.5)+');\n')

    #drow the yellow line in col 
    for i in L_drow_col:

        if L_ways[i[0][0]][i[0][1]].dir[0] == True:
            file.write('    \\draw[dashed, yellow] ('+str(i[0][1]+0.5)+','+str(i[0][0]-0.5)+')')
        else:
            file.write('    \\draw[dashed, yellow] ('+str(i[0][1]+0.5)+','+str(i[0][0]+0.5)+')')
        if L_ways[i[-1][0]][i[-1][1]].dir[1] == True:
            file.write(' -- ('+str(i[-1][1]+0.5)+','+str(i[-1][0]+1.5)+');\n')
        else:
            file.write(' -- ('+str(i[-1][1]+0.5)+','+str(i[-1][0]+0.5)+');\n')        



    #end 
    file.write('\\end{tikzpicture}\n')
    file.write('\\end{center}\n')
    file.write('\\vspace*{\\fill}\n')
    file.write('\n')
    file.write('\\end{document}\n')

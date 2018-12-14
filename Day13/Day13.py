import numpy as np
import pandas as pd
import itertools as it
from collections import defaultdict,Counter,deque
import copy

filename = 'input.txt'
with open(filename) as f:
    content = f.read().splitlines()
    
grid = np.chararray((len(content[0]),len(content)))    
for y in range(len(content)):
    for x in range(len(content[0])):
        grid[y,x] = content[y][x]
        
right = np.asarray(np.where(grid == '>')).T
left = np.asarray(np.where(grid == '<')).T
up = np.asarray(np.where(grid == '^')).T
down = np.asarray(np.where(grid == 'v')).T

##Make List of all Carts
carts = [list('>')+list(i)+['L'] for i in right] + [list('<')+list(i)+['L'] for i in left] + [list('^')+list(i)+['L'] for i in up] + [list('v')+list(i)+['L'] for i in down]
carts.sort(key = lambda x: (x[1],x[2]))


base_grid = copy.deepcopy(grid)
for i in up:
    base_grid[i[0],i[1]] = '|'
for i in down:
    base_grid[i[0],i[1]] = '|'
for i in left:
    base_grid[i[0],i[1]] = '-'
for i in right:
    base_grid[i[0],i[1]] = '-'
    
           
#no_crash = True
#while no_crash: 
while len(carts) >1:
    carts.sort(key = lambda x: (x[1],x[2]))
    for c in carts:
        if c[0] == '>':
            if base_grid[c[1],c[2]+1] == '-':
                c[2] +=1
            elif base_grid[c[1],c[2]+1] == '\\':
                c[2] +=1
                c[0] = 'v'
            elif base_grid[c[1],c[2]+1] == '/':
                c[2] +=1
                c[0] = '^'
            elif base_grid[c[1],c[2]+1] == '+':
                if c[3] == 'L':
                    c[3] = 'S'
                    c[2] +=1
                    c[0] = '^'
                elif c[3] == 'S':
                    c[3] = 'R'
                    c[2] +=1
                    c[0] = '>'
                else:
                    c[3] = 'L'
                    c[2] +=1
                    c[0] = 'v'

        elif c[0] == '<':
            if base_grid[c[1],c[2]-1] == '-':
                c[2] -=1
            elif base_grid[c[1],c[2]-1] == '\\':
                c[2] -=1
                c[0] = '^'
            elif base_grid[c[1],c[2]-1] == '/':
                c[2] -=1
                c[0] = 'v'
            elif base_grid[c[1],c[2]-1] == '+':
                if c[3] == 'L':
                    c[3] = 'S'
                    c[2] -=1
                    c[0] = 'v'
                elif c[3] == 'S':
                    c[3] = 'R'
                    c[2] -=1
                    c[0] = '<'
                else:
                    c[3] = 'L'
                    c[2] -=1
                    c[0] = '^'
                    
        elif c[0] == '^':
            if base_grid[c[1]-1,c[2]] == '|':
                c[1] -=1
            elif base_grid[c[1]-1,c[2]] == '\\':
                c[1] -=1
                c[0] = '<'
            elif base_grid[c[1]-1,c[2]] == '/':
                c[1] -=1
                c[0] = '>'
            elif base_grid[c[1]-1,c[2]] == '+':
                if c[3] == 'L':
                    c[3] = 'S'
                    c[1] -=1
                    c[0] = '<'
                elif c[3] == 'S':
                    c[3] = 'R'
                    c[1] -=1
                    c[0] = '^'
                else:
                    c[3] = 'L'
                    c[1] -=1
                    c[0] = '>'
                    
        elif c[0] == 'v':
            if base_grid[c[1]+1,c[2]] == '|':
                c[1] +=1
            elif base_grid[c[1]+1,c[2]] == '\\':
                c[1] +=1
                c[0] = '>'
            elif base_grid[c[1]+1,c[2]] == '/':
                c[1] +=1
                c[0] = '<'
            elif base_grid[c[1]+1,c[2]] == '+':
                if c[3] == 'L':
                    c[3] = 'S'
                    c[1] +=1
                    c[0] = '>'
                elif c[3] == 'S':
                    c[3] = 'R'
                    c[1] +=1
                    c[0] = 'v'
                else:
                    c[3] = 'L'
                    c[1] +=1
                    c[0] = '<'

        #Check for crashes
        if len([(x[1],x[2]) for x in carts]) != len(set([(x[1],x[2]) for x in carts])):
    #            no_crash = False
    #            break
    
    ## Part 2
            dupes = [item for item, count in Counter([(x[1],x[2]) for x in carts]).items() if count > 1]
            carts = [x for x in carts if (x[1],x[2]) not in dupes]
print(carts)
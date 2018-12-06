import numpy as np
import pandas as pd
filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]
points = content

def mdist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def make_grid(points):
    all_x = []
    all_y = []
    for i in range(len(points)):
        all_x.append(int(points[i].split(', ')[0]))
        all_y.append(int(points[i].split(', ')[1]))
    
    the_grid = np.zeros(( max(all_x)+1 , max(all_y)+1 ))
    
    for i in range(len(points)):
        the_grid[all_x[i],all_y[i]] = i
        
    for j in range(max(all_x)+1):
        for k in range(max(all_y)+1):
            min_dist = 99999999
            for l,m in zip(all_x,all_y):
                if mdist(j,k,l,m) == min_dist:
                    new_point = -1
                elif mdist(j,k,l,m) < min_dist:
                    min_dist = int(mdist(j,k,l,m))
                    new_point = int(the_grid[l,m])
            the_grid[j,k] = new_point
    
    return the_grid    

#go along edges and remove all edge points, which are the infinite area points
def denote_infinite_points(a_grid):
    infinite_numbers = []
    for x in [0,a_grid.shape[0]-1]:
        for y in range(0,a_grid.shape[1]-1):
            infinite_numbers.append(a_grid[x,y])
            
    for x in range(0,a_grid.shape[0]-1):
        for y in [0,a_grid.shape[1]-1]:
            infinite_numbers.append(a_grid[x,y])     
    
    
    return list(set(infinite_numbers))
    
from collections import Counter        
def find_area(a_grid):
    c = Counter()
    for i in a_grid.flatten():
        c.update([i])
    return c

def remove_infinites(a_counter,a_list):
    for number in list(a_counter):
        if number in a_list:
            del a_counter[number]
    return a_counter
        
        
x = make_grid(content)
infinites = denote_infinite_points(x)
area = find_area(x)
part1 = remove_infinites(area,infinites).most_common(1)

print(part1)


## Part 2

def make_grid2(points):
    safe = 0
    all_x = []
    all_y = []
    for i in range(len(points)):
        all_x.append(int(points[i].split(', ')[0]))
        all_y.append(int(points[i].split(', ')[1]))
    
    the_grid = np.zeros(( max(all_x)+1 , max(all_y)+1 ))
    
    for i in range(len(points)):
        the_grid[all_x[i],all_y[i]] = i

    for j in range(max(all_x)+1):
        for k in range(max(all_y)+1):
            dist = 0
            for l,m in zip(all_x,all_y):
                dist += mdist(j,k,l,m)
            if dist <10000:
                safe +=1
    
    return safe

y = make_grid2(content)
print(y)



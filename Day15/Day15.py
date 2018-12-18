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
        
elves = np.asarray(np.where(grid == 'E')).T
goblins = np.asarray(np.where(grid == 'G')).T

##Make List of all Peoples
people = [list('E')+list(i)+[200,3] for i in elves] + [list('G') + list(i) +[200,3] for i in goblins] 
people.sort(key = lambda x: (x[1],x[2]))

#base_grid = copy.deepcopy(grid)
#for i in people:
#    base_grid[i[1],i[2]] = '.'

import networkx as nx
def make_graph(person,enemy):
    base_grid = copy.deepcopy(grid)
    base_grid[person[1],person[2]] = '.'
    base_grid[enemy[1],enemy[2]] = '.'
    G = nx.Graph()
    for g in range(len(base_grid)):
        for h in range(len(base_grid[0])):
            if base_grid[g][h] == '.':
                if base_grid[g+1][h] == '.':
                    G.add_edge((g,h),(g+1,h))
                if base_grid[g-1][h] == '.':
                    G.add_edge((g,h),(g-1,h))
                if base_grid[g][h+1] == '.':
                    G.add_edge((g,h),(g,h+1))
                if base_grid[g][h-1] == '.':
                    G.add_edge((g,h),(g,h-1))
    return G             
    
def find_path_length(person,enemy):
    graph = make_graph(person,enemy)
    try:
        return nx.shortest_path_length(graph,(person[1],person[2]), (enemy[1],enemy[2]))
    except:
        return 999

def find_closest_enemy(person,people):    
    enemies = [x for x in people if x[0] != person[0]]
    
    y = copy.deepcopy(enemies)
    for x in y:
#        try:
        x.append(find_path_length(person,x))
#        except:
#            x.append(999)
#            continue
    
    y.sort(key = lambda x: (x[5],x[1],x[2]))
    return y[0]

def determine_step_to_enemy(person,enemy):
    graph = make_graph(person,enemy)
    if find_path_length(person,enemy) == 1:
        return [person[1],person[2]]
    else:
        try:
            x = [p for p in nx.all_shortest_paths(graph, source=(person[1],person[2]), target=(enemy[1],enemy[2]))]        
            options = []
            for a in x:
                options.append(a[1])
        
            options.sort(key = lambda x: (x[0],x[1]))
            
            #First in reading order is the lowest..
            new_position = options[0]
            return new_position
        except:
            return [person[1],person[2]]

def attack_target(person,people):
    enemies = [x for x in people if x[0] != person[0]]
    
    y = copy.deepcopy(enemies)
    for x in y:
#        try:
        x.append(find_path_length(person,x))
#        except:
#            x.append(999)
#            continue
    
    enemies_within_reach = [x for x in y if x[5] == 1]
    enemies_within_reach.sort(key = lambda x: (x[5],x[3],x[1],x[2]))
    
    if len(enemies_within_reach) > 0:
        for p in people:
            if p[1:3] == enemies_within_reach[0][1:3]:
                p[3] -= person[4]
                break

    return people
    
def purge_dead(people):
    people = [x for x in people if x[3] > 0]
    return people


def check_done(people):
    if len(set([x[0] for x in people])) == 1:
        return True
    else:
        return False

import sys
i = 0
while True:
    people.sort(key = lambda x: (x[1],x[2]))
    for p in people:
        if p[3] <=0:
            continue
        else:
            try:
                enemy = find_closest_enemy(p,[x for x in people if x[3] > 0])
            except IndexError:
                continue
            step = determine_step_to_enemy(p,enemy)
            old_place = copy.deepcopy(p[1:3])
            if step != old_place:
                p[1:3] = list(step)
                grid[p[1],p[2]] = p[0]
                grid[old_place[0],old_place[1]] = '.'
            people = attack_target(p,[x for x in people if x[3] > 0])
            
            for j in [x for x in people if x[3] <= 0]:
                grid[j[1],j[2]] = '.'
                
                        
    #        print(people)
    people = [x for x in people if x[3] > 0]
    if check_done(people):
        break


    i+=1
    print(i)
    print('remaining: ' + str(len(people)))

    
print(i * sum([x[3] for x in people]))

## Part 2 

elf_power = 4
z = 0
done = False
while not done:
    people = [list('E')+list(i)+[200,elf_power+z] for i in elves] + [list('G') + list(i) +[200,3] for i in goblins] 
    people.sort(key = lambda x: (x[1],x[2]))
    while len(elves) == len([x for x in people if x[0] == 'E']):
        people.sort(key = lambda x: (x[1],x[2]))
        for p in people:
            if p[3] <=0:
                continue
            else:
                try:
                    enemy = find_closest_enemy(p,[x for x in people if x[3] > 0])
                except IndexError:
                    continue
                step = determine_step_to_enemy(p,enemy)
                old_place = copy.deepcopy(p[1:3])
                if step != old_place:
                    p[1:3] = list(step)
                    grid[p[1],p[2]] = p[0]
                    grid[old_place[0],old_place[1]] = '.'
                people = attack_target(p,[x for x in people if x[3] > 0])
                
                for j in [x for x in people if x[3] <= 0]:
                    grid[j[1],j[2]] = '.'
                    
                            
        #        print(people)
        people = [x for x in people if x[3] > 0]
        if check_done(people):
            done = True
    z +=1

print(i * sum([x[3] for x in people]))
    
#    print(i)
#    print('remaining: ' + str(len(people)))
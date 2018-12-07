import numpy as np
import pandas as pd
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

def make_dict():
    reqs = {}
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        reqs[i] = ''  
    for j in content:
        reqs[j.split(' ')[7]] += j.split(' ')[1]
    return reqs

reqs = make_dict()
stack = []
remaining = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while remaining != '':
    for k in remaining:
        if reqs[k] == '':
            stack.append(k)
            remaining = remaining.replace(k,'')
            for l in remaining:
                reqs[l] = reqs[l].replace(k,'')
            break

print(''.join(stack))

## Part 2

reqs = make_dict()
stack = []
remaining = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
time= 0

def str_to_time(achar):
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(achar)+61

workers = []
workers_letters = []

while remaining != '' or workers != []:
    for k in remaining:
        if reqs[k] == '' and len(workers) < 5:
            workers.append(str_to_time(k))
            workers_letters.append(k)
            remaining = remaining.replace(k,'')
    
    workers = [x-1 for x in workers]    
    workers_to_delete = []
    for c in range(len(workers)):
        if workers[c] == 0:
            workers_to_delete = [c] + workers_to_delete
    
    for d in workers_to_delete:
        temp = workers_letters[d]
        del workers[d]
        del workers_letters[d]
        for l in remaining:
            reqs[l] = reqs[l].replace(temp,'')
        continue
    
    time +=1

print(time)
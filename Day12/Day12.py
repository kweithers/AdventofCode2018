import numpy as np
import pandas as pd
import itertools as it
from collections import defaultdict,Counter,deque
import copy

filename = 'input.txt'
with open(filename) as f:
    content = f.read().splitlines()
 
content = [x.replace('#','1').replace('.','0') for x in content ]
s0 = ''.join(c for c in content[0] if c in ['1','0'])
       
rules = {}
for i in range(2,len(content)):
    rules[content[i][0:5]] = content[i][-1]
    
d0 = defaultdict(lambda:'0')
for i in range(len(s0)):
    d0[i] = s0[i] 
    
def apply_rule(a_dict,i):
    the_str = a_dict[i-2]+a_dict[i-1]+a_dict[i]+a_dict[i+1]+a_dict[i+2]
    new_char = rules[the_str]
    return new_char

def make_next_generation(d0):
    d1 = copy.deepcopy(d0)
    #walk back
    walk = 0
    while d1[walk-2]+d1[walk-1]+d1[walk]+d1[walk+1]+d1[walk+2] != '00000' or -100 < walk < 100:
        d1[walk] = apply_rule(d0,walk)
        walk -=1

    #walk forward   
    walk = 0
    while d1[walk-2]+d1[walk-1]+d1[walk]+d1[walk+1]+d1[walk+2] != '00000' or -100 < walk < 100:
        d1[walk] = apply_rule(d0,walk)
        walk +=1

    
    return d1

generations = [d0]
for i in range(20):
    generations.append(make_next_generation(generations[-1]))

print(sum([k for k,v in generations[-1].items() if float(v) == 1]))

#Part 2

generations = [d0]
pots = {}
pots[0] = sum([k for k,v in generations[-1].items() if float(v) == 1])
#i = 1
#while True:
for i in range(1,100):
    generations.append(make_next_generation(generations[-1]))
    pots[i] = sum([k for k,v in generations[-1].items() if float(v) == 1])
#    if pots[i] == pots[i-1]:
#        break
#    i+=1
#    print(i, pots[i])
#    print(pots[i] - pots[i-1])
   
#The pattern begins here ###(92, 18135)###

print (18135 + (50000000000-92)*186)



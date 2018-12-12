import numpy as np
import pandas as pd
import itertools as it
filename = 'input.txt'
with open(filename) as f:
    content = f.read().splitlines()

x0,y0,vx,vy = [],[],[],[]

for i in content:
    x0.append(int(i[10:16]))
    y0.append(int(i[18:24]))
    vx.append(int(i[36:38]))
    vy.append(int(i[40:42]))
    
from operator import add

def find_range(x):
    return max(x)-min(x)

#lowest = 99999
a = 0
while True:
    x0 = map(add, x0, vx)
    y0 = map(add, y0, vy)
    a +=1
#    lowest = min(lowest,find_range(y0))
#    print find_range(y0)
    if find_range(y0) == 9:
        print a
        break
    

pic = np.zeros((205,205))
for i,j in zip(x0,y0):
    pic[j,i] +=1
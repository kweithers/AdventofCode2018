filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

import numpy as np

fabric_matrix = np.zeros((1000,1000))

squares = []

for i in content:
    a = i.split(' ')
    b = a[2].split(',')
    b = [x.replace(':','') for x in b]
    c = a[3].split('x')
    z = []
    z.append(a[0])
    squares.append(b+c+z)

for j in squares:
    for k in range(int(j[0]),int(j[0])+int(j[2])):
        for l in range(int(j[1]),int(j[1])+int(j[3])):
            fabric_matrix[k,l] +=1
            
for j in squares:
    temp_sum = 0
    for k in range(int(j[0]),int(j[0])+int(j[2])):
        for l in range(int(j[1]),int(j[1])+int(j[3])):
            temp_sum += fabric_matrix[k,l]
    if temp_sum == int(j[2])*int(j[3]):
        print j[4]
        break
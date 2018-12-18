import numpy as np
import pandas as pd
import itertools as it
from collections import defaultdict,Counter,deque
import copy

filename = 'input1.txt'
with open(filename) as f:
    content = f.read().splitlines()

content = [x for x in content if x != '']
befores = [x for x in content if x[0] == 'B']
afters = [x for x in content if x[0] == 'A']
instructions = [x for x in content if x[0] in ['1','2','3','4','5','6','7','8','9','0']]

for i in range(len(befores)):
    y = befores[i].replace('Before: ','').replace('[','').replace(']','').split(', ')
    befores[i] = [int(x) for x in y]

for i in range(len(afters)):
    y = afters[i].replace('After: ','').replace('[','').replace(']','').split(', ')
    afters[i] = [int(x) for x in y]

for i in range(len(instructions)):
    y = instructions[i].split(' ')
    instructions[i] = [int(x) for x in y]


def addr(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] + reg[instructions[2]]
    return reg

def addi(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] + instructions[2]
    return reg

def mulr(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] * reg[instructions[2]]
    return reg

def muli(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] * instructions[2]
    return reg

def banr(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] & reg[instructions[2]]
    return reg

def bani(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] & instructions[2]
    return reg

def borr(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] | reg[instructions[2]]
    return reg

def bori(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]] | instructions[2]
    return reg

def setr(instructions,reg):
    reg[instructions[3]] = reg[instructions[1]]
    return reg

def seti(instructions,reg):
    reg[instructions[3]] = instructions[1]
    return reg

def gtir(instructions,reg):
    if instructions[1] > reg[instructions[2]]:
        reg[instructions[3]] = 1
        return reg
    else:
        reg[instructions[3]] = 0
        return reg

def gtri(instructions,reg):
    if reg[instructions[1]] > instructions[2]:
        reg[instructions[3]] = 1
        return reg
    else:
        reg[instructions[3]] = 0
        return reg

def gtrr(instructions,reg):
    if reg[instructions[1]] > reg[instructions[2]]:
        reg[instructions[3]] = 1
        return reg
    else:
        reg[instructions[3]] = 0
        return reg

def eqir(instructions,reg):
    if instructions[1] == reg[instructions[2]]:
        reg[instructions[3]] = 1
        return reg
    else:
        reg[instructions[3]] = 0
        return reg

def eqri(instructions,reg):
    if reg[instructions[1]] == instructions[2]:
        reg[instructions[3]] = 1
        return reg
    else:
        reg[instructions[3]] = 0
        return reg

def eqrr(instructions,reg):
    if reg[instructions[1]] == reg[instructions[2]]:
        reg[instructions[3]] = 1
        return reg
    else:
        reg[instructions[3]] = 0
        return reg
    
fl = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

done = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
xyz = []
a = 0
for i in range(len(befores)):
    results = [g(instructions[i],list(befores[i])) for g in fl]
    good_results = [r for r in results if r == afters[i]] 
    if len(good_results) >=3:
        a+=1
print(a)

import sys
codes = {}
while sum(done) < 16:
    for i in range(len(befores)):
        results = [g(instructions[i],list(befores[i])) for g in fl]
        good_functions = []
        for j in range(16):
            if results[j] == afters[i] and done[j] == 0:
                good_functions.append(j)
        if len(good_functions) == 1 and not bool(codes.get(instructions[i][0])):
            codes[instructions[i][0]] = fl[good_functions[0]]
            done[good_functions[0]] = 1
#            print len(codes)
#            print sum(done)
#            print codes
#            print done
#            print instructions[i]
#            if len(codes) != sum(done):
##            if len(codes) == 1:
#                sys.exit()


filename2 = 'input2.txt'
with open(filename2) as f:
    content2 = f.read().splitlines()  

for i in range(len(content2)):
    y = content2[i].split(' ')
    content2[i] = [int(x) for x in y]   

register = [0,0,0,0]
for i in content2:
    register = codes[i[0]](i,register)
    
print(register)
import numpy as np
import pandas as pd
filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

import UserString

s = UserString.MutableString(content[0])

#broken = True
#while broken:
#    indices_to_remove = []
#    for i in range(len(s)-1):
#        if s[i].islower() and i not in indices_to_remove:
#            if s[i].lower() == s[i+1].lower() and s[i+1].isupper():
#                indices_to_remove.append(i)
#                indices_to_remove.append(i+1)
#        elif s[i].isupper() and i not in indices_to_remove:
#            if s[i].lower() == s[i+1].lower() and s[i+1].islower():
#                indices_to_remove.append(i)
#                indices_to_remove.append(i+1)
#    for index in sorted(indices_to_remove, reverse=True):
#        del s[index]
#    if len(indices_to_remove) == 0:
#        broken=False
#print(len(s))

#more effficient
def react_chain(s):
    stack = []
    for c in s:
        if stack:
            last = stack[-1]
            if last.lower() == c.lower() and last.islower() != c.islower():
                stack.pop()
                continue
        stack.append(c)

    return len(stack)

print(react_chain(s))

##Part 2

chains = []
for i in 'abcdefghijklmnopqrstuvwxyz':
    reduced_chain = s.replace(i,'').replace(i.upper(),'')
    chains.append(react_chain(reduced_chain))
print(min(chains))
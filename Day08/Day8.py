import numpy as np
import pandas as pd
import itertools as it
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()
content = content[0].split(' ')
content = [int(x) for x in content]

i = 0
meta = 0

def next_int(A):
    global i
    i += 1
    return A[i-1]


def parse_node(A):
    global meta
    metadata = []
    results = []

    nchild = next_int(A)
    nentries = next_int(A)
    for j in range(0, nchild):
        chld = parse_node(A)
        results.append(chld)
    for j in range(0, nentries):
        entry = next_int(A)
        metadata.append(entry)
        meta += entry

    if nchild == 0:
        return sum(metadata)
    else:
        out = 0
        for entry in metadata:
            if 0 <= entry-1 < nchild:
                out += results[entry-1]
        return out

res = parse_node(content)
print(meta)
print(res)
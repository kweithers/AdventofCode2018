import numpy as np
import pandas as pd
filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]


df = pd.DataFrame(columns = ['ts','y'])
for i in content:
    a = i.split(']')
    b = a[0].replace('[','')
    c = pd.to_datetime(b,infer_datetime_format=True)
    d = a[1]
    
    e = {'ts':[c],'y':[d]}
    f = pd.DataFrame(e)
    df = df.append(f)
df = df.sort_values('ts').reset_index()
df = df.drop(columns = 'index')


ids = []
guards = [x for x in df.y if x[1] == 'G']
for a in guards:
    ids.append(a.split(' ')[2].replace('#',''))
ids = list(set(ids))

time_matrix = np.zeros((len(ids),61))
time_matrix[:,0] = ids

current_guard = 0
current_start = 0
current_stop = 0
for index,row in df.iterrows():
   if row[1][1] == 'G':
       current_guard = int(row[1].split(' ')[2].replace('#',''))
   elif row[1][1] == 'f':
       current_start = row[0].minute
   elif row[1][1] == 'w':
       current_stop = row[0].minute
       for m in range(0,60):
           for n in range(len(ids)):
               if current_guard == time_matrix[n,0] and m in range(current_start,current_stop):
                   time_matrix[n,m+1] +=1
                   
mins = {}
for r in range(len(ids)):
    mins[int(ids[r])] = np.sum(time_matrix[r,1:61])
longest_worker = max(mins,key=mins.get)

the_min = time_matrix[np.where(time_matrix[:,0] == longest_worker)][:,1:61].argmax()

print(longest_worker * the_min)



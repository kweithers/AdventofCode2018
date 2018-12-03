filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]
ints = [int(x) for x in content]

current_sum = 0
sums = []
i = 0
while len(set(sums)) == len(sums):
    current_sum += ints[i%len(ints)]
    sums.append(current_sum)
    i +=1

print(current_sum)
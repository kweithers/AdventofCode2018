filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]
ints = [int(x) for x in content]
sum(ints)
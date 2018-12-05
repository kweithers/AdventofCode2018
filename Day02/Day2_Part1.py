filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

twos = 0
threes = 0

for i in content:
    for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        if i.count(j) == 2:
            twos +=1
            break

for i in content:
    for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        if i.count(j) == 3:
            threes +=1
            break

checksum = twos*threes
print(checksum)
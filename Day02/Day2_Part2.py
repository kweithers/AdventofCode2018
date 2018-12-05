filename = 'part1.txt'
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

import Levenshtein

the_strings = [i for i in content for j in content if i!=j if Levenshtein.distance(i,j) == 1]

#qyzphxoiseldjrntfygvdmanu
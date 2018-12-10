players = 471
last_marble = 72026*100

from collections import Counter, deque

c = Counter()
#marbles = [0]
#current_marble_index = 0
#
#for i in range(1,last_marble+1):
#    current_marble = i
#    current_player = i%players
#
#    if current_marble % 23 != 0:
#        marbles.insert( (current_marble_index + 2) % len(marbles) , i)
#        current_marble_index = marbles.index(i)
##        print(marbles)
#    else:
#        c[current_player] += i
#        marble_to_remove = marbles[ (current_marble_index-7) % len(marbles)]
#        current_marble_index = (current_marble_index - 7) % len(marbles)
#        c[current_player] += marble_to_remove
#        marbles.remove(marble_to_remove)
##        print(marbles)
#        
#print c.most_common(1)

## Faster using deque

marbles = deque()
for current_marble in range(last_marble):
    marbles.rotate(-2)
    if current_marble and current_marble % 23 == 0:
        marbles.rotate(9)
        c[current_marble%players] += marbles.popleft()+ current_marble
    else:
        marbles.appendleft(current_marble)

print(c.most_common(1))
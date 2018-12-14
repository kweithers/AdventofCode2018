#from collections import deque
my_input = 409551
scoreboard = [3,7]
pos_1 = 0
pos_2 = 1

#while len(scoreboard) < my_input + 10:
#    score_1,score_2 = scoreboard[pos_1], scoreboard[pos_2]
#    the_sum = str(score_1+score_2)
#    for i in the_sum:
#        scoreboard.append(int(i))
#    
#    pos_1 = (pos_1 + 1 + score_1) % len(scoreboard) 
#    pos_2 = (pos_2 + 1 + score_2) % len(scoreboard) 
#    
#print(''.join([str(x) for x in scoreboard[-10:]]))

## Part 2

while int(''.join([str(x) for x in scoreboard[-len(str(my_input)):]])) != my_input:
    score_1,score_2 = scoreboard[pos_1], scoreboard[pos_2]
    the_sum = str(score_1+score_2)
    for i in the_sum:
        scoreboard.append(int(i))
        if int(''.join([str(x) for x in scoreboard[-len(str(my_input)):]])) == my_input:
            break
    
    pos_1 = (pos_1 + 1 + score_1) % len(scoreboard) 
    pos_2 = (pos_2 + 1 + score_2) % len(scoreboard) 

    
print(len(scoreboard) - len(str(my_input)))

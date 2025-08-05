# snake and ladder game 
# Requirements -- 1) Board = (1 to 100 position )
# 2) two player -- {two dicionary storing {position,newposition}} 
# 3) snake -- 14 to 5 , 99 to 2
# 4)ladder 
# dice -- random number from 1 to 6 
# player moves with the number -- new position become old position 
# this would continue till anyone player reach 100 
import random
player_position = {}
snake_Position = {}
ladder_position = {}
def dice():
    return(random.randint(1,6))
def movePlayer(snake_Position,ladder_position,dice,player_position):
    dices = dice()
    print(dices)


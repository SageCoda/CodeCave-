# from random import randint
# import time 

# def rolls():
#  hi=1 
#  roll1=randint(1,6)
#  roll1_2=randint(1,6)
#  print(roll1,roll1_2)
#  if roll1==1 or roll1_2==1:
#    score=int(0)
#    print("Awww your luck is rotten"or"Better luck next time")
#    second_player()
#    first_player()
# #    score=scor
# #    return scor
   
   
#  else:
#    score=roll1+roll1_2
#  return score


# def first_player():
#    print(f"{player1_name}'s roll:")
#    score=rolls()
#    print(f"{player1_name},your score is {score}")

#    roll_again=input("Test your luck and roll again? ")
#    if roll_again=="Yes":
#       score=rolls()+ score 
#       print(f"Your new score is {score}") 
#    while roll_again!="No":
#       roll_again=input("Test your luck and roll again? ")
#       score=rolls()+ score
#       print(f"Your new score is {score}") 
      
#    else :
#       second_player()


# def second_player():
#    print(f"{player2_name}'s roll:")
#    score=rolls()
#    print(f"{player2_name},your score is {score}")
#    roll_again=input("Test your luck and roll again? ")
#    if roll_again=="Yes":
#       score=rolls()

#    while roll_again!="No":
#        roll_again=input("Test your luck and roll again? ")
#        score=rolls()
#    else:
#       first_player()



# print("There's a maximum of four players")
# time.sleep(0.5)
# player_num=input("How many players are there? ")
# time.sleep(0.5)

# if player_num =="2":
#    player1_name=input("Player 1 enter your name ")
#    player2_name=input("Player 2 enter your name ")
    
# first_player()

from random import randint
import time

def rolls():
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    print(roll1, roll2)
    
    if roll1 == 1 or roll2 == 1:
        score_0 = 0
        print("Awww, your luck is rotten. Better luck next time")
        print(score_0)
        second_player()
    else:
        score = roll1 + roll2
    
    return score


def first_player():
    print(f"{player1_name}'s roll:")
    score = rolls()
    print(f"{player1_name}, your score is {score}")

    roll_again = input("Test your luck and roll again? ")
    while roll_again.lower() != "no":
        if roll_again.lower() == "yes":
            score_roll += rolls()
            print(f"Your new score is {score_roll}")
        roll_again = input("Test your luck and roll again? ")

    second_player()


def second_player():
    print(f"{player2_name}'s roll:")
    score_play2 = rolls()
    print(f"{player2_name}, your score is {score_play2}")
    
    roll_again = input("Test your luck and roll again? ")
    while roll_again.lower() != "no":
        if roll_again.lower() == "yes":
            score_play2 += rolls()
        roll_again = input("Test your luck and roll again? ")

    first_player()


print("There's a maximum of four players")
time.sleep(0.5)
player_num = input("How many players are there? ")
time.sleep(0.5)

if player_num == "2":
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")

first_player()



    


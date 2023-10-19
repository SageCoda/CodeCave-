from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3


move= input("Enter your move(Rock, Paper or Scissors) ")
if move=="Rock":
    print("YOUR MOVE:"  )
    print(rock)
elif move=="Paper":
    print("YOUR MOVE:"  )
    print(paper)
elif move=="Scissors":
    print("YOUR MOVE:"  )
    print(scissors)

# Turn that random number into the computer's RPS move
num = randint(1,3)
if num ==1:
    print("COMPUTER MOVE:"  )      
    print(rock)
elif num ==2:
    print("COMPUTER MOVE:"  )
    print(paper)
else:
    print("COMPUTER MOVE:"  )
    print(scissors)


# Ask a user to enter their move
if move=="Rock" and num==1:
    print("Its a Tie")
elif move=="Rock" and num==2:
    print("Paper beats rock.You lose!")
elif move=="Rock" and num==3:
    print("Rock beats Scissors .You win! :)")

elif move=="Paper" and num==1:
    print("Paper beats Rock.You Win")
elif move=="Paper" and num==2:
    print("Its a tie")
elif move=="Paper" and num==3:
    print("Scissors beats Paper.You lose")

elif move=="Scissors" and num==3:
    print("Its a tie")
elif move=="Scissors" and num==2:
    print("Scissors beats Paper.You Win")
elif move=="Scissors" and num==1:
    print("Rock beats Scissors.You lose")
else:
    print("Invalid Move!Try again")


# Print the rock, paper, or scissors ASCII art that corresponds to the player's move


# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move


# Figure out who wins and print the result! 

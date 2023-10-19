print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction=input("Where do you want to go?...\n")
if direction.lower()=="right":
    print("Ha!You went RIGHT over a cliff.Adventurers these day tsk tsk")
    print("****You fell over a cliff.Game Over****")
elif direction.lower()=="left":
    action=input("You come come out of the bushes, before you lies a lake.Do you wait or swim?...\n ")
    if action.lower()=="Swim":
        print("Oh, the crocdiles gobble you in one fell snap.You are dead.Game over,adventurer")
    elif action.lower()=="wait":
        print("What's that cave over there? Doors of some sort?")
        door=input("Red, Blue and Green door, which door do you go through?\n ")
        if door.lower()=="blue":
         print("Alas,adventurer, that is but the door of flames")
         print("*****You burned to a crisp.Game Over.*****")
        elif door.lower()=="red":
         print("Such a grave decision adventurer,the wraiths of the underworld claim your soul for  + the end of the ends")
         print("*****The underworld has claimed your soullll.Game Over.*****")
        else:
           print("It couldnt be...it is...the treasure- The treasure of Azbureth!!")
           print("You did it adventurer, you found the treasure!")
           print("*****Congratulations.You found the treasure.******")
           print("***FIN***")
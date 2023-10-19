from random import randint

def rolls():
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    print(roll1, roll2)

    if roll1 == 1 or roll2 == 1:
        score = 0
        print("Awww, snake eye! Your score for this round is 0.")
    else:
        score = roll1 + roll2
        print(f"Your score for this round is {score}.")
    
    return score


def play_game_2_players():
    player1_score = 0
    player2_score = 0

    while True:
        print(f"{player1}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
            player1_score = 0
        else:
            player1_score += score
            print(f"{player1}'s total score: {player1_score}")
            if player1_score >= 50:
                print(f"{player1} wins!")
                break
            roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
                    player1_score = 0
                    break
                player1_score += score
                print(f"{player1}'s total score: {player1_score}")
                if player1_score >= 50:
                    print(f"{player1} wins!")
                    break
                roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")

        if player1_score >= 50:
            break

        print(f"{player2}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
            player2_score = 0
        else:
            player2_score += score
            print(f"{player2}'s total score: {player2_score}")
            if player2_score >= 50:
                print(f"{player2} wins!")
                break
            roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
                    player2_score = 0
                    break
                player2_score += score
                print(f"{player2}'s total score: {player2_score}")
                if player2_score >= 50:
                    print(f"{player2} wins!")
                    break
                roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")

        if player2_score >= 50:
            break
def play_game_3_players():
    player1_score = 0
    player2_score = 0
    player3_score = 0

    while True:
        print(f"{player1}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
            player1_score = 0
        else:
            player1_score += score
            print(f"{player1}'s total score: {player1_score}")
            if player1_score >= 50:
                print(f"{player1} wins!")
                break
            roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player2}'s turn.")
                    player1_score = 0
                    break
                player1_score += score
                print(f"{player1}'s total score: {player1_score}")
                if player1_score >= 50:
                    print(f"{player1} wins!")
                    break
                roll_again = input(f"{player1}, do you want to roll again? (yes/no): ")

        if player1_score >= 50:
            break

        print(f"{player2}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player3}'s turn.")
            player2_score = 0
        else:
            player2_score += score
            print(f"{player2}'s total score: {player2_score}")
            if player2_score >= 50:
                print(f"{player2} wins!")
                break
            roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player3}'s turn.")
                    player2_score = 0
                    break
                player2_score += score
                print(f"{player2}'s total score: {player2_score}")
                if player2_score >= 50:
                    print(f"{player2} wins!")
                    break
                roll_again = input(f"{player2}, do you want to roll again? (yes/no): ")

        if player2_score >= 50:
            break

        print(f"{player3}'s turn:")
        input("Press Enter to roll the dice.")
        score = rolls()
        if score == 0:
            print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
            player3_score = 0
        else:
            player3_score += score
            print(f"{player3}'s total score: {player3_score}")
            if player3_score >= 50:
                print(f"{player3} wins!")
                break
            roll_again = input(f"{player3}, do you want to roll again? (yes/no): ")
            while roll_again.lower() == "yes":
                score = rolls()
                if score == 0:
                    print(f"Awww, too bad! Your total score has reset to 0. It's {player1}'s turn.")
                    player3_score = 0
                    break
                player3_score += score
                print(f"{player3}'s total score: {player3_score}")
                if player3_score >= 50:
                    print(f"{player3} wins!")
                    break
                roll_again = input(f"{player3}, do you want to roll again? (yes/no): ")


print("Let's play the dice game!")
player_num=input("How many players are there?")
if player_num==str(2):
  player1 = input("Player 1, what's your name? ")
  player2 = input("Player 2, what's your name? ")
  play_game_2_players()
elif player_num==str(3):
  player1 = input("Player 1, what's your name? ")
  player2 = input("Player 2, what's your name? ")
  player3 = input("Player 3, what's your name? ")
  play_game_3_players()
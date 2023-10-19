import random

def choose_random_word():
    words = ["apple", "queen", "dalmatian", "toy"]
    return random.choice(words)

def display_blanks(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def get_guess():
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            return guess

def play_game():
    word = choose_random_word()
    guessed_letters = set()
    attempts = 7

    print("Welcome to Hangman!")
    print(display_blanks(word, guessed_letters))

    while attempts > 0 and "_" in display_blanks(word, guessed_letters):
        guess = get_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.add(guess)
            if guess not in word:
                attempts -= 1
                print(f"Wrong guess! {attempts} {'attempts' if attempts != 1 else 'attempt'} left.")

        print(display_blanks(word, guessed_letters))

    if "_" not in display_blanks(word, guessed_letters):
        print("Congratulations! You won the game!")
    else:
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    play_game()

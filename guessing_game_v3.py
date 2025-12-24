import random

def get_secret_number():
    return random.randint(1,10)

def get_guess():
    try:
        return int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Invalid input.")
        return None
    
def play_game():
    secret = get_secret_number()
    attempts = 0
    guess = None

    while guess != secret:
        guess = get_guess()
        if guess is None:
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct!")
            print("Attempts:", attempts)

play_game()
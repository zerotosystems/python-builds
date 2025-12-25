import random

def get_guess():
    try:
        return int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Invalid input.")
        return None
    
secret = random.randint(1,10)
guesses = []

while True:
    guess = get_guess()
    if guess is None:
        continue
    if guess in guesses:
        print("You already guessed that number. Try again.")
        continue
    guesses.append(guess)

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        print("You guessed", len(guesses), "times.")
        print("Your guesses were:", guesses)
        break
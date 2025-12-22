import random
secret_number = random.randint(1,10)
guess = None
attempts = 0

while guess != secret_number:
    attempts += 1
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Correct! You guessed it in",attempts,"tries!")
    except ValueError:
        print("Please enter a valid number.")
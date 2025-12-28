import random

player = {
    "name": input("Enter your name: "),
    "attempts": 0,
    "guesses": []
}

secret = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Invalid input.")
        continue

    player["attempts"] += 1
    player["guesses"].append(guess)

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        print("\nGame Summary")
        print("Player Name:", player["name"])
        print("Total Attempts:", player["attempts"])
        print("Guesses:", player["guesses"])
        if player["attempts"] <= 3:
            print("Excellent performance!")
        elif player["attempts"] <= 6:
            print("Good job!")
        else:
            print("Keep practicing!")
        break



    

  
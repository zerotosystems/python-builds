import random
secret_number = random.randint(1,10)

try: 
    guess_number = int(input("Guess a number between 1 to 10: "))
except ValueError:
    print("Please enter a number.")
    exit()

if guess_number == secret_number:
    print("Correct!")
elif guess_number > secret_number:
    print("Too High!")
else:
    print("Too Low!")
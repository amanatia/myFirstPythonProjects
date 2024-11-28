import random

import asciiArt 

print(asciiArt.number_guessing_game)

def find_number(number, guess):
    if guess == number:
        print("You won")
        return 0
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
        
        
ran_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct = True
while correct:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        correct = False
        attempts = 5
        print("You have 5 attempts remaining to guess the number")
    elif difficulty == "easy":
        correct = False
        attempts = 10
        print("You have 10 attempts remaining to guess the number")
    else:
        print("Enter a valid answer")
    


for i in range (0, attempts):
    guess = int(input("Make a guess: "))
    result = find_number(ran_number, guess)
    if result == 0:
        break
    attempts = attempts - 1
    if attempts == 0:
        print("You've run out of guesses, you lost.")
    else:
        print(f"You have {attempts} attempts remaining") 
    


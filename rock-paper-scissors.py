import random

print('''Welcome to ROCK-PAPER-SCISSORS''')

print("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
---'_____)_____
          ______)
          _______)
         _______)
---.__________) '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

win = "You win"
lose = "You lose"

game_images = [rock, paper, scissors]

players_choice = int(input())
print(f"You chose: {players_choice} ")
print(game_images[players_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")
print(game_images[computer_choice])

if players_choice >=3 or players_choice < 0:
    print("You typed an invalid number. Try again.")

if (players_choice == 0 and computer_choice == 2) or ( players_choice > computer_choice) :
    print(win)
elif computer_choice == players_choice:
    print("It's a draw")
else:
    print(lose)

    

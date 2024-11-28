import random
import Begginer_Level.Hangman_words as Hangman_words
from Begginer_Level.Hangman_art import stages


word  = random.choice(Hangman_words.word_list)
print(word)


placeholder = " "
for letter in word:
    placeholder = placeholder + "_"
print("this is your word: " + placeholder)

won = False

display = " "

lives = -1
not_in_word = False
guessed_letters = []

while not won:
    display = ""
    guess = input("Insert a letter: ").lower()
    for letter in word:
        if letter == guess:
            display = display + letter
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            display = display + letter
        else: 
            display = display +  "_" 
            not_in_word = True
    if not_in_word:
        lives = lives +1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
    print(f"{stages[lives]}")
    print(f"You have {6 - lives} remaining")
    print(display)
    if lives == 6 :
        won = True 
        print("You Lose!")
    elif "-" not in display:
        won = True 
        print("You win!")
    
    
    
    





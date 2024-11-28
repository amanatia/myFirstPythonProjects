import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def generate(card_list):
    return random.choice(card_list)

def count_cards(cards):
    
    count = sum(cards)
    
    if count == 21 and len(cards)==2 :
        return 0
    
    if 11 in cards and count > 21:
        cards.remove(11)
        cards.append(1)
    if count == 21:
        return 0
    else: 
       return count
    
def compare(score1, score2):
    if score1 == score2 :
        return("It's a draw")
    elif score2 == 0:
        return("Computer wins")
    elif score1 == 0:
        return("You win")
    elif score1 > 21:
        return("Computer wins")
    elif score2 > 21:
        return("You win")
    elif score1 > score2:
        return("You win")
    else:
        return("Computer wins")
        
def game():
    user = []
    computer = []
#Lists with the cards of the players
    user.append(generate(cards))
    user.append(generate(cards))
    computer.append(generate(cards))
    computer.append(generate(cards))

    comp_score = -1
    user_score = -1
    game_over = False

    while not game_over:
    
        user_score = int(count_cards(user))
        comp_score = int(count_cards(computer))
    
        print(f"Your cards: {user}")
        print(f"Computer's cards: {computer[0]}")
    
        if user_score == 0 or comp_score == 0 or user_score > 21: 
            game_over = True
        else:
            print("Do you want to draw another card? 'yes', 'no' ")
            answer = input().lower()
            if answer == "yes":
                user.append(generate(cards))
            else:
                game_over = True

            
    while comp_score < 17 and comp_score != 0:
        computer.append(generate(cards))
        comp_score = count_cards(computer)

    user_score = count_cards(user)
    comp_score = count_cards(computer)
    
    print(f"Your final hand: {user} (score: {user_score})")
    print(f"Computer's final hand: {computer} (score: {comp_score})")       
    print(compare(user_score, comp_score))   
        
    if input("Do you want to play again? 'yes', 'no' ").lower() == "yes":
        game()

        
game()  
    


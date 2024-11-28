import Begginer_Level.asciiArt as asciiArt
import random
from Begginer_Level.data import data
import Begginer_Level.asciiArt as asciiArt

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_desc}, from {account_country}")


# Compare answer
def compare_answer(acc1, acc2, answer, flag):
    highest = acc1
    if acc2 > highest:
        highest = acc2
    if answer == "a" and acc1 > acc2:
        print("True")
        
    elif answer == "a" and acc1 < acc2:
        print("False")
        flag = False
    elif answer == "b" and acc1 > acc2:
        print("False")
        flag = False
    elif answer == "b" and acc1 < acc2:
            print("True")
            
    else: 
        print("Invalid answer")
        flag = False
    return highest, flag

def find_acc_by_followers(data, max_followers):
    for account in data:
        if account['followers'] == max_followers:
            return account
    return None 




#   Here starts the game!!
print("Welcome to the Higher or Lower Game!")

count = 0 

#Generate Random Account
account1 = random.choice(data)
account2 = random.choice(data)
flag = True
while flag:
    while account1 == account2:
        account2 = random.choice(data)

    print(f"Compare A: {format_data(account1)}")
    print(asciiArt.vs)
    print(f"Compare B: {format_data(account2)}")

    answer = input("Which one has more followers? Type 'A' or 'B': ").lower()
    
    print("\n" * 20)
    print(asciiArt.Higher_Lower)

#Which one has more followers?
    account1_followers = int(account1["followers"])
    account2_followers = int(account2["followers"])
    print(account1_followers)
    print(account2_followers)

    current_max, flag = compare_answer(account1_followers, account2_followers, answer, flag)
    if flag == True:
        count = count + 1
    else: 
        print("Sorry, that was wrong!")
        print(f"Your total score is: {count}")

    print(f"current max: {current_max}")        

    account1 = find_acc_by_followers(data, current_max)
    if not account1:
        print("No account found with the maximum followers. Exiting the game.")
        break
    account2 = random.choice(data)

    

    

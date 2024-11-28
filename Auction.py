        
def highest_bid(dictionary):
    
    winner = ""
    highest_bid = 0
    
    for bidder in dictionary:
        amount = dictionary[bidder]
        if amount > highest_bid :
          highest_bid = amount
          winner = bidder  
    print(f"The winnre is : {winner} with a bid of : {highest_bid}")



print('''                   _   _             
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
                                    
                                     ''')


more = True
dictionary = {}

while more:
    
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))


    
    dictionary[name] = bid

    answer = input("Are there any other biders? Type 'yes' or 'no' \n").lower()
    
    if answer == "no":
        highest_bid(dictionary)
        more = False
    else:
        print("\n" * 100)
   
    
    

        
import Begginer_Level.data as data

VALUE_OF_QUARTER = 0.25
VALUE_OF_DIME = 0.10
VALUE_OF_NICKEL = 0.05
VALUE_OF_PENNY = 0.01

# Calculate the resources
def calculate_resources(answer):
    coffee = data.coffee_data[answer]
    for item in coffee["ingredients"]:
        data.resources[item] -= coffee["ingredients"][item]
    #data.resources["water"] = data.resources["water"] - data.coffee_data[answer]["ingredients"]["water"]
    #data.resources["milk"] = data.resources["milk"] - data.coffee_data[answer]["ingredients"]["milk"]
    #data.resources["coffee"] = data.resources["coffee"] - data.coffee_data[answer]["ingredients"]["coffee"]
    #data.resources["money"] = data.resources["money"] + data.coffee_data[answer]["cost"]
    data.resources["money"] += coffee["cost"]
    return data.resources

#Check if the machine has sufficient resources
def sufficient_resources(order_ingredients, resources):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}. ") 
            is_enough = False
    return is_enough
        
# Total coins value inserted by the user
def process_coins(answer):
    print(f"Your total is: {data.coffee_data[answer]["cost"]}")
    print("Enter your coins")
    
    quarters = 0
    dimes = 0
    nickels = 0 
    pennies = 0
    total_value = 0
    
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickels = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))
    
    total_value = (quarters * VALUE_OF_QUARTER) + (dimes * VALUE_OF_DIME) + (nickels * VALUE_OF_NICKEL) + (pennies * VALUE_OF_PENNY)
    
    print(f"The amount inserted: {total_value}")
    return total_value 

# Check if transaction was successful and returns the change
def transaction_successful(total_value, answer):
    change = 0
    if total_value == data.coffee_data[answer]["cost"]:
        print("Thank you for your payment!")
    elif total_value > data.coffee_data[answer]["cost"]:
        change = data.coffee_data[answer]["cost"] - total_value
    else:
        print("Not enough money. Money refunded! ")
    return change
 

        




#Starts Here!!!!
turn_off = False
while not turn_off:
    # Insert what coffee you like
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    current_resource_value = data.resources

    
   

    if answer == "report":
        print(f"Water: {current_resource_value["water"]} ml")
        print(f"Milk: {current_resource_value["milk"]}  ml")
        print(f"Coffee: {current_resource_value["coffee"]} g")
        print(f"Money: {current_resource_value["money"]} $")
    elif answer == "off":
        turn_off = True
    else: 
        if sufficient_resources(data.coffee_data[answer]["ingredients"], current_resource_value):
            current_resource_value = calculate_resources(answer)
            amount_of_money = process_coins(answer)
            change = transaction_successful(amount_of_money, answer)
            rounded_change = round(change, 2)
            print(f"This is your change: {rounded_change} 💸")
    
    

    print(f"Available resources: {current_resource_value} ☕")
       

    
    
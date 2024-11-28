import random 

# Option 1
friends = ["Christina", "Elpida", "Marina", "Katerina", "Chara", "Amanda"]
pay = random.choice(friends)

print("The person who is going to pay is: " + str(pay))

# Option 2
random_index = random.randint(0, 5)
print("The person who is going to pay is: " + str(friends[random_index]))
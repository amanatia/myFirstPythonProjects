def is_prime(num):
    count = 0 
    for number in range(1,99):
        if num % number == 0:
            count = count + 1
    print(count) 
    if count  == 2 :
        return True
    else: 
        return False

number = int(input("Enter your number:\n"))


print(f"Number is prime: {is_prime(number)}")
        
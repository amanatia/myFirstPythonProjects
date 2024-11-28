print(''' 
      _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

 ''')


def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operations ={
    "+" : add, 
    "-" : sub, 
    "*" : mul, 
    "/" : div
}

flag = True
x = float(input("Enter number: "))
while flag:
    y = float(input("Enter number: "))
    action = input("Enter action ('*', '+', '-','/'): ")
    if action == "+":
        result = operations["+"](x,y)
        print(result)
    elif action == "-":
        result = operations["-"](x,y)
        print(result)
    elif action == "*":
        result = operations["*"](x,y)
        print(result)
    elif action == "/":
        result = operations["/"](x, y)
        print(result)
    else: 
        print("Enter again your values")
    print("Do you wish to continue on your previous result? 'yes', ''no: " )
    answer = input().lower()
    if answer == "no":
        flag = False
    else: 
        x = result 
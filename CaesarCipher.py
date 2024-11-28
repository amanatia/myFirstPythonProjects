alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar (text, shift_num, direction):
    output_text = ""
    for letter in text:
        if letter in alphabet:
            if direction == "encode":
                index = alphabet.index(letter) + shift_num
                index = index % len(alphabet)
            elif direction == "decode":
                index = alphabet.index(letter) - shift_num
                index = index % len(alphabet)  
            output_text += alphabet[index]
        else:
            output_text += letter   
      
    print(f"This is your {direction}d message: {output_text}" )
    
    
    
stop = False 
should_continue = True
while should_continue:   
    while not stop:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            stop = True 
        else: 
            print("Please type 'encode' or 'decode'")
        
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(text, shift, direction)
    print("Do you wish to continue: ")
    answer = input(" Type yes or no: ").lower()
    if answer == "no":
        should_continue= False    
    
       
            



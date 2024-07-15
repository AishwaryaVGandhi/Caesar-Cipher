import string

def technique(message, key, operation):
    if operation == "decrypt":
        key = key * -1
        
    converted_message = ""    
    for char in message:
        if char.islower() and char in alphabets_lower:
                converted_message += alphabets_lower[(alphabets_lower.index(char) + key) % 26]
        elif char.isupper() and char in alphabets_upper:
                converted_message += alphabets_upper[(alphabets_upper.index(char) + key) % 26]
        else:
            converted_message += char
                
    return converted_message


alphabets_lower = list(string.ascii_lowercase)
alphabets_upper = list(string.ascii_uppercase)
print("Caesar Cipher !!")

quit = True
while quit:
    operation = input("\nType 'ENCRYPT' for Encryption, Type 'DECRYPT' for Decryption : ").lower()
    
    if operation == "encrypt" or operation == "decrypt":
        message = input("Type your message : ")
        
        while True:
            try:
                key = int(input("Enter key (positive integer): "))
                if key > 0:
                    break
                else:
                    print("Invalid key. Please enter a positive integer.")
            except ValueError:
                print("Invalid key. Please enter an integer.")
        
        if operation == "encrypt":
            print("Encrypted Message : ", technique(message, key, operation))
        else:
            print("Decrypted Message : ", technique(message, key, operation))
      
        choice = input("\nType 'YES' if you to wish to repeat. Otherwise 'NO' : ").lower()
        if choice != "yes":
            quit = False
            print("\nYou wish to quit. Bye !!")
    
    else:
        print("Invalid Operation !!")

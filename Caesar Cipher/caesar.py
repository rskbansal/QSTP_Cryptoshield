def caesar_cipher(message, key, mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #We are only considering capital letters, Now try to add numbers also in this,what all changes have to be made.
    translated = ''

    message = message.upper() #Convert all letters to capital

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 1:
                num = (num + key) % len(LETTERS) #Shift all letters by the key
            elif mode == 2:
                num = (num - key) % len(LETTERS) # Why is modulus taken??
            
            translated += LETTERS[num]
        else:
            translated += symbol

    return translated

def main():
    message = input("Enter the message: ")
    key = int(input("Enter The Key: "))
    print("Enter \n1.Encrypt\n2.Decrypt")
    mode = int(input())

    translated = caesar_cipher(message, key, mode) # Call the caesar function 

    print(translated)

#Call the main method
#Q. What is the siginificance of the below statement if we can directly print without writing main in python
if __name__ == "__main__":
    main()

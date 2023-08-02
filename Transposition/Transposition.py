def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with a '|' after it.
    print(ciphertext + '|')

if __name__ == '__main__':
    main()

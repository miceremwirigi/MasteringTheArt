"""This emulates Caesar's cypher where a message is encrypted by translating it to numbers,
performing addition or subtraction operations in them and then translating the numbers back to letters: Inspired by a
project on Segway;s the Big book for small projects in Python"""


while True:  # Prompt te user to choose the mode (encrypt or decrypt)
    print('Do yu want to (e)ncrypt or (d)encrypt?')
    mode = input('>> ').lower()
    if mode == 'e':
        mode = 'encrypt'
        print('mode: {}'.format(mode))
        break
    elif mode == 'd':
        mode = 'decrypt'
        print('mode: {}'.format(mode))
        break
    else:
        continue

print('\nWhich message would you like to {}?\n '  # Prompt the user to input a message
      'NB: Letters only'.format(mode))
message = (input('>>')).upper()
print('\n\nWhich translation key would you like to use?\n '  # Prompt the user for the translation key,
      'NB: Number btn 0 and 26')                             # i.e. number to add or subtract
key = int(input('>>'))
print('Your message is: {}'.format(message))  # Print the message
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Create a string of the alphabet for reference
maxKey = len(letters)  # Find the length of the reference string
encrypted = ''  # Create a string variable to store the encrypted/decrypted message


for i in message:  # loop to check translate each letter in the message
    if i in letters:
        num = letters.find(i)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num >= maxKey:  # move to the beginning in case translated letter overflows
            num -= maxKey
        elif num < 0:  # move to end of the alphabet in case letter reference is below 0 after translation
            num += maxKey
        encrypted = encrypted + letters[num]  # concatenate translated letter to create the (d)encrypted string
    else:
        encrypted = encrypted + i  # Add symbol as is if it's not in the alphabet
print(encrypted)  # Print the encrypted message
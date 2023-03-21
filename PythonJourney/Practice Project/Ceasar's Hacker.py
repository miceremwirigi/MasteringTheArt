"""This is program designed to hack any Ceasar's cipher  using brute force. Ceasar's cipher encrypts  messages 
    by translating it to numbers, performing addition or subtraction operations in them and then translating
    the numbers back to letters. Try inputting: 'OCDN DN OCZ HZNNVBZ. RZ NOMDFZ OJHHJMMJR IDBCO.'
    and check the 6th line """

print('''Please input the encrypted message''')  # Prompt the user for the message to decrypt
message = input('>>').upper()  # get input and covert it to upper case
print(message)  # Print the message
print()  # Print a blank line

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Create a string variable to store the letters of the alphabet
maxKey = len(letters)  # Find the length of the alphabet

for i in range(0, maxKey):  # Loop to find end print every possible decrypted message in Caesar's cypher
    translated = ''  # Create a string variable to store the decrypted message
    for symbol in message:
        if symbol in letters:  # Translate every letter in the message
            num = letters.find(symbol)
            num = num + i
            if num in range(0,maxKey):
                translated = translated + letters[num]
            elif num >= maxKey:  # Start from the beginning of the alphabet in case of overflow
                num -= maxKey
                translated = translated + letters[num]
            elif num < 0:  # Go to the end of the alphabet in case of a negative reference
                num += maxKey
                translated = translated + letters[num]
        else:
            translated = translated + symbol  # Print symbol as is if it iss not in the alphabet
    print(translated)

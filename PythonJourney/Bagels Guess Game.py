'''I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:
That means:
Pico
One digit is correct but in the wrong position.
Fermi
One digit is correct and in the right position.
Bagels
No digit is correct.
I have thought up a number.
You have 10 guesses to get it.'''

import random
MAX_DIGIT = 3
MAX_GUESS = 10

def main:
    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:
    That means:
    Pico
    One digit is correct but in the wrong position.
    Fermi
    One digit is correct and in the right position.
    Bagels
    No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(MAX_DIGIT))

    while true:
        secretNum  = secretNumGues()
        print("I have thought up a number")
        print("You have {} guesses to get it right".format(MAX_GUESS))



def getSecretNum:
    numbers = list('0123456789') #Create a list of numbrs 0 - 10
    random.shuffle(numbers) # Shuffle the elements in the list

    secretNum


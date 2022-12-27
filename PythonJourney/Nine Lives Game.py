"""
In this nerve-shredding game, you have
to guess the secret word one letter at
a time. If your guess is wrong, you lose
a life. Choose your letters carefully,
because you only have nine lives. Lose
all your lives, and it’s game over!

from Coding Projects in Python by Dk
"""
import random

lives = 9
words = ['teeth', 'night', 'prince', 'candy',
         'float', 'crush', 'ankle', 'panda',
         'drink', 'light', 'prize']
secretWord = random.choice(words)
correct_Guess = False
clue = list('?????')
heart_symbol = u'\u2764'

def getClue(guess, secretWord, clue):
    count = 0
    while count < len(secretWord):
        if guess == secretWord[count]:
            clue[count] = guess
        count += 1


while lives > 0:
    print('Lives left:' + heart_symbol * lives)
    print('Clue is: ' + str(clue))

    guess = input('I have a secret word. Guess a letter in the secret word \n >>')

    if guess in secretWord:
        getClue(guess, secretWord, clue)
    else:
        print('You guessed incorrectly. You lose a life\n')
        lives -= 1
    guess = ''
    for i in clue:
        guess = guess + i
    if guess == secretWord:
        correct_Guess = True
        break

if correct_Guess:
    print('You won!!! The secret word is ' + secretWord)
    print(guess)
else:
    print('You lose. The secret word is: \n' + secretWord)
    print(guess)

'''Define a function named count that takes a single parameter.
 The parameter is a string. The string will contain a single
 word divided into syllables by hyphens'''

def count(letters):
    syllables = 1
    for i, letter in enumerate(letters):
        if letter == '-':
            syllables += 1
    return syllables


num_syllables = count('ter-mi-na-tor')
print(f'{num_syllables} syllabes')

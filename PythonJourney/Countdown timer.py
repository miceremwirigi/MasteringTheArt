"""
This is a countdown timer that prints in seven segment digits, which are
defined in the file sevseg.py. This file has to be imported to use the
getsevsegstr method defined therein. In case this file is not available,
the code is commented at  the end of this file.
"""

import sys
import sevseg
import time

# Prompt the user to input yhe countdown time
while True:
    print('Enter the number of hours')
    hours = input('>>')
    if hours.isdecimal():
        break
while True:
    print('Enter the number of minutes')
    minutes = input('>>')
    if minutes.isdecimal():
        break
while True:
    print('Enter the number of seconds')
    seconds = input('>>')
    if seconds.isdecimal():
        break

totalsec = int(hours) * 3600 + int(minutes) * 60 + int(seconds)  # Convert the total time into seconds

try:
    while True:
        thours = totalsec // 3600  # Find the total hours
        tmin = (totalsec % 3600) // 60  # Find the total minutes
        tsec = ((totalsec % 3600) % 60)  # Find the total seconds

        hDigits = sevseg.getsevsegstr(thours, 2)  # Get the seven segment hours string
        hTopRow, hMidRow, hBottomRow = hDigits.splitlines()  # Split the string to accommodate the colon separating minutes and seconds

        mDigits = sevseg.getsevsegstr(tmin, 2)  # Get the seven segment minutes string
        mTopRow, mMidRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getsevsegstr(tsec, 2)  # Get the seven segment seconds string
        sTopRow, sMidRow, sBottomRow = sDigits.splitlines()

        if totalsec < 0:
            print('TIME\'S UP!!!')
        print(hTopRow + ' ' + mTopRow + ' ' + sTopRow)  # Print out the timer
        print(hMidRow + '*' + mMidRow + '*' + sMidRow)
        print(hBottomRow + '*' + mBottomRow + '*' + sBottomRow)
        print()
        print('press Ctrl-C to quit')
        time.sleep(1)  # Add a one-second delay
        totalsec -= 1  # Countdown
except KeyboardInterrupt:
    print('...Timer Exit...')
    sys.exit()  # Exit once Ctrl + C is pressed

"""
# sevseg.py code
\"""This creates a string of seven segment display numbers\"""



def getsevsegstr(number, minwidth=0):  # returns a string of seven segment digits
    row = ['', '', '']  # List to store the rows of the seven segment display
    number = str(number).zfill(minwidth)  # Convert the argument to string and zero fill to minwidth digits
    for i, numeral in enumerate(number):  # Loop to convert each number to seven segment digit
        if i != len(number)-1:
            row[0] += ' '
            row[1] += ' '
            row[2] += ' '
        if numeral == '.':
            row[0] += ' '
            row[1] += ' '
            row[2] += '.'
        elif numeral == '-':
            row[0] += '    '
            row[1] += ' -- '
            row[2] += '    '
        elif numeral == '0':
            row[0] += ' __ '
            row[1] += '|  |'
            row[2] += '|__|'
        elif numeral == '1':
            row[0] += '    '
            row[1] += '   |'
            row[2] += '   |'
        elif numeral == '2':
            row[0] += ' __ '
            row[1] += ' __|'
            row[2] += '|__ '
        elif numeral == '3':
            row[0] += ' __ '
            row[1] += ' __|'
            row[2] += ' __|'
        elif numeral == '4':
            row[0] += '    '
            row[1] += '|__|'
            row[2] += '   |'
        elif numeral == '5':
            row[0] += ' __ '
            row[1] += '|__ '
            row[2] += ' __|'
        elif numeral == '6':
            row[0] += ' __ '
            row[1] += '|__ '
            row[2] += '|__|'
        elif numeral == '7':
            row[0] += ' __ '
            row[1] += '   |'
            row[2] += '   |'
        elif numeral == '8':
            row[0] += ' __ '
            row[1] += '|__|'
            row[2] += '|__|'
        elif numeral == '9':
            row[0] += ' __ '
            row[1] += '|__|'
            row[2] += ' __|'
    return '\n'.join(row)  # Join the rows to get a seven segment digit


if __name__ == '__main__':  # Run if not imported, print seven segment numbers 0 to 99
    print('This module is meant to be imported rather than ran')
    print('This will print seven segments numbers 0 to 99')
    for i in range(0, 100):
        myNumber = getsevsegstr(i, 3)
        row = ['', '', '']
        print(i)
        print(myNumber)
"""

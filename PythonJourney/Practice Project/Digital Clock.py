"""
This is a digital clock that shows current time in seven segment digits, which are
defined in the file sevseg.py. This file has to be imported to use the
getsevsegstr method defined therein. In case this file is not available,
the code is commented at  the end of this file.
"""
import sys
import sevseg
import time


try:
    while True:
        print('\n'*30)  # Print blank lines to get current output in clean space
        currentTime = time.localtime(time.time())
        hours = currentTime.tm_hour
        minutes = currentTime.tm_min
        seconds = currentTime.tm_sec

        hDigits = sevseg.getsevsegstr(hours, 2)  # Get the seven segment hours string
        hTopRow, hMidRow, hBottomRow = hDigits.splitlines()  # Split the string to accommodate the colon separating minutes and seconds

        mDigits = sevseg.getsevsegstr(minutes, 2)  # Get the seven segment minutes string
        mTopRow, mMidRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getsevsegstr(seconds, 2)  # Get the seven segment seconds string
        sTopRow, sMidRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + ' ' + mTopRow + ' ' + sTopRow)  # Print out the clock
        print(hMidRow + '*' + mMidRow + '*' + sMidRow)
        print(hBottomRow + '*' + mBottomRow + '*' + sBottomRow)
        print()
        print('press Ctrl-C to quit')
        while True:  # Wait for the seconds to change
            time.sleep(0.01)
            if currentTime.tm_sec != time.localtime(time.time()).tm_sec:
                break
except KeyboardInterrupt:
    sys.exit()
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

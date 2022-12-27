""" Finding the chance two people share a birthday in a group"""

import random
import datetime as d  # import datetime as letter d for ease


def getbirthdays(numBirthdays):  # function to return a set of random birthdays
    birthdays = []  # list to store the birthdays
    startOfYear = d.date(2000, 1, 1)  # Set the beginning date
    for i in range(numBirthdays):
        randomNumberOfDays = d.timedelta(random.randint(1, 364))
        birthday = startOfYear + randomNumberOfDays  # Get a random date of the year
        birthdays.append(birthday)  # Add the date to the list of birthdays
    return birthdays  # Return the list of birthdays


def getmatch(birthdays):  # Function to return matching birthday
    if len(birthdays) == len(set(birthdays)):  # Check if there is any recurring birthday
        return None                            # and return none if there isn't
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:  # Check the recurring birthday if there is any
                return birthdayA  # Return the recurring birthday


while True:  # Prompt the user to input a value btn 0 and 100
    print('How many birthdays do you want?')
    numBirthdays = int(input('>> '))
    if 0 < numBirthdays <= 100:
        break
    else:
        print()
birthdays = getbirthdays(numBirthdays)  # Generate a list of random birthdays
match = getmatch(birthdays)  # Check for matching birthdays in the list of matching birthdays
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June',  # Create a list of months of the year
          'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

print('The birthdays for the {} people are:'. format(numBirthdays))
for j, birthday in enumerate(birthdays):  # Print the random birthdays generated
    print('{} {} {}, '. format(birthday.year, months[birthday.month-1], birthday.day), end='')
print()

if match is None:  # Print matching birthday if exists
    print('There are no matching birthdays')
else:
    matchMonth = match.month-1
    print('The matching birthday is {} {} {}'. format(match.year, months[matchMonth], match.day))

# Run 1_000_000 Simulations to calculate the probability of matching birthdays
print('I will now run 1_000_000 simulations to determine the probability')
input('Press Enter to begin')
print('Running 1_000_000 simulations ...')
simNum = 0

for j in range(1_000_000):  # Generate random birthdays and check for  matching ones 1_000_000 times
    birthdays = getbirthdays(numBirthdays)
    if getmatch(birthdays) is None:
        simNum = simNum
    else:
        simNum += 1
    if j % 200_000 == 0:  # Print progress every 200_000 simulations
        print('{} simulations ran'.format(j))

probability = round((simNum/1_000_000) * 100, 2)  # Calculate the probability of matching birthdays in a group of random people

# Print the results of the simulation
print('Having ran 2_00_000 simulations for a group of \n {} people, there is a {} % \n chance that two people share a birthday'.format(numBirthdays, probability))

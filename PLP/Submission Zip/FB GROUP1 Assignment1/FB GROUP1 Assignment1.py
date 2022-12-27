# Question 1
# Print squares of numbers 1 - 6
print('Question 1')
print("Squares of numbers 1 - 6:")
print("Number  Sqaure")

for i in range(1, 7):
    print(i, "\t", i*i)
print()               #Print empty line between questions
#----------------------------------------------------------------#


# Question 2
# Prints the length of any string
print('Question 2')

def findStringLength(a):
    stringLength = len(str(a))
    print("Length of '{}' is {} characters".format(a,stringLength))
findStringLength('Paul') # change 'Paul' to any string to get its length
findStringLength("Power Learn Project (PLP)")
userString = input("Enter a string then press Enter\n")
findStringLength(userString)
print()                  #Print empty line between questions

#----------------------------------------------------------------#


# Question 3
# Prints the character at specified position in a sentence or string
print('Question 3')
print('Print the character at index i in the string "Live happily "')

def printChar(a):
    my_string = a
    
    while True:  # Loop to ensure correct input
        try:
            index = int(input("Please enter string index to be printed.(starting 0 and above)\n"))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number")
    stringLength = len(my_string)
    
    if index >= stringLength:
        print("{} is out of range".format(index))
    elif stringLength == 0:
        print("Empty String")
    else:
       print("{} is the {}th character in {}".format(
            my_string[index], index, my_string))

printChar("Live Happily") # Call printChar function
                          # to print any characters in 'Live Happily'
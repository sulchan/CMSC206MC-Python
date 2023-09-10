# Number Converter Project 1
# Author: Sulchan Yoon
# Class: CMSC 206

# Instructions
# Build an application which will convert the following:
# - A Decimal (base-10) number to its equivalents in hexadecimal (base-16), Octal (base-8), and binary (base-2)
# - Prompt user: Decimal to Hexadecimal
# - Prompt user: Decimal to Octal
# - Prompt user: Octal to decimal
# - Prompt user: Binary to Decimal

# Input must be between 0 and 2048, reject out of range
# Input cannot be text string such as 'xyz' or 'nice day'

# Extra:
# Convert Base-10 to Base-26

import time

def decToHex():
    # Decimal to Hexidecimal
    val = None
    # Validate input is within 0 and 2048. We will keep as integers and skip on fractionals
    try:
        val = int(input("Please enter a Decimal Value between 0 and 2048:  "))
    except:
        print("Not an integer, please try again")
        decToHex()
        exit()
    answer = ""
    # Validate number in range
    if val < 0 or val > 2048:
        print("Number not in bounds, please try again")
        decToHex()
        exit()
    # Calculate hex on 16
    while val != 0:
        hexCalc = val%16
        if hexCalc < 10:
            answer = str(hexCalc) + answer
        else:
            answer = chr(65 + hexCalc - 10) + answer
        val = val//16
    # Add leading 0x value to represent Hex
    print("Your Result in Hexadecimal is 0x", answer, sep="")

def decToOct():
    # Decimal to Octal
    val = None
    # Validate input is within 0 and 2048. We will keep as integers and skip on fractionals
    try:
        val = int(input("Please enter a Decimal Value between 0 and 2048:  "))
    except:
        print("Not an integer, please try again")
        decToOct()
        exit()
    retList = []
    # Validate number in range
    if val < 0 or val > 2048:
        print("Number not in bounds, please try again")
        decToOct()
        exit()
    else:
        # Add to list
        while val != 0:
            retList.append(val%8)
            val = val//8
    answer = 0
    # Reprint list starting from the ones place up to 10^index
    for index, value in enumerate(retList):
        answer += value * (10**index)
    print("Your Result in Octal is 0", answer, sep="")

def decToBi():
    # Decimal to Binary
    val = None
    # Validate input is within 0 and 2048. We will keep as integers and skip on fractionals
    try:
        val = int(input("Please enter a Decimal Value between 0 and 2048:  "))
    except:
        print("Not an integer, please try again")
        decToBi()
        exit()
    # Try different method with list processing rather than character processing
    retList = []
    # Validate number in range
    if val < 0 or val > 2048:
        print("Number not in bounds, please try again")
        decToBi()
        exit()
    else:
        # Add to list
        while val != 0:
            retList.append(val%2)
            val = val//2
    answer = 0
    # Reprint list starting from the ones place up to 10^index
    for index, value in enumerate(retList):
        answer += value * (10**index)
    print("Your Result in Binary is", answer)

def hexToDec():
    # Hexidecimal to Decimal
    val = None
    # Try to keep within bounds from 0 to 800 (0 to 2048 in decimal)
    try:
        val = input("Please enter an Octal Value between 0 and 0x800 (without comma):  ")
        # Remove leading 0x if available
        if val[:2] == "0x":
            print("We will assume you entered a leading 0 for your Hexadecimal value")
            val = val[2:]
            time.sleep(0.5)
    except:
        print("Not an valid input, please try again")
        hexToDec()
        exit()
    answer = 0
    valLength = len(val)
    # Verify input within bounds
    if val > "800" or val < "0":
        print("Value is out of range, please try again")
        hexToDec()
        exit()
    # Calculate with base 16
    for index in range(valLength):
        # If value is within 0-9 we will use the specified value
        if 47 < ord(val[index]) < 58:
            answer += (ord(val[index]) - 48) * (16 ** (valLength - 1 - index))
        # If value is within A to F will need to calculated separately
        elif 57 < ord(val[index]) < 71:
            answer += (ord(val[index]) - 55) * (16 ** (valLength - 1 - index))
        else:
            print("You entered an invalid character, please try again")
            hexToDec()
            exit()
    print("Your Result in Decimal is", answer)

def octToDec():
    # Octal to Decimal
    val = None
    # Try to keep within specific bounds
    try:
        val = input("Please enter an Octal Value between 0 and 04000 (without comma):  ")
        if val[0] == "0":
            print("We will assume you entered a leading 0 for your Octal value")
            val = val[1:]
            time.sleep(1)
    except:
        print("Not an integer, please try again")
        octToDec()
        exit()
    # Verify that there are no 8's or 9's in the input as that is not a valid octal number
    for char in val:
        if char == "8" or char == "9":
            print("You entered a value that contains an 8 or 9, this is an invalid Octal Number, please try again")
            octToDec()
            exit()
        # double check that the values are within bounds of characters
        elif 48 > ord(char) or ord(char)> 57:
            print("You entered an invalid character, please try again")
            octToDec()
            exit()
    # Validate bounds
    if val < "0" or val > "4000":
        print("Value is out of range, please try again")
        octToDec()
        exit()
    answer = 0
    valLength = len(val)
    # Calculate decimal from octal
    for index in range(valLength):
        answer += int(val[index]) * (8 ** (valLength - 1 - index))
    print("Your Result in Decimal is", answer)

def biToDec():
    # Binary to Decimal
    val = None
    # Value 100,000,000,000 = 2048 in decimal. Comma used to help with counting zero's
    try:
        val = int(input("Please enter a Binary Value between 0 and 100,000,000,000 (without comma):  "))
    except:
        print("Not an integer, please try again")
        biToDec()
        exit()
    # Remove non 0 or 1 values
    for char in str(val):
        if ord(char) < 48 or ord(char) > 49:
            print("You entered an invalid binary, please try again")
            biToDec()
            exit()
    # Validate bounds
    if val > 100000000000 or val < 0:
        print("Value out of bounds, please try again")
        biToDec()
        exit()
    answer = 0
    valLength = len(str(val))
    # Calculation of the decimal from the binary values
    while val > 0:
        answer += 2**(valLength-1)
        val -= 10**(valLength-1)
        valLength = len(str(val))
    print("Your Result in Decimal is", answer)


def decTo26():
    # Decimal to base 26 (not base alphabet)
    val = None
    # Validate input is within 0 and 2048. We will keep as integers and skip on fractionals
    try:
        val = int(input("Please enter a Decimal Value between 0 and 2048:  "))
    except:
        print("Not an integer, please try again")
        decTo26()
        exit()
    answer = ""
    # Validate number in range
    if val < 0 or val > 2048:
        print("Number not in bounds, please try again")
        decTo26()
        exit()
    while val != 0:
        # Calculate with a 26 base
        hexCalc = val % 26
        if hexCalc < 10:
            answer = str(hexCalc) + answer
        else:
            answer = chr(65 + hexCalc - 10) + answer
        val = val // 26
    print("Your Result in Base 26 is", answer)

def base26ToDec():
    # Base 26 to decimal
    val = None
    # 30K = 2048 in decimal
    try:
        val = input("Please enter an Octal Value between 0 and 30K (without comma):  ")
    except:
        print("Not an valid input, please try again")
        base26ToDec()
        exit()
    answer = 0
    valLength = len(val)
    # Keep within bounds
    if val > "30K" or val < "0":
        print("Value is out of range, please try again")
        base26ToDec()
        exit()
    for index in range(valLength):
        # Calculate with 26 base
        if 47 < ord(val[index]) < 58:
            answer += (ord(val[index]) - 48) * (26 ** (valLength - 1 - index))
        elif 57 < ord(val[index]) < 81:
            answer += (ord(val[index]) - 55) * (26 ** (valLength - 1 - index))
        else:
            # If value is not within 0 - 9 or A - P then error
            print("You entered an invalid character, please try again")
            base26ToDec()
            exit()
    print("Your Result in Decimal is", answer)



def main():
    # Initial function
    # Introduction Statement
    print("Welcome to the Number Converter")
    print("For Simplicity, we are looking at whole number and not fractional")
    print("Author: Sulchan Yoon")
    time.sleep(0.5)
    # Start of options
    print("Please select your desired conversion type")
    print("Enter 1 - Decimal to Hexadecimal")
    print("Enter 2 - Hexadecimal to Decimal")
    print("Enter 3 - Decimal to Octal")
    print("Enter 4 - Octal to Decimal")
    print("Enter 5 - Decimal to Binary")
    print("Enter 6 - Binary to Decimal")
    print("Enter 7 - Decimal to Base 26")
    print("Enter 8 - Base 26 to Decimal")
    print("Enter X - Exit Function")
    selection = None
    # Validate input values
    # This doesn't necessarily need to be converted to integer. Was testing integer as potential other functionality
    while selection is None:
        try:
            selection = input("Enter your choice: ")
            if selection == "X":
                print("You have selected Exit. Thank you.")
                break
            selection = int(selection)
        except:
            print("Invalid Entry")
            exit()
    # Selection of which function to enter
    match selection:
        case 1:
            print("You have selected Decimal to Hexadecimal")
            decToHex()
        case 2:
            print("You have selected Hexadecimal to Decimal")
            hexToDec()
        case 3:
            print("You have selected Decimal to Octal")
            decToOct()
        case 4:
            print("You have selected Octal to Decimal")
            octToDec()
        case 5:
            print("You have selected Decimal to Binary")
            decToBi()
        case 6:
            print("You have selected Binary to Decimal")
            biToDec()
        case 7:
            print("You have selected Decimal to Base 26")
            decTo26()
        case 8:
            print("You have selected Base 26 to Decimal")
            base26ToDec()
        # Allow for exit
        case "X":
            exit()
        # Restart if not within any approved option
        case other:
            print("You entered an invalid choice, please try again!")
            main()
            exit()

if __name__ == '__main__':
    main()
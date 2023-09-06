import time

# Author: Sulchan Yoon
# Class: CMSC206 MC

# This will be for program 1 - four integers
def fourInts(input):
    # Confirm length of the value.
    # If less than 4, print error
    if len(input) < 4:
        print("Not enough values entered")
    # If greater than 4, print error
    elif len(input) > 4:
        print("Too many values entered")
    # If value includes a non-integer, print error
    elif all(not isinstance(x, int) for x in input):
        print("Not all values are integers")
    # Else find min and max of the list and fprint values
    else:
        print(f"Your maximum value is {max(input)}, and your minimum value is {min(input)}.")

# This will be for program 2 - grades
def grades(input):
    # Confirm value is within 0 and 1
    # If negative, print error
    if input < 0:
        print("Your input value is too low!")
    # If positive, print error
    elif input > 1.0:
        print("Your input value is too high!")
    # Else use match case for letter grade values
    else:
        match input:
            case num if num >= 0.9:
                print("You got an A!")
            case num if 0.9 > num >= 0.8:
                print("You got a B!")
            case num if 0.8 > num >= 0.7:
                print("You got a C!")
            case num if 0.7 > num >= 0.6:
                print("You got a D!")
            case num if num < 0.6:
                print("You got an F!")

def firstInput():
    funcSel = None
    while funcSel is None:
        try:
            return int(input("Enter Selection: "))
        except ValueError:
            return 0


# Here I will choose with program to run and gather the required inputs
def main():
    print("Hello, please choose a function with the number selection.\n1 - The Four Integers \n2 - Grade Translator")
    time.sleep(0.5)
    funcSel = firstInput()

    match funcSel:
        case 1:
            print("Thanks for choosing 1")
            print("For this function, you will need to enter 4 separate integers")
        case 2:
            print("Thanks for choosing 2")
            print("Please enter a value from 0.0 to 1.0 inclusively")
        case 0:
            print("This is not a valid selection")
            exit()
        case other:
            print("This option is not in the selection")
            exit()
    time.sleep(0.5)

    # If the selection is valid and 1, we will confirm the value and run the fourInts function
    if funcSel == 1:
        sel1Input = None
        while sel1Input is None:
            try:
                # Get a list of the input as integer values and map to list with blank as the splitter
                sel1Input = list(map(int, input("Enter 4 separate integer values: ").split()))
            except ValueError:
                # On error, show error message and exit
                print("You have entered an invalid value")
                exit()
        # If value is valid, we will run the fourInts function
        fourInts(sel1Input)
    # If the selection is valid and 2, we will confirm the value and run the grades function
    elif funcSel == 2:
        sel2Input = None
        # Gather the second input for the grade amount into sel2Input
        while sel2Input is None:
            try:
                sel2Input = float(input("Enter  value: "))
            except ValueError:
                # On error, show error message and exit
                print("You have entered an invalid value")
                exit()
        # If the value is valid, we will run the grades function
        grades(sel2Input)

if __name__ == "__main__":
    main()
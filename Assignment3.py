# Sulchan Yoon
# Assignment 3.1

# Create 2 new functions
# - print_big_enough() accept two parameters
# - reDate() accept date mm/dd/yy

import datetime

def print_big_enough(inList, maxVal):
    output = [i for i in inList if i >maxVal]
    output.sort()
    print(output)

def dateConv(dateIn):
    output = dateIn.strftime("%B %d, %Y")
    print(f"Converted date will be {output}")
    exit()

def bigEnoughInput():
    output = []
    maxVal = None
    while True:
        try:
            output.append(int(input("Enter an Integer (Exit with other values): ")))
        except:
            print("End of list")
            break
    while maxVal is None:
        try:
            maxVal = int(input("Please enter a target number: "))
        except:
            print("Invalid Entry")
            exit()
    print_big_enough(output,maxVal)
    exit()

def dateConvInput():
    output = None
    while output is None:
        output = input("Please enter date in mm/dd/yy format: ")
        try:
            output = datetime.datetime.strptime(output, "%m/%d/%y")
            break
        except:
            print("Invalid date format")
            exit()
    dateConv(output)
    exit()


def main():
    print("Here are a list of functions available")
    print("Author: Sulchan Yoon")
    print("Enter 1 - Print Big Enough")
    print("Enter 2 - Date Conversion")
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
            print("You have selected Print Big Enough")
            bigEnoughInput()
        case 2:
            print("You have selected Date Conversion")
            dateConvInput()


if __name__ == "__main__":
    main()

# Assignment 4
# Author: Sulchan Yoon

# Assignment process file "state_data.csv"
# Allow user to query the data (i.e. population, GDP by state, other categories)
# The goal is to make information available for your users to consume

import pandas as pd

def searchState(inputFile):
    selection = None
    # Validate input values
    while selection is None:
        try:
            selection = input("What State are you interested in?: ")
            if selection == "X":
                print("You have selected Exit. Thank you.")
                break
        except:
            print("Invalid Entry")
            exit()
    df = inputFile.where(inputFile.State == selection)
    df = df.dropna().reset_index(drop=True)
    if df.empty:
        print("You selected an invalid state")
    else:
        print(df)
    exit()

def searchRegion(inputFile):
    selection = None
    # Validate input values
    while selection is None:
        try:
            selection = input("What Region are you interested in?: ")
            if selection == "X":
                print("You have selected Exit. Thank you.")
                break
        except:
            print("Invalid Entry")
            exit()
    df = inputFile.where(inputFile.Region == selection)
    df = df.dropna().reset_index(drop=True)
    if df.empty:
        print("You selected an invalid region")
    else:
        print(df)
    try:
        selection = input("Do you want stats? Y/N: ")
        if selection == "Y" or selection == "y":
            print(df.describe())
    except:
        print("Exiting")
        exit()
    exit()

def genStats(inputFile):
    print(inputFile.describe())
    exit()


def processFile(inputFile):
    print("Welcome to the Processor")
    print("Select your requested process")
    print("Enter 1 - Search State")
    print("Enter 2 - Filter by Region")
    print("Enter 3 - General Statistics")
    print("Enter X - Exit")
    selection = None
    # Validate input values
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
            print("You have selected to search by state")
            searchState(inputFile)
        case 2:
            print("You have selected to filter by region")
            searchRegion(inputFile)
        case 3:
            print("You have selected to receive general statistics")
            genStats(inputFile)
        # Allow for exit
        case "X":
            exit()
        # Restart if not within any approved option
        case other:
            print("You entered an invalid choice, please try again!")
            processFile(inputFile)
            exit()
    exit()

def main():
    print("Welcome to the csv file reader")
    print("Author: Sulchan Yoon")
    fileTest = ''
    inp = ''
    try:
        with open(input("Enter file name with extension: ")) as fileTest:
            inp = pd.read_csv(fileTest)
    except:
        print(f"Your requested file, {fileTest}, cannot be opened")
        exit()
    print(f"Length of file: {len(inp)}")
    print(inp[:10])
    request = input("Ready to process?: Y/N ")
    if request == "Y" or request == "y":
        processFile(inp)
    else:
        print("Exit")
        exit()
if __name__ == "__main__":
    main()
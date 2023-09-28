# Assignment 5
# Author: Sulchan Yoon

# Create dictionary by processing a file "fake-names.txt"
# Allow user to look up one or more persons by name or birthday
# Additional enhancement
# Output name and birthday

from datetime import datetime
import json

def main():
    print("Welcome to the Birthday Finder")
    print("Author: Sulchan Yoon")
    print("Enter 1 - Name Search")
    print("Enter 2 - Birthday Search")
    print("Enter 3 - Show List")
    print("Enter X - Exit Function")
    loadData = {}
    with open("fake-names.txt", "r") as f:
        for line in f:
            # The issue with using the commented below is that it will skip first line due to already being at end of line
            #loadData = dict(line.rstrip().split(",") for line in f)
            s = line.rstrip().split(",")
            loadData[s[0]] = s[1]
    selection = 0
    while selection == 0:
        try:
            selection = input("What would you like to do? ")
            if selection == "X":
                print("You have selected Exit. Thank you.")
                break
            selection = int(selection)
        except:
            print("Invalid selection")
            exit()
    # Selection of which function to enter
    match selection:
        case 1:
            print("You have selected Name Search")
            name = None
            bDate = None
            while name is None:
                try:
                    name = input("Who's birthday do you want to look up? ")
                    if name == "X":
                        break
                    # Pull value from key
                    bDate = loadData[name]
                    print(name + "'s birthday: " + bDate)
                except:
                    print("Could not find that name")
                    name = None
            if name == "X":
                print("Exiting")
                exit()
            # Do search
        case 2:
            print("You have selected Birthday Search")
            bDate = None
            name = None
            while bDate is None:
                try:
                    bDate = datetime.strptime(input("Enter the birthdate (mm/dd/yyyy): "), "%m/%d/%Y")
                    # This is just to double check and reenter into a string
                    bDate = bDate.strftime("%m/%d/%Y")
                    if bDate == "X":
                        break
                    try:
                        # Pull key from value
                        name = list(filter(lambda x: loadData[x] == bDate, loadData))[0]
                        print(name + "'s birthday: " + bDate)
                    except:
                        print("Could not find anyone with this birthday")
                        bDate = None
                except:
                    print("Invalid entry")
                    bDate = None
            if bDate == "X":
                print("Exiting")
                exit()
        case 3:
            print(json.dumps(loadData,indent=4, sort_keys=True))
        # Allow for exit
        case "X":
            exit()
        case other:
            print("You entered an invalid choice, please try again!")
            main()
            exit()






if __name__ == "__main__":
    main()
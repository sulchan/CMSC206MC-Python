# Homework 3
# Author: Sulchan Yoon

# Create a function to create a list of non-duplicate words by processing a block of text
# exclude the, a, an
# values with punctuation are the same word
# Down, down, down. are the same word

# Create a list of 3 x 3
# Allow input to find value from the row and column
import string

def nonDupWords():
    inputText = input("Please input your text: ")
    # This will handle what is considered punctuation to be removed from the list of words
    punc = string.ascii_letters + string.digits + " " + "'"
    # Here is the calculation to remove the punctuation from the list
    inputTextCleaned = ""
    for i in inputText:
        if i in punc:
            inputTextCleaned += i
        else:
            inputTextCleaned += " "
    # remove all of stop words as required in hw assignment
    # As noted in the assignment requirements, I am removing the a an from the list of words
    words = inputTextCleaned.split()
    stopwords = ["the", "a", "an"]
    for word in list(words):
        if word in stopwords:
            words.remove(word)
    # Create a set of the words such that we can handle values that are capitalized or partially capitalized
    wordset = set(words)
    output = []
    for item in wordset:
        if item.istitle() or item.title() not in wordset:
            output.append(item)
        else:
            # This is a very inefficient method to be able to handle the word 19 (numeric text values)
            nextitem = None
            while True:
                try:
                    nextItem = int(item)
                    break
                except:
                    nextItem = -1
                    break
            if nextItem >= 0:
                output.append(str(nextItem))
    # Sort default is ascending order, so we can leave to default
    output.sort()
    print(output)

def selectValueList():
    # This will be just a simple 3x3 list
    sampleList = []
    for i in range(3):
        sampleList.append([])
        for j in range(1,4):
            # We use this to create a running list of numbers to be verified.
            # The number 3 can be replaced with an input of n if desired to create an n x n list instead
            sampleList[i].append((i*3)+j)
    print("Here is the sample 3x3 list: ")
    print(sampleList)
    firstVal = None
    # The goal here is to verify the input requests
    try:
        firstVal = int(input("Please select the row number (1, 2, or 3):  "))
    except:
        print("Not an valid input, please try again")
        selectValueList()
        exit()
    secondVal = None
    try:
        secondVal = int(input("Please select the row number (1, 2, or 3):  "))
    except:
        print("Not an valid input, please try again")
        selectValueList()
        exit()
    # Goal to validate values are within the appropriate ranges
    if firstVal < 1 or firstVal > 3:
        print("You selected a Row value outside of the range")
        exit()
    if secondVal < 1 or secondVal > 3:
        print("You selected a Column value outside of the range")
        exit()
    # Print -1 for index starts at 0, but user experience will desire index to start a 1
    print("Your selected value in the list is:", sampleList[firstVal-1][secondVal-1])

def main():
    # Stnadard call to function request
    print("Here are a list of functions available")
    print("Author: Sulchan Yoon")
    print("Enter 1 - Non-Duplicate Words")
    print("Enter 2 - Select Value in 3x3 List")
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
            print("You have selected Non-Duplicate Words")
            nonDupWords()
        case 2:
            print("You have selected Select Value in 3x3 List")
            selectValueList()
        # Allow for exit
        case "X":
            exit()
        case other:
            print("You entered an invalid choice, please try again!")
            main()
            exit()


if __name__ == "__main__":
    main()
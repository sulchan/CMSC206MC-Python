# Homework 4
# Author: Sulchan Yoon

# Write a program to generate a list of 50 random numbers between 100 and 500 (inclusive)
# Sort the list descending and save in a file called numbers.txt, with one number per line
# Make one additional enhancement

# Write another program to prompt user for file name
# Process the file to determine:
# - Total number of sentences
# - Total number of words
# - Total number of characters (excluding punctuation marks
# - Skip blank lines

# Write up a learning experience with screenshots of tests

import random
import os
import time
import string

def printingTxt():
    randList = []
    for i in range(0,50):
        randList.append(random.randint(100,501))
    randList.sort(reverse=True)

    # Request file name as enhancement
    newName = input("Please provide a new file name to be created: ")
    if newName[-4:] != ".txt":
        newName += ".txt"

    try:
        if os.path.getsize(newName) != 0:
            open(newName,"w").close()
    except:
        print("A new file will be created")
    try:
        with open(newName, "w") as txtFile:
            for value in randList:
                txtFile.write(str(value) + "\n")
    except FileNotFoundError:
        print("File not found")
    print(f"A file has been created as {newName}")
    print("Complete")

def fileReader():
    txtFile = input("Please enter your text file name: ")
    wordList = []
    try:
        with open(txtFile, "r") as openFile:
            for word in openFile.read().split():
                wordList.append(word)
    except FileNotFoundError:
        print("File not found")
        exit()

    # Count number of sentences (assume . ! ? : as sentences)
    numSent = 0
    for word in wordList:
        numSent += word.count(".") + word.count("!") + word.count("?") + word.count(":")
    print(f"Total number of sentences: {numSent}")

    # Count number of words
    removePun = str.maketrans("","",string.punctuation)
    cleanList = []
    for word in wordList:
        cleanWord = word.translate(removePun)
        cleanList.append(cleanWord)
    print(f"Total number of words is: {len(cleanList)}")

    # Count number of characters
    numChar = 0
    for word in cleanList:
        numChar += len(word)
    print(f"Total number of characters: {numChar}")

    # Find unique words
    wordset = set(cleanList)
    outputUnique = []
    for item in wordset:
        if item.istitle() or item.title() not in wordset:
            outputUnique.append(item)
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
                outputUnique.append(str(nextItem))
    print(f"Total number of unique words: {len(outputUnique)}")



def main():
    # Standard call to function request
    print("Here are a list of functions available")
    print("Author: Sulchan Yoon")
    print("Enter 1 - Random Values Write to File")
    print("Enter 2 - Count Line Word Character in File")
    print("Enter X - Exit Function")
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
            main()
            exit()
    # Selection of which function to enter
    match selection:
        case 1:
            print("You have selected Random Values Write to File")
            printingTxt()
        case 2:
            print("You have selected Count Line Word Character in File")
            fileReader()
        # Allow for exit
        case "X":
            exit()
        case other:
            print("You entered an invalid choice, please try again!")
            main()
            exit()

if __name__ == "__main__":
    main()
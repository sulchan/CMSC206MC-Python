# Homework 5
# Author: Sulchan Yoon

# Part 1
# Create a dictionary for Gary, Alice, and Tyler
# For each student display their data: Name, Homework, Quizzes, Tests
# Write an Average() that accepts a list of numbers and returns the average
# This function will have one argument, a list of numbers
# This function will return one value - average
# Calculate various averages for students, Homework, Quiz, Test

# Part 2
# Process the attached file 50-states.txt
# Create a dictionary of the US states and their capitals

import json
import time


def average(input):
    sum = 0
    for value in input:
        sum += value
    result = sum/len(input)
    return result

def student():
    # Define each student
    Gary = {
        "Name": "Gary",
        "Homework": [90.0,97.0,75.0,92.0],
        "Quizzes": [88.0,40.0,94.0],
        "Tests": [75.0,90.0]
    }
    Alice = {
        "Name": "Alice",
        "Homework": [100.,92.0,98.0,100.0],
        "Quizzes": [82.0,83.0,91.0],
        "Tests": [89.0,97.0]
    }
    Tyler = {
        "Name": "Tyler",
        "Homework": [0.0,87.0,75.0,22.0],
        "Quizzes": [0.0,75.0,78.0],
        "Tests": [100.0,100.0]
    }
    # Print in json format each student
    print("--------Gary--------")
    print(json.dumps(Gary, indent=4, sort_keys=True))
    time.sleep(1)
    print("--------Alice--------")
    print(json.dumps(Alice, indent=4, sort_keys=True))
    time.sleep(1)
    print("--------Tyler--------")
    print(json.dumps(Tyler, indent=4, sort_keys=True))
    time.sleep(1)
    cont = None
    # Check to continue
    while cont is None:
        try:
            cont = input("Would you like to see averages? (Y/N): ")
            if cont not in ["Y","y","N","n"]:
                print("Please enter in Y or N")
                cont = None
        except:
            print("Error")
            exit()

    # Print and calc average for each value. Use average() function defined above
    if cont == "Y" or cont == "y":
        print("--------Gary--------")
        print(f"\tHomework Average: {average(Gary['Homework']):.2f}")
        print(f"\tQuiz Average: {average(Gary['Quizzes']):.2f}")
        print(f"\tTest Average: {average(Gary['Tests']):.2f}")
        print("--------Alice--------")
        print(f"\tHomework Average: {average(Alice['Homework']):.2f}")
        print(f"\tQuiz Average: {average(Alice['Quizzes']):.2f}")
        print(f"\tTest Average: {average(Alice['Tests']):.2f}")
        print("--------Tyler--------")
        print(f"\tHomework Average: {average(Tyler['Homework']):.2f}")
        print(f"\tQuiz Average: {average(Tyler['Quizzes']):.2f}")
        print(f"\tTest Average: {average(Tyler['Tests']):.2f}")
    elif cont == "N" or cont == "n":
        print("Thank you, now exiting")
        exit()
    else:
        exit()


def states():
    loadData = {}
    with open("50-states.txt", "r") as f:
        for line in f:
            s = line.rstrip().split(", ")
            loadData[s[0]] = s[1]
    print(json.dumps(loadData, indent=4, sort_keys=True))
    time.sleep(1)
    print("---Completed load---")

def main():
    # Stnadard call to function request
    print("Here are a list of functions available")
    print("Author: Sulchan Yoon")
    print("Enter 1 - Student Dictionary")
    print("Enter 2 - State Dictionary")
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
            selection = None
    # Selection of which function to enter
    match selection:
        case 1:
            print("You have selected Student Dictionary")
            student()
        case 2:
            print("You have selected State Dictionary")
            states()
        # Allow for exit
        case "X":
            exit()
        case other:
            print("You entered an invalid choice, please try again!")
            main()
            exit()


if __name__ == "__main__":
    main()
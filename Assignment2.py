# Assignment 2.1
# Author: Sulchan Yoon

# Write a function that will draw a sideways tree with (*)
# Allow user to decide the max number of *'s for the center row


import time

def flagBuilder(input):
    if input < 2:
        print("Your number is too small")
        exit()
    elif input > 10:
        print("Your number is too large")
        exit()
    for i in range(input*2 - 3):
        if i < (input*2 - 1)//2:
            for j in range(i+2):
                print("*", end="")
        else:
            for j in range(input*2 - 2 - i):
                print("*", end="")
        print("")


def main():
    print("Hello, welcome to the Flag generator")
    print("We will build a flag with (*) values")
    print("The smallest flag can be 2 stars long")
    print("The largest flag can be 10 stars long")
    time.sleep(0.5)
    selection = None
    while selection is None:
        try:
            selection = int(input("Enter the Number of Max Stars: "))
        except:
            print("Invalid Entry")
            exit()
    flagBuilder(selection)

if __name__ == '__main__':
    main()
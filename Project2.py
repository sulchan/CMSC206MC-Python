# Project 2
# Author: Sulchan Yoon

# Cookout Estimations

# Ask customer the following:
# Total number of guests
# Food choices - Burger, Chicken, one additional
# Add-ons - chips, fries, drinks, and none
# Duration of the cookout

# Material Costs
# Burgers patties: $18 per package; 6 burger patties per package
# Chicken patties: $10 per package; 5 chicken patties per package
# Buns: $4 per package; 12 buns per package
# Chips: $12 per 24 bags
# Sodas: $6 per 12 cans
# Hosting: $40 per hour; 2 hour minimum

# Calculations
# Minimum number of packages of materials
# Minimize the number of leftovers, purchase only what you need to max your profit
# Out of pocket costs - total amount you will spend to purchase the min number of packages
# Catering cost - Charging per customer to host the cookout
## This should be 120% of your out of pocket cost (a 20% profit margin + hosting cost)
# Allow customer to calculate multiple estimates

import pandas as pd
import time
import math

def estimate(menu):
    numGuests, numBeefBurg, numChickenBurg, \
        numHotDogs, numChDog, numSoda, numChips = None, \
        None, None, None, None, None, None
    while numGuests is None:
        try:
            numGuests = int(input("How many guests are you expecting?: "))
        except:
            print("Invalid Entry")

    # Make your order of all items
    while numBeefBurg is None:
        try:
            numBeefBurg = int(input("How many Beef Burgers would you like?: "))
        except:
            print("Invalid Entry")
    while numChickenBurg is None:
        try:
            numChickenBurg = int(input("How many Chicken Burgers would you like?: "))
        except:
            print("Invalid Entry")
    while numHotDogs is None:
        try:
            numHotDogs = int(input("How many Beef Hotdogs would you like?: "))
        except:
            print("Invalid Entry")
    while numChDog is None:
        try:
            numChDog = int(input("How many Chicken Hotdogs would you like?: "))
        except:
            print("Invalid Entry")
    while numSoda is None:
        try:
            numSoda = int(input("How many Sodas would you like?: "))
        except:
            print("Invalid Entry")
    while numChips is None:
        try:
            numChips = int(input("How many Chips would you like?: "))
        except:
            print("Invalid Entry")


    duration = 0.0
    while duration == 0.0:
        try:
            duration = float(input("How long would you like to reserve for? (In Hours. 2hr Minimum): "))
            if duration < 2.0:
                print("Not enough hours")
                duration = 0.0
        except:
            print("Invalid Entry")


    # Calculations on minimum number of packages
    packBB, packCB, packHD,packCD, packBuns, packSoda, packChips = 0,0,0,0,0,0,0

    # How many packs of beef burger?
    packBB = math.ceil(numBeefBurg/menu.at[0,"Count per Package"])
    # How many packs of chicken burger?
    packCB = math.ceil(numChickenBurg/menu.at[1,"Count per Package"])
    # How many packs of hot dogs?
    packHD = math.ceil(numHotDogs/menu.at[5,"Count per Package"])
    # How many packs of chicken dogs?
    packCD = math.ceil(numChDog/menu.at[6,"Count per Package"])
    # How many packs of buns?
    packBuns = math.ceil((numBeefBurg+numChickenBurg+numHotDogs+numChDog)/menu.at[2,"Count per Package"])
    # How many packs of soda?
    packSoda = math.ceil(numSoda/menu.at[4,"Count per Package"])
    # How many packs of Chips?
    packChips = math.ceil(numChips/menu.at[3,"Count per Package"])

    print("------------------------Receipt------------------------")
    print(f"Your order summary \n"
          f"{packBB} pack(s) of Beef Burgers @ $", menu.at[0,"Price per Package"], "ea. Total $", packBB*menu.at[0,"Price per Package"], "\n"
          f"{packCB} pack(s) of Chicken Burgers @ $", menu.at[1,"Price per Package"], "ea. Total $", packCB*menu.at[1,"Price per Package"], "\n"
          f"{packHD} pack(s) of Hot Dogs @ $", menu.at[5,"Price per Package"], "ea. Total $", packHD*menu.at[5,"Price per Package"], "\n"
          f"{packCD} pack(s) of Chicken Dogs @ $", menu.at[6,"Price per Package"], "ea. Total $", packCD*menu.at[6,"Price per Package"], "\n"
          f"{packBuns} pack(s) of Buns @ $", menu.at[2,"Price per Package"], "ea. Total $", packBuns*menu.at[2,"Price per Package"], "\n"
          f"{packSoda} pack(s) of Soda @ $", menu.at[4,"Price per Package"], "ea. Total $", packSoda*menu.at[4,"Price per Package"], "\n"
          f"{packChips} pack(s) of Chips @ $", menu.at[3,"Price per Package"], "ea. Total $", packChips*menu.at[3,"Price per Package"])
    # Calculate total cost, using the minimum number of packages, calculate cost of goods
    totalCost = 0
    totalCost +=packBB*menu.at[0,"Price per Package"]
    totalCost +=packCB*menu.at[1,"Price per Package"]
    totalCost +=packHD*menu.at[5,"Price per Package"]
    totalCost +=packCD*menu.at[6,"Price per Package"]
    totalCost +=packBuns*menu.at[2,"Price per Package"]
    totalCost +=packSoda*menu.at[4,"Price per Package"]
    totalCost +=packChips*menu.at[3,"Price per Package"]
    time.sleep(1)
    # Calculate Customer's price (total cost + 20% margin + duration cost)
    customerCost = totalCost * 1.2 + duration*40
    profit = customerCost - totalCost
    print("-------------------------Totals-------------------------")
    print(F"The total out of pocket cost will be ${round(totalCost,2):.2f}")
    print(f"The total with service fees comes out to ${round(customerCost,2):.2f}")
    print(f"The profit amount is ${round(profit,2):.2f}")
    time.sleep(1)

    # Allow customer to calculate multiple estimates
    tryAgain = None
    while tryAgain is None:
        try:
            tryAgain = input("Would you like to restart your estimate? Y/N: ")
            if tryAgain == "Y" or tryAgain == "y" or tryAgain == "N" or tryAgain == "n":
                continue
            else:
                print("Invalid entry")
                tryAgain = None
        except:
            print("Invalid Entry")
    if tryAgain == "Y" or tryAgain == "y":
        print("Okay, let us restart your estimate.")
        print("------------------------Estimate------------------------")
        estimate(menu)
        exit()
    elif tryAgain == "N" or tryAgain == "n":
        print("Thank you for using the estimator.")
        exit()

def menu():
    data = {"Item":["Beef Patty", "Chicken Patty", "Buns", "Chips", "Soda", "Hot Dog", "Chicken Dog"],
            "Price per Package":[18, 10, 4, 12, 6, 10, 8],
            "Count per Package":[6, 5, 12, 24, 12, 10, 10]}
    fullMenu = pd.DataFrame(data)
    return fullMenu

def main():
    print("------------------Cookout Calculations------------------")
    print("This calculator is used to estimate the cost of your cookout.")
    print("Enter 1: See the Menu")
    print("Enter 2: Start Estimate")
    print("Enter X: Exit")
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
            print("You entered an invalid choice, please try again!")
            main()
            exit()
    # Selection of which function to enter
    match selection:
        case 1:
            print("Here is the menu!")
            print("--------------------------Menu--------------------------")
            print(menu())
            print("*Note* Buns can handle both beef and chicken burger and beef and chicken hot dogs")
            time.sleep(1)
            main()
        case 2:
            print("Let us start the estimate.")
            print("------------------------Estimate------------------------")
            estimate(menu())
        # Allow for exit
        case "X":
            exit()
        case other:
            print("You entered an invalid choice, please try again!")
            main()
            exit()
    exit()

if __name__ == "__main__":
    main()
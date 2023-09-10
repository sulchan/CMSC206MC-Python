# Homework 2
# Author: Sulchan Yoon

# Instructions
# Write code to print out the following sequence of numbers: 1000, 995, 990, ..., 5, 0.
# Create a function which can accept an unlimited number of values and return the sum, average, max, min of all the input values

# Discuss learning experience

# Create function to accept 3 arguments to output a range of values.
def buildSeq(start,stop,step):
    seq1 = range(start,stop,step)
    print(*seq1)

# Create funtion to accept 3 arguments to output a list of values.
def buildSeqManual(start,stop,step):
    try:
        start = float(start)
        stop = float(stop)
        step = float(step)
    except:
        print("Invalid input")
        exit()
    answer = []
    value = start
    while value > stop:
        answer.append(value)
        value += step
    print("Your final list:", answer)

# Create function to accept any number of inputs.
def generalNum(*input):
    # Verify the input can be a number (float) for calculation
    try:
        for val in input:
            val = float(val)
    except:
        # If invalid, tell them which value is invalid
        print("Invalid input value:", val)
        exit()
    # Provide a general statistics of numbers such as sum, average, min, max of the input.
    print(f"The sum of the numbers: {sum(input)}")
    print(f"The average of the numbers: {sum(input)/len(input)}")
    print(f"The max of the numbers: {max(input)}")
    print(f"The min of the numbers: {min(input)}")

# Start range from 1000 down to -1 (exclusive) and go by a -5 step
buildSeq(1000,-1,-5)
# Build a list with a sequence of numbers
buildSeqManual(100,-1,-5)
generalNum(1,5,6,9,10)
generalNum(1,2,3,4,5,"x")
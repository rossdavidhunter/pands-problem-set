# Ross Hunter, 2019 Solution 1 sumupto

#Adapted from: https://www.quora.com/How-do-you-find-the-sum-of-a-given-range-of-integers-in-python and GMIT course videos

# entering of string text via use on input fuction, as it is integer, create variable i = and int for integer
i=int(input("Please enter a positive integer:  "))

total = 0

# use of while loop and decrement i by 1
while i > 0:
    total = total + i
    i = i - 1

# can add string text to output
print("Output From Entry is",total) 
# solution to problem 1
# entering of string text via use on input fuction, as it is integer, create variable i = and int for integer
i=int(input("Please enter a positive integer:  "))

total = 0

# use of while loop
while i > 0:
    total = total + i
    i = i - 1

# can add string text to output
print("Output From Entry is",total) 
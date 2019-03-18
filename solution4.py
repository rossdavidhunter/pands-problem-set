# Ross Hunter, 2019 Solution 4 use of collatz conjecture

# Adapted from: https://stackoverflow.com/a/13366858

# Create and input
x = int(input("Please enter a positive integer:  "))

# while x is not equal to 1
while x != 1:

    print(x)
# if even divide by 2, use of // to remove decimal point and return integer
    if x % 2 == 0:
        x = x // 2
      
    else:
        
# if odd multiply by 3 and add 1
        x = 3 * x + 1
print (x)
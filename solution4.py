# Solution 4
# Create and input
x = int(input("Please enter a positive integer:  "))

while x!= 1:

    print(x)
# if even divide by 2
    if x % 2 == 0:
        x = x // 2
    else:
# if odd multiply by 3 and add 1
        x = 3 * x + 1
print (x)
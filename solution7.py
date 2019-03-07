# Ross Hunter, 2019 Solution 7 square root

# Adapted from:https://www.programiz.com/python-programming/examples/square-root and https://www.codecademy.com/en/forum_questions/51382b87954cc276830008f9

# Use of package called math
import math
# create variable and input for floating point number
Num = float(input("Please enter a positive number:  "))

# Use string and math sq root function to dispay output as string, %.1f displays floating point to 1 decimal place
print("The Square Root of" ,Num, "is Approx. " '%.1f' % math.sqrt(Num))


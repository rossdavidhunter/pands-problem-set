# Ross Hunter, 2019 Solution 6 secondstring

#Adapted from: http://book.pythontips.com/en/latest/enumerate.html

# create input string with text 
x = input("Please enter a sentence:")

# and use of enumerate and split functions
for i, s in enumerate (x.split()):

    # if i is odd 
    if i % 2 == 1:

        print(s)
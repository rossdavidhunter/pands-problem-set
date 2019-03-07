# Ross Hunter, 2019 Solution 6 secondstring

#Adapted from: http://book.pythontips.com/en/latest/enumerate.html

# create string with text and use split() and use of enumerate and split functions
for i, s in enumerate ("The quick brown fox jumps over the lazy dog".split()):

    # if i is odd 

    if i % 2 == 1:

        print(s)
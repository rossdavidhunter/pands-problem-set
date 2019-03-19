# Ross Hunter, 2019 Solution 5 Prime Numbers

# Adapted from:https://www.sanfoundry.com/python-program-check-prime-number/

# A number is prime if is is divisable by 1 and itself
#Create and input for number
a = int(input("Please enter a positive integer:"))

# prime number is always greater than 1
if a > 1:   

#dividing all numbers in range of 2 and number entered
    for i in range(2,a):
        if(a % i)==0:
            print(a, "That is not a prime")
            
# break statement is used to come out of loop as soon as positive divider is found
            break

    else:
        print(a, "That is a prime")

else:
    print(a,"That is not a prime")
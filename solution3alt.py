# Ross Hunter, 2019 Solution 3 alternative divisors

# Import using numpy
import numpy as np

# create varaibale and use of range 
value=np.array(range(1000,10000))

# then say if value is divided by 6 == even number
Newvalue=value[value%6==0]

print(Newvalue)
# Ross Hunter, 2019 Solution 10 Display a Plot Garph

# Adapted from: https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

# import numpy and mathplotlib
import numpy as np  
import matplotlib.pyplot as plt  

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)

# Plot your graph and set your linestyle, marker and colour
    plt.plot(x, y,linestyle='--',marker='o',color='g')  
    plt.show()


graph('x+x**2+2*x', range(0, 4))


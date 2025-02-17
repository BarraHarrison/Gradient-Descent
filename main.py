# Gradient Descent in Python
import numpy as np 
import matplotlib.pyplot as plt


def y_function(x):
    return x ** 2

def y_derivative(x):
    return 2 * x

x = np.arange(-100, 100, 0.1)
y = y_function(x)

current_position = (80, y_function(80))

plt.plot(x, y)
plt.scatter(current_position[0], current_position[1], color="red")
plt.show()
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

learning_rate = 0.01

for _ in range(1000):
    new_x = current_position[0] - learning_rate * y_derivative(current_position[0])
    new_y = y_function(new_x)
    current_position = (new_x, new_y)

plt.plot(x, y, label="y = x²")
plt.scatter(current_position[0], current_position[1], color="red", label="Final Position")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient Descent Optimization")
plt.grid()
plt.show()

# Gradient Descent in Python
import numpy as np 
import matplotlib.pyplot as plt


def y_function(x):
    return np.sin(x)

def y_derivative(x):
    return np.cos(x)

x = np.arange(-5, 5, 0.1)
y = y_function(x)

current_position = (1.5, y_function(1.5))
learning_rate = 0.01

plt.ion()
fig, ax = plt.subplots()
ax.plot(x, y, label="y = x²")
scatter = ax.scatter(current_position[0], current_position[1], color="red", label="Current Position")
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Gradient Descent Optimization")
ax.grid()

for _ in range(1000):
    new_x = current_position[0] - learning_rate * y_derivative(current_position[0])
    new_y = y_function(new_x)
    current_position = (new_x, new_y)

    scatter.set_offsets([current_position[0], current_position[1]])
    plt.pause(0.1)

plt.ioff()
plt.show()


import numpy as np 
import matplotlib.pyplot as plt

def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5


def calculate_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)

x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

current_position = (0.7, 0.4, z_function(0.7, 0.4))
learning_rate = 0.01

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d", computed_zorder=False)
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8, zorder=0)
scatter = ax.scatter(current_position[0], current_position[1], current_position[2], color="magenta", s=100, zorder=1)

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Gradient Descent Visualization")

for _ in range(1000):
    x_derivative, y_derivative = calculate_gradient(current_position[0], current_position[1])
    x_new = current_position[0] - learning_rate * x_derivative
    y_new = current_position[1] - learning_rate * y_derivative
    z_new = z_function(x_new, y_new)

    current_position = (x_new, y_new, z_new)

    scatter.remove()
    scatter = ax.scatter(x_new, y_new, z_new, color="magenta", s=100, zorder=1)
    plt.pause(0.1)

plt.ioff()
plt.show()



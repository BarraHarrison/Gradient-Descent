# 🚀 Gradient Descent Algorithm Project

## 📌 Introduction
Gradient Descent is a fundamental optimization algorithm used in Machine Learning to **find the minimum of a function** by iteratively adjusting parameters in the direction of the negative gradient. This project visualizes Gradient Descent in **both 2D and 3D**, showing how an initial point moves towards the function's minimum.  

I implemented **interactive plots** using Matplotlib to visualize the descent dynamically, both in a **1D function (`main.py`)** and a **3D surface (`main_3d.py`)**.

---

## 🧠 Understanding Gradient Descent

### 💯 **1. Purpose of Gradient Descent in Machine Learning**
Gradient Descent is used to **minimize a loss function** in Machine Learning models by adjusting parameters based on the gradient of the function.  

For example, in **Linear Regression**, I adjust the model’s weights using Gradient Descent to reduce prediction errors.  

In this project, I used it to **find the lowest point of a mathematical function**.

---

### 📉 **2. What is `y_derivative` for?**
In `main.py`, I defined:
```python
def y_derivative(x):
    return np.cos(x)
```
- This represents the **derivative of the function `y = sin(x)`**.
- The derivative (gradient) tells us **the slope at any given point**.
- I use this slope to determine **how to move in the negative direction** to reach a minimum.

🔹 **Key concept:** The derivative helps us decide **how much and in which direction** to adjust our position.

---

### 🎯 **3. What is `learning_rate`?**
```python
learning_rate = 0.01
```
- The `learning_rate` determines **how big each step should be** when updating our position.
- A **high learning rate** moves faster but may overshoot the minimum.
- A **low learning rate** moves slowly but ensures a more precise descent.

🔹 **Key concept:** The learning rate balances **speed vs. accuracy** in optimization.

---

### 🔄 **4. Understanding `current_position`, `new_x`, and `new_y`**
In `main.py`, I updated our position using:
```python
new_x = current_position[0] - learning_rate * y_derivative(current_position[0])
new_y = y_function(new_x)
```
- `current_position` stores our current `(x, y)` values.
- I computed the **new `x` value** by subtracting the derivative times the learning rate.
- I computed `new_y` using `y_function(new_x)`, so I stayed on the function.

🔹 **Key concept:** This step moves us **downhill toward the function's minimum** in small increments.

---

### 🌍 **5. Making the Plot 3D with `z_function`**
In `main_3d.py`, I defined:
```python
def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5
```
- This function creates a **3D wavy surface**.
- The **`calculate_gradient(x, y)` function** computes the derivatives for movement in both `x` and `y` directions.

To visualize in 3D:
```python
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis")
```
🔹 **Key concept:** The 3D plot shows **how Gradient Descent moves towards a minimum on a curved surface**.

---

### 🎨 **6. Making the Plot Interactive with `plt.ion()` and `plt.ioff()`**
In both `main.py` and `main_3d.py`, I used:
```python
plt.ion()  # Enables interactive mode
plt.pause(0.1)  # Pauses to show movement step by step
plt.ioff()  # Turns off interactive mode at the end
plt.show()  # Displays final plot
```
- `plt.ion()` makes **real-time updates possible**.
- `plt.pause(0.1)` **animates the movement**, so you see the descent happen gradually.
- `plt.ioff()` ensures the final result stays visible.

🔹 **Key concept:** **Interactive plotting brings Gradient Descent to life**, showing how the point moves down towards the minimum!

---

## 🏆 Conclusion
This project provides an interactive visualization of **Gradient Descent in 2D and 3D**. It helps in understanding:
- The role of **derivatives** in optimization.
- How **learning rate** affects movement.
- How **interactive plots** can show optimization in action.

🔹 Gradient Descent is a powerful concept in **Machine Learning**, used in models like Neural Networks and Regression!🎉 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_prime(x):
    return 2 * x

def gradient_descent(starting_point, learning_rate, num_iterations, tolerance=1e-6):
    x = starting_point
    x_values = [x]  

    for i in range(num_iterations):
        gradient = f_prime(x)
        
        # Stop if the gradient is smaller than the tolerance
        if abs(gradient) < tolerance:
            break

        x = x - learning_rate * gradient
        x_values.append(x)

        if (i + 1) % 100 == 0:
            print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {f(x):.6f}")

    return x, x_values

# Parameters
starting_point = 10   # Initial guess
learning_rate = 0.1   # Step size
num_iterations = 1000  

final_x, x_values = gradient_descent(starting_point, learning_rate, num_iterations)
print(f"Final result: x = {final_x:.6f}, f(x) = {f(final_x):.6f}")

# Plot the function and the gradient descent path
x_range = np.linspace(-12, 12, 400)
y_range = f(x_range)

plt.plot(x_range, y_range, label='f(x) = x^2', color='blue')
plt.scatter(x_values, [f(x) for x in x_values], color='red', label='Gradient Descent Path', alpha=0.6)
plt.title('Gradient Descent for f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

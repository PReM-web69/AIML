import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_prime(x):
    return 2 * x


def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    x_values = [x]  

    for i in range(num_iterations):
        gradient = f_prime(x)
        x = x - learning_rate * gradient
        x_values.append(x)

        if i % 100 == 0:
            print(f"Iteration {i}: x = {x}, f(x) = {f(x)}")

    return x, x_values

# Parameters
starting_point = 10  # Initial guess
learning_rate = 0.1  # Step size
num_iterations = 1000  

final_x, x_values = gradient_descent(starting_point, learning_rate, num_iterations)
print(f"Final result: x = {final_x}, f(x) = {f(final_x)}")
x_range = np.linspace(-10, 10, 400)
y_range = f(x_range)

plt.plot(x_range, y_range, label='f(x) = x^2')
plt.scatter(x_values, [f(x) for x in x_values], color='red', label='Gradient Descent Path')
plt.title('Gradient Descent for f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()




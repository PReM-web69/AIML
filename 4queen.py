

import numpy as np
import random
import math

# Define parameters
n = 8  # Number of queens
initial_temp = 1000  # Initial temperature
cooling_rate = 0.95  # Cooling rate
min_temp = 0.01  # Stopping temperature

# Initialize board randomly (each index represents a column, value represents row)
board = [random.randint(0, n - 1) for _ in range(n)]

# Compute initial number of attacking pairs
attacks = 0
for i in range(n):
    for j in range(i + 1, n):
        if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
            attacks += 1

T = initial_temp

# Simulated Annealing process
while T > min_temp and attacks > 0:
    # Generate a neighbor by moving a random queen to a new row
    new_board = board[:]
    col = random.randint(0, n - 1)  # Select a random column
    new_row = random.randint(0, n - 1)  # Select a random row
    new_board[col] = new_row  # Move the queen in this column

    # Compute number of attacking pairs for new board
    new_attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if new_board[i] == new_board[j] or abs(new_board[i] - new_board[j]) == abs(i - j):
                new_attacks += 1

    # Compute change in cost function
    delta_E = new_attacks - attacks

    # Acceptance Probability
    if delta_E < 0 or random.uniform(0, 1) < math.exp(-delta_E / T):
        board = new_board  # Accept the new board
        attacks = new_attacks

    # Reduce temperature
    T *= cooling_rate

# Print the final solution
print("Final Board State (Row positions of Queens):", board)
print("Final Number of Attacking Pairs:", attacks)

# Display the chessboard
for row in range(n):
    line = ""
    for col in range(n):
        if board[col] == row:
            line += " Q "
        else:
            line += " . "
    print(line)



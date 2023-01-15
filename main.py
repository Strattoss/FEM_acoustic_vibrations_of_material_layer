import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin

# ask if program should print matrices to the console
print("Should program print matrices?: [y/n] ", end="")
should_print = input()
should_print = True if should_print == 'Y' or should_print == 'y' else False if should_print == 'N' or should_print == 'n' else None
while should_print is None:
	print("Invalid value, please write 'y', or 'n'")
	should_print = input()
	should_print = True if should_print == 'Y' or should_print == 'y' else False if should_print == 'N' or should_print == 'n' else None

print("n = ", end="")
n = int(input())

# differential equation domain
omega = (0, 2)
h = (omega[1] - omega[0]) / n

# x_i
x = [h * i for i in range(n + 1)]


# function e_i, return a function
def e(i):
	if i == n:
		return lambda y: (y - x[i - 1]) / h if x[i - 1] < y <= x[i] else 0
	return lambda y: (y - x[i - 1]) / h if x[i - 1] < y <= x[i] else (
		(x[i + 1] - y) / h if x[i] < y < x[i + 1] else 0)


def B(i, j):
	if i == j == n:
		k1 = -1
	else:
		k1 = 0

	if abs(i - j) >= 2:
		k2 = 0
	elif abs(i - j) == 1:
		k2 = -1 / h
	elif i != n:
		k2 = 2 / h
	else:
		k2 = 1 / h

	if abs(i - j) >= 2:
		k3 = 0
	elif abs(i - j) == 1:
		k3 = h / 6
	elif i != n:
		k3 = 2 * h / 3
	else:
		k3 = h / 3

	return k1 + k2 - k3


def L(i):
	if i == n:
		return -cos(x[n]) + (-sin(x[n - 1]) + sin(x[n])) / h
	return (-sin(x[i - 1]) + 2 * sin(x[i]) - sin(x[i + 1])) / h


M_mat = [[0 for j in range(n)] for i in range(n)]

for i in range(1, n + 1):
	for j in range(1, n + 1):
		M_mat[i - 1][j - 1] = B(j, i)

L_mat = [0 for i in range(n)]
for i in range(1, n + 1):
	L_mat[i - 1] = L(i)

# solving M * X = L equation
X_mat = np.linalg.solve(M_mat, L_mat)

result = [0]

for i in range(1, n + 1):
	result.append(X_mat[i - 1] * e(i)(x[i]))

if should_print:
	print("M = ")
	for row in M_mat:
		print(row)

	print("L = ")
	print(L_mat)

	print("X = ")
	print(X_mat)

	print("Result: ")
	print(result)

plt.plot(x, result)
plt.grid(True)
plt.show()

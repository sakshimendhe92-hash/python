#Generate two 3×3 random matrices (1 to 9) and perform matrix addition and matrix multiplication

import numpy as np

A = np.random.randint(1, 10, (3,3))
B = np.random.randint(1, 10, (3,3))

print("Matrix A:\n", A)
print()
print("Matrix B:\n", B)
print()
print()

# Addition
add = A + B
print("Addition of A and B:\n", add)
print()

# Multiplication
mul = np.dot(A, B)
print("Multiplication of A and B:\n", mul)
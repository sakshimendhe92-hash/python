#Multiply 5×3 matrix × 3×2 matrix (User Input)

import numpy as np

print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)

print()

A = np.array(A)
B = np.array(B)

product = np.dot(A, B)

print("Matrix A:\n", A)
print()
print("Matrix B:\n", B)
print()
print("Product Matrix:\n", product)
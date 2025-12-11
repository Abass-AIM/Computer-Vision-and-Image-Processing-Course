# Load library
import numpy as np
# Create matrix
matrix = np.array([[1, 4],
 [2, 5]])
# Calculate inverse of matrix
inverse = np.linalg.inv(matrix)
dot_product = np.dot(matrix, inverse)

print(matrix)
print(inverse)
print(dot_product)
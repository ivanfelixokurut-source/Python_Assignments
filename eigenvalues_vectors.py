# Import numpy
import numpy as np
# define a square matrix.
B = np.array([[3, 1],[0, 2]])
print(f"--- Input Matrix B ---\n{B}\n")

# 5. Use NumPy's numpy.linalg.eig() function to compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(B)

# 6. Display the results
print("--- Results ---")
print(f"Eigenvalues (A):\n{eigenvalues}")
print(f"Corresponding Eigenvectors (v):\n{eigenvectors}")

# Displaying the pairs clearly
print("\n--- Eigenpairs ---")
for i in range(len(eigenvalues)):
    print(f"Eigenvalue {i+1} (λ): {eigenvalues[i]:.4f}")
    print(f"Eigenvector {i+1} (v): {eigenvectors[:, i]}")
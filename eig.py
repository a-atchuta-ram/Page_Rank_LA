import numpy as np

# Define the matrix A
A=np.array([[0.0, 0.0, 1.0, 0.5], [0.3333333333333333, 0.0, 0.0, 0.0], [0.3333333333333333, 0.5, 0.0, 0.5], [0.3333333333333333, 0.5, 0.0, 0.0]])

def pgr(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the indices of the eigenvalues closest to 1
    index = np.where(np.isclose(eigenvalues, 1))[0]
    if len(index) > 0:
    # Iterate over the indices and find the corresponding eigenvectors
        for i in index:
            eigenvector = eigenvectors[:, i]
            if np.allclose(A @ eigenvector, eigenvector):
            # Normalize the eigenvector
                eigenvector = eigenvector / np.sum(eigenvector)
                print("Eigenvectors corresponding to the eigenvalue 1:")
                print(eigenvector)
    else:
        print("No eigenvectors corresponding to the eigenvalue 1 were found.")


k=pgr(A)
print(k)
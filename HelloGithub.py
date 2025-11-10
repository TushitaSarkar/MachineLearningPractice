import numpy as np
def greet(name):
    return f"Hello, {name}!"
def add_numbers(a, b):
    return a + b    
def multiply_matrices(mat1, mat2):
    return np.dot(mat1, mat2)
if __name__ == "__main__":
    print(greet("GitHub"))
    print("Sum:", add_numbers(5, 7))
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])
    print("Matrix Product:\n", multiply_matrices(mat1, mat2))

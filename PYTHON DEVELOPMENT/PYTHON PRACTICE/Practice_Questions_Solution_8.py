# 8. **Transpose a Matrix**: Given a 2D list, transpose the matrix (swap rows with columns).

"""

So, let's say we have:

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

We need to convert it to:

a = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

"""

def transpose(a):
    # Get the number of rows and columns in the original matrix
    rows = len(a)
    cols = len(a[0])
    
    # Initialize a new matrix for the transposed result
    transposed = [[0] * rows for _ in range(cols)]
    
    # Collect index pairs and transpose values
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = a[i][j]
    
    # Print the original and transposed matrices
    print(f"Original matrix: {a}")
    print(f"Transposed matrix: {transposed}")

# Original matrix
a = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
# Transpose the matrix
transpose(a)

"""

a = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

"""

"""
row=0, col=1 = 4 = row=1, col=0
row=1, col=2 = 8 = row=2, col=1
row=2, col=1 = 6 = row=1, col=2
row=0, col=0 = 1 = row=0, col=0
row=0, col=2 = 7 = row=2, col=0
row=1, col=1 = 5 = row=1, col=1
row=2, col=0 = 3 = row=0, col=2
row=2, col=2 = 9 = row=2, col=2
row=1, col=0 = 2 = row=0, col=1

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

"""
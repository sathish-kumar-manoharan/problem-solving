"""
How to calculate the prefix sum of a 2D matrix?
The prefix sum of a 2D matrix is a new matrix where each element at position (i, j) contains the sum of all elements from the original matrix that are above and to the left of (i, j), inclusive. 
This can be calculated using the following formula:
prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

Where:
- matrix[i][j] is the value of the original matrix at position (i, j).
- prefix[i-1][j] is the prefix sum of the row above.
"""
def prefix_sum(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = matrix[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

    return prefix

print(prefix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
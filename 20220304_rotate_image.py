# Rotate Image (leetcode)

# rotate by row/col
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        L, R = 0, len(matrix) - 1
        
        while L < R:
            # set boundary
            top, bottom = L, R
            for i in range(R - L):
                # temporary buffer
                buffer = matrix[top][L + i]
                # left -> top
                matrix[top][L + i] = matrix[bottom - i][L]
                # bottom -> left
                matrix[bottom - i][L] = matrix[bottom][R - i]
                # right -> bottom
                matrix[bottom][R - i] = matrix[top + i][R]
                # top -> right
                matrix[L + i][R] = buffer
            # increment/decrement boundaries
            L += 1
            R -= 1
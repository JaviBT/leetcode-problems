# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

# Solution by: Javi Barranco

# Problem:
# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
# You must do it in place.

# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowSet = set()
        colSet = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)

        for row in rowSet:
            matrix[row] = [0] * len(matrix[0])
        
        for col in colSet:
            for row in matrix:
                row[col] = 0


class Solution2:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []

        for i in range(len(matrix)):
            if 0 in matrix[i]: 
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0: cols.append(j)
                rows.append(i)
                matrix[i] = [0 for _ in range(len(matrix[i]))]

        for row in range(len(matrix)):
            if row not in rows:
                for col in cols:
                    matrix[row][col] = 0


exercise = Solution()
input = [[1,1,1],[1,0,1],[1,1,1]]
expected_output = [[1,0,1],[0,0,0],[1,0,1]]
exercise.setZeroes(input)
output = input
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

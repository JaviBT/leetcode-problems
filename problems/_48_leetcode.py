# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/

# Solution by: Javi Barranco

# Problem:
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, r = 0, len(matrix) - 1
        

        while l < r:
            for i in range(r - l):
                t, b = l, r
                # Save Top Left
                topLeft = matrix[t][l + i]
                # Move Bottom Left to Top Left
                matrix[t][l + i] = matrix[b - i][l]
                # Move Bottom Right to Bottom Left
                matrix[b - i][l] = matrix[b][r - i]
                # Move Top Right to Bottom Right
                matrix[b][r - i] = matrix[t + i][r]
                # Move Top Left to Top Right
                matrix[t + i][r] = topLeft
            l, r= l + 1, r - 1   


class Solution2:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j < i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
       

exercise = Solution()

input = [[1,2,3],[4,5,6],[7,8,9]]

expected_output = [[7,4,1],[8,5,2],[9,6,3]]

exercise.rotate(input)
output = input
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

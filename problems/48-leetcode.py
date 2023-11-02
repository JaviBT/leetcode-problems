# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/

# Solution by: Javi Barranco

class Solution:
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

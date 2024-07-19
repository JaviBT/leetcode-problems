# 1380. Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix

# Solution by: Javi Barranco

# Problem:
# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        lucky = []

        for i in range(n):
            curMin = min(matrix[i])
            for j in range(m):
                curVal = matrix[i][j]
                
                rowMin = (matrix[i][j] == curMin)
                colMax = True
                for k in range(n):
                    if matrix[k][j] > curVal: 
                        colMax = False
                        break
                
                if rowMin and colMax: lucky.append(curVal)

        return lucky
    

exercise = Solution()

input = [[3,7,8],[9,11,13],[15,16,17]]

expected_output = [15]

output = exercise.luckyNumbers(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
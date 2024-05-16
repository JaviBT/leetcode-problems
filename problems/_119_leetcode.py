# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii

# Solution by: Javi Barranco

# Problem:
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

#              1
#            1   1
#          1   2   1
#        1   3   3   1
#      1   4   6   4   1

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        prev = [1, 1]
        
        for i in range(3, rowIndex + 2):
            cur = [1] * i

            for j in range(1, i - 1):
                cur[j] = prev[j] + prev[j - 1]

            prev = cur

        return prev
    

exercise = Solution()

input = 3

expected_output = [1,3,3,1]

output = exercise.getRow(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
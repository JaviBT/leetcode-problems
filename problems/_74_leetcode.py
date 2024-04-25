# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix

# Solution by: Javi Barranco

# Problem:
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# - Integers in each row are sorted from left to right.
# - The first integer of each row is greater than the last integer of the previous row.

# Example:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m * n - 1

        while l <= r:
            mid = int(l + (r - l) / 2)

            mid_x, mid_y = int(mid / m), mid % m

            if matrix[mid_x][mid_y] == target: return True
            elif matrix[mid_x][mid_y] < target: l = mid + 1
            elif matrix[mid_x][mid_y] > target: r = mid - 1

        return False
    

exercise = Solution()

input = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3]

expected_output = True

output = exercise.searchMatrix(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
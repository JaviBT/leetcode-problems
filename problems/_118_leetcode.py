# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

# Solution by: Javi Barranco

class Solution:
    def generate(self, numRows: int) -> [[int]]:
        
        rows = []

        for i in range(numRows):
            newRow = []

            for j in range(i + 1):
                if j == 0 or j == i: newRow.append(1)
                else: newRow.append(rows[-1][j-1] + rows[-1][j])

            rows.append(newRow)

        return rows
        

exercise = Solution()
input = 5
expected_output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
output = exercise.generate(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

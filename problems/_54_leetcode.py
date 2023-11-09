# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

# Solution by: Javi Barranco

class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        
        top = 0
        left = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1

        n = len(matrix) * len(matrix[0])

        output = []
        direction = ['top', 'right', 'bottom', 'left']
        current_dir = 0

        while len(output) < n:
            print(output)
            if direction[current_dir] == 'top':
                for i in range(len(matrix[top][left:right+1])):
                    output.append(matrix[top][left + i])
                top += 1
            
            if direction[current_dir] == 'right':
                for row in matrix[top:bottom]:
                    output.append(row[right])
                right -= 1
            
            if direction[current_dir] == 'bottom':
                for i in range(len(matrix[bottom][left:right+2])):
                    output.append(matrix[bottom][right - i + 1])
                bottom -= 1
            
            if direction[current_dir] == 'left':
                for i in range(len(matrix[top:bottom+1])):
                    output.append(matrix[bottom - i][left])
                left += 1

            current_dir = (current_dir + 1) % 4

        return output


exercise = Solution()
input = [[1,2,3],[4,5,6],[7,8,9]]
expected_output = [1,2,3,6,9,8,7,4,5]
output = exercise.spiralOrder(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

# Solution by: Javi Barranco

# Problem:
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        res = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        while True:
            # Move to the Top Right
            for num in matrix[t][l:r+1]:
                res.append(num)
            t += 1
            if t > b: break
            # Move to the Bottom Right
            for i in matrix[t:b+1]:
                res.append(i[r])
            r -= 1
            if r < l: break
            # Move to the Bottom Left
            for num in matrix[b][r:l-1 if l != 0 else 0:-1]:
                res.append(num)
            if l == 0: res.append(matrix[b][0])
            b -= 1
            if b < t: break
            # Move to the Top Left
            for i in matrix[b:t-1:-1]:
                res.append(i[l])
            l += 1
            if l > r: break

        return res
    

class Solution2:
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

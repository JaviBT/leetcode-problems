# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

# Solution by: Javi Barranco

# Problem:
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def maxArea(self, height: [int]) -> int:

        max_area = 0
        a, b = 0, len(height)-1

        while a != b:
            area = (b - a) * min(height[a], height[b])
            if area > max_area: max_area = area

            if height[a] < height[b]:
                a += 1
            else:
                b -= 1

        return max_area

class Solution2: # Timeout
    def maxArea(self, height: [int]) -> int:

        max_area = 0

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = (j - i) * min(height[i], height[j])
                if area > max_area: max_area = area
        
        return max_area
    

class Solution3:
    def maxArea(self, height: [int]) -> int:
        l, r = 0, len(height) - 1

        largest = 0

        while l != r:
            area = min(height[l], height[r]) * (r - l)
            largest = max(largest, area)

            if height[l] > height[r]: r -= 1
            else: l += 1

        return largest
    

exercise = Solution()
input = [1,8,6,2,5,4,8,3,7]
expected_output = 49
output = exercise.maxArea(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

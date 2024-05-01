# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Solution by: Javi Barranco

# Problem:
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10

class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            idx, h = i, heights[i]

            while stack and stack[-1][1] > h:
                poppedIdx, poppedHeight = stack.pop()
                idx = poppedIdx
                maxArea = max(maxArea, poppedHeight * (i - poppedIdx))

            stack.append([idx, h])

        while stack:
            poppedIdx, poppedHeight = stack.pop()
            maxArea = max(maxArea, poppedHeight * (len(heights) - poppedIdx))

        return maxArea
    

exercise = Solution()

input = [2,1,5,6,2,3]

expected_output = 10

output = exercise.largestRectangleArea(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
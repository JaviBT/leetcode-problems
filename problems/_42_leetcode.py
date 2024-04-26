# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# Solution by: Javi Barranco

# Problem:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9


class Solution:
    def trap(self, height: [int]) -> int:
        l = 0
        water = 0

        while l < len(height) - 1:
            if height[l] <= 0:
                l += 1
            else:
                for i in range(height[l]):
                    r_bef, r = l + 1, l + 1
                    while r < len(height) and height[r] < height[l] - i:
                        r += 1
                    if r == len(height): r = r_bef
                    else: break

                l_bef = l
                while l < r:
                    water = max(water, water + height[l_bef] - i - height[l])
                    print(l, r, water)
                    l += 1
                
        return water
    

exercise = Solution()

inputs = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5]
]

expected_outputs = [
    6,
    9
]

for input, expected_output in zip(inputs, expected_outputs):
    output = exercise.trap(input)
    print(output)
    assert output == expected_output, "Wrong answer"
print("Accepted")
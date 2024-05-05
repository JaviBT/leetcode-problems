# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if  len(nums) == 1: return nums[0]
        
        maxSum = max(nums)
        curSum = 0

        for n in nums:
            if n < 0 and curSum + n < 0:
                curSum = 0
            else:
                curSum += n
                maxSum = max(maxSum, curSum)

        return maxSum
    

exercise = Solution()

input = [-2,1,-3,4,-1,2,1,-5,4]

expected_output = 6

output = exercise.maxSubArray(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
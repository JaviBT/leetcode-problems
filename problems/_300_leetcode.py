# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [None] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1: dp[i] = 1

            maxRes = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxRes = max(1, maxRes, 1 + dp[j])

            dp[i] = maxRes

        return max(dp)
    

exercise = Solution()

input = [10,9,2,5,3,7,101,18]

expected_output = 4

output = exercise.lengthOfLIS(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
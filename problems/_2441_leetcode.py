# 2441. Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums that does not contain any zeroes, fund the largest positive integer k such that -k also exists in the array. Return the largest positive integer k possible. If there is no such integer, return -1.

# Example 1:
# Input: nums = [-1, 10, 6, 7, -7, 1]
# Output: 7

class Solution:
    def findMaxK(self, nums: [int]) -> int:
        numSet = set()
        res = 0

        for num in nums:
            if -num in numSet:
                res = max(res, abs(num))
            else:
                numSet.add(num)

        return res if res else -1
    

exercise = Solution()

input = [-1, 10, 6, 7, -7, 1]

expected_output = 7

output = exercise.findMaxK(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
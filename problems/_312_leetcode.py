# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons

# Solution by: Javi Barranco

# Problem:
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167

from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def rec(l: int, r: int):
            if l > r: return 0
            if (l, r) in dp: return dp[(l, r)]
            
            res = 0
            for i in range(l, r + 1):
                res = max(res, (nums[l - 1] * nums[i] * nums [r + 1]) + rec(l, i - 1) + rec(i + 1, r))

            dp[(l, r)] = res
            return res

        return rec(1, len(nums) - 2)
    

exercise = Solution()

input = [3,1,5,8]

expected_output = 167

output = exercise.maxCoins(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 494. Target Sum
# https://leetcode.com/problems/target-sum

# Solution by: Javi Barranco

# Problem:
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i: int, cur: int):
            if (i, cur) in dp: return dp[(i, cur)]
            if cur == target and i == len(nums): return 1
            if i >= len(nums): return 0

            res = dfs(i + 1, cur + nums[i])
            res += dfs(i + 1, cur - nums[i])

            dp[(i, cur)] = res
            return res

        return dfs(0, 0)
    

exercise = Solution()

input = ([1,1,1,1,1], 3)

expected_output = 5

output = exercise.findTargetSumWays(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 198. House Robber
# https://leetcode.com/problems/house-robber

# Solution by: Javi Barranco

# Problem:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4

class Solution:
    def rob(self, nums: [int]) -> int:
        dp = [None] * len(nums)

        def robRec(i: int):
            if i >= len(nums):
                return 0
            if dp[i] != None:
                return dp[i]

            dp[i] = max(robRec(i+1), nums[i] + robRec(i+2))
            return dp[i]

        robRec(0)
        return max(dp)
    

class Solution2:
    def rob(self, nums: [int]) -> int:
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            temp = max(rob1 + nums[i], rob2)
            rob1, rob2 = rob2, temp
        
        return max(rob1, rob2)
    

exercise = Solution()

input = [1,2,3,1]

expected_output = 4

output = exercise.rob(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
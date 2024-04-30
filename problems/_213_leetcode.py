# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii

# Solution by: Javi Barranco

# Problem:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3

class Solution:
    def rob(self, nums: [int]) -> int:
        def houseRob(nums: [int]) -> int:
            rob1, rob2 = 0, 0

            for i in range(len(nums)):
                temp = max(rob1 + nums[i], rob2)
                rob1, rob2 = rob2, temp

            return temp

        return max(houseRob(nums[1:]), houseRob(nums[:-1])) if len(nums) > 1 else nums[0]
    

exercise = Solution()

input = [2,3,2]

expected_output = 3

output = exercise.rob(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
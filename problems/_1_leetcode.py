# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Solution by: Javi Barranco

# Problem:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        
        dic = {}

        for i in range(len(nums)):
            if target - nums[i] in dic.keys():
                return [dic[target - nums[i]], i]
            if nums[i] not in dic.keys():
                dic[nums[i]] = i

        return


exercise = Solution()

input = [2,7,11,15]
target = 9
expected_output = [0,1]

output = exercise.twoSum(input, target)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

# Solution by: Javi Barranco

# Problem:
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]


class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            nums[i] = current_sum

        return nums
    

class Solution2:
    def runningSum(self, nums: [int]) -> [int]:
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]

        return nums
    

exercise = Solution()

input = [1,2,3,4]

expected_output = [1,3,6,10]

output = exercise.runningSum(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
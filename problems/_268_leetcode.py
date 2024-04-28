# 268. Missing Number
# https://leetcode.com/problems/missing-number

# Solution by: Javi Barranco

# Problem:
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example:
# Input: nums = [3,0,1]
# Output: 2

class Solution:
    def missingNumber(self, nums: [int]) -> int:
        numSum = 0
        expectedSum = 0
        for i in range(len(nums)):
            numSum += nums[i]
            expectedSum += i
        return expectedSum + len(nums) - numSum


class Solution2:
    def missingNumber(self, nums: [int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums: return i


class Solution3:
    def missingNumber(self, nums: [int]) -> int:
        hashSet = set(range(0, len(nums) + 1))
        for num in nums:
            hashSet.remove(num)
        return hashSet.pop()


exercise = Solution()

input = [3,0,1]

expected_output = 2

output = exercise.missingNumber(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number

# Solution by: Javi Barranco

# Problem:
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

class Solution: # Floyd's Tortoise and Hare (Cycle Detection)
    def findDuplicate(self, nums: [int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2: return slow


class Solution: # Brute force solution
    def findDuplicate(self, nums: [int]) -> int:
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(len(nums) - i - 1):
                if cur == nums[i + j + 1]: return cur


exercise = Solution()

input = [1,3,4,2,2]

expected_output = 2

output = exercise.findDuplicate(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
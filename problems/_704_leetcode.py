# 704. Binary Search
# https://leetcode.com/problems/binary-search

# Solution by: Javi Barranco

# Problem:
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# Example:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = int(l + (r -l) / 2)

            if nums[mid] == target: return mid
            elif target < nums[mid]: r = mid - 1
            elif target > nums[mid]: l = mid + 1

        return -1
    

exercise = Solution()

input = [[-1,0,3,5,9,12], 9]

expected_output = 4

output = exercise.search(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
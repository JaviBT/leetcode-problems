# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Solution by: Javi Barranco

# Problem:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.

# Example:
# Input: [3,4,5,1,2]
# Output: 1

class Solution:
    def findMin(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        l, r = 0, n - 1
        mid = 0

        while l <= r:
            mid = int(l + (r - l)/2)

            if nums[mid] < nums[(mid - 1) % n] and nums[mid] <= nums[0] and nums[mid] <= nums[n - 1]: return nums[mid]
            elif nums[mid] > nums[n - 1]: l = mid + 1
            else: r = mid - 1


exercise = Solution()

input = [3,4,5,1,2]

expected_output = 1

output = exercise.findMin(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
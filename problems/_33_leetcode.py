# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Solution by: Javi Barranco

# Problem:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

# Example:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

class Solution:
    def search(self, nums: [int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = int((r + l) / 2)
            print(mid, nums[mid])

            if nums[mid] == target: return mid
            
            # Left Side:
            if nums[0] <= nums[mid]:
                if nums[mid] < target: l = mid + 1
                elif nums[mid] > target:
                    if target < nums[0]: l = mid + 1
                    elif target >= nums[0]: r = mid -1
            # Right Side:
            else:
                if nums[mid] > target: r = mid - 1
                elif nums[mid] < target:
                    if target > nums[n-1]: r = mid - 1
                    elif target <= nums[n-1]: l = mid + 1
    
        return nums[r] if nums[r] == target else -1
    

exercise = Solution()

input = [[4,5,6,7,0,1,2], 0]

expected_output = 4

output = exercise.search(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

import heapq

class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for _ in range(k):
            num = heapq.heappop(heap)

        return -num
    

exercise = Solution()

input = [3,2,1,5,6,4]

expected_output = 5

output = exercise.findKthLargest(input, 2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
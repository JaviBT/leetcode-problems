# Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
# Return the shortest such subarray and output its length.

from typing import List
import math

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        monotonic_stack = []

        first_exception = math.inf
        largest_exception = -math.inf
        last_exception = None

        for i, num in enumerate(nums):

            while monotonic_stack and num < monotonic_stack[-1]:
                monotonic_stack.pop()
                first_exception = min(first_exception, len(monotonic_stack))
                largest_exception = max(largest_exception, nums[i - 1])

            if num < largest_exception:
                last_exception = i

            monotonic_stack.append(num)

        if first_exception == math.inf: 
            return 0
        else: 
            return last_exception - first_exception + 1
        

exercise = Solution()

input = [2,6,4,8,10,9,15]

expected_output = 5

output = exercise.findUnsortedSubarray(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Solution by: Javi Barranco

# Problem:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000

import math

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        n, m = len(nums1), len(nums2)
        target = math.ceil((n + m) / 2)
        leftPart, rightPart = None, None
        l1, r1 = 0, len(nums1) - 1
        m1 = l1
        while True:
            m1 = l1 + int((r1 - l1) / 2)
            leftPart = nums1[0:m1 + 1]
            rightPart = nums2[0:target - len(leftPart)]
            rem = target - len(leftPart) - len(rightPart)
            if rem > 0: leftPart = leftPart + nums1[m1+1:(m1+1+rem)]
            if rem < 0: leftPart = leftPart[:rem]
            print(leftPart, rightPart)
            if rightPart and (len(nums1) > m1 + 1) and rightPart[-1] > nums1[m1 + 1]:
                l1 = l1 + 1
            elif leftPart and (len(nums2) > target - len(leftPart)) and (leftPart[-1] > nums2[target - len(leftPart)]):
                r1 = r1 - 1
            else:
                break

        if (n + m) % 2 == 1:
            return max(leftPart[-1] if leftPart else -math.inf, rightPart[-1] if rightPart else -math.inf)
        else:
            left = max(leftPart[-1] if leftPart else -math.inf, rightPart[-1] if rightPart else -math.inf)
            right = min(nums1[len(leftPart):][0] if len(nums1) > len(leftPart) else math.inf, nums2[len(rightPart):][0] if len(nums2) > len(rightPart) else math.inf)
            return (left + right) / 2
        

exercise = Solution()

input = [[1,2,3,4,5,8], [6,7]]

expected_output = 4.5

output = exercise.findMedianSortedArrays(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
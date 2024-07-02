# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii

# Solution by: Javi Barranco

# Problem:
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map, nums2_map = {}, {}
        res = []

        for num in nums1: nums1_map[num] = nums1_map.get(num, 0) + 1
        for num in nums2: nums2_map[num] = nums2_map.get(num, 0) + 1

        for k, v in nums1_map.items():
            if nums2_map.get(k, 0) != 0: 
                for i in range(min(v, nums2_map.get(k, 0))): 
                    res.append(k)

        return res
    

exercise = Solution()

input = [
    [1,2,2,1],
    [2,2]
]

expected_output = [2,2]

output = exercise.intersect(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
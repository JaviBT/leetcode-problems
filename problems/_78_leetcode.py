# 78. Subsets
# https://leetcode.com/problems/subsets

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        ret = [[]]
        self.subsetsRec(nums, ret)
        return ret
    
    def subsetsRec(self, nums: [int], sub: [[int]]) -> None:
        print(nums, sub)
        num = nums[0]
        for s in sub.copy():
            sub.append(s + [num])

        if len(nums) > 1:
            self.subsetsRec(nums[1:], sub)


exercise = Solution()

input = [1,2,3]

expected_output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

output = exercise.subsets(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
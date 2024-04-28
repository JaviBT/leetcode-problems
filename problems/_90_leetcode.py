# 90. Subsets II
# https://leetcode.com/problems/subsets-ii

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        ret = []
        self.subsetsWithDupRec(nums, [], ret)
        return ret

    def subsetsWithDupRec(self, nums: [int], sub: [int], ret: [[int]]) -> None:
        if not nums:
            sub.sort()
            if sub not in ret:
                ret.append(sub.copy())
            return
        
        num = nums[0]
        new_nums = nums[1:] if len(nums) > 1 else []

        new_sub = sub.copy()
        new_sub.append(num)
        self.subsetsWithDupRec(new_nums, new_sub.copy(), ret)
        new_sub.pop()
        self.subsetsWithDupRec(new_nums, new_sub.copy(), ret)


exercise = Solution()

input = [1,2,2]

expected_output = [[],[1],[1,2],[1,2,2],[2],[2,2]]

output = exercise.subsetsWithDup(input)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out in output:
    assert out in expected_output, "Wrong answer"
print("Accepted")
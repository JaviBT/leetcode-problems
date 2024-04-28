# 46. Permutations
# https://leetcode.com/problems/permutations

# Solution by: Javi Barranco

# Problem:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        ret = []
        self.permuteRec(nums, [], ret)
        return ret

    def permuteRec(self, nums: [int], perm: [int], ret: [[int]]) -> None:
        if len(nums) == 1: ret.append(perm + nums)

        for i in range(len(nums)):
            cur_nums = nums.copy()
            cur_nums.pop(i)
            cur_perm = perm + [nums[i]]
            self.permuteRec(cur_nums, cur_perm, ret)


exercise = Solution()

input = [1,2,3]

expected_output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

output = exercise.permute(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
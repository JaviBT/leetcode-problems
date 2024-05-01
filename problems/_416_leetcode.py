# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum

# Solution by: Javi Barranco

# Problem:
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

class Solution:
    def canPartition(self, nums: [int]) -> bool:
        if sum(nums) % 2 == 1: return False
        target = int(sum(nums) / 2)
        subsets = set()

        for i in range(len(nums) - 1, -1, -1):
            if not subsets: 
                subsets.add(nums[i])
                if nums[i] == target: return True
            else:
                for val in subsets.copy():
                    subsets.add(val + nums[i])
                    if val + nums[i] == target: return True

        return False
    

exercise = Solution()

input = [1,5,11,5]

expected_output = True

output = exercise.canPartition(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
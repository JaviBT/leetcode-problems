# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# Solution by: Javi Barranco

# Problem:
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example:
# Input: [1,2,3,1]
# Output: true

class Solution:
    def containsDuplicate(self, nums):
        exist_dict = {}

        for num in nums:
            if num in exist_dict.keys():
                return True
            else:
                exist_dict[num] = 1

        return False
    

exercise = Solution()

input = [1,2,3,1]

expected_output = True

output = exercise.containsDuplicate(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
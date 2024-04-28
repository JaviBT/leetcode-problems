# 136. Single Number
# https://leetcode.com/problems/single-number/

# Solution by: Javi Barranco

# Problem:
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Example:
# Input: [2,2,1]
# Output: 1

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


class Solution2:
    def singleNumber(self, nums: [int]) -> int:
        
        dic = {}

        for n in nums:
            if n not in dic.keys():
                dic[n] = 0
            dic[n] += 1

            if dic[n] == 2:
                dic.pop(n)
        
        return list(dic.keys())[0]


exercise = Solution()

input = [2,2,1]
expected_output = 1

output = exercise.singleNumber(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

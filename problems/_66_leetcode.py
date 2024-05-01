# 66. Plus One
# https://leetcode.com/problems/plus-one

# Solution by: Javi Barranco

# Problem:
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        
        for i in range(len(digits)):
            if digits[-i - 1] + 1 == 10: 
                digits[-i - 1] = 0
                carry = 1
            else:
                digits[-i - 1] += 1
                return digits
        digits = [1] + digits

        return digits
    

exercise = Solution()

input = [1,2,3]

expected_output = [1,2,4]

output = exercise.plusOne(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 258. Add Digits
# https://leetcode.com/problems/add-digits/

# Solution by: Javi Barranco

# Problem:
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2.
# Since 2 has only one digit, return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 >= 1:
            digits = [ int(digit) for digit in str(num) ]
            num = sum(digits)
        
        return num
    

exercise = Solution()

input = 38

expected_output = 2

output = exercise.addDigits(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
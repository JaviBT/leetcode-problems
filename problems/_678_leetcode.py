# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string

# Solution by: Javi Barranco

# Problem:
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Any right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# Example:
# Input: s = "*)()*)(*"
# Output: true

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            if c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            if c == '*':
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False

        return leftMin == 0
    

exercise = Solution()

input = "*)()*)(*"

expected_output = True

output = exercise.checkValidString(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
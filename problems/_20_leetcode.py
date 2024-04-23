# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# Solution by: Javi Barranco

# Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example:
# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(': return False
            elif char == ']':
                if not stack or stack.pop() != '[': return False
            elif char == '}':
                if not stack or stack.pop() != '{': return False

        return True if not stack else False
    

exercise = Solution()

input = "()"

expected_output = True

output = exercise.isValid(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
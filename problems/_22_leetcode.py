# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

# Solution by: Javi Barranco

# Problem:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        stack = []
        combinations = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                combinations.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return combinations
    

exercise = Solution()

input = 3

expected_output = ["((()))","(()())","(())()","()(())","()()()"]

output = exercise.generateParenthesis(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
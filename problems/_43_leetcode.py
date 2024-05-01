# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/

# Solution by: Javi Barranco

# Problem:
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1Digits = [int(c) * 10**(len(num1) - i - 1) for i, c in enumerate([c for c in num1])]
        num2Digits = [int(c) * 10**(len(num2) - i - 1) for i, c in enumerate([c for c in num2])]

        res = 0
        for a in num1Digits:
            for b in num2Digits:
                res += (a * b)

        return str(res)
    

exercise = Solution()

input = ["123", "456"]

expected_output = "56088"

output = exercise.multiply(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 263. Ugly Number
# https://leetcode.com/problems/ugly-number

# Solution by: Javi Barranco

# Problem:
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

# Example 1:
# Input: n = 6
# Output: true

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False

        while n % 5 == 0: n /= 5
        while n % 3 == 0: n /= 3
        while n % 2 == 0: n /= 2

        return n == 1
    

exercise = Solution()

input = 6

expected_output = True

output = exercise.isUgly(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
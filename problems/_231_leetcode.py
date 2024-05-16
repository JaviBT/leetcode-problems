# 231. Power of Two
# https://leetcode.com/problems/power-of-two

# Solution by: Javi Barranco

# Problem:
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2^x.

# Example 1:
# Input: n = 1024
# Output: true

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        if n <= 0: return False

        while n > 1:
            if n % 2 != 0: return False
            n /= 2

        return True
    

exercise = Solution()

input = 1024

expected_output = True

output = exercise.isPowerOfTwo(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
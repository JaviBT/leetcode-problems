# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Solution by: Javi Barranco

# Problem:
# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

# Example:
# Input: 00000000000000000000000000001011
# Output: 3

from math import log

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        while n > 0:
            i = int(log(n, 2))
            n = n - 2**i
            count += 1

        return count
    

exercise = Solution()

input = 11
expected_output = 3

output = exercise.hammingWeight(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

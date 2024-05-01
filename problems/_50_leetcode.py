# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n

# Solution by: Javi Barranco

# Problem:
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive(x: float, n: int) -> float:
            if x == 0: return 0
            if n == 0: return 1

            res = recursive(x, n // 2)
            res = res * res
            return x * res if n % 2 == 1 else res
        
        res = recursive(x, abs(n))
        return res if n >= 0 else 1 / res


class Solution2: # Brute force solution
    def myPow(self, x: float, n: int) -> float:
        if n < 0: 
            x = 1 / x
            n = abs(n)
        if n == 1: return x
        
        return self.myPow(x, math.ceil(n / 2)) * self.myPow(x, math.floor(n /2))
    

exercise = Solution()

input = [2.00000, 10]

expected_output = 1024.00000

output = exercise.myPow(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
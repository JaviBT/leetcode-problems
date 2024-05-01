# 202. Happy Number
# https://leetcode.com/problems/happy-number/

# Solution by: Javi Barranco

# Problem:
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        
        current = n
        visited = [n]

        while True:
            digits = [char for char in str(current)]

            current = 0
            for digit in digits:
                current += int(digit)**2
            
            if current == 1:
                return True

            if current in visited: return False
            else: visited.append(current)


class Solution2:
    def isHappy(self, n: int) -> bool:
        
        current = n
        iters = 0

        while True:
            digits = [char for char in str(current)]

            current = 0
            for digit in digits:
                current += int(digit)**2

            if current == 1:
                return True

            iters += 1
            if iters >= 500 or current >= 1000000: return False


class Solution3:
    def isHappy(self, n: int) -> bool:
        loopsLim = 10
        
        while loopsLim > 0:
            m = 0
            digits = self.getDigits(n)
            if sum(digits) == 1: return True
            for digit in digits:
                m += digit ** 2
            n = m

            loopsLim -= 1

        return False
    
    def getDigits(self, n: int) -> [int]:
        digits = []

        while n > 0:
            digits.append(n % 10)
            n = n // 10

        return digits


exercise = Solution()
input = 19
expected_output = True
output = exercise.isHappy(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

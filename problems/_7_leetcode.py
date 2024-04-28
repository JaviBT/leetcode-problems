# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer

# Solution by: Javi Barranco

# Problem:
# Given a 32-bit signed integer, reverse digits of an integer.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

# Example:
# Input: x = 123
# Output: 321

class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)

        while x != 0:
            if (reverse > max_int // 10) or (reverse == max_int // 10 and ((x % 10) if x > 0 else -(abs(x) % 10)) >= max_int % 10):
                return 0
            if (reverse < min_int // 10) or (reverse == min_int // 10 and ((x % 10) if x > 0 else -(abs(x) % 10)) <= min_int % 10):
                return 0

            reverse = (reverse * 10) + ((x % 10) if x > 0 else -(abs(x) % 10))
            x = int(x / 10)

        return reverse
    

exercise = Solution()

input = 123

expected_output = 321

output = exercise.reverse(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
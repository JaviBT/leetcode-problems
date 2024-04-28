# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers

# Solution by: Javi Barranco

# Problem:
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
    

class Solution2:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])
    

exercise = Solution()

input = [1, 2]

expected_output = 3

output = exercise.getSum(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
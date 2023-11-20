# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/

# Solution by: Javi Barranco

# Problem:
# Reverse bits of a given 32 bits unsigned integer.

# Example:
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000

from math import log

class Solution:
    def reverseBits(self, n: int) -> int:
        
        p = 0
        sum = 0

        string = '0'*32
        while n > 0:
            index = int(log(n, 2))
            string = string[:index] + '1' + string[index+1:]
            n = n - 2**int(log(n, 2))

        for i in range(len(string)):
            val = int(string[-1-i])
            if val == 1: sum += 2 ** p
            p += 1
        
        return sum

class Solution2:
    def reverseBits(self, n: int) -> int:
        
        p = 0
        sum = 0

        vals = []
        while n > 0:
            vals.append(int(log(n, 2)))
            n = n - 2**int(log(n, 2))
        string = ''
        for i in range(0, 32):
            if i in vals: string += '1'
            else: string += '0'

        for i in range(len(string)):
            val = int(string[-1-i])
            if val == 1: sum += 2 ** p
            p += 1
        
        return sum
    

exercise = Solution()

input = 43261596
expected_output = 964176192

output = exercise.reverseBits(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

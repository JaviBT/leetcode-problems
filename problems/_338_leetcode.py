# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/

# Solution by: Javi Barranco

# Problem:
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example:
# Input: 12
# Output: [0,1,1,2,1,2,2,3,1,2,2,3,2]

class Solution:
    def countBits(self, n: int) -> [int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i: offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
    

class Solution2:
    def countBits(self, n: int) -> [int]:
        return [i.bit_count() for i in range(n+1)]
    

class Solution3:
    def countBits(self, n: int) -> [int]:
        ans = []
        for i in range(n + 1):
            ans.append(0)
            j = i
            while j != 0:
                j &= j-1
    

exercise = Solution()

input = 12

expected_output = [0,1,1,2,1,2,2,3,1,2,2,3,2]

output = exercise.countBits(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
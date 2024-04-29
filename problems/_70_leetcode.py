# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs

# Solution by: Javi Barranco

# Problem:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example:
# Input: n = 2
# Output: 2

class Solution: # Dynamic Programming (Memoization)
    def climbStairs(self, n: int) -> int:
        dp = [None] * n

        def backtrack(count: int) -> int:
            if count == n:
                return 1
            if count > n:
                return 0

            if dp[count] == None: 
                dp[count] = backtrack(count + 1) + backtrack(count + 2)
           
            return dp[count]
            
        backtrack(0)
        return dp[0]


class Solution2: # Brute Force (Recursion)
    def climbStairs(self, n: int) -> int:
        count = [0]

        def backtrack(rem: int):
            if rem < 0: 
                return
            elif rem == 0:
                count[0] += 1
                return

            backtrack(rem - 1)
            backtrack(rem - 2)

        backtrack(n)
        return count[0]
    

exercise = Solution()

input = 2

expected_output = 2

output = exercise.climbStairs(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
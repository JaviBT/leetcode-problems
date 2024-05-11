# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii

# Solution by: Javi Barranco

# Problem:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4

from typing import List

class Solution: # Dynamic programming solution with O(n * m) time complexity and O(n) space complexity
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            
            dp = nextDP

        return dp[amount]
    

class Solution2: # Memoization solution with O(n * m) time complexity
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
    
        def dfs(i: int, cur: int):
            if (i, cur) in dp: return dp[(i, cur)]
            if cur == amount: return 1
            if not coins or cur > amount: return 0

            res = 0
            for j in range(len(coins) - i):
                res += dfs(i + j, cur + coins[i + j])

            dp[(i, cur)] = res
            return res

        return dfs(0, 0)


class Solution3: # Non-dynamic programming solution (DFS) will Time Limit Exceeded
    def change(self, amount: int, coins: List[int]) -> int:
    
        def dfs(cur: int):
            if cur == amount: return 1
            if not coins or cur > amount: return 0

            res = 0
            res += dfs(cur + coins[-1])
            tmp = coins.pop()
            res += dfs(cur)
            coins.append(tmp)

            return res

        return dfs(0)
    

exercise = Solution()

input = (5, [1,2,5])

expected_output = 4

output = exercise.change(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
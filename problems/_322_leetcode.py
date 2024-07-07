# 322. Coin Change
# https://leetcode.com/problems/coin-change

# Solution by: Javi Barranco

# Problem:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3

from typing import List
import math

class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[(i - coin)])

        return dp[-1] if dp[-1] != math.inf else -1
    
    
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        for i in range(amount + 1):
            for coin in coins:
                if i - coin in memo:
                    memo[i] = min(memo.get(i, math.inf), memo.get(i - coin) + 1)

        return memo.get(amount, -1)
    

exercise = Solution()

input = [1, 2, 5], 11

expected_output = 3

output = exercise.coinChange(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
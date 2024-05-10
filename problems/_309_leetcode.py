# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Solution by: Javi Barranco

# Problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def maxProfitRec(i: int, buying: bool):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cd = maxProfitRec(i + 1, buying)
            if buying:
                buy = maxProfitRec(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(cd, buy)
            else:
                sell = maxProfitRec(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(cd, sell)

            return dp[(i, buying)]

        return maxProfitRec(0, True)
    

exercise = Solution()

input = [1,2,3,0,2]

expected_output = 3

output = exercise.maxProfit(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
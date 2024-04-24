# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution by: Javi Barranco

# Problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        best_profit = 0
        best_buy = prices[0]

        for price in prices:
            best_buy = min(best_buy, price)
            best_profit = max(best_profit, price - best_buy)

        return best_profit


class Solution2: # Brute force
    def maxProfit(self, prices: [int]) -> int:
        best_delta = 0

        for i, buy in enumerate(prices):
            for sell in prices[i+1:]:
                delta = sell - buy
                if delta > best_delta: best_delta = delta

        return best_delta


class Solution3:
    def maxProfit(self, prices: [int]) -> int:
        best_delta = 0
        best_buy = prices[0]

        for price in prices:
            best_delta = max(best_delta, price - best_buy)
            best_buy = min(best_buy, price)

        return best_delta


exercise = Solution()
input = [7,1,5,3,6,4]
expected_output = 5
output = exercise.maxProfit(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

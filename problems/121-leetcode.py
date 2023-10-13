# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        best_profit = 0
        best_buy = prices[0]

        for price in prices:
            best_buy = min(best_buy, price)
            best_profit = max(best_profit, price - best_buy)

        return best_profit
    

exercise = Solution()
input = [7,1,5,3,6,4]
expected_output = 5
output = exercise.maxProfit(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        current_buy = -1
        total_profit = 0
        
        for price in prices:
            if (price > current_buy and current_buy != -1):
                total_profit += price - current_buy
            current_buy = price

        return total_profit
    

exercise = Solution()
input = [7,1,5,3,6,4]
expected_output = 7
output = exercise.maxProfit(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

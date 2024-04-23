# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# Solution by: Javi Barranco

# Problem:
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        output = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temp_pop, index_pop = stack.pop()
                output[index_pop] = i - index_pop
            stack.append([temp, i])

        return output


class Solution: # Timeout at 35/48 test cases
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        stack = []
        aux = []
        output = []

        for i, temp in enumerate(temperatures[-1::-1]):
            if i == 0: # First Step
                output.append(0)
                stack.append(temp)
            else: # Other Steps
                j = 0
                while stack: # While the stack isn't empty
                    ele = stack.pop()
                    j += 1
                    aux.append(ele)
                    if ele > temp:
                        output.append(j)
                        break
                if len(output) < i + 1: output.append(0)
                while aux:
                    stack.append(aux.pop())
                stack.append(temp)

        return output[-1::-1]
    

exercise = Solution()

input = [73,74,75,71,69,72,76,73]

expected_output = [1,1,4,2,1,1,0,0]

output = exercise.dailyTemperatures(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

# Solution by: Javi Barranco

class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        
        nums.sort() # O(nlog(n))
        output = 0
        count = 0
        currentNum = None

        for n in nums:
            if currentNum == None or n == currentNum + 1:
                count += 1
                output = max(output, count)
            elif n == currentNum:
                continue # Repeating number doesn't break sequence
            else:
                count = 1
            currentNum = n

        return output
        

exercise = Solution()
input = [100,4,200,1,3,2]
expected_output = 4
output = exercise.longestConsecutive(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

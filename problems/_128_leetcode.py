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
        

class Solution2:
    def longestConsecutive(self, nums: [int]) -> int:
        nums.sort() # nlog(n)

        current = 0
        longest = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] - 1 == nums[i-1]:
                current += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                current = 1
            longest = max(longest, current)
        
        return longest
    

class Solution3:
    def longestConsecutive(self, nums: [int]) -> int:
        nums_set = set(nums) # We use this set to check if a number is in the list in O(1) time

        best = 0
        for num in nums:
            # Check if this num is the start of a sequence
            if num - 1 not in nums_set:
                current = 1
                i = 1
                while num + i in nums_set:
                    current += 1
                    i += 1
                best = max(best, current)

        return best
    

exercise = Solution()
input = [100,4,200,1,3,2]
expected_output = 4
output = exercise.longestConsecutive(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

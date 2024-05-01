# 139. Word Break
# https://leetcode.com/problems/word-break/

# Solution by: Javi Barranco

# Problem:
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        dp = [None] * len(s)

        def wordBreakRec(s: str) -> bool:
            if s == '': return True
            if dp[len(dp) - len(s)] == False: return False

            for word in wordDict:
                if (len(s) >= len(word)) and (s[:len(word)] == word):
                    res = wordBreakRec(s[len(word):])
                    if res: return res

            dp[len(dp) - len(s)] = False
            return False

        return wordBreakRec(s)
    

class Solution: # Brute force solution
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        
        def wordBreakRec(s: str) -> bool:
            if s == '': return True

            for word in wordDict:
                if (len(s) >= len(word)) and (s[:len(word)] == word):
                    res = wordBreakRec(s[len(word):])
                    if res: return res

            return False

        return wordBreakRec(s)
    

exercise = Solution()

input = "leetcode"
wordDict = ["leet","code"]

expected_output = True

output = exercise.wordBreak(input, wordDict)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
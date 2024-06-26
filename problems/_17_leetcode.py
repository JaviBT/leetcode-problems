# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Solution by: Javi Barranco

# Problem:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        DICT = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        ret = []

        def dfs(i, cur):
            if len(cur) >= len(digits):
                ret.append(cur)
                return

            for char in DICT[digits[i]]:
                dfs(i+1, cur + char)

        if digits: dfs(0, '')
        return ret
    

class Solution2:
    def letterCombinations(self, digits: str) -> [str]:
        DICT = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        ret = []
        cur = []

        def dfs(i):
            if len(cur) >= len(digits):
                if cur: ret.append(''.join(cur))
                return

            for char in DICT[digits[i]]:
                cur.append(char)
                dfs(i+1)
                cur.pop()

        dfs(0)
        return ret
    

exercise = Solution()

input = "23"

expected_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

output = exercise.letterCombinations(input)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out in output:
    assert out in expected_output, "Wrong answer"
print("Accepted")
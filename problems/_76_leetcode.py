# 76. MInimun Window Substring
# https://leetcode.com/problems/minimum-window-substring/

# Solution by: Javi Barranco

# Problem:
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# Example:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_substring = s + t

        sub_dict = {}
        t_dict = {}
        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)
        have, need = 0, len(t_dict.keys())

        l = 0
        for r in range(len(s)):
            # Add char
            char = s[r]
            sub_dict[char] = 1 + sub_dict.get(char, 0)
            if char in t_dict and sub_dict[char] == t_dict[char]: have += 1

            while have == need:
                if r - l + 1 <= len(best_substring): 
                    best_substring = s[l:r+1]
                # Remove char 
                char = s[l]
                sub_dict[char] -= 1
                l += 1
                if char in t_dict and sub_dict[char] == t_dict[char] - 1: have -= 1
        
        if best_substring == s + t: return ''
        return best_substring 
    

class Solution2: # Not optimal solution
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        char_map = {} # char : count (inside current window)
        min_len = math.inf
        res = ''

        for char in t:
            char_map[char] = char_map.get(char, 0) + 1

        while r < len(s): # This loop is O(n)
            cur = s[r]
            if cur in char_map:
                char_map[cur] -= 1

            # Update min. window if all char have count <= 0
            update_l = False
            for i, (key, val) in enumerate(char_map.items()):
                if val > 0: 
                    break
                if i == len(char_map.items()) - 1: 
                    if r - l + 1 < min_len:
                        res = s[l:r+1]
                        min_len = r - l + 1
                    update_l = True

            if update_l:
                while l <= r and (s[l] not in char_map or char_map[s[l]] + 1 <= 0):
                    if s[l] in char_map: char_map[s[l]] += 1
                    l += 1
                    if r - l + 1 < min_len:
                        res = s[l:r+1]
                        min_len = r - l + 1

            r += 1
        
        return res
    

exercise = Solution()

input = ["ADOBECODEBANC", "ABC"]

expected_output = "BANC"

output = exercise.minWindow(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
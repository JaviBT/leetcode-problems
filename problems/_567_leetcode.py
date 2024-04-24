# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

# Solution by: Javi Barranco

# Problem:
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_dict = {}
        s2_dict = {}

        # Load s1_dict
        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char, 0)

        for r in range(len(s2)):
            char = s2[r]
            if char not in s1_dict.keys():
                l = r + 1
                s2_dict = {}
            else:
                s2_dict[char] = 1 + s2_dict.get(char, 0)
                if s2_dict[char] > s1_dict[char]:
                    while s2_dict[char] > s1_dict[char]:
                        s2_dict[s2[l]] -= 1
                        l += 1
                # Check if permutation was found
                flag = True
                for key, val in s1_dict.items():
                    if s2_dict.get(key, 0) != val: 
                        flag = False
                        break
                if flag: return True

        return False
    

exercise = Solution()

input = ["ab", "eidbaooo"]

expected_output = True

output = exercise.checkInclusion(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
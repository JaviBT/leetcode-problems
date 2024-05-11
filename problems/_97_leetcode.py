# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string

# Solution by: Javi Barranco

# Problem:
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

class Solution: # Backtracking solution with O(n + m) time complexity
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        memo = set()
        
        def backtrack(i: int, j: int, k: int) -> bool:
            if i == len(s1) and j == len(s2) and k == len(s3): return True
            if (i, j, k) in memo: return False

            if i < len(s1) and s1[i] == s3[k] and backtrack(i + 1, j, k + 1): return True
            if j < len(s2) and s2[j] == s3[k] and backtrack(i, j + 1, k + 1): return True

            memo.add((i, j, k))
            return False

        return backtrack(0, 0, 0)
    

class Solution2: 
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = set()
        
        def backtrack(i: int, j: int, k: int) -> bool:
            if i == len(s1) and j == len(s2) and k == len(s3): return True
            if (i, j, k) in memo: return False

            for d in range(len(s1[i:])):
                if s3[k:k+1+d] == s1[i:i+1+d]:
                    if backtrack(i + 1 + d , j, k + 1 + d): return True

            for d in range(len(s2[j:])):
                if s3[k:k+1+d] == s2[j:j+1+d]:
                    if backtrack(i, j + 1 + d, k + 1 + d): return True

            memo.add((i, j, k))
            return False

        return backtrack(0, 0, 0)
    

exercise = Solution()

input = ("aabcc", "dbbca", "aadbbcbcac")

expected_output = True

output = exercise.isInterleave(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
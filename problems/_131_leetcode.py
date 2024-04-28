# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning

# Solution by: Javi Barranco

# Problem:
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

class Solution:
    def partition(self, s: str) -> [[str]]:
        ret = []
        part = []

        def dfs(i):
            if i >= len(s):
                ret.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return ret

    def isPalindrome(self, word: str) -> bool:
        for i in range(int(len(word)/2)):
            if word[i] != word[-i - 1]: return False
        return True
    

class Solution2_better:
    def partition(self, s: str) -> [[str]]:
        ret = []

        def partitionRec(palindromes: [str], s: str) -> None:
            if not s:
                ret.append(palindromes)
                return

            for i in range(len(s)):
                if self.isPalindrome(s[:i+1]):
                    new_palindromes = palindromes.copy()
                    new_palindromes.append(s[:i+1])
                    new_s = s[i+1:]
                    partitionRec(new_palindromes, new_s)

        partitionRec([], s)
        return ret

    def isPalindrome(self, word: str) -> bool:
        for i in range(int(len(word)/2)):
            if word[i] != word[-i - 1]: return False
        return True
    

class Solution2:
    def partition(self, s: str) -> [[str]]:
        ret = []

        def partitionRec(palindromes: [str], s: str) -> None:
            if not self.allPalindrome(palindromes): 
                return
            elif not s:
                ret.append(palindromes)
                return

            for i in range(len(s)):
                new_palindromes = palindromes.copy()
                new_palindromes.append(s[:i+1])
                new_s = s[i+1:]
                partitionRec(new_palindromes, new_s)

        partitionRec([], s)
        return ret

    def isPalindrome(self, word: str) -> bool:
        for i in range(int(len(word)/2)):
            if word[i] != word[-i - 1]: return False
        return True

    def allPalindrome(self, words: [str]) -> bool:
        for word in words:
            if not self.isPalindrome(word): return False
        return True
    

class Solution3: # Brute force solution
    def partition(self, s: str) -> [[str]]:
        ret = []

        def partitionRec(parts: [str]) -> None:
            for i in range(len(parts)):
                string = parts[i]
                if len(string) > 1:
                    for j in range(len(string) - 1):
                        new_parts = parts.copy()
                        new_parts.insert(i+1, string[:j+1])
                        new_parts.insert(i+2, string[j+1:])
                        new_parts.pop(i)
                        partitionRec(new_parts)

            if self.allPalindrome(parts):
                if parts not in ret:
                    ret.append(parts)

        partitionRec([s])
        return ret

    def isPalindrome(self, word: str) -> bool:
        for i in range(int(len(word)/2)):
            if word[i] != word[-i - 1]: return False
        return True

    def allPalindrome(self, words: [str]) -> bool:
        for word in words:
            if not self.isPalindrome(word): return False
        return True
    

exercise = Solution()

input = "aab"

expected_output = [["a","a","b"],["aa","b"]]

output = exercise.partition(input)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out in output:
    assert out in expected_output, "Wrong answer"
print("Accepted")
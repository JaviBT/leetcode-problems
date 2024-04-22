# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

# Solution by: Javi Barranco

# Problem:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example:
# Input: "A man, a plan, a canal: Panama"
# Output: true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        string = ''.join([x for x in string if x.isalnum()])
        
        for i in range(int(len(string)/2)):
            if (string[i] != string[-i - 1]): 
                return False
                
        return True
    

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([x for x in s.lower() if x.isalnum()])
        
        for i in range(int(len(s)/2)):
            if s[i] != s[-i-1]: return False

        return True
    

exercise = Solution()
input = "A man, a plan, a canal: Panama"
expected_output = True
output = exercise.isPalindrome(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")


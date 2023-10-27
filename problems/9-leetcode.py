# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# Solution by: Javi Barranco

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)

        for i in range(int(len(y)/2)):
            if y[i] != y[-i - 1]: return False

        return True
    

exercise = Solution()
input = 121
expected_output = True
output = exercise.isPalindrome(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

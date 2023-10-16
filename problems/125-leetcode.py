# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        string = ''.join([x for x in string if x.isalnum()])
        
        for i in range(int(len(string)/2)):
            if (string[i] != string[-i - 1]): 
                return False
                
        return True
    

exercise = Solution()
input = "A man, a plan, a canal: Panama"
expected_output = True
output = exercise.isPalindrome(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")


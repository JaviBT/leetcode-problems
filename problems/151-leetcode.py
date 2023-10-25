# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split(' ')
        wordList.reverse()
        string = ''

        for word in wordList:
            if word == '': continue
            string += word + ' '
        
        return string[:-1]
    

exercise = Solution()
input = "  hello world!  "
expected_output = "world! hello"
output = exercise.reverseWords(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

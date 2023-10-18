# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        translator = {}

        word_list = s.split(' ')
        if len(pattern) != len(word_list): return False

        for i in range(len(pattern)):
            if pattern[i] not in translator.keys():
                if word_list[i] in translator.values(): return False
                translator[pattern[i]] = word_list[i]
        
        for i in range(len(pattern)):
            if word_list[i] != translator[pattern[i]]: return False

        return True
    

exercise = Solution()
input = "abba"
input2 = "dog cat cat dog"
expected_output = True
output = exercise.wordPattern(input, input2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

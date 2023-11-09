# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        translator = {}

        for i in range(len(s)):
            if s[i] not in translator.keys():
                if t[i] in translator.values(): return False
                translator[s[i]] = t[i]
            else:
                if translator[s[i]] != t[i]: return False                    

        return True
    

exercise = Solution()
input = "egg"
input2 = "add"
expected_output = True
output = exercise.isIsomorphic(input, input2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

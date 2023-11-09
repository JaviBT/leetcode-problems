# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        isHere = True

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + len(needle) > len(haystack): continue
                isHere = True
                for j in range(i, i + len(needle)):
                    if haystack[j] != needle[j - i]: isHere = False
                if isHere: return i

        return -1


exercise = Solution()
input = "hello"
needle = "ll"
expected_output = 2
output = exercise.strStr(input, needle)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

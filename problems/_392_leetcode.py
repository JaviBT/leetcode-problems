# 393. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        pointer = 0

        for char in t:
            if char == s[pointer]:
                pointer += 1

                if pointer >= len(s):
                    return True

        return False
    

exercise = Solution()
input = "abc"
input2 = "ahbgdc"
expected_output = True
output = exercise.isSubsequence(input, input2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

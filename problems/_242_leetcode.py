# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_count = {}

        for char in s:
            if char not in char_count.keys():
                char_count[char] = 1
            else:
                char_count[char] += 1

        for char in t:
            if char not in char_count.keys(): return False
            else:
                char_count[char] -= 1
                if char_count[char] < 0: return False

        for value in char_count.values():
            if value != 0: return False

        return True
    

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        char_sum = {}

        for i in range(len(s)):
            s_char, t_char = s[i], t[i]

            if s_char in char_sum.keys():
                char_sum[s_char] += 1
            else:
                char_sum[s_char] = 1

            if t_char in char_sum.keys():
                char_sum[t_char] -= 1
            else:
                char_sum[t_char] = -1

        for val in char_sum.values():
            if val != 0: return False

        return True
    

exercise = Solution()
input = "anagram"
input2 = "nagaram"
expected_output = True
output = exercise.isAnagram(input, input2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

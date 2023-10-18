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
    

exercise = Solution()
input = "anagram"
input2 = "nagaram"
expected_output = True
output = exercise.isAnagram(input, input2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

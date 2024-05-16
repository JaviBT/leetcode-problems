# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number

# Solution by: Javi Barranco

# Problem:
# Given a string columnTitle that represents the column title as it appears in an Excel sheet, return its corresponding column number.

# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# Example 1:
# Input: columnTitle = "ZY"
# Output: 701

import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        char_map = { char: i + 1 for i, char in enumerate(string.ascii_uppercase) }

        digits = [ char_map[char] for char in columnTitle[::-1] ]
        values = [ pow(26, i) * digit for i, digit in enumerate(digits) ]
        
        return sum(values)
    

exercise = Solution()

input = "ZY"

expected_output = 701

output = exercise.titleToNumber(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
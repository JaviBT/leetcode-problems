# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

# Solution by: Javi Barranco

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s): return s

        rows = [[] for row in range(numRows)]
        zig = True
        index = 0
        string = ''

        for i in range(len(s)):
            rows[index].append(s[i])

            if zig == True:
                index += 1
            else:
                index -= 1

            if index == numRows - 1:
                zig = False
            elif index == 0:
                zig = True

        for row in rows:
            string += "".join(row)

        return string

class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        n = len(s)
        cols = []
        index = 0
        string = ''

        while index < n:
            cols.append(s[index:index + numRows].ljust(numRows))
            index += numRows
            
            for i in range(numRows - 2):
                if index >= n: break
                newCol = [" " for j in range(numRows)]
                newCol[numRows - i - 2] = s[index]
                cols.append("".join(newCol))
                index += 1
        
        for i in range(numRows):
            for col in cols:
                string += col[i]

        return string.replace(" ", "")
    
class Solution3:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        row = []
        row_i = 1
        zig = True
        string = ""

        while len(row) < len(s):
            row.append(row_i)
            if zig == True:
                row_i += 1
            else:
                row_i -= 1
            if row_i == numRows: zig = False
            if row_i == 1: zig = True

        index = 1
        while index <= numRows:
            for i in range(len(s)):
                if row[i] == index:
                    string += s[i]
            index += 1

        return string


exercise = Solution()
input = ["PAYPALISHIRING", 3]
expected_output = "PAHNAPLSIIGYIR"
output = exercise.convert(input[0], input[1])
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

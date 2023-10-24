# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        sol = ''

        diff = len(a) - len(b)
        if diff < 0:
            a = '0' * abs(diff) + a
        else:
            b = '0' * abs(diff) + b
        
        for i in range(1, max(len(a),len(b)) + 1):
            current = int(a[-i]) + int(b[-i]) + carry
            if current >= 2:
                carry = 1
            else:
                carry = 0
            current = current % 2
            sol = '{}'.format(str(current)) + sol

        if carry == 1:
            sol = '1' + sol

        return sol


exercise = Solution()
input = ["11", "1"]
expected_output = "100"
output = exercise.addBinary(input[0], input[1])
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

# 12. Integer to Roman
from math import floor

class Solution:
    def intToRoman(self, num: int) -> str:
        
        digits = len(str(num))
        remaining = num
        string = ''

        translator = {
            1: 'I', 4: 'IV',  5: 'V',  9: 'IX',  10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',  500: 'D', 900: 'CM', 1000: 'M',
        }

        for i in range(digits-1,-1,-1):
            divisor = 10 ** i
            current_val = floor(remaining / divisor) * divisor
            remaining = remaining % divisor

            # Turn number to string
            new_chars = ''
            if current_val not in translator.keys():
                mult = int(current_val / divisor)
                mult_1 = mult % 5
                mult_5 = int(mult / 5)
                if mult_5 != 0: new_chars += (translator[5 * divisor] * mult_5)
                if mult_1 != 0: new_chars += (translator[1 * divisor] * mult_1)   
            else:
                new_chars += translator[current_val]

            string += new_chars
        
        return string
    

exercise = Solution()
input = 1994
expected_output = "MCMXCIV"
output = exercise.intToRoman(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

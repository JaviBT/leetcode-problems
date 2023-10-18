# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        current = n
        visited = [n]

        while True:
            digits = [char for char in str(current)]

            current = 0
            for digit in digits:
                current += int(digit)**2
            
            if current == 1:
                return True

            if current in visited: return False
            else: visited.append(current)

class Solution2:
    def isHappy(self, n: int) -> bool:
        
        current = n
        iters = 0

        while True:
            digits = [char for char in str(current)]

            current = 0
            for digit in digits:
                current += int(digit)**2

            if current == 1:
                return True

            iters += 1
            if iters >= 500 or current >= 1000000: return False


exercise = Solution()
input = 19
expected_output = True
output = exercise.isHappy(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

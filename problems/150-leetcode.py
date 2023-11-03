# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Solution by: Javi Barranco

class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        
        stack = []
        
        for token in tokens:
            if (token not in ['+', '-', '*', '/']):
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+': c = a + b
                elif token == '-': c = a - b
                elif token == '*': c = a * b
                elif token == '/': c = int(a / b)
                stack.append(c)
        
        return int(stack.pop())


exercise = Solution()
input = ["2","1","+","3","*"]
expected_output = 9
output = exercise.evalRPN(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

# 155. Min Stack
# https://leetcode.com/problems/min-stack

# Solution by: Javi Barranco

# Problem:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# - MinStack() initializes the stack object.
# - void push(val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == None or val < self.min: self.min = val

    def pop(self) -> None:
        val = self.stack[-1]
        self.stack = self.stack[:len(self.stack)-1]
        if val == self.min:
            if not self.stack: self.min = None
            else: self.min = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
    

exercise = MinStack()

commands = ["MinStack","push","push","push","getMin","pop","top","getMin"]
inputs = [[],[-2],[0],[-3],[],[],[],[]]

expected_output = [None,None,None,None,-3,None,0,-2]

output = []
for i in range(len(commands)):
    if commands[i] == "push":
        output.append(exercise.push(*inputs[i]))
    elif commands[i] == "pop":
        output.append(exercise.pop())
    elif commands[i] == "top":
        output.append(exercise.top())
    elif commands[i] == "getMin":
        output.append(exercise.getMin())
    else:
        output.append(None)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out, exp in zip(output, expected_output):
    assert out == exp, "Wrong answer"
print("Accepted")
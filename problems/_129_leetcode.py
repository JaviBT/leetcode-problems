# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

# Example:
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25

# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: [TreeNode]) -> int:

        def listNumbers(root: [TreeNode]) -> [str]:
            if root == None: return

            current_list = []

            new_left = listNumbers(root.left)
            if new_left != None: 
                for path in new_left: current_list.append(path)

            new_right = listNumbers(root.right)
            if new_right != None:
                for path in new_right: current_list.append(path)

            if not current_list: current_list.append(str(root.val))
            else:
                print(current_list)
                for i in range(len(current_list)):
                    current_list[i] = str(root.val) + current_list[i]

            return current_list

        output = 0
        for path in listNumbers(root):
            output += int(path)
        return output


exercise = Solution()

input = TreeNode(1, TreeNode(2), TreeNode(3))
expected_output = 25

output = exercise.sumNumbers(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

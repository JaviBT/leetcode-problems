# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/

# Solution by: Javi Barranco

# Problem:
# Given a complete binary tree, count the number of nodes.
# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as
# far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:
# Input:
#       1
#      / \
#     2   3
#    / \  /
#   4  5 6

# Output: 6

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: [TreeNode]) -> int:
        return 0 if root == None else 1 + self.countNodes(root.left) + self.countNodes(root.right)


exercise = Solution()

input = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
expected_output = 6

output = exercise.countNodes(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

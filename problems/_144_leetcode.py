# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Solution by: Javi Barranco

# Problem:
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node: Optional[TreeNode]):
            if node is None: return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res
    

exercise = Solution()

input = TreeNode(1, None, TreeNode(2, TreeNode(3)))

expected_output = [1,2,3]

output = exercise.preorderTraversal(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
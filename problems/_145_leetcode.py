# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Solution by: Javi Barranco

# Problem:
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node: Optional[TreeNode]):
            if node is None: return

            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res
    

exercise = Solution()

input = TreeNode(1, None, TreeNode(2, TreeNode(3)))

expected_output = [3,2,1]

output = exercise.postorderTraversal(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
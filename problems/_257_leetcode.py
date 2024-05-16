# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

# Solution by: Javi Barranco

# Problem:
# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(node: Optional[TreeNode]):
            nonlocal cur

            if not node: return
            if node.left == node.right == None: 
                cur =  cur + [str(node.val)]
                res.append(''.join(cur))
                return

            cur = cur + [str(node.val), '->']
            dfs(node.left)
            while cur[-1] != '->': cur = cur[:-1]
            dfs(node.right)
            while cur[-1] != '->': cur = cur[:-1]
            cur = cur[:-1]

        cur = []
        dfs(root)
        return res
    

exercise = Solution()

input = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))

expected_output = ["1->2->5", "1->3"]

output = exercise.binaryTreePaths(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
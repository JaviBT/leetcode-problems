# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Example:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4

import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesRec(root, [])
    
    def goodNodesRec(self, root: TreeNode, path: [TreeNode]) -> int:
        if not root: return 0
        
        ret = 1
        for val in path:
            if root.val < val: 
                ret = 0
                break
        
        return ret + self.goodNodesRec(root.left, [*path, root.val]) + self.goodNodesRec(root.right, [*path, root.val])
    

class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesRec(root, -math.inf)
    
    def goodNodesRec(self, root: TreeNode, maxVal: int) -> int:
        if not root: return 0

        ret = 1 if root.val >= maxVal else 0
        
        return ret + self.goodNodesRec(root.left, max(maxVal, root.val)) + self.goodNodesRec(root.right, max(maxVal, root.val))
    

exercise = Solution()

input = TreeNode(3, TreeNode(1, TreeNode(3), TreeNode(1)), TreeNode(4, None, TreeNode(5)))

expected_output = 4

output = exercise.goodNodes(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
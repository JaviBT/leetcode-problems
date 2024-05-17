# 1325. Delete Leaves With a Given Value
# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target, if it's a parent of other leaf nodes with value target, those leaf nodes will also be deleted after that deletion.
# Also, you should delete the leaf nodes in the order from left to right.

# Example 1:
# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right
    
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root or root.left == root.right == None and root.val == target: root = None
        
        def postorder_dfs(node: Optional[TreeNode]):
            if node == None: return

            node.left = postorder_dfs(node.left)
            node.right = postorder_dfs(node.right)
            if node.left == node.right == None and node.val == target: return None
            return node

        return postorder_dfs(root)
    

exercise = Solution()

input = TreeNode(1, TreeNode(2, TreeNode(2, None, None), None), TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None))), 2

expected_output = TreeNode(1, None, TreeNode(3, None, TreeNode(4)))

output = exercise.removeLeafNodes(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
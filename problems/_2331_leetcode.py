# 2331. Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Solution by: Javi Barranco

# Problem:
# You are given the root of a full binary tree with the following properties:

# Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
# Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:

# If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
# Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.

# A full binary tree is a binary tree where each node has either 0 or 2 children.

# A leaf node is a node that has zero children.

# Example 1:
# Input: root = [2,1,3,null,null,0,1]
# Output: True

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def postorder_evaluation(node: Optional[TreeNode]) -> bool:
            if node.left == node.right == None:
                return True if node.val else False
            
            left = postorder_evaluation(node.left)
            right = postorder_evaluation(node.right)
            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right
                
        return postorder_evaluation(root)
    

exercise = Solution()

input = TreeNode(2, TreeNode(1, None, None), TreeNode(3, TreeNode(0, None, None), TreeNode(1, None, None)))

expected_output = True

output = exercise.evaluateTree(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
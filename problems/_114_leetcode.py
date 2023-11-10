# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Solution by: Javi Barranco

# Problem:
# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Example:
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def flatten(self, root: [TreeNode]) -> None:
        if root is None: return
        
        self.flatten(root.left)
        self.flatten(root.right)

        temp = root.right
        root.right = root.left
        root.left = None
        if root.right != None:
            node = root.right
            while node.right != None:
                node = node.right
            node.right = temp
        else: root.right = temp

        return root
    

exercise = Solution()

input = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
expected_output = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))))

def sameTree(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    if t1.val != t2.val: return False

    return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)

output = exercise.flatten(input)
print(output)
assert sameTree(output, expected_output), "Wrong answer"
print("Accepted")

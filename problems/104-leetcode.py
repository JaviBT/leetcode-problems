# 104. Maximun Depth of Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if root is None: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


exercise = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left = TreeNode(7)

input = root
expected_output = 3
output = exercise.maxDepth(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

# 226. Invert Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left  = left
        self.right = right

def isSameTree(p: [TreeNode], q: [TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
            return True
        return False

class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root
       

class Solution2:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        self.invertTreeRec(root)
        return root
    
    def invertTreeRec(self, root: [TreeNode]) -> [TreeNode]:
        if root == None: return

        root.left, root.right = root.right, root.left
        self.invertTreeRec(root.left)
        self.invertTreeRec(root.right)


exercise = Solution()
input = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
expected_output = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
output = exercise.invertTree(input)
print(output)
assert isSameTree(output, expected_output), "Wrong answer"
print("Accepted")

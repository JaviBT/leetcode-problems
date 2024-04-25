# 100. Same Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left  = left
        self.right = right


class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False
    

class Solution2:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        if (p == None and q == None): return True
        elif p == None or q == None: return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) and (p.val == q.val)

exercise = Solution()
input = TreeNode(1, TreeNode(2), TreeNode(3))
expected_output = True
output = exercise.isSameTree(input, input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
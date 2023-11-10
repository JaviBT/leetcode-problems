# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Solution by: Javi Barranco

# Problem:
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Example:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> [TreeNode]:
        inorderIndex = { val: index for index, val in enumerate(inorder) }

        def buildTreeIdx(left, right):
            if left > right: return None

            root = TreeNode(postorder.pop())

            val_index = inorderIndex[root.val]
            root.right = buildTreeIdx(val_index+1, right)
            root.left = buildTreeIdx(left, val_index-1)

            return root
        
        return buildTreeIdx(0, len(inorder)-1)

class Solution2: # This solution is can be optimized by using a hashmap to store the index of each value in inorder (increase space complexity but decrease time complexity significantly)
    def buildTree(self, inorder: [int], postorder: [int]) -> [TreeNode]:
        if not inorder: return None

        root = TreeNode(postorder.pop())

        val_index = inorder.index(root.val)
        root.right = self.buildTree(inorder[val_index+1:], postorder)
        root.left = self.buildTree(inorder[:val_index], postorder)

        return root

class Solution3: # Very unoptimized solution because we are calculating postorder split instead of taking advantage of the fact that we know the root is the last element of postorder
    def buildTree(self, inorder: [int], postorder: [int]) -> [TreeNode]:
        if not inorder or not postorder: return None

        val = postorder[-1]
        val_index = inorder.index(val)

        inorder_l = inorder[:val_index]
        inorder_r = inorder[val_index+1:]

        postorder_l = []
        postorder_r = []
        for num in postorder:
            if num == val: break
            if num in inorder_r: 
                postorder_r.append(num)
            else:
                postorder_l.append(num)

        return TreeNode(val, self.buildTree(inorder_l, postorder_l), self.buildTree(inorder_r, postorder_r))
    

exercise = Solution()

input = [9,3,15,20,7]
input2 = [9,15,7,20,3]

expected_output = TreeNode(3)
expected_output.left = TreeNode(9)
expected_output.right = TreeNode(20)
expected_output.right.left = TreeNode(15)
expected_output.right.right = TreeNode(7)

def sameTree(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    if t1.val != t2.val: return False

    return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)

output = exercise.buildTree(input, input2)
print(output)
assert sameTree(output, expected_output), "Wrong answer"
print("Accepted")

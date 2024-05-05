# 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Solution by: Javi Barranco

# Problem:
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other: return False
        return self.val == other.val and self.next == other.next

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next == None: node = None
        curNode = node
  
        while curNode.next.next != None:
            curNode.val = curNode.next.val
            curNode = curNode.next
        curNode.val = curNode.next.val
        curNode.next = None


exercise = Solution()

input = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))

expected_output = ListNode(4, ListNode(1, ListNode(9)))

exercise.deleteNode(input.next)

output = input
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
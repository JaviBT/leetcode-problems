# 2487. Remove Nodes From Linked List
# https://leetcode.com/problems/remove-nodes-from-linked-list

# Solution by: Javi Barranco

# Problem:
# You are given the head of a linked list.
# Remove every node which has a node with a greater value anywhere to the right side of it.
# Return the head of the modified linked list.

# Example:
# Input: head = [5,2,13,3,8]
# Output: [13,8]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other: return False
        return self.val == other.val and self.next == other.next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNodes = []
        maxVal = 0

        cur = head
        while cur != None:
            if maxVal < cur.val:
                while newNodes and newNodes[-1].val < cur.val: newNodes.pop()
            newNodes.append(cur)
            cur = cur.next

        head = newNodes[0]
        cur = head
        for node in newNodes[1:]:
            cur.next = node
            cur = cur.next
        cur.next = None

        return head
    

exercise = Solution()

input = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))

expected_output = ListNode(13, ListNode(8))

output = exercise.removeNodes(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists

# Solution by: Javi Barranco

# Problem:
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Example 1:
# Input: listA = [4,1,8,4,5], listB = [5,0,1,8,4,5]
# Output: 8

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Find lengths of linked lists
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next
        
        # Calculate difference in lengths
        diff = abs(lenA - lenB)
        if lenA > lenB:
            # Move pointer of A ahead
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            # Move pointer of B ahead
            while diff > 0:
                headB = headB.next
                diff -= 1
        
        # Traverse both linked lists in parallel
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        # No intersection found
        return None


exercise = Solution()

input = [
    ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))),
    ListNode(5, ListNode(0, ListNode(1, None))),
]

input[1].next.next.next = input[0].next.next

expected_output = 8

output = exercise.getIntersectionNode(input[0], input[1])
output = output.val if output else 0
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
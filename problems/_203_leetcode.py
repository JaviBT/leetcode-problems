# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

# Solution by: Javi Barranco

# Problem:
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.next == other.next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            if cur.val == val:
                if prev == None: 
                    head = cur.next
                else: 
                    prev.next = cur.next
            else:
                prev = cur
                
            cur = cur.next

        return head
    

exercise = Solution()

input = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6

expected_output = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
                           
output = exercise.removeElements(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
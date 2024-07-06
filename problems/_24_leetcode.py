# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs

# Solution by: Javi Barranco

# Problem:
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other: return False
        return self.val == other.val and self.next == other.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        prev = None
        cur = head

        while cur:
            if not prev:  
                new_head = cur.next
            if not cur.next:
                cur = cur.next
                continue
        
            nxt = cur.next
            if nxt: 
                cur.next = nxt.next
                nxt.next = cur
            if prev: 
                prev.next = nxt
            
            prev = cur
            cur = cur.next

        return new_head
    

exercise = Solution()

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

expected_output = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))

output = exercise.swapPairs(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
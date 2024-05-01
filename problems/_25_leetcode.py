# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Solution by: Javi Barranco

# Problem:
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Define a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sameLinkedList(head1: [ListNode], head2: [ListNode]) -> bool:
    while head1 != None and head2 != None:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    
    return head1 == None and head2 == None


class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        res = ListNode()
        cur, prev = head, res

        while cur != None:
            tmp = cur
            for _ in range(k - 1):
                tmp = tmp.next
                if tmp is None: return res.next

            cur, prev = self.reverseGroup(prev, cur, k)

        return res.next

    def reverseGroup(self, prevNode: [ListNode], head: [ListNode], k:int) -> [ListNode]:
        if k == 1: 
            prevNode.next = head
            return head.next, head

        prev, cur = None, head

        for _ in range(k - 1):
            tmp = prev
            prev, cur = cur, cur.next
            prev.next = tmp

        head.next = cur.next
        cur.next = prev
        if prevNode is not None: prevNode.next = cur
        
        return head.next, head
    

exercise = Solution()

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
                 
expected_output = ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))

output = exercise.reverseKGroup(input, 2)
print(output)
assert sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")          
# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Solution by: Javi Barranco

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        
        prev_node = None
        current_node = head

        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        return prev_node
    
    def sameLinkedList(self, head1: [ListNode], head2: [ListNode]) -> bool:
        while head1 != None and head2 != None:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return head1 == None and head2 == None
    

exercise = Solution()
input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
expected_output = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
output = exercise.reverseList(input)
print(output)
assert exercise.sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")

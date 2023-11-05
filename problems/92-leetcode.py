# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# Solution by: Javi Barranco

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        
        origin = head # Initial node might be required for output
        top = None # First node prior to reversed sublist
        bottom = None # Next node after reversed sublist

        prev_node = None
        current_node = head
        index = 1
        while current_node != None:
            if left > 1 and index == left - 1: # Capture top
                top = current_node
            if index == right: # Capture bottom
                bottom = current_node.next
    
            if index >= left and index <= right:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
            else:
                current_node = current_node.next
            index += 1
        
        output = prev_node
        if top != None:
            top.next = prev_node
            output = origin
        if bottom != None:
            current_node = output
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = bottom
        
        return output
    
    def sameLinkedList(self, head1: [ListNode], head2: [ListNode]) -> bool:
        while head1 != None and head2 != None:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return head1 == None and head2 == None
    

exercise = Solution()
input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
expected_output = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
output = exercise.reverseBetween(input, 2, 4)
print(output)
assert exercise.sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")
    
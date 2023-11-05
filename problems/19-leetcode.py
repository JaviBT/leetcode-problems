# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Solution by: Javi Barranco

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        
        origin = head

        size = 0
        node = head
        while node != None:
            size += 1
            node = node.next
        if size == 1: return None
        
        prev = None
        current_node = head
        index = 0
        while current_node != None:
            if index == (size - n) and index > 0:
                prev.next = current_node.next
            elif index == (size - n) and index == 0:
                origin = current_node.next
            else:
                prev = current_node
                current_node = current_node.next
            index += 1

        return origin
        
    def sameLinkedList(self, head1: [ListNode], head2: [ListNode]) -> bool:
        while head1 != None and head2 != None:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return head1 == None and head2 == None
    

exercise = Solution()
input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
expected_output = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
output = exercise.removeNthFromEnd(input, 2)
print(output)
assert exercise.sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")

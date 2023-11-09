# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Solution by: Javi Barranco

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if head == None: return head

        valid = None
        prev = None
        node = head
        val = head.val
        count = 0

        while node != None:
            if node.val == val: 
                count += 1
            else: # New Value Found
                if count > 1 and prev.val == head.val:
                    head = node
                    valid = head
                elif count > 1:
                    valid.next = node
                elif count == 1:
                    valid = prev
                val = node.val
                count = 1
            prev = node
            node = node.next
        if count > 1:
            if val == head.val: head = None
            else: valid.next = None

        return head

    def sameLinkedList(self, head1: [ListNode], head2: [ListNode]) -> bool:
        while head1 != None and head2 != None:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return head1 == None and head2 == None
    

exercise = Solution()
input = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
expected_output = ListNode(1, ListNode(2, ListNode(5)))
output = exercise.deleteDuplicates(input)
print(output)
assert exercise.sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")

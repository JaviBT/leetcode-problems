# 61. Rotate List
# https://leetcode.com/problems/rotate-list/

# Solution by: Javi Barranco

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        if head == None or head.next == None or k == 0: return head

        n = 0
        node = head
        while node != None:
            n += 1
            node = node.next
        
        k = n - (k % n)
        if k == n: return head
        
        prev = None
        node = head
        count = 0
        while node != None:
            if node.next == None:
                node.next = head
                head = node
                break

            prev = node
            node = node.next
            count += 1
            
            if count == k:
                output = node
                prev.next = None

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
expected_output = ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
output = exercise.rotateRight(input, 2)
print(output)
assert exercise.sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")

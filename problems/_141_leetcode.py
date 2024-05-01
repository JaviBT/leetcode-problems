# 141. Linked List Cycle

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        if head == None: return False

        visited = []

        while head.next != None:
            if head in visited: return True
            visited.append(head)
            head = head.next

        return False
    

class Solution2:
    def hasCycle(self, head: [ListNode]) -> bool:
        visited = set()

        cur = head
        while cur:
            if cur in visited: return True
            visited.add(cur)
            cur = cur.next

        return False
    

exercise = Solution()

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = head

input = head
expected_output = True
output = exercise.hasCycle(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

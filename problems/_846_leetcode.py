# 846. Hand of Straights
# https://leetcode.com/problems/hand-of-straights

# Solution by: Javi Barranco

# Problem:
# Alice has a hand of cards, given as an array of integers.
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
# Return true if and only if she can.

# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        handMap = {}
        minHeap = []

        for card in hand:
            if card not in handMap: heapq.heappush(minHeap, card)
            handMap[card] = handMap.get(card, 0) + 1

        while minHeap:
            cur = minHeap[0]
            if cur not in handMap or handMap[cur] == 0:
                heapq.heappop(minHeap)
                continue
            handMap[cur] -= 1
            if handMap[cur] == 0:
                heapq.heappop(minHeap)

            for i in range(1, groupSize):
                if cur + i not in handMap or handMap[cur + i] == 0: 
                    return False
                else:
                    handMap[cur + i] -= 1
        
        return True
    

class Solution2: # Brute force
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        minHeap = hand
        heapq.heapify(minHeap)
        cur, prev = None, None
        cnt = 0
        tmp = []
        currentList = []

        while minHeap:
            cur = heapq.heappop(minHeap)
            if cnt != 0:
                while prev and minHeap and cur != prev + 1:
                    if cur > prev + 1: return False
                    tmp.append(cur)
                    cur = heapq.heappop(minHeap)
                if not minHeap and cur != prev + 1: return False
            prev = cur
            for _ in range(len(tmp)):
                heapq.heappush(minHeap, tmp.pop())
            cnt = (cnt + 1) % groupSize

        return True
    

exercise = Solution()

input = [1,2,3,6,2,3,4,7,8]

expected_output = True

output = exercise.isNStraightHand(input, 3)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
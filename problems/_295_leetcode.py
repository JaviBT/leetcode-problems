# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream

# Solution by: Javi Barranco

# Problem:
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Constraints:
# -10^5 <= num <= 10^5
# There will be at most 5 * 10^4 calls to addNum and findMedian.

# Example 1:
# Input
#   ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
#   [[], [1], [2], [], [3], []]
# Output
#   [null, null, null, 1.5, null, 2.0]

import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = [] # ceil(k)_largest values
        self.maxHeap = [] # floor(k)_smallest values

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        # Check maxHeap <= minHeap for all values
        if self.minHeap and self.maxHeap and self.minHeap[0] < -self.maxHeap[0]:
            popped = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, popped)

        # Check sizes
        if len(self.maxHeap) > len(self.minHeap) + 1:
            popped = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, popped)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            popped = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -popped)
        

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            if len(self.minHeap) > len(self.maxHeap): return self.minHeap[0]
            else: return -self.maxHeap[0]


class MedianFinder2: # Naive solution

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        arrLen = len(self.arr)
        if arrLen % 2 != 0: 
            return self.arr[int(arrLen / 2)]
        else:
            return (self.arr[int(arrLen / 2) - 1] + self.arr[int(arrLen / 2)]) / 2
        

exercise = MedianFinder()

inputs = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
data = [[], [1], [2], [], [3], []]

expected_output = [None, None, None, 1.5, None, 2.0]

output = [None]
for input, dat in zip(inputs[1:], data[1:]):
    if input == "addNum":
        output.append(exercise.addNum(dat[0]))
    elif input == "findMedian":
        output.append(exercise.findMedian())
    else:
        output.append(None)
print(output)
for out, exp in zip(output, expected_output):
    assert out == exp, "Wrong answer"
print("Accepted")
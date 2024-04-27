# 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream

# Solution by: Javi Barranco

# Problem:
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Returns the element representing the kth largest element in the stream.

# Example:
# Input ["KthLargest", "add", "add", "add", "add", "add"]
#       [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output [null, 4, 5, 5, 8, 8]

import heapq


class KthLargest:
    def __init__(self, k: int, nums: [int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: heapq.heappop(self.minHeap)
        return self.minHeap[0]
    

inputs = ['KthLargest', 'add', 'add', 'add', 'add', 'add']
values = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

expected_outputs = [None, 4, 5, 5, 8, 8]

output = []
for input, value in zip(inputs, values):
    if input == 'KthLargest':
        exercise = KthLargest(value[0], value[1])
        output.append(None)
    else:
        output.append(exercise.add(value[0]))
print(output)
assert output == expected_outputs, "Wrong answer"
print("Accepted")
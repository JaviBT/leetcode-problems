# 786. K-th Smallest Prime Fraction
# https://leetcode.com/problems/k-th-smallest-prime-fraction

# Solution by: Javi Barranco

# Problem:
# A sorted list A contains 1, plus some number of primes. Then, for every p < q in the list, we consider the fraction p/q.
# What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

# Example 1:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]

from typing import List
import heapq

class Solution: # Optimized solution (Time Complexity: O(n * log(n)))
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap, n = [], len(arr)
    
        for j in range(1, n):
            heapq.heappush(heap, (arr[0]/arr[j], 0, j))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            
            if i + 1 < j:
                heapq.heappush(heap, (arr[i + 1]/arr[j], i + 1, j))
        
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
    

class Solution2: # Brute force solution (Time Complexity: O(n^2 * log(n)))
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heapq.heappush(minHeap, (arr[i] / arr[j], [arr[i], arr[j]]))

        for _ in range(k - 1): heapq.heappop(minHeap)

        return heapq.heappop(minHeap)[1]
    

class Solution: # Super optimized solution with binary search (Copied from LeetCode)
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def con(value):
            nb_smallest_fraction = 0
            numer = arr[0]
            denom = arr[-1]

            slow = 0
            for fast in range(1, len(arr)):
                while slow < fast and arr[slow] / arr[fast] < value:
                    if arr[slow] / arr[fast] > numer / denom:
                        numer, denom = arr[slow], arr[fast]

                    slow += 1

                nb_smallest_fraction += slow

            return nb_smallest_fraction, numer, denom

        l = arr[0] / arr[-1]
        r = 1

        while l < r:
            m = (l+r) / 2

            count, numer, denom = con(m)

            if count == k:
                return [numer, denom]

            if count > k:
                r = m
            else:
                l = m
    

exercise = Solution()

input = [
    [1, 2, 3, 5],
    3
]

expected_output = [2, 5]

output = exercise.kthSmallestPrimeFraction(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
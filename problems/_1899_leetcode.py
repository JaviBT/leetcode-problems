# 1899. Merge triplets to form target triplet
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet

# Solution by: Javi Barranco

# Problem:
# A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.
# To obtain target, you may apply the following operation on triplets any number of times (possibly zero):
# Choose two integers (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

# Example:
# Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
# Output: true
# Explanation: Perform the following operations:
# - Choose the first and second triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the second triplet to be [max(2,1), max(5,8), max(3,4)] = [2,8,4].

from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = []
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                valid_triplets.append(triplets[i])

        a, b, c = False, False, False
        for triplet in valid_triplets:
            if triplet[0] == target[0]: a = True
            if triplet[1] == target[1]: b = True
            if triplet[2] == target[2]: c = True
        

        return all([a, b, c])
    

exercise = Solution()

input = [[2,5,3],[1,8,4],[1,7,5]], [2,7,5]

expected_output = True

output = exercise.mergeTriplets(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
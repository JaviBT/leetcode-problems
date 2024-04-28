# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii

# Solution by: Javi Barranco

# Problem:
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

class Solution: # Brute force solution
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort() # O(nlog(n))
        ret = []
        self.combinationSum2Rec(candidates, target, [], ret)
        return ret

    def combinationSum2Rec(self, candidates: [int], target: int, sub: [int], ret: [[int]]) -> None:
        if sum(sub) == target: 
            ret.append(sub)
            return
        elif not candidates or sum(sub) > target:
            return

        candidate = candidates[0]

        new_sub = sub.copy()
        new_sub.append(candidate)
        new_candidates = candidates[1:] if len(candidates) > 1 else []
        self.combinationSum2Rec(new_candidates, target, new_sub.copy(), ret)
        new_sub.pop()
        while new_candidates and new_candidates[0] == candidate: new_candidates = new_candidates[1:]
        self.combinationSum2Rec(new_candidates, target, new_sub.copy(), ret)


exercise = Solution()

input = [10,1,2,7,6,1,5]

expected_output = [[1,1,6],[1,2,5],[1,7],[2,6]]

output = exercise.combinationSum2(input, 8)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out in output:
    assert out in expected_output, "Wrong answer"
print("Accepted")
# 39. Combination Sum
# https://leetcode.com/problems/combination-sum

# Solution by: Javi Barranco

# Problem:
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        ret = []
        self.combinationSumRec(candidates, target, [], ret)
        return ret

    def combinationSumRec(self, candidates: [int], target: int, sub: [int], ret: [[int]]) -> None:
        if not candidates or sum(sub) > target: return
        candidate = candidates[0]

        if sum(sub + [candidate]) == target:
            ret.append(sub + [candidate])

        new_candidates = [] if len(candidates) <= 1 else candidates[1:]
        self.combinationSumRec(new_candidates, target, sub, ret)
        self.combinationSumRec(candidates, target, sub + [candidate], ret)


class Solution2: # Brute force solution
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        ret = []
        subs = [[]]

        while subs:
            for _ in range(len(subs)):
                sub = subs[0]
                if len(subs) > 1:
                    subs = subs[1:]
                else:
                    subs = []

                for candidate in candidates:
                    new_sub = sub + [candidate]
                    if sum(new_sub) == target: 
                        new_sub.sort()
                        if new_sub not in ret: ret.append(new_sub)
                    elif sum(new_sub) < target: 
                        subs.append(new_sub)

        return ret
    

exercise = Solution()

input = [2,3,6,7]
target = 7

expected_output = [[2,2,3],[7]]

output = exercise.combinationSum(input, target)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out, exp in zip(output, expected_output):
    assert out in expected_output, "Wrong answer"
print("Accepted")
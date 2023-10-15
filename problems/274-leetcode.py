# 274. H-Index

class Solution:
    def hIndex(self, citations: [int]) -> int:
        max_citations = max(citations)
        cumulative_feq = []

        for i in range(0, max_citations + 1):
            count = 0
            for citation in citations:
                if (citation >= i): count += 1
            cumulative_feq.append(count)

        for i in range(len(cumulative_feq) - 1, -1, -1):
            if (cumulative_feq[i] >= i): 
                return i

        return 0
    

exercise = Solution()
input = [3,0,6,1,5]
expected_output = 3
output = exercise.hIndex(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

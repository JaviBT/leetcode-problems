# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Solution by: Javi Barranco

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:

        dic = {}
        
        for string in strs:
            key = [char for char in string]
            key.sort()
            key = ''.join(key)

            if key not in dic.keys():
                dic[key] = [string]
            else:
                dic[key].append(string)

        return list(dic.values())


class Solution2: # TimeLimitExceeded
    def groupAnagrams(self, strs: [str]) -> [[str]]:

        output = []
        
        for string in strs:
            groupFound = False
            for group in output:
                if self.isAnagram(group[0], string): 
                    group.append(string)
                    groupFound = True
                    break
            if not groupFound: output.append([string])
        
        return output
            
    def isAnagram(self, a: str, b: str) -> bool:

        dic = {}

        for char in a:
            if char in dic.keys():
                dic[char] += 1
            else:
                dic[char] = 1

        for char in b:
            if char not in dic.keys():
                return False
            else:
                dic[char] -= 1

        for val in dic.values():
            if val != 0:
                return False

        return True


def same(a: [[str]], b: [[str]]) -> bool:
    # Check if to lists of list are the same (order doesn't matter in the list of lists and in the individual lists)
    if len(a) != len(b): return False
    for group in a:
        found = False
        for group2 in b:
            if sorted(group) == sorted(group2):
                found = True
                break
        if not found: return False
    return True


exercise = Solution()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected_output = [["bat"],["nat","tan"],["ate","eat","tea"]]
output = exercise.groupAnagrams(input)
print(output)
assert same(output, expected_output), "Wrong answer"
print("Accepted")

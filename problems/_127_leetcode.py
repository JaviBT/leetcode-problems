# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/

# Solution by: Javi Barranco

# Problem:
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# - Every adjacent pair of words differs by a single letter.
# - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# - sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Get a graph like data structure that contains the words with connections when words differ by one char
        wordMap = {}
        for word in wordList:
            for i, char in enumerate(word):
                pseudoWord = word[:i] + '*' + word[i+1:]
                if pseudoWord not in wordMap:
                    wordMap[pseudoWord] = []
                wordMap[pseudoWord].append(word)

        # Run BFS and count the distance to endWord or 0 if it can't be found
        q = deque()
        q.append(beginWord)
        visited = set()
        cnt = 1
        while q:
            qLen = len(q)
            cnt += 1
            for _ in range(qLen):
                cur = q.popleft()
                
                # Get possible pseudoWords from cur
                for i, char in enumerate(cur):
                    pseudoWord = cur[:i] + '*' + cur[i+1:]
                    if pseudoWord in visited or pseudoWord not in wordMap: continue
                    visited.add(pseudoWord)
                    for nextWord in wordMap[pseudoWord]:
                        if nextWord == endWord: return cnt
                        if nextWord not in q: q.append(nextWord)

        return 0
    

exercise = Solution()

input = ["hit", "cog", ["hot","dot","dog","lot","log","cog"]]

expected_output = 5

output = exercise.ladderLength(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
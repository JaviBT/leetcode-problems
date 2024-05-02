# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/

# Solution by: Javi Barranco

# Problem:
# Given an m x n board of characters and a list of words, return all words in the list that can be found in the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

class TrieNode:
    def __init__(self):
        self.endWord = False
        self.children = {}

    def insert(self, word: str) -> None:
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True


class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        trie = TrieNode()
        res = set()

        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        visited = set()

        def _helperFindWords(row:int, col:int, node: TrieNode, curWord: str):
            if (row < 0 or col < 0 or
                row >= m or col >= n or
                board[row][col] not in node.children or
                (row, col) in visited): return
            
            visited.add((row, col))
            node = node.children[board[row][col]]
            curWord += board[row][col]
            if node.endWord: res.add(curWord)

            _helperFindWords(row + 1, col, node, curWord)
            _helperFindWords(row - 1, col, node, curWord)
            _helperFindWords(row, col + 1, node, curWord)
            _helperFindWords(row, col - 1, node, curWord)

            visited.remove((row, col))

        for i in range(m):
            for j in range(n):
                _helperFindWords(i, j, trie, '')

        return list(res)
    

exercise = Solution()

input = [[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]]
output = exercise.findWords(*input)

expected_output = ["eat","oath"]

print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out in output:
    assert out in expected_output, "Wrong answer"
print("Accepted")
# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Solution by: Javi Barranco

# Problem:
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can be matched later.
# - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

# Example 1:
# Input
# ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
# [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
# Output
# [null, null, null, null, false, true, true, true]

class TrieNode:
    def __init__(self):
        self.endWord = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True

    def search(self, word: str) -> bool:

        def helperSearch(node: TrieNode, word: str) -> bool:
            cur = node

            for i, c in enumerate(word):
                if c == '.':
                    for key in cur.children:
                        if helperSearch(cur.children[key], word[i+1:]): return True
                    return False
                if c not in cur.children: return False
                cur = cur.children[c]

            return cur.endWord

        return helperSearch(self.root, word)
    

class WordDictionary2:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for i, c in enumerate(word):
            if c == '.':
                for key in cur.children:
                    if self.search(word[:i] + key + word[i+1:]): return True
                return False
            if c not in cur.children: return False
            cur = cur.children[c]

        return cur.endWord
    

exercise = WordDictionary()

commands = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
input = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]

expected_output = [None, None, None, None, False, True, True, True]

output = []
for command, args in zip(commands, input):
    if command == "WordDictionary":
        output.append(None)
    elif command == "addWord":
        output.append(exercise.addWord(*args))
    elif command == "search":
        output.append(exercise.search(*args))
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out, exp in zip(output, expected_output):
    assert out == exp, "Wrong answer"
print("Accepted")
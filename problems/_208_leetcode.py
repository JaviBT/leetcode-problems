# 208. Implements Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

# Solution by: Javi Barranco

# Problem:
# Implement a trie with insert, search, and startsWith methods.

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

class TrieNode:
    def __init__(self):
        self.endWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children: return False
            cur = cur.children[c]

        return cur.endWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children: return False
            cur = cur.children[c]

        return True
    

exercise = Trie()

commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
input = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

expected_output = [None, None, True, False, True, None, True]

output = []
for command, args in zip(commands, input):
    if command == "insert":
        output.append(exercise.insert(*args))
    elif command == "search":
        output.append(exercise.search(*args))
    elif command == "startsWith":
        output.append(exercise.startsWith(*args))
    else:
        output.append(None)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out, exp in zip(output, expected_output):
    assert out == exp, "Wrong answer"
print("Accepted")
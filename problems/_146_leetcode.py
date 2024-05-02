# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

# Solution by: Javi Barranco

# Problem:
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# - int get(int key) Return the value of the key if the key exists, otherwise return -1.
# - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

class Node:
    def __init__(self, key= 0, val=0, next=None, prev=None):
        self.key, self.val = key, val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.lru, self.back = Node(0, 0), Node(0, 0)
        self.lru.next, self.back.prev = self.back, self.lru

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int):
        if key in self.dic:
            self.delete(self.dic[key])
        self.dic[key] = Node(key, value)
        self.insert(self.dic[key])
        
        if len(self.dic) > self.cap:
            node = self.lru.next
            self.dic.pop(node.key)
            self.delete(node)

    def insert(self, node: Node):
        node.prev = self.back.prev
        node.prev.next = node
        node.next = self.back
        self.back.prev = node
    
    def delete(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev


exercise = LRUCache(2)

commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

expected_output = [None, None, None, 1, None, -1, None, -1, 3, 4]

output = []
for command, input in zip(commands, inputs):
    if command == "put":
        output.append(exercise.put(*input))
    elif command == "get":
        output.append(exercise.get(*input))
    else:
        output.append(None)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out, exp in zip(output, expected_output):
    assert out == exp, "Wrong answer"
print("Accepted")
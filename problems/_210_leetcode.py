# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii

# Solution by: Javi Barranco

# Problem:
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Load courses and prereqs into a hash map
        courses = {}
        
        for i in range(numCourses):
            courses[i] = []

        for i, prereq in prerequisites:
            courses[i].append(prereq)

        # Define DFS function to get the order of courses
        def dfs(i):
            if not courses[i]: 
                if i not in order: order.append(i)
                return True
            if i in cycle: return False
            if i in visited: return True

            cycle.add(i)
            for prereq in courses[i]:
                if not dfs(prereq): return False
            cycle.remove(i)

            order.append(i)
            visited.add(i)
            return True

        # Run the DFS function on every course
        order = []
        visited, cycle = set(), set()
        for i in courses:
            if not dfs(i): return []

        return order


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Load courses and prereqs into a hash map
        courses = {}
        
        for i in range(numCourses):
            courses[i] = []

        for i, prereq in prerequisites:
            courses[i].append(prereq)

        # Define DFS function to get the order of courses
        def dfs(i, visited, order):
            if not courses[i]: 
                if i not in order: order.append(i)
                return True
            if i in visited: return False

            visited.add(i)
            for prereq in courses[i]:
                if not dfs(prereq, visited, order): return False
            visited.remove(i)

            if i not in order: order.append(i)
            return True

        # Run the DFS function on every course
        order = []
        for i in courses:
            if not dfs(i, set(), order): return []

        return order
    

exercise = Solution()

input = 4, [[1,0],[2,0],[3,1],[3,2]]

expected_output = [
    [0, 2, 1, 3],
    [0, 1, 2, 3]
]

output = exercise.findOrder(*input)
print(output)
assert output in expected_output, "Wrong answer"
print("Accepted")
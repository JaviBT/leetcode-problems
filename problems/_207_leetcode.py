# 207. Course Schedule
# https://leetcode.com/problems/course-schedule

# Solution by: Javi Barranco

# Problem:
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true

from typing import List

class Course:
    def __init__(self, val=-1):
        self.val = val
        self.prereqTo = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create prereq map
        courses = {}
        for i in range(numCourses):
            courses[i] = []

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        # Define the DFS function
        def dfs(cur: int, visited: [int]):
            if not courses[cur]: return True
            if cur in visited: return False

            visited.add(cur)
            for prereq in courses[cur]:
                if not dfs(prereq, visited): return False
                else: courses[cur].remove(prereq)
            visited.remove(cur)

            return True

        # Run DFS on all courses
        for course in courses:
            if not dfs(course, set()): return False

        return True


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Load the courses into Course objects
        courses = {}
        for i in range(numCourses):
            courses[i] = Course(i)

        # Load the prerequisites into the object's prereqTo attribute
        for course, prereq in prerequisites:
            courses[prereq].prereqTo.append(courses[course])

        # Run DFS on each course looking for loops
        def dfs(curCourse, visited, cache):
            if curCourse in visited: return False
            if not curCourse.prereqTo or curCourse in cache: return True

            visited.add(curCourse)
            for nextCourse in curCourse.prereqTo:
                if not dfs(nextCourse, visited, cache): return False
            visited.remove(curCourse)

            cache.add(curCourse)
            return True

        for course in courses:
            if not dfs(courses[course], set(), set()): return False

        return True
    

exercise = Solution()

input = 2, [[1,0]]

expected_output = True

output = exercise.canFinish(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
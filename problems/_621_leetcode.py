# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler

# Solution by: Javi Barranco

# Problem:
# You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task.
# Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# You need to return the least number of units of times that the CPU will take to finish all the given tasks.

# Constraints:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8

import collections
import heapq

class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        task_dict = {}
        for task in tasks:
            if task not in task_dict:
                task_dict[task] = 1
            else:
                task_dict[task] += 1

        queue = collections.deque()
        heap = [-val for val in task_dict.values()]
        heapq.heapify(heap)
        
        cycles = 1
        while heap or queue:
            if heap:
                task = heapq.heappop(heap)
                if task + 1 < 0:
                    queue.append([task + 1, cycles + n + 1])

            # Just cycles += 1 works too but this saves some iterations
            if not heap and queue: cycles += (queue[0][1] - cycles)
            else: cycles += 1

            if queue and queue[0][1] <= cycles:
                heapq.heappush(heap, queue.popleft()[0])

        return cycles - 1


class Solution2: # Naive solution
    def leastInterval(self, tasks: [str], n: int) -> int:
        task_dict = {}
        for task in tasks:
            if task not in task_dict:
                task_dict[task] = [1, 0]
            else:
                task_dict[task][0] += 1

        cycles = 0
        while sum([task[0] for task in task_dict.values()]) > 0:
            # Pick non cooldown task with the most uses left
            best_task, uses = '', 0
            for key, val in task_dict.items():
                if val[1] == 0 and val[0] > uses: best_task, uses = key, val[0]
                val[1] = max(0, val[1] - 1)
            if best_task != '':
                task_dict[best_task][0] -= 1
                task_dict[best_task][1] += n

            cycles += 1

        return cycles
    

exercise = Solution()

input = ["A","A","A","B","B","B"]

expected_output = 8

output = exercise.leastInterval(input, 2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
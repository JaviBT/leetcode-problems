# 2013. Detect Squares
# https://leetcode.com/problems/detect-squares

# Solution by: Javi Barranco

# Problem:
# You are given a stream of points on the X-Y plane. Design an algorithm that:
# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points in the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel to the x-axis or y-axis.
# Implement the DetectSquares class:
# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

# Example 1:
# Input
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
# Output
# [null, null, null, null, 1, 0, null, 2]

class DetectSquares: # Using only list

    def __init__(self):
        self.points = []

    def add(self, point: [int]) -> None:
        self.points.append(point)

    def count(self, point: [int]) -> int:
        pX, pY = point[0], point[1]

        count = 0
        for q in self.points:
            qX, qY = q[0], q[1]
            if qX == pX or qY == pY: continue
            if abs(qX - pX) != abs(qY - pY): continue

            found_qp = 0
            found_pq = 0
            for c in self.points:
                cX, cY = c[0], c[1]
                if cX == qX and cY == pY: found_qp += 1
                if cX == pX and cY == qY: found_pq += 1
            
            count += (found_qp * found_pq)

        return count
    

class DetectSquares2: # Using dictionary

    def __init__(self):
        self.points = {}

    def add(self, point: [int]) -> None:
        if tuple(point) not in self.points: self.points[tuple(point)] = 0
        self.points[tuple(point)] += 1

    def count(self, point: [int]) -> int:
        pX, pY = point[0], point[1]

        count = 0
        for q in list(self.points.keys()).copy():
            qX, qY = q[0], q[1]
            qCount = self.points[q]
            if qX == pX or qY == pY: continue
            if abs(qX - pX) != abs(qY - pY): continue

            count += qCount * (self.points[(qX, pY)] * self.points[(pX, qY)]) if (pX, qY) in self.points and (qX, pY) in self.points else 0

        return count
    

class DetectSquares3: # Using dictionary and list

    def __init__(self):
        self.points = []
        self.hashPoints = {}

    def add(self, point: [int]) -> None:
        self.points.append(point)
        if point[0] not in self.hashPoints:
            self.hashPoints[point[0]] = {}
        if point[1] not in self.hashPoints[point[0]]:
            self.hashPoints[point[0]][point[1]] = 0
        self.hashPoints[point[0]][point[1]] += 1

    def count(self, point: [int]) -> int:
        pX, pY = point[0], point[1]

        count = 0
        for q in self.points:
            qX, qY = q[0], q[1]
            if qX == pX or qY == pY: continue
            if abs(qX - pX) != abs(qY - pY): continue

            count += (self.hashPoints[qX].get(pY, 0) * self.hashPoints[pX].get(qY, 0) if pX in self.hashPoints else 0)

        return count
    

exercise = DetectSquares()

commands = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
inputs = [[], [3, 10], [11, 2], [3, 2], [11, 10], [14, 8], [11, 2], [11, 10]]

expected_output = [None, None, None, None, 1, 0, None, 2]

output = []
for i, command in enumerate(commands):
    if command == "add":
        output.append(exercise.add(inputs[i]))
    elif command == "count":
        output.append(exercise.count(inputs[i]))
    else:
        output.append(None)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out, exp in zip(output, expected_output):
    assert out == exp, "Wrong answer"
print("Accepted")
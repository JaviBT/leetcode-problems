# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/

# Solution by: Javi Barranco

# Problem:
# N cars are going to the same destination along a one-lane road. The destination is target miles away.
# Each car i has a constant speed of speed[i] miles per hour.
# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
# The distance between these two cars is never zero.
# A car fleet is some non-empty set of cars driving at the same speed. Note that a single car is also a car fleet.
# If a car catches up to another car while driving at the same speed, we don't include it in the car fleet.
# The time of arrival of two cars is the same if they are at the same position.
# A car fleet is a group of cars driving at the same speed that arrive at the destination at the same time.
# The number of car fleets is the number of car fleets that will arrive at the destination.
# Return the number of car fleets.

# Example:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation: The cars starting at 10 and 8 become a fleet, meeting each other at 12, 8, and 6 miles.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6 miles.

class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        fleets = 0
        elapsed_hours = 0

        # Fill the stack and order by distance to target
        cars = []
        for i in range(len(position)):
            cars.append([i,position[i], speed[i]])
        cars.sort(key=lambda x: x[1]) 
            
        while cars:
            fleet = cars.pop()
            fleets += 1
            elapsed_hours = ((target - fleet[1])/fleet[2])
            while cars and ((target - cars[-1][1])/cars[-1][2]) <= elapsed_hours: cars.pop()

        return fleets
    

exercise = Solution()

input = [12, [10,8,0,5,3], [2,4,1,1,3]]

expected_output = 3

output = exercise.carFleet(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
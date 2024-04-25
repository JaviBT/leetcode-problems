# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store

# Solution by: Javi Barranco

# Problem:
# Create a timebased key-value store class TimeMap, that supports two operations.
# 1. set(string key, string value, int timestamp)
#     Stores the key and value, along with the given timestamp.
# 2. get(string key, int timestamp)
#     Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
#     If there are multiple such values, it returns the one with the largest timestamp_prev.
#     If there are no values, it returns the empty string ("").
#
# Example:
# Input: ["TimeMap", "set", "get", "get", "set", "get", "get"], [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output: [null, null, "bar", "bar", null, "bar2", "bar2"]

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store: self.store[key].append([value, timestamp])
        else: self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        nums = self.store.get(key, None)
        if not nums: return ""
        # We can assume the timestamps are in order (Read description)
        l, r = 0, len(nums) - 1
        closest_smaller = None

        while l <= r:
            mid = int((l + r) / 2)

            if nums[mid][1] == timestamp: 
                return nums[mid][0]
            elif nums[mid][1] < timestamp:
                closest_smaller = nums[mid][0]
                l = mid + 1
            elif nums[mid][1] > timestamp: 
                r = mid - 1

        if len(nums) == 1 and nums[0][1] <= timestamp: return nums[0][0]
        return closest_smaller if closest_smaller else ""
    

exercise = TimeMap()

input = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

expected_output = [None, None, "bar", "bar", None, "bar2", "bar2"]

output = []
for inp, exp in zip(input, expected_output):
    if len(inp) == 3:
        out = exercise.set(*inp)
    elif len(inp) == 2:
        out = exercise.get(*inp)
    else:
        out = None
    output.append(out)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
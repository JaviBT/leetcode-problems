tests = [
	{
	"input": {
		"list1": [2, 4, 3],
		"list2": [5, 6, 4]
	},
	"expected_output": [7, 0, 8]
	},
	{
	"input": {
		"list1": [9, 9, 9],
		"list2": [1]
	},
	"expected_output": [0, 0, 0, 1]
	},
	{
	"input": {
		"list1": [0],
		"list2": [0]
	},
	"expected_output": [0]
	},
	{
	"input": {
		"list1": [3, 5, 9],
		"list2": [7, 1, 6]
	},
	"expected_output": [0, 7, 6, 1]
	},
	{
	"input": {
		"list1": [1],
		"list2": [9, 9, 9]
	},
	"expected_output": [0, 0, 0, 1]
	},
	{
	"input": {
		"list1": [6, 7, 8],
		"list2": [3, 2, 1]
	},
	"expected_output": [9, 9, 9]
	},
	{
	"input": {
		"list1": [1, 2, 3],
		"list2": [4, 5, 6]
	},
	"expected_output": [5, 7, 9]
	},
	{
	"input": {
		"list1": [2, 4, 9],
		"list2": [5, 6, 4, 5]
	},
	"expected_output": [7, 0, 4, 6]
	},
	{
	"input": {
		"list1": [8, 7, 6],
		"list2": [5, 4, 3]
	},
	"expected_output": [3, 2, 0, 1]
	},
	{
	"input": {
		"list1": [1, 2],
		"list2": [9, 8, 7]
	},
	"expected_output": [0, 1, 8]
	},
	{
	"input": {
		"list1": [4, 0, 0],
		"list2": [9, 9]
	},
	"expected_output": [3, 0, 1]
	},
	{
	"input": {
		"list1": [5, 6, 4],
		"list2": [2, 4, 3]
	},
	"expected_output": [7, 0, 8]
	},
	{
	"input": {
		"list1": [1, 0, 0, 0],
		"list2": [9, 9, 9]
	},
	"expected_output": [0, 0, 0, 1, 0]
	},
	{
	"input": {
		"list1": [9, 2, 5],
		"list2": [6, 8, 7]
	},
	"expected_output": [5, 1, 3, 1]
	},
	{
	"input": {
		"list1": [2, 0, 0],
		"list2": [8, 9, 1]
	},
	"expected_output": [0, 0, 2, 1]
	},
	{
	"input": {
		"list1": [9, 1],
		"list2": [6, 8, 4]
	},
	"expected_output": [5, 0, 5]
	},
	{
	"input": {
		"list1": [5, 0, 1],
		"list2": [2, 1, 3]
	},
	"expected_output": [7, 1, 4]
	},
	{
	"input": {
		"list1": [7, 4, 2],
		"list2": [3, 6, 1]
	},
	"expected_output": [0, 1, 4, 1]
	},
	{
	"input": {
		"list1": [3, 3, 3],
		"list2": [7, 7, 7]
	},
	"expected_output": [0, 1, 1, 1]
	},
	{
	"input": {
		"list1": [1, 2, 3],
		"list2": [4, 5, 6]
	},
	"expected_output": [5, 7, 9]
	},
]

# Import ListNode and Solution from problems/2-leetcode.py
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems._2_leetcode import ListNode, Solution

# Read arguments from command line (log)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="Show individual test results", type=int, choices=[True, False], default=False)
args = parser.parse_args()
log = args.log

exercise = Solution()

all_passed = True
num_tests = len(tests)
num_passed = 0
for test in tests:
    input1 = test['input']['list1']
    input2 = test['input']['list2']
    expected_output = test['expected_output']

    # Convert input to ListNode
    list1 = ListNode(input1[0])
    loop = list1
    for i in range(1, len(input1)):
        loop.next = ListNode(input1[i])
        loop = loop.next

    list2 = ListNode(input2[0])
    loop = list2
    for i in range(1, len(input2)):
        loop.next = ListNode(input2[i])
        loop = loop.next

    output = exercise.addTwoNumbers(list1, list2)
    output_list = []
    while output != None:
        output_list.append(output.val)
        output = output.next

    if not exercise.same(ListNode(expected_output[0]), ListNode(output_list[0])):
        all_passed = False
        print("Failed test case: " + str(input1) + " + " + str(input2) + " -> " + str(output_list) + " != " + str(expected_output))
        break
    else:
        num_passed += 1	
        if log:
        	print("Passed test case: " + str(input1) + " + " + str(input2) + " -> " + str(output_list))

assert all_passed, "Test Failed (only " + str(num_passed) + " of " + str(num_tests) + " passed)"
print("All tests passed (" + str(num_passed) + " of " + str(num_tests) + ")")
# Import TreeNode and Solution from problems/_105_leetcode.py
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems._105_leetcode import TreeNode, Solution

# Read arguments from command line (log)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="Show individual test results", type=int, choices=[True, False], default=False)
args = parser.parse_args()
log = args.log

tests = [
    {"preorder": [1,2,3], "inorder": [2,1,3], "expected": TreeNode(1, TreeNode(2), TreeNode(3))},
    {"preorder": [3,9,20,15,7], "inorder": [9,3,15,20,7], "expected": TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))},
    {"preorder": [1,2,4,5,3,6,7], "inorder": [4,2,5,1,6,3,7], "expected": TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))},
    {"preorder": [1,2,3,4,5], "inorder": [5,4,3,2,1], "expected": TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))},
    {"preorder": [1], "inorder": [1], "expected": TreeNode(1)},
    {"preorder": [1,2], "inorder": [2,1], "expected": TreeNode(1, TreeNode(2))},
    {"preorder": [2,1,3], "inorder": [1,2,3], "expected": TreeNode(2, TreeNode(1), TreeNode(3))},
    {"preorder": [4,2,1,3], "inorder": [1,2,3,4], "expected": TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)))},
    {"preorder": [3,1,2,4], "inorder": [1,2,3,4], "expected": TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))},
    {"preorder": [5,4,3,2,1], "inorder": [1,2,3,4,5], "expected": TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))},
    {"preorder": [1,2,3,4,5], "inorder": [5,4,3,2,1], "expected": TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))},
    {"preorder": [1,2,3,4,5], "inorder": [2,1,4,3,5], "expected": TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))},
]

exercise = Solution()

all_passed = True
num_tests = len(tests)
num_passed = 0
for test in tests:
    output = exercise.buildTree(test["preorder"], test["inorder"])
   
    if exercise.sameTree(output, test["expected"]):
        num_passed += 1
        if log:
            print("Passed test case: " + str(test["preorder"]) + ", " + str(test["inorder"]))
    else:
        all_passed = False
        print("Failed test case: " + str(test["preorder"]) + ", " + str(test["inorder"]))
        break

assert all_passed, "Test Failed (only " + str(num_passed) + " of " + str(num_tests) + " passed)"
print("All tests passed (" + str(num_passed) + " of " + str(num_tests) + ")")

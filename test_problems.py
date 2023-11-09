# Open the problems directory and run all the scripts in it
# Show the problems number, name, and the accepted status of the problem including a tick or cross and finish with overall score and time taken

import os
import sys
import time
import subprocess

# Get the current directory
current_dir = os.getcwd()

# Get the problems directory
problems_dir = os.path.join(current_dir, "problems")

# Get the list of files in the problems directory
problems = os.listdir(problems_dir)

# Number of problems
num_problems = 0

# Total counts
num_accepted = 0
total_time_taken = 0

# Order the problems by number using the file name (_[problem_number]_leetcode.py)
temp = []
for problem in problems:
    # Ignore __* files or directories
    if problem.startswith("__"):
        continue
    # Get the problem number
    problem_number = int(problem.split("_")[1])
    temp.append((problem_number, problem))
    num_problems += 1

# Sort the problems by number
temp.sort()
problems = []
for problem in temp:
    problems.append(problem[1])

# Print Header:
print("Leetcode Problems by Javi Barranco")
print("(Only one test case is used for each problem)")
print("")
print("-" * 98)
print("Problem".ljust(13) + "Name".ljust(60) + "Status".ljust(16) + "Time".ljust(5))
print("-" * 98)

# Run the scripts in the problems directory
for problem in problems:
    # Get the problem number
    problem_number = problem.split("_")[1]

    # Get the problem name from the first line of the script
    problem_path = os.path.join(problems_dir, problem)
    problem_file = open(problem_path, "r")
    problem_name = problem_file.readline().strip()
    problem_file.close()
    # Remove the #, number and . from the start of the problem name
    problem_name = problem_name.split(".", 1)[1].strip()


    # Run the problem
    start_time = time.time()
    problem_output = subprocess.run(["python3", problem_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end_time = time.time()

    # Get the problem status from last line of the output
    problem_status = problem_output.stdout.decode("utf-8").split("\n")[-2]
    if problem_status == "Accepted":
        num_accepted += 1

    # Get the problem time taken
    problem_time_taken = end_time - start_time
    total_time_taken += problem_time_taken

    # Status emoji: ✓ or ✗
    if problem_status == "Accepted":
        status_emoji = ("\033[92m" + "✓" + "\033[0m")
    else:
        status_emoji = ("\033[91m" + "✗" + "\033[0m")

    # Print the problem number, name, status, score and time taken (Time in miliseconds and 3 decimal places)
    print("Problem " + "{}".format(problem_number).ljust(3) + ": " + problem_name.ljust(60) + problem_status.ljust(10) + "{}".format(status_emoji) + "     " + str(round(problem_time_taken * 1000, 3)).ljust(6) + " ms")

# Totals
print("-" * 98)
print("\n----------- Results ------------")
print("Overall score".ljust(20) + ": " + str(num_accepted) + "/" + str(num_problems))
print("Overall time taken".ljust(20) + ": " + str(round(total_time_taken * 1000, 3)).ljust(6) + " ms")
print("-" * 32)

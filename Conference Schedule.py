#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxPresentations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY scheduleStart
#  2. INTEGER_ARRAY scheduleEnd
#

def maxPresentations(scheduleStart, scheduleEnd):
    # 1. Combine start and end times into a list of tuples (end, start)
    # Storing as (end, start) ensures that Python's default sort prioritizes
    # the end time first, which is crucial for the greedy approach.
    presentations = []
    for s, e in zip(scheduleStart, scheduleEnd):
        presentations.append((e, s))
    
    # 2. Sort the list of (end, start) tuples.
    # This ensures we always consider the presentation that finishes earliest first.
    presentations.sort()
    
    count = 0
    # Initialize the time the current person becomes free.
    # Set to 0 because start times are positive integers (e.g., 1-3).
    current_free_time = 0
    
    # 3. Iterate through the presentations, sorted by end time
    for end, start in presentations:
        # 4. If the presentation's start time is at or after the current free time,
        # it doesn't overlap with previously selected presentations.
        if start >= current_free_time:
            count += 1
            # Update the free time to the end time of this newly selected presentation.
            current_free_time = end
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scheduleStart_count = int(input().strip())

    scheduleStart = []

    for _ in range(scheduleStart_count):
        scheduleStart_item = int(input().strip())
        scheduleStart.append(scheduleStart_item)

    scheduleEnd_count = int(input().strip())

    scheduleEnd = []

    for _ in range(scheduleEnd_count):
        scheduleEnd_item = int(input().strip())
        scheduleEnd.append(scheduleEnd_item)

    result = maxPresentations(scheduleStart, scheduleEnd)

    fptr.write(str(result) + '\n')

    fptr.close()

# https://leetcode.com/problems/task-scheduler/

from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)

        # Step 2: Create a max-heap using the task counts
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)  # Convert list into a heap

        # Step 3: Initialize variables
        time = 0
        wait_queue = deque()  # Queue to track tasks in cooldown

        # Step 4: Process the tasks
        while max_heap or wait_queue:
            time += 1  # Increment time in each cycle

            # If there are tasks left in heap, process the most frequent one
            if max_heap:
                current_task = heapq.heappop(max_heap) + 1  # Add 1 since we negated

                # If there are still occurrences left, add to wait_queue
                if current_task != 0:
                    wait_queue.append((current_task, time + n))

            # If a task has finished its cooldown, re-add it to the heap
            if wait_queue and wait_queue[0][1] == time:
                heapq.heappush(max_heap, wait_queue.popleft()[0])

        return time


# 🔹 Why Is This Problem Solved This Way?
# The problem is about scheduling tasks efficiently while respecting the cooldown constraint.

# We solve it using Greedy + Heap + Queue because:

# Greedy Choice: Always schedule the most frequent task first.
# Heap (Priority Queue): Helps efficiently pick the most frequent task.
# Queue (Cooldown Management): Ensures tasks respect the n cooldown rule.

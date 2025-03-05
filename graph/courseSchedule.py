# https://leetcode.com/problems/course-schedule/


# this exceeds time limit!
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adjacency list with courses as keys and prerequisites as values
        adj = {course: [] for course in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        # run iterative DFS and check for any cycles
        for course in range(numCourses):
            stack = [(course, set())]
            while stack:
                cur_course, visited = stack.pop()
                if cur_course in visited:
                    return False  # cycle detected
                visited_copy = visited.copy() # create a copy of visited set
                visited_copy.add(cur_course)
                for pre in adj[cur_course]:
                    stack.append((pre, visited_copy))
        return True

# another solution: using Topological Sorting using Kahn's Algorithm (or a similar approach that uses indegrees).

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list and indegree array
        adj = {course: [] for course in range(numCourses)}
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)  # Note the reversed order: pre -> course
            indegree[course] += 1

        # 2. Initialize the queue with courses having indegree 0
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])

        # 3. Perform topological sort
        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. Check if all courses were visited
        return count == numCourses

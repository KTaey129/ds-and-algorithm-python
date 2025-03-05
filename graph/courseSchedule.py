# https://leetcode.com/problems/course-schedule/

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

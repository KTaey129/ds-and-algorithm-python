class Graph():
    def __init__(self):
        self.graph = {}

    def add(self, from_vertex, to_vertex):
        # add edge
        if from_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
        # add vertex
        else:
            self.graph[from_vertex] = [to_vertex]

    # BFS Traversal
    def bfs(self, start_vertex):
        # Check if the start_vertex exists in the graph
        if start_vertex not in self.graph:
            return []  # If not, return an empty list

        queue = [start_vertex]  # Initialize a queue with the start_vertex
        traversal = []  # initialize an empty list to store the BFS traversal result

        while queue:  # Continue until the queue is empty
            vertex = queue.pop(0)  # Remove and retrieve the first vertex from the queue (FIFO)
            if vertex not in traversal:  # Check if the vertex has not been visited
                traversal.append(vertex)  # Add the vertex to the traversal result
                if vertex in self.graph:  # Check if the vertex exists in the graph
                    queue.extend(self.graph[vertex])  # Add all adjacent vertices of the current vertex to the queue

        return traversal  # Return the BFS traversal result

    # DFS Traversal
    def dfs(self, start_vertex):
        # Check if the start_vertex exists in the graph
        if start_vertex not in self.graph:
            return []  # If not, return an empty list

        stack = [start_vertex]  # Initialize a stack with the start_vertex
        traversal = []  # Initialize an empty list to store the DFS traversal result

        while stack:  # Continue until the stack is empty
            vertex = stack.pop()  # Remove and retrieve the last vertex from the stack (LIFO)
            if vertex not in traversal:  # Check if the vertex has not been visited
                traversal.append(vertex)  # Add the vertex to the traversal result
                if vertex in self.graph:  # Check if the vertex exists in the graph
                    stack.extend(reversed(self.graph[vertex]))  # Add all adjacent vertices of the current vertex to the stack

        return traversal  # Return the DFS traversal result

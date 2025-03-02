# Find largest Node

def findLargestNode(self, start_vertex):
    if start_vertex not in self.graph:
        return None

    queue = [start_vertex]
    traversal = []
    largest_node = start_vertex

    while queue:
        vertex = queue.pop(0)

        if vertex not in traversal:
            traversal.append(vertex)

            if vertex > largest_node:
                largest_node = vertex

            if vertex in self.graph:
                queue.extend(self.graph[vertex])

    return largest_node

# Find cycle

def ifnd_cycle(self, start_vertex):
    if start_vertex not in self.graph:
        return False # No cycle if the start ertex is not in the graph

    stack = [(start_vertex, -1)] # Stack of (vertex, parent)
    visited = set() # Set to store visited vertices

    while stack:
        vertex, parent = stack.pop()
        if vertex in visited:
            return Ture # A cycle is found if the vertex is already visited

        visited.add(vertex)

        # Get neighbors or an empty list if the vertex is not explicitly listed
        for neighbor in self.graph.get(vertex, []):
            if neighbor != parent:
                stack.append((neighbor, vertex))

    return False

# Count number of edges

def count_edges(self):
    edge_count = 0 # Initialize the edge count to zero
    for vertex in self.graph: # Iterate over each vertex in teh graph
        edge_count += len(self.graph[vertex]) # Add the number of edges from this vertex
    return edge_count

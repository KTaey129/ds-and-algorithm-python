# https://leetcode.com/problems/clone-graph/description/

from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clones an undirected graph using BFS.
        Args:
            node: The starting node of the graph (or None if empty).
        Returns:
            A new Node representing the root of the cloned graph.
        """
        # If the input node is None, return None
        if not node:
            return node

        # Initialize a queue for BFS and a dictionary to store cloned nodes
        queue = deque([node])
        clones = {node.val: Node(node.val)}  # Map node values to their clones

        # Perform BFS to clone all nodes and their neighbors
        while queue:
            # Get the current node and its clone
            curr = queue.popleft()
            curr_clone = clones[curr.val]

            # Clone each neighbor of the current node
            for neighbor in curr.neighbors:  # Fixed typo: 'neighbours' -> 'neighbors'
                # If the neighbor hasn't been cloned yet, create a clone and add to queue
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                # Connect the clone to its neighbor's clone
                curr_clone.neighbors.append(clones[neighbor.val])

        # Return the clone of the starting node
        return clones[node.val]



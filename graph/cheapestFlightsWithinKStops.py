# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# The idea behind Bellman Ford Algorithm:
# Principle of Relaxation of Edges for Bellman-Ford
# you can solve it in other ways: 1. Dijkstra's algorithm 2. Level-Based BFS

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize prices array with infinity for all nodes
        prices = [float("inf")] * n
        # set the prices to reach the source node to 0
        prices[src] = 0

        # Perform up to k + 1 iterations (0 to k stops)
        for i in range(k + 1):
            # Make a copy of the current prices to update in this iteration
            tmpPrices = prices.copy()

            # Iterate through all flights
            for from_node, to_node, cost in flights:
                # If the source node has not been reached, skip this flight
                if prices[from_node] == float("inf"):
                    continue
                # If a cheaper price to destination is found, update temporary prices
                if prices[from_node] + cost < tmpPrices[to_node]:
                    tmpPrices[to_node] = prices[from_node] + cost

            # Update prices with the temporary prices after processing all flights
            prices = tmpPrices

        # If the destination prices is still infinity, it means it is unreachable
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]


# Algorithm: Modified Bellman-Ford Algorithm

# The code implements a variation of the Bellman-Ford algorithm. Let's understand what that means:

# Bellman-Ford Basics:

# The Bellman-Ford algorithm is designed to find the shortest paths from a single source vertex to all other vertices in a weighted graph, even if some edge weights are negative.
# It works by repeatedly relaxing edges. "Relaxing" an edge means checking if the current shortest path to a vertex can be improved by going through a neighboring vertex.
# The algorithm performs |V| - 1 iterations, where |V| is the number of vertices. This ensures that it finds the shortest paths, even in the presence of negative weights.
# Modifications for This Problem:

# Limited Stops (k): In our case, we have a constraint: the maximum number of stops allowed is k. This changes the termination condition. Instead of |V| - 1 iterations, we perform k + 1 iterations.
# No Negative Weights: The problem description implies that flight prices are non-negative. This simplifies the algorithm, as we don't need to worry about negative weight cycles.
# Single Destination: We're only interested in the shortest path to a specific destination (dst), not all vertices.
# Why Bellman-Ford (Variation) is Suitable:

# Handling Stops:

# The iterative nature of Bellman-Ford allows us to easily incorporate the k stops constraint. Each iteration represents allowing one more stop.
# By iterating k+1 times, we are sure to find the shortest path that uses 0 up to k stops.
# Finding Shortest Paths:

# The relaxation process ensures that we find the shortest paths by continuously updating the minimum costs.
# Simplicity:

# For this specific problem, the Bellman-Ford variation is relatively simple to implement.
# It does not require complex data structures like priority queues, which are used in Dijkstra's algorithm.
# Why Not Dijkstra's Algorithm?

# Dijkstra's Limitation: Dijkstra's algorithm is a more efficient algorithm for finding shortest paths in graphs with non-negative weights. However, it doesn't have a built-in mechanism to handle a specific number of stops.
# To implement a stop constraint with Dijkstra, you would have to change the algorithm, and it would likely become more complex than the Bellman-Ford variation used here.

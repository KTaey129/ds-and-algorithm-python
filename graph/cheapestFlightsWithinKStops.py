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

# https://leetcode.com/problems/k-closest-points-to-origin/description/#

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []  # Max heap to store the k closest points

        for x, y in points:
            dist = -(x * x + y * y)  # Use negative distance to simulate a max heap
            if len(max_heap) == k:
                heapq.heappushpop(max_heap, (dist, x, y))  # Replace the farthest point if necessary
            else:
                heapq.heappush(max_heap, (dist, x, y))  # Push new point into heap

        return [[x, y] for (_, x, y) in max_heap]  # Extract only the coordinates

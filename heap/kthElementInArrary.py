# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1549729354/

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        # Maintain a heap of size k
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:  # Remove smallest element if heap exceeds size k
                heapq.heappop(heap)

        return heap[0]  # Root of the heap is the k-th largest element


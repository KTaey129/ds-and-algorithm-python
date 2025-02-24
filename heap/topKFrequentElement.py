# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element in the array
        count = Counter(nums)

        # Step 2: Use a min heap to find the K most frequent elements
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))

        # Extract the elements from the heap
        top_k = [num for freq, num in heap]

        return top_k


# If k is large compared to N, a bucket sort approach is more efficient

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):  # Start from most frequent
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

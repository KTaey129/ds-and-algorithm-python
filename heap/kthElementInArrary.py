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

# Which One Should You Use?
# If n is small (<= 10⁵) → Sorting is fine.
# If k is small compared to n → Min-heap (O(n log k)) is better.
# If n is very large (millions of elements) → Quickselect (O(n) average) is best.

import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot_index = random.randint(left, right)  # Random pivot
            pivot = nums[pivot_index]
            
            # Move pivot to the end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # Partitioning step
            i = left
            for j in range(left, right):
                if nums[j] >= pivot:  # Keep larger numbers on the left
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            # Swap pivot into its correct position
            nums[i], nums[right] = nums[right], nums[i]
            return i

        left, right = 0, len(nums) - 1
        k_index = k - 1  # Convert k-th largest to zero-based index
        
        while left <= right:
            pivot_index = partition(left, right)
            if pivot_index == k_index:
                return nums[pivot_index]
            elif pivot_index < k_index:
                left = pivot_index + 1  # Search right half
            else:
                right = pivot_index - 1  # Search left half

# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1549729354/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, i)

        for i in range(len(nums) - k):
            heapq.heappop(heap)

        return heapq.heappop(heap)

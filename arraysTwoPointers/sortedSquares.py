# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # edge cases
        if nums[0] >= 0:
            return [num**2 for num in nums]

        if nums[-1] <= 0:
            return [num**2 for num in nums][::-1]

        # find index first positive
        m = 0
        for i, n in enumerate(nums):
            if n >= 0:
                m = i
                break

        # A = positive nums
        # B = reversed negatives
        A, B = nums[m:], [-1 * n for n in reversed(nums[:m])]

        def merge(A, B):
            a = b = 0
            ret = []
            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a += 1
                else:
                    ret.append(B[b])
                    b += 1

            if a < len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])

            return [n**2 for n in ret]

        return merge(A, B)

# more optimized using bisect

from typing import List
from bisect import bisect_left

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # If all numbers are non-negative or non-positive, square them and sort accordingly
        if nums[0] >= 0:
            return [num**2 for num in nums]  # Already sorted
        if nums[-1] <= 0:
            return [num**2 for num in nums[::-1]]  # Reverse sorted

        # Find the first non-negative number's index using binary search
        m = bisect_left(nums, 0)

        # Split into two sorted lists: 
        # A (non-negative numbers) and B (negatives in reverse)
        A, B = nums[m:], [-num for num in reversed(nums[:m])]

        # Merge two sorted lists into one sorted list
        def merge(A, B):
            a = b = 0
            ret = []
            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a += 1
                else:
                    ret.append(B[b])
                    b += 1

            # Extend remaining elements
            ret.extend(A[a:] + B[b:])

            # Square all numbers
            return [n**2 for n in ret]

        return merge(A, B)

# more optimized way - two pointers

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        l, r = 0, len(nums) - 1

        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.append(left * left)
                l += 1
            else:
                answer.append(right * right)
                r -= 1

        return answer[::-1]

# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)

                total -= nums[l]
                l += 1

        if res == float('inf'):
            return 0
        else:
            return res

# O(nlog(n)) solution: requires more time

import bisect

class Solution:
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Build the prefix sum array: prefix[i] is the sum of nums[0:i]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = float('inf')
        # For each starting index i, we look for the smallest j such that
        # prefix[j] - prefix[i] >= target, i.e., prefix[j] >= prefix[i] + target.
        for i in range(n + 1):
            desired = prefix[i] + target
            # Use binary search to find the minimal index j with prefix[j] >= desired.
            j = bisect.bisect_left(prefix, desired)
            if j <= n:
                res = min(res, j - i)

        return 0 if res == float('inf') else res

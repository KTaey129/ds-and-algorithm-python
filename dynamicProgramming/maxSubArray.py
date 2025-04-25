# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, n in enumerate(nums):
            dp[i] = max(n, dp[i - 1] + n)

        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0

            currentSum += n
            maxSum = max(maxSum, currentSum)

        return maxSum

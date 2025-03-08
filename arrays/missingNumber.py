# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    def missingNumber_sum(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

    def missingNumebr_bitwise(self, nums: List[int]) -> int:
        n = len(nums)
        result = n
        for i in range(n):
            result ^= i ^ nums[i]
        return result       

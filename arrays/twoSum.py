# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        hash_map = {} # val, idx
        for i, v in enumerate(nums):
            if target - v in hash_map:
                return i, hash_map[target - v] # python return multiple returns as a list
            else:
                hash_map[v] = i

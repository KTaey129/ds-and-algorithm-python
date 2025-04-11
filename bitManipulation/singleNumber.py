# https://leetcode.com/problems/single-number/description/

# Solutions
# 1. Brute force
# 2. Sorting
# 3. Hashing/Set
# 4. Bit manipulation: Best solution for performance

def singleNumber(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num
          
def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            if freq == 1:
                return num

def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res

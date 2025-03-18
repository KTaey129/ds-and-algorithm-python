# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()  # Sorting is crucial for two-pointer approach

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:  # Skip duplicates
                continue

            left, right = idx + 1, len(nums) - 1

            while left < right:
                currentSum = nums[idx] + nums[left] + nums[right]

                if currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    triplets.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}

        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i

        ret = []

        for i in nums:
            ret.append(d[i])

        return ret


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: Create a count array
        count = [0] * 101  # Since 0 <= nums[i] <= 100
        
        # Step 2: Count occurrences of each number in nums
        for num in nums:
            count[num] += 1
        
        # Step 3: Compute prefix sum to find "how many numbers are smaller"
        for i in range(1, 101):
            count[i] += count[i - 1]

        # Step 4: Build result using count array
        result = []
        for num in nums:
            if num == 0:
                result.append(0)  # No smaller numbers than 0
            else:
                result.append(count[num - 1])  # Prefix sum gives count of smaller numbers
        
        return result
# ✅ Uses Counting Sort, an optimal sorting technique for small range values.
# ✅ Avoids sorting, making it O(N) instead of O(N log N).
# ✅ Uses prefix sum for quick lookups (great for data processing).
# ✅ Ideal for fixed-range problems (0-100).

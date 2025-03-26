# https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ret = 0
        
        for i in range(1, n - 1):
            # Check if arr[i] is a valid peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = r = i
                
                # Expand left
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1
                
                # Expand right
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1
                
                # Update maximum length
                ret = max(ret, r - l + 1)
        
        return ret

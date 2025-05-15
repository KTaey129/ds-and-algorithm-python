# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result

# 🧠 path[:] → Makes a copy of the list

# result.append(path[:])
# This creates a new list with the current contents of path.

# It freezes that state, so changes to path later won’t affect the saved copy.

# ✅ This is the correct choice in backtracking.

# ❌ path → Just saves a reference

# result.append(path)
# This just stores a reference (pointer) to the same list in memory.

# So when path changes later (due to path.pop()), the result also changes!

# You’ll end up with many copies of the same final list, which is wrong.

# 🔍 Mini Example

# result = []
# path = [1]
# result.append(path)
# path.append(2)
# print(result)  # Outputs: [[1, 2]] → even though we appended [1]
        
# But with a copy:

# result = []
# path = [1]
# result.append(path[:])  # copy
# path.append(2)
# print(result)  # Outputs: [[1]]

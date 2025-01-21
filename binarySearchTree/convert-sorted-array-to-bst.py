# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution_iterative_bfs:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])

        # Queue to keep track of (parent, left, right) tuples
        q = deque()
        q.append((root, 0, mid - 1))
        q.append((root, mid + 1, n - 1))

        while q:
            parent, left, right = q.popleft()
            if left <= right:
                mid = (left + right) // 2
                child = TreeNode(nums[mid])
                if nums[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                q.append((child, left, mid - 1))
                q.append((child, mid + 1, right))

        return root

  

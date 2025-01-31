from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traversal(root):
            nodes = []
            stack = []
            current = root

            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left

                current = stack.pop()
                nodes.append(current.val)  # Fixed typo here
                current = current.right

            return nodes

        def sortedArrayToBST(nums):
            if not nums:
                return None

            n = len(nums)  # Fixed typo here
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
                    if nums[mid] < parent.val:  # Fixed typo here
                        parent.left = child
                    else:
                        parent.right = child
                    q.append((child, left, mid - 1))
                    q.append((child, mid + 1, right))

            return root

        sorted_nodes = inorder_traversal(root)  # Get sorted node values
        return sortedArrayToBST(sorted_nodes)   # Build a balanced BST

# LeetCode 226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            curr = stack.pop()

            if curr:
                curr.left, curr.right = curr.right, curr.left
                stack.extend([curr.left, curr.right])

        return root

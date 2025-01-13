# LeetCode 637. Average of Levels in Binary Tree

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level_sum / level_count)
        
        return result

# Automated construction of tree and test
# def construct_tree(values):
#     if not values or values[0] is None:
#         return None

#     root = TreeNode(values[0])
#     queue = deque([root])
#     i = 1

#     while queue and i < len(values):
#         node = queue.popleft()
#         if values[i] is not None:  # Left child
#             node.left = TreeNode(values[i])
#             queue.append(node.left)
#         i += 1

#         if i < len(values) and values[i] is not None:  # Right child
#             node.right = TreeNode(values[i])
#             queue.append(node.right)
#         i += 1

#     return root


# values = [3, 9, 20, 15, 17, None, None]
# root = construct_tree(values)


# solution = Solution()
# print(solution.averageOfLevels(root))

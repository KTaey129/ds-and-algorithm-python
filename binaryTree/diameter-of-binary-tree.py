# LeetCode 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_iterative:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        max_height_dict = {}
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                if node.left is None:
                    left_height = 0
                else:
                    left_height = max_height_dict.pop(node.left)

                if node.right is None:
                    right_height = 0
                else:
                    right_height = max_height_dict.pop(node.right)

                diameter = max(diameter, left_height + right_height)
                max_height_dict[node] = max(left_height, right_height) + 1
        return diameter


class Solution_recursion:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def depth(root):
            if not root: return 0

            left_depth = depth(root.left)
            right_depth = depth(root.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter

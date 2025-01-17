# LeetCode 104. Maximum Depth of Binary Tree

# Recursive
class Solution_recursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left,), self.maxDepth(root.right)) + 1

# Iterative
class Solution_iterative:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()

            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        return level

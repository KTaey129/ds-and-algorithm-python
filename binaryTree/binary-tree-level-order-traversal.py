# LeetCode 102. Binary Tree Level Order Traversal

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = deque([root])
        tree = []

        while queue:
            level = []
            for i in range(len(queue)):

                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            tree.append(level)

        return tree

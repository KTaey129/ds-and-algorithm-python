# https://leetcode.com/problems/number-of-islands/

from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] =='1' and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    count += 1

        return count

# BFS Approach: Safer for large grids (avoids recursion limits).
# DFS Approach: Less memory overhead (modifies grid in-place).
      def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1

        return count


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initially, each node is its own parent
        self.rank = [1] * size  # Rank is used for optimization
        self.count = size  # Initially, every land cell is a separate island

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:  # Merge only if they belong to different sets
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1  # Reduce the number of unique islands

def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)  # Each cell is initially a separate node
    num_water = 0  # Count number of water cells to adjust island count

    # Convert (r, c) to 1D index: index = r * cols + c
    def get_index(r, c):
        return r * cols + c

    # Process grid and union adjacent land cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '0':  # Water, so it’s not counted in islands
                num_water += 1
            else:
                # Check adjacent cells (right, down) and merge them
                for dr, dc in [(1, 0), (0, 1)]:  # Down, Right
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        uf.union(get_index(r, c), get_index(nr, nc))

    # Total possible islands = all land cells - merged ones
    return uf.count - num_water

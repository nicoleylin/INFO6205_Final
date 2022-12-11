class Solution:
    def numberOfIsland(self, grid:list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return
            grid[i][j] = "*"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count
    #time complexity: O(m*n)


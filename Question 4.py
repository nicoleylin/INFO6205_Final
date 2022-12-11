class Solution:
    def uniquePath(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0:
            return 0
        for i in range(1, cols):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
        for i in range(1, rows):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] != 1:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]

    #time complexity: O(m*n)

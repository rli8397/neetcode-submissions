class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 0
            for x, y in dirs:
                area += dfs(row + x, col + y)
            print(area)
            return area + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
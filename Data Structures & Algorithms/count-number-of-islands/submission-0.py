class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return 
            grid[row][col] = "0"
            for x, y in dirs:
                dfs(row + x, col + y)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        
        return ans
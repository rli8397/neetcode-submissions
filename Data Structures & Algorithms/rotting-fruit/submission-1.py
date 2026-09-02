class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1

        while len(q) > 0:
            r, c, lvl = q.popleft()
            ans = max(ans, lvl)
            for x, y in dirs: 
                nr = r + x
                nc = c + y
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1: 
                    q.append((r + x, c + y, lvl + 1))
                    grid[nr][nc] = 2
                    fresh -= 1

        if fresh > 0:
            return -1
        return ans
            

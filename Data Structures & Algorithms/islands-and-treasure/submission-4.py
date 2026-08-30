class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        INF = 2 ** 31 - 1

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            
            while len(q) > 0:
                r, c = q.popleft()
                for x, y in dirs:
                    newX = r + x
                    newY = c + y
                    if 0 <= newX and newX < len(grid) and 0 <= newY and newY < len(grid[0]):
                        if grid[newX][newY] > grid[r][c] + 1:
                            grid[newX][newY] = grid[r][c] + 1
                            q.append((newX, newY))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)

        
        
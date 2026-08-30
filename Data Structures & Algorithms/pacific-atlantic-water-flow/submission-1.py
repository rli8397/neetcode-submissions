class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pacific = set()
        atlantic = set()
    
        def dfs(r, c, visited):
            if (r, c) not in visited:
                visited.add((r, c))
                for x, y in dirs:
                    newR = r + x
                    newC = c + y
                    if 0 <= newR < len(heights) and 0 <= newC < len(heights[0]) and heights[newR][newC] >= heights[r][c]:
                        dfs(newR, newC, visited)

            
        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0]) - 1, atlantic)
        
        for i in range(len(heights[0])):
            dfs(0, i, pacific)
            dfs(len(heights) - 1, i, atlantic)
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res

        


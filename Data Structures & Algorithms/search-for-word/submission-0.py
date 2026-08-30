class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def backtracking(x, y, index) -> bool:
            if index == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x, y) in visited or board[x][y] != word[index]:
                return False
            
            visited.add((x, y))
            for dx, dy in dirs:
                if backtracking(x + dx, y + dy, index + 1):
                    return True
            visited.remove((x, y))
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i, j, 0):
                    return True
        return False
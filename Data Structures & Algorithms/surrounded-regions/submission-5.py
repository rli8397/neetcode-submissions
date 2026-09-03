class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c) -> None:
            for x, y in dirs:
                nr = r + x
                nc = c + y
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O":
                    board[nr][nc] = "!"
                    dfs(nr, nc)
                        

        for i in range(len(board)):
            if board[i][0] == "O":
                board[i][0] = "!"
                dfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                board[i][len(board[0]) - 1] = "!"
                dfs(i, len(board[0]) - 1)
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                board[0][i] = "!"
                dfs(0, i)
            if board[len(board) - 1][i] == "O":
                board[len(board) - 1][i] = "!"
                dfs(len(board) - 1, i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "!":
                    board[i][j] = "O"
                else: board[i][j] = "X"


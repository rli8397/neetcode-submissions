class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                curr = board[row][col]
                if curr == ".":
                    continue
                if curr in rowSet[row] or curr in colSet[col] or curr in boxSet[row//3][col//3]:
                    return False
                else:
                    rowSet[row].add(curr)
                    colSet[col].add(curr)
                    boxSet[row//3][col//3].add(curr)
        
        return True


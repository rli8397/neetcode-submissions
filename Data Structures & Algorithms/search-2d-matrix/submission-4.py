class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = 0
        lj = 0
        hi = len(matrix) - 1
        hj = len(matrix[0]) - 1
        lnum = 0
        hnum = len(matrix[0]) * len(matrix)
        while lnum <= hnum:
            mnum = (lnum + hnum) // 2
            mi = mnum // len(matrix[0])
            mj = mnum % len(matrix[0])
            if mi >= len(matrix):
                return False
            print(lnum, hnum, mnum)
            print(mi, mj)
            if matrix[mi][mj] == target:
                return True
            elif matrix[mi][mj] > target: 
                hi = mi
                hj = mj - 1
                while hj < 0:
                    hj = len(matrix[0]) - hj
                    hi -= 1
                hnum = mnum - 1
            else:
                li = mi + 1
                lj = mj + 1
                while hj >= len(matrix[0]):
                    hj = hj - len(matrix[0])
                    hi += 1
                lnum = mnum + 1
                # print("run")

        
        return False
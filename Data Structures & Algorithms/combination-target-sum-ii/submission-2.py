class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.subset = []
        self.subsum = 0
        candidates = sorted(candidates)
        def dfs(i):
            if i >= len(candidates):
                return 
            self.subsum += candidates[i]
            self.subset.append(candidates[i])
            nextDistinct = i + 1 
            while nextDistinct < len(candidates) and candidates[nextDistinct] == candidates[i]:
                nextDistinct += 1
            if self.subsum != target:
                dfs(i + 1)
            elif self.subsum:
                self.res.append(self.subset.copy())
            self.subsum -= self.subset.pop()
            dfs(nextDistinct)
        
        dfs(0)
        return self.res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.subset = []
        self.subsum = 0
        self.res = []

        def dfs(i):
            if i >= len(nums):
                return 
            
            self.subset.append(nums[i])
            self.subsum += nums[i]

            if self.subsum >= target:
                if self.subsum == target:
                    self.res.append(self.subset.copy())
                self.subsum -= self.subset.pop()
            else:
                dfs(i)
                self.subsum -= self.subset.pop()
            
            dfs(i + 1)

        dfs(0)
        return self.res
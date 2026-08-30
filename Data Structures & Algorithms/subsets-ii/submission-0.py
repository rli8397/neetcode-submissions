class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = [[]]
        def dfs(i, subset):
            if i >= len(nums):
                return 

            subset.append(nums[i])
            res.append(subset.copy())
            dfs(i + 1, subset)

            subset.pop()
            nextDistinct = i + 1

            while nextDistinct < len(nums) and nums[nextDistinct] == nums[i]:
                nextDistinct += 1
            
            dfs(nextDistinct, subset)


        dfs(0, [])
        return res
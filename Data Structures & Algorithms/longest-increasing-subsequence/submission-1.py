class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            cont = False
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j])
                    cont = True
            if cont: dp[i] += 1
            res = max(dp[i], res)
        return res
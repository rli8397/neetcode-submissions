class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        prev = [0] * len(nums)
        prev[0] = nums[0]
        prev[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = prev[i - 2] + nums[i]
            if curr > prev[i - 1]:
                prev[i] = curr
            else:
                prev[i] = prev[i - 1]
        
        return prev[len(nums) - 1]

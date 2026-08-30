class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0] 
        res = nums[0]
        for i in range(1, len(nums)):
            temp = maxProd * nums[i]
            maxProd = max(maxProd * nums[i], nums[i], minProd * nums[i])
            minProd = min(temp, nums[i], minProd * nums[i])
            res = max(res, maxProd)
        return res
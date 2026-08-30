class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        currMin = prices[0]

        for i in range(1, len(prices)):
            currMin = min(currMin, prices[i])
            ans = max(ans, prices[i] - currMin)
        
        return ans



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = -1
        for i in piles:
            ans = max(ans, i)

        low = 1
        high = ans

        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / mid)

            if hours > h:
                low = mid + 1
            else:
                ans = min(ans, mid)
                high = mid - 1
        
        return ans
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        ans = 0

        while l <= r:
            if lmax <= rmax:
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                ans += rmax - height[r]
                r -= 1

        return ans
            
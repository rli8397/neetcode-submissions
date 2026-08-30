class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for i in nums:
            if i - 1 not in s:
                curr = 1
                while i + curr in s:
                    curr += 1
                ans = max(curr, ans)

        return ans
                    
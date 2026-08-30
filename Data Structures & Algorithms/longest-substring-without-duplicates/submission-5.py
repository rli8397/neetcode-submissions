class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        d = dict()
        ans = 0
        for h in range(len(s)):
            if s[h] in d.keys():
                l = max(l, d[s[h]] + 1)
            print(l, h, d)
            d[s[h]] = h
            ans = max(ans, h - l + 1)
        return ans
         
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 2 and s[0] == s[1]:
            return s

        res = s[0]
        for i in range(1, len(s) - 1):
            # even
            l = i - 1
            r = i + 1
            if s[l] == s[i]:
                l -= 1
            elif s[r] == s[i]:
                r += 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1

            if r - l > len(res):
                res = s[l + 1 : r]
            # odd
            l = i - 1
            r = i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1

            if r - l > len(res):
                res = s[l + 1 : r]

        return res
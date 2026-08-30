class Solution:
    def countSubstrings(self, s: str) -> int:    
        res = 0         

        for i in range(len(s)):
            # odd
            l = i
            r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l2 = i 
            r2 = i + 1
            
            while l2 >= 0 and r2 < len(s) and s[l2] == s[r2]:
                res += 1
                l2 -= 1
                r2 += 1
            
        return res
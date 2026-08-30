class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        maxRepeats = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in counts.keys():
                counts[s[i]] = 0
            counts[s[i]] += 1
            maxRepeats = max(maxRepeats, counts[s[i]])
            while (i - l + 1) - maxRepeats > k:
                counts[s[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        
        return ans


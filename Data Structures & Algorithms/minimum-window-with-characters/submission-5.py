class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_counts = {}
        for letter in t: 
            if letter not in target_counts:
                target_counts[letter] = 0
            target_counts[letter] += 1

        l = 0
        charsMatched = 0
        charsNeeded = len(target_counts)
        cur_counts = {}
        ans = ""
        for r in range(len(s)):
            cur = s[r]

            if cur in target_counts: 
                if cur not in cur_counts:
                    cur_counts[cur] = 0
                cur_counts[cur] += 1
                if cur_counts[cur] == target_counts[cur]:
                    charsMatched += 1

                while l <= r and charsMatched == charsNeeded:
                    print(s[l:r + 1])
                    left = s[l]
                    if ans == "" or len(ans) > r - l + 1:
                        ans = s[l:r + 1]                    
                    if left in target_counts:
                        cur_counts[left] -= 1
                        if cur_counts[left] < target_counts[left]:
                            charsMatched -=1 
                    l += 1
        return ans

            
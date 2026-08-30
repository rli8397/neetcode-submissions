class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == 0:
            return 0

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in reversed(range(len(s))):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] += dp[i + 1]
                if i < len(s) - 1 and 1 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]
        return dp[0]
            
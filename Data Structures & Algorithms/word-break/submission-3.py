class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {0: True}
        def dfs(s: str, wordDict: List[str]) -> bool:
            if len(s) in memo:
                return memo[len(s)]
            wordSet = set(wordDict)
            for j in range(len(s)):
                if s[:j + 1] in wordSet:
                    if dfs(s[j + 1:], wordDict):
                        memo[len(s[j + 1:])] = True
                        return True
            memo[len(s)] = False
            return False
        
        return dfs(s, wordDict)

            
                           
            
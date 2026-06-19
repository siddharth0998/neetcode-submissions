class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[-1] * (n+1) for _ in range(n+1)]
        def find(s:str) -> bool:
            for word in wordDict:
                if s == word:
                    return True
            return False
        def dfs(i,j):
            if j == n-1:
                if find(s[i:j+1]):
                    return True
                else: return False
            if dp[i][j] != -1: return dp[i][j]
            take = ""
            if find(s[i:j+1]):
                take = dfs(j+1,j+1)
            notTake = dfs(i,j+1)
            dp[i][j] = take or notTake
            return dp[i][j]
        return dfs(0,0)
        
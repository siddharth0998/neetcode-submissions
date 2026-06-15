class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n+1)
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            notTake= 0
            take = dfs(i+1)
            if i < n-1 and s[i:i+2] >= "10" and s[i:i+2] <= "26":
                notTake = dfs(i+2)
            dp[i] = take + notTake
            return dp[i]
        return dfs(0)
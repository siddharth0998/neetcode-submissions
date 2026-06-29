class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s),len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        for j in range(2, m+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[j-1] == '.' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    res = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        res = res or dp[i-1][j]
                    dp[i][j] = res
                else:
                    dp[i][j] = False
        return dp[n][m]

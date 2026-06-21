class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        def LCS(i,j) -> int:
            if i == n or j == m:
                return 0
            if dp[i][j] != -1:return dp[i][j]
            res = 0
            if text1[i] == text2[j]:
                res = 1 + LCS(i+1,j+1)
            else:
                res = max(LCS(i+1,j),LCS(i,j+1))
            dp[i][j] = res
            return dp[i][j]
        return LCS(0,0)
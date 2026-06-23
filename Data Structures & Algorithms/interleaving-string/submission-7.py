class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):return False
        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i < len(s1) and s3[i+j] == s1[i]:
                    dp[i][j] = dp[i+1][j]
                if j < len(s2) and s3[i+j] == s2[j]:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0]
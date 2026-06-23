class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        if len(s1)+len(s2) != n:return False
        dp = {}
        def dfs(i,j,k):
            if k >= n:return True
            if (i,j) in dp:return dp[(i,j)]
            res = False
            if i < len(s1) and s3[k] == s1[i]:
                res = dfs(i+1,j,k+1)
            if j < len(s2) and s3[k] == s2[j]:
                res = dfs(i,j+1,k+1)
            dp[(i,j)] = res
            return res
        return dfs(0,0,0)
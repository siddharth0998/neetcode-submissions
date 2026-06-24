class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        if m > n: return 0
        dp = {}
        def dfs(i,j):
            if j == m: return 1
            if i == n: return 0
            if (i,j) in dp: return dp[(i,j)]
            take = 0
            if s[i] == t[j]:
                take = dfs(i+1,j+1)
            notTake = dfs(i+1,j)
            dp[(i,j)] = take + notTake
            return dp[(i,j)]
        return dfs(0,0)
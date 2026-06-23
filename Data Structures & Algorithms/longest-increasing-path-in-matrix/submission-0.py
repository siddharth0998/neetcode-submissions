class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = {}
        def dfs(r,c,prev):
            if r not in range(m) or c not in range(n) or matrix[r][c] <= prev:
                return 0
            if (r,c) in dp:return dp[(r,c)]
            res = 1
            res = max(res,1 + dfs(r+1,c,matrix[r][c]))
            res = max(res,1 + dfs(r,c+1,matrix[r][c]))
            res = max(res,1 + dfs(r-1,c,matrix[r][c]))
            res = max(res,1 + dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,-1)
        return max(dp.values())
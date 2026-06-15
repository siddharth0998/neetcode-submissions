class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1]*(n+1)
        def dfs(i):
            if i == 0:
                return 1
            if arr[i] != -1:
                return arr[i]
            ans = 0
            if i-1 >= 0: ans += dfs(i-1)
            if i-2 >= 0: ans += dfs(i-2)
            arr[i] = ans
            return ans
        return dfs(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        if n == 1: return nums[0]
        def dfs(i,n):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            take = nums[i] + dfs(i+2,n)
            notTake  = dfs(i+1,n)
            dp[i] = max(take,notTake)
            return dp[i]
        ans1 = dfs(0,n-1)
        dp = [-1] * (n+1)
        ans2 = dfs(1,n)
        return max(ans1,ans2)
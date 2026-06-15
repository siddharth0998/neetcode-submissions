class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        def dfs(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            take = nums[i] + dfs(i+2)
            notTake  = dfs(i+1)
            dp[i] = max(take,notTake)
            return dp[i]
        return dfs(0)

            
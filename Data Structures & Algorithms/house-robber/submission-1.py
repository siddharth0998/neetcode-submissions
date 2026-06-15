class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]* 2 for i in range(n+1)]
        def dfs(i,flag):
            if i >= n:
                return 0
            if dp[i][flag] != -1:
                return dp[i][flag]
            take = notTake = 0
            if flag:
                take = nums[i] + dfs(i+1,0)
            notTake  = dfs(i+1,1)
            dp[i][flag] = max(take,notTake)
            return dp[i][flag]
        return dfs(0,1)

            
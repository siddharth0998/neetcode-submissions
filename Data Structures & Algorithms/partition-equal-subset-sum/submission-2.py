class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2 == 1:return False
        k = total//2
        dp = [[-1] * (k+1) for _ in range(n+1)]
        def dfs(i,cur,k):
            if i >= n or cur > k:
                return False
            if cur == k:
                return True
            if dp[i][cur] != -1:return dp[i][cur]
            take = dfs(i+1,cur+nums[i],k)
            notTake = dfs(i+1,cur,k)
            dp[i][cur] = take or notTake
            return dp[i][cur]
        return dfs(0,0,k)
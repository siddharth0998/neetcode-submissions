class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2 == 1:return False
        k = total//2
        dp = [[False] * (k+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(n+1):
            for j in range(k+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]

        return dp[n][k]
       
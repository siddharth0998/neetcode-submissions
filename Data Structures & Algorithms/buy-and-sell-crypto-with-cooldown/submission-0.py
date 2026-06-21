class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for _ in range(len(prices))]
        def dfs(i,flag):
            if i >= len(prices):
                return 0
            if dp[i][flag] != -1:return dp[i][flag]
            coolDown = dfs(i+1,flag)
            if flag:
                buy = dfs(i+1,0) - prices[i]
                dp[i][flag] = max(buy,coolDown)
                return dp[i][flag]
            else:
                sell = dfs(i+2,1) + prices[i]
                dp[i][flag] = max(sell,coolDown)
                return dp[i][flag]
        return dfs(0,1)
                
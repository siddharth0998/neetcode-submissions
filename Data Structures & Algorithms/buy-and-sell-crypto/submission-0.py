class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l,r = 0,1
        if n == 1:
            return 0
        elif n == 2:
            if prices[0] >= prices[1]:
                return 0
            else:
                return prices[1] - prices[0]

        profit = 0
        while r < n:
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else:
                profit = max(profit,prices[r]-prices[l])
                r += 1

        return profit
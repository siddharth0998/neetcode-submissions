class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def dfs(i,prev):
            if i >= n:
                return 0
            if (i,prev) in dp: return dp[(i,prev)]
            take = float("-inf")
            if nums[i] > prev:
                take = 1 + dfs(i+1,nums[i])
            notTake = dfs(i+1,prev)
            dp[(i,prev)] = max(take,notTake)
            return dp[(i,prev)]
        
        return dfs(0,float("-inf"))
        
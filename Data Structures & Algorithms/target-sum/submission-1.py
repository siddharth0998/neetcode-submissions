class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i,cur):
            if i >= n:
                if cur == target:return 1
                else: return 0
            if (i,cur) in dp:return dp[(i,cur)]
            p_take = dfs(i+1,cur + nums[i])
            n_take = dfs(i+1,cur - nums[i])
            dp[(i,cur)] = p_take + n_take
            return p_take + n_take
        return dfs(0,0)
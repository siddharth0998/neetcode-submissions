class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = float('-inf')
        for i in range(len(nums)):
            if nums[i] > curr + nums[i]:
                curr = nums[i]
            else: curr += nums[i]
            ans = max(ans,curr)
        return ans

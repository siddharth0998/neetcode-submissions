class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(nums[0],self.helper(nums,0,n-1),self.helper(nums,1,n))
    def helper(self,nums,start,end):
        rob1,rob2 = 0,0
        for i in range(start,end):
            temp = max(rob2,nums[i] + rob1)
            rob1 = rob2
            rob2 = temp
        return rob2
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n == 0: return [[lower,upper]]
        if nums[0] > lower:
            ans.append([lower,nums[0]-1])
        for i in range(len(nums)):
            if i == n-1:
                if nums[i] < upper:
                    ans.append([nums[i]+1,upper])
            else:
                if nums[i] == nums[i+1] - 1:
                    continue
                else:
                    ans.append([nums[i]+1,nums[i+1]-1])
        return ans
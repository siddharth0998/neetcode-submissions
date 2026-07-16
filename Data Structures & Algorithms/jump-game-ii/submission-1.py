class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        res = 0

        while r < n - 1:
            new_r = 0
            for i in range(l,r+1):
                new_r = max(new_r, i + nums[i])
            l = r + 1
            r = new_r
            res += 1
        return res
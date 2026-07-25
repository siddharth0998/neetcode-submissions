class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        n = len(nums)
        nums.sort()
        low , high = 0 , nums[n-1] - nums[0]
        def isValid(mid):
            cnt = 0
            i = 0
            while i in range(n-1):
                if abs(nums[i] - nums[i+1]) <= mid:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False

        while low < high:
            mid = low + (high - low)//2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1
        return low
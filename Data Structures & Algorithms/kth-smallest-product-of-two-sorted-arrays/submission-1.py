class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        low, high = -10**10 , 10**10
        def count(val) -> int:
            total = 0
            for num in nums1:
                if num > 0:
                    total += bisect.bisect(nums2,val//num)
                elif num < 0:
                    total += len(nums2) - bisect.bisect(nums2,math.ceil(val/num)-1)
                else:
                    if val >= 0:
                        total += len(nums2)
            return total

        while low < high:
            mid = (high + low) // 2
            if count(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

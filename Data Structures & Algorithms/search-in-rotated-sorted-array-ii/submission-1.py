class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        arr = set(nums)
        arr2 = list(arr)
        nums = arr2
        low , high = 0 , len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
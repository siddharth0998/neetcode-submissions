class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid) -> int:
            cnt = 0
            sum = 0
            for i in range(len(weights)):
                if sum + weights[i] <= mid:
                    sum += weights[i]
                else:
                    cnt += 1
                    sum = weights[i]
            return cnt + 1
        
        low , high = max(weights) , sum(weights)
        while low < high:
            mid = low + (high - low) // 2
            if check(mid) <= days:
                high = mid
            else:
                low = mid + 1
        return low


        
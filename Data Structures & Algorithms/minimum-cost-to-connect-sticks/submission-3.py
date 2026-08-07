class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        if n == 1:return 0
        if n == 2:return sticks[0] + sticks[1]
        heapq.heapify(sticks)
        cost = 0
        while sticks:
            curr1 = heapq.heappop(sticks)
            if not sticks:
                return cost
            curr2 = heapq.heappop(sticks)
            cost += curr1 + curr2
            heapq.heappush(sticks,curr1 + curr2)

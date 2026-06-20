class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1: return stones[0]
        if n == 2: return abs(stones[0]-stones[1])
        mod_stones = [-x for x in stones]
        heapq.heapify(mod_stones)
        while len(mod_stones) > 1:
            el1 = heapq.heappop(mod_stones)
            el2 = heapq.heappop(mod_stones)
            res = abs(el1 - el2)
            heapq.heappush(mod_stones,res*(-1))
        return mod_stones[0] * (-1)



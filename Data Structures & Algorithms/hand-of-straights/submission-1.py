class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize: return False
        mpp = {}
        minheap = list(set(hand))
        heapq.heapify(minheap)
        for element in hand:
            mpp[element] = mpp.get(element,0) + 1
        mini = minheap[0]
        cnt = 0
        while mpp:
            if cnt == groupSize:
                mini = minheap[0]
                cnt = 0
            if mpp.get(mini):
                mpp[mini] -= 1
                if mpp[mini] == 0:
                    heapq.heappop(minheap)
                    del mpp[mini]
                mini += 1
                cnt += 1
            else:
                return False
        return True
        
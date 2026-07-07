class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1: return 0
        intervals.sort(key = lambda x : (x[0],x[1]))
        res = [intervals[0]]
        for i in range(1,n):
            if res[-1][1] > intervals[i][0]:
                if intervals[i][1] > res[-1][1]:
                    continue
                else:
                    res[-1] = intervals[i]
            else:
                res.append(intervals[i])
        return n - len(res)
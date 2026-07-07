"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n == 0 or n == 1:
            return True
        intervals.sort(key = lambda x : x.start)
        res = [intervals[0]]
        for i in range(1,n):
            if res[-1].end > intervals[i].start:
                return False
            else:
                res.append(intervals[i])
        return True
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        i = 0
        j = 0
        cnt = 0
        ans = 0
        while i < n:
            if start[i] < end[j]:
                cnt += 1
                ans = max(ans,cnt)
                i += 1
            else:
                cnt -= 1
                j += 1
        return ans

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        q = []
        for i in intervals:
            q.append((i.start, 1))
            q.append((i.end, -1))
        q.sort()

        res = count = 0

        for i in q:
            count += i[1]
            res = max(res, count)
        return res
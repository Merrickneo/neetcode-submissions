"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = list(sorted(intervals, key=lambda x: x.end))
        prev = None
        for interval in intervals:
            if prev == None:
                prev = interval
                continue
            if prev.end > interval.start:
                return False
            prev = interval
        return True


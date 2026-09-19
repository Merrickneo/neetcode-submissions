class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Need to find the slot for us to insert the newInterval

        1. Check if curr can be inserted directly
        - No elements in the output
        '''
        output = []
        for i, interval in enumerate(intervals):
            start, end = interval
            if end < newInterval[0]:
                output.append(interval)
            elif start > newInterval[1]:
                output.append(newInterval)
                output.extend(intervals[i:])
                return output
            else:
                newInterval = (min(newInterval[0], start), max(newInterval[1], end))
        output.append(newInterval)
        return output
        
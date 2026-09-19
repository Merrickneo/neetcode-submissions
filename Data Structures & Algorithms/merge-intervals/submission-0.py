class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = output[-1]
            curr = intervals[i]
            if curr[0] <= prev[1]:
                curr = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                output.pop()
            output.append(curr)
        return output




        
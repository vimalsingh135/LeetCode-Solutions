class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i, n = 0, len(intervals)
        start, end = newInterval

        # 1. intervals entirely before newInterval
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        # 2. intervals overlapping newInterval -> merge
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        # 3. intervals entirely after
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
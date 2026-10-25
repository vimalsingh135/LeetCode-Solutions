class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        result = []
        n = len(firstList)
        m = len(secondList)
        while i < n and j < m:
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]
            if start1 <= start2:
                if end1 >= start2:
                    s = max(start1, start2)
                    e = min(end1, end2)
                    result.append([s, e])
            else:
                if end2 >= start1:
                    s = max(start1, start2)
                    e = min(end1, end2)
                    result.append([s, e])
            if end1 <= end2:
                i += 1
            else:
                j += 1
        return result
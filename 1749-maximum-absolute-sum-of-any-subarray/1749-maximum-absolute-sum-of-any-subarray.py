class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max=0
        curr_min=0
        best_min=0
        best_max=0
        for x in nums:
            curr_min=min(x, curr_min+x)
            curr_max=max(x, curr_max+x)
            best_max=max(best_max, curr_max)
            best_min=min(best_min, curr_min)
        return max(best_max, abs(best_min))

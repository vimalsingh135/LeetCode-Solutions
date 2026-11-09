class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        hi=max(piles)
        lo=1
        while lo<hi:
            mid = (lo+hi)//2
            hours= sum((p+mid-1)//mid for p in piles)
            if hours<=h:
                hi=mid
            else:
                lo=mid+1
        return lo
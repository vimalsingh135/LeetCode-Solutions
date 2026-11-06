class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low=0
        high=len(arr)-1
        res=-1
        while low<=high:
            guess=(low+high)//2
            if arr[guess]<arr[guess+1]:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res
        


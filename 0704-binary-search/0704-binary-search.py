class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]==target:
                return guess
            elif nums[guess]<target:
                low=guess+1
            else:
                high=guess-1
        return -1

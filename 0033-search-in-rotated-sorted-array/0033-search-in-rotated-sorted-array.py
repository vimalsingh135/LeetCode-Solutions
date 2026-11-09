class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        low, high=0, n-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]==target:
                return guess
            if nums[guess] > nums[n-1]:        # guess is in the left (larger) part
                if nums[guess] < target:
                    low = guess + 1
                elif nums[0] > target:         # target is in the right part
                    low = guess + 1
                else:
                    high = guess - 1
            else:                              # guess is in the right (smaller) part
                if nums[guess] > target:
                    high = guess - 1
                elif nums[n-1] < target:       # target is in the left part
                    high = guess - 1
                else:
                    low = guess + 1
                    
        return -1

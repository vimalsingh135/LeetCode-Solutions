class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                # minimum is strictly to the right of mid
                low = mid + 1
            else:
                # minimum is at mid or to the left
                high = mid

        return nums[low]
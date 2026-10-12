class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest=0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest=max(farthest, i+nums[i])
        return True
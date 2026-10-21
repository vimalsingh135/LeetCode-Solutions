class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        min_len=float('inf')
        left=0
        current_sum=0
        for right in range(n):
            current_sum+=nums[right]

            while current_sum>=target:
                min_len=min(min_len, right-left+1)
                current_sum-=nums[left]
                left+=1
        return min_len if min_len!=float('inf') else 0
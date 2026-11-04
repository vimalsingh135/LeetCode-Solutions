class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for x in nums:
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif x > max2:
                max2, max3 = x, max2
            elif x > max3:
                max3 = x
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x
        return max(max1 * max2 * max3, min1 * min2 * max1)
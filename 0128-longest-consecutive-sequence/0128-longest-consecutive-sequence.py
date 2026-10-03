class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set=set(nums)
        longest=0

        for num in num_set:
            if num-1 not in num_set:
                current=num
                lenght=1
                while current+1 in num_set:
                    current+=1
                    lenght+=1
                longest=max(longest,lenght)

        return longest


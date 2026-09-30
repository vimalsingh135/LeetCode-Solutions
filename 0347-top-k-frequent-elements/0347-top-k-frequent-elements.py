class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
       
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # buckets[c] holds all numbers that appear exactly c times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in freq.items():
            buckets[c].append(num)

        res = []
        for c in range(len(buckets) - 1, 0, -1):
            for num in buckets[c]:
                res.append(num)
                if len(res) == k:
                    return res
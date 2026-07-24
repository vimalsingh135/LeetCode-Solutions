class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = max(nums)
        size = 1
        while size <= max_num:
            size<<=1

        pair_xor = bytearray(size)
        for i in range(n):
            ni = nums[i]
            for j in range(i, n):
                pair_xor[ni ^ nums[j]] = 1

        pair_values = [v for v in range(size) if pair_xor[v]]
        
        result = bytearray(size)
        for k in nums:
            for p in pair_values:
                result[p ^ k] = 1

        return sum(result)
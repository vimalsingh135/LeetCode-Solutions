class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        X = n 
        for i in range(n):
            X ^= i ^ nums[i]
        return X
        

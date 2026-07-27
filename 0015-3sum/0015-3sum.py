class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            # skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # since sorted, if nums[i] > 0, no triplet summing to 0 is possible
            if nums[i] > 0:
                break

            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates for left and right
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1   # sum too small, move left pointer right to increase it
                else:
                    right -= 1  # sum too big, move right pointer left to decrease it

        return result
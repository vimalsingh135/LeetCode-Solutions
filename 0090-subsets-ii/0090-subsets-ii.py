class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


        
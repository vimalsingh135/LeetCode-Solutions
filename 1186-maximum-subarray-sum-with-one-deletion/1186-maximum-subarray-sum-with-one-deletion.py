class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        no_delete = arr[0]          # best sum of subarray ending here, no deletion used
        one_delete = float('-inf')  # best sum ending here, exactly one deletion used
        res = arr[0]

        for i in range(1, len(arr)):
            # either delete arr[i] (keep previous no_delete sum),
            # or extend a subarray that already used its deletion
            one_delete = max(one_delete + arr[i], no_delete)
            # standard Kadane
            no_delete = max(no_delete + arr[i], arr[i])
            res = max(res, no_delete, one_delete)

        return res
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break  # sorted, no point going further
                path.append(c)
                # i (not i+1) since we can reuse the same number
                backtrack(i, remaining - c, path)
                path.pop()

        backtrack(0, target, [])
        return result
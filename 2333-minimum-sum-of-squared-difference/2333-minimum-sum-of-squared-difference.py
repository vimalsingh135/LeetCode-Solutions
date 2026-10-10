class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        d = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)

        if sum(d) <= k:
            return 0

        n = len(d)
        d.append(0)          # sentinel
        i = 0

        # Level the top (i+1) values down to d[i+1] while budget allows
        while i < n:
            cnt = i + 1
            cost = cnt * (d[i] - d[i + 1])
            if cost > k:
                break
            k -= cost
            i += 1

        cnt = i + 1                  # top cnt values are all equal to d[i]
        level = d[i] - k // cnt      # spread the remaining budget evenly
        extra = k % cnt              # this many get one more reduction

        total = extra * (level - 1) ** 2 + (cnt - extra) * level ** 2
        total += sum(x * x for x in d[cnt:n])
        return total
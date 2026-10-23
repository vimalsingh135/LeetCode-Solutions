from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        best_start = 0
        best_len = float('inf')

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]
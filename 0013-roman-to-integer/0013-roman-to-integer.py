class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        prev = 0

        for ch in reversed(s):
            curr = values[ch]
            if curr < prev:
                ans -= curr
            else:
                ans += curr
            prev = curr

        return ans
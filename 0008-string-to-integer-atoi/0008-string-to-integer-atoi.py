class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 1. skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # 2. check sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. read digits
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            # early exit optimization: stop if already out of range
            if sign * result < INT_MIN:
                return INT_MIN
            if sign * result > INT_MAX:
                return INT_MAX

        result *= sign

        # 4. clamp (redundant given early exit, but safe)
        return max(INT_MIN, min(INT_MAX, result))

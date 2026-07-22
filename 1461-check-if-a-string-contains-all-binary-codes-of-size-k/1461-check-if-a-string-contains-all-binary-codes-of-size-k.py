class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        need = 1 << k  # 2^k
        
        # Not enough substrings possible to cover all codes
        if n - k + 1 < need:
            return False
        
        seen = set()
        left = 0
        # right pointer expands the window
        for right in range(n):
            # once window reaches size k, record it, then slide left forward
            if right - left + 1 == k:
                seen.add(s[left:right + 1])
                left += 1
        
        return len(seen) == need
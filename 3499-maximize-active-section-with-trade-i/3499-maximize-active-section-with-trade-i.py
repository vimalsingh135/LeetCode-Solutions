class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        
        # Two-pointer run-length encoding: i marks run start, j scans to find run end
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j
        
        total_ones = s.count('1')
        
        # Slide a 3-run window (0-run, 1-run, 0-run) to find best gain
        best_gain = 0
        for k in range(1, len(runs) - 1):
            char, length = runs[k]
            if char == '1':
                left_char, left_len = runs[k - 1]
                right_char, right_len = runs[k + 1]
                if left_char == '0' and right_char == '0':
                    best_gain = max(best_gain, left_len + right_len)
        
        return total_ones + best_gain
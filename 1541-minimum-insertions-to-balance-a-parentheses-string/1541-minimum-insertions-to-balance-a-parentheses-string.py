class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0      # insertions made
        need = 0     # closing ')' still required for the open '(' seen so far
        for ch in s:
            if ch == '(':
                # If we owe an odd number of ')', the pending '(' only has one ')'
                # so far. Insert one ')' to complete that pair first.
                if need % 2 == 1:
                    res += 1
                    need -= 1
                need += 2
            else:  # ch == ')'
                need -= 1
                if need < 0:
                    # Unmatched ')': insert a '(' for it, which now needs one more ')'
                    res += 1
                    need += 2
        return res + need
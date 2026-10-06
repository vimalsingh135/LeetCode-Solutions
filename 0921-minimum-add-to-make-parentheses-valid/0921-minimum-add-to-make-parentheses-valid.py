class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_needed = 0   # unmatched '(' so far
        added = 0         # ')' with nothing to match, so we must add a '('

        for ch in s:
            if ch == '(':
                open_needed += 1
            else:  # ch == ')'
                if open_needed > 0:
                    open_needed -= 1
                else:
                    added += 1

        return added + open_needed  
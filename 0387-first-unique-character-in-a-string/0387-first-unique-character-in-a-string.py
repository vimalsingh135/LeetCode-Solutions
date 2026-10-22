class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for i in range(len(s)):
            if freq[s[i]]==1:
              return i
        return -1
            
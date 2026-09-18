class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
           return False

        count=[0]*256
        for i in range(len(s)):
            count[ord(s[i])]+=1
            count[ord(t[i])]-=1

        for c in count:
            if c != 0:
                return False
        return True

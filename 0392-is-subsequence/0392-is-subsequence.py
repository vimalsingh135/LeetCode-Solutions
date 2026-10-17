class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pointer_1=0
        for pointer_2 in range(len(t)):
            if pointer_1<len(s) and s[pointer_1]==t[pointer_2]:
                pointer_1+=1
        return pointer_1==len(s)
        
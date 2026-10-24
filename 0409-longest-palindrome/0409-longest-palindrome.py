class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        have={}
        for ch in s:
            have[ch]=have.get(ch,0)+1
        lenght=0
        has_odd=False
        for count in have.values():
            lenght+=(count//2)*2
            if count%2==1:
                has_odd=True
            
        if has_odd:
            lenght+=1
        return lenght

                
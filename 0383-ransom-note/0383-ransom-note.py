class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        demand={}
        available={}
        for ch in ransomNote:
            demand[ch]=demand.get(ch,0)+1
        for ch in magazine:
            available[ch]=available.get(ch,0)+1
        for ch in demand:
            if available.get(ch,0)<demand[ch]:
                return False
        return True
        
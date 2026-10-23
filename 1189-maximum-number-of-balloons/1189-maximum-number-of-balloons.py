class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        have={}
        wanted="balloon"
        need={}
        for ch in text:
            have[ch]=have.get(ch,0)+1
        for ch in wanted:
            need[ch]=need.get(ch,0)+1
        result=len(text)
        for ch in need:
            result=min(result, have.get(ch,0)//need[ch])
            
        return result
        
        

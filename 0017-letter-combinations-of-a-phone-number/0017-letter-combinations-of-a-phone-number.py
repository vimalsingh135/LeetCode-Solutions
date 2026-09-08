class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        dict = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],
                5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'],
                8:['t','u','v'], 9:['w','x','y','z']}
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):
                result.append(''.join(path))
                return
            letters = dict[int(digits[index])]
            for ch in letters:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()          # undo the choice
        
        backtrack(0, [])
        return result
        
        """
        :type digits: str
        :rtype: List[str]
        """
        
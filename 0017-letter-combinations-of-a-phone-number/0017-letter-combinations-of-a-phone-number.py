class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, current):
            if index == len(digits):
                result.append(''.join(current))
                return
            
            for letter in phone[digits[index]]:
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result
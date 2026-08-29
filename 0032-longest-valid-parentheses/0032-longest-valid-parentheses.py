class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        max_len = 0
        # Stack stores indices; start with -1 as a base for length calculation
        stack = [-1]

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    # No matching '(' — this ')' becomes the new base
                    stack.append(i)
                else:
                    # Valid substring found; length = current index - base index
                    max_len = max(max_len, i - stack[-1])

        return max_len
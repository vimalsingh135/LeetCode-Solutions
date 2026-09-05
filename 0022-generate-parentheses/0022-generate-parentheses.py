class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(curr, openCount, closeCount):

            if len(curr) == 2 * n:
                ans.append(curr)
                return

            # Add '(' if possible
            if openCount < n:
                backtrack(curr + "(", openCount + 1, closeCount)

            # Add ')' if valid
            if closeCount < openCount:
                backtrack(curr + ")", openCount, closeCount + 1)

        backtrack("", 0, 0)
        return ans
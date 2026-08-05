class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets with existing numbers
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    b = (r // 3) * 3 + c // 3
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b].add(val)
                else:
                    empties.append((r, c))

        def backtrack(idx):
            if idx == len(empties):
                return True

            r, c = empties[idx]
            b = (r // 3) * 3 + c // 3

            for num in '123456789':
                if num in rows[r] or num in cols[c] or num in boxes[b]:
                    continue

                # place
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if backtrack(idx + 1):
                    return True

                # undo
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

            return False

        backtrack(0)
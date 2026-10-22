class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        result = [[0] * cols for _ in range(rows)]

        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        for i in range(rows):
            for j in range(cols):
                live = 0
                for dr, dc in dirs:
                    r, c = i + dr, j + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        live += board[r][c]

                if board[i][j] == 1:
                    if live == 2 or live == 3:
                        result[i][j] = 1
                else:
                    if live == 3:
                        result[i][j] = 1

        for i in range(rows):
            for j in range(cols):
                board[i][j] = result[i][j]